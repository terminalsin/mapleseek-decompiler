"""
AI client for communicating with DeepSeek API with agentic decompilation capabilities
"""

import json
import os
from typing import Optional, Dict, Any, List, Callable, Generator
from openai import OpenAI

from . import prompts
from . import agent_utils


class AgenticAIClient:
    """Agentic AI client that can analyze class relationships and decompile with context"""

    def __init__(self, provider: str = "deepseek", api_key: Optional[str] = None):
        """Initialize AI client

        Args:
            provider: Either "deepseek" or "openai"
            api_key: API key for the service
        """
        self.provider = provider
        self.all_classes = {}  # Store all parsed classes for context
        self.class_relationships = {}  # Store dependency relationships
        self.decompiled_classes = {}  # Store already decompiled classes

        if provider == "deepseek":
            # DeepSeek uses OpenAI-compatible API
            api_key = api_key or os.getenv("DEEPSEEK_API_KEY")
            if not api_key:
                raise ValueError(
                    "DEEPSEEK_API_KEY environment variable or api_key parameter required"
                )

            self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
            self.model = "deepseek-reasoner"
        elif provider == "openai":
            api_key = api_key or os.getenv("OPENAI_API_KEY")
            if not api_key:
                raise ValueError(
                    "OPENAI_API_KEY environment variable or api_key parameter required"
                )

            self.client = OpenAI(api_key=api_key)
            self.model = "gpt-4"
        elif provider == "gemini":
            api_key = api_key or os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise ValueError(
                    "GEMINI_API_KEY environment variable or api_key parameter required"
                )

            self.client = OpenAI(
                api_key=api_key,
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
            )
            self.model = "gemini-2.5-flash-preview-05-20"
        else:
            raise ValueError(f"Unsupported provider: {provider}")

    def analyze_codebase(self, classes: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        """Analyze all classes to understand relationships and dependencies

        Args:
            classes: List of parsed class data

        Returns:
            Dictionary mapping class names to their dependencies
        """
        print("Analyzing codebase relationships...")

        # Store all classes for reference
        for cls in classes:
            self.all_classes[cls["name"]] = cls

        # Analyze relationships
        system_prompt = prompts.CODEBASE_ANALYZER_SYSTEM_PROMPT

        class_summaries = []
        for cls in classes:
            summary = f"Class: {cls['name']}\n"
            summary += f"Super: {cls.get('super_class', '')}\n"
            summary += f"Interfaces: {cls.get('interfaces', [])}\n"
            summary += f"Methods: {[m['name'] for m in cls.get('methods', [])]}\n"
            class_summaries.append(summary)

        user_prompt = f"""Analyze these MapleIR class definitions:

{chr(10).join(class_summaries)}

Identify the dependencies and optimal processing order."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                response_format={"type": "json_object"},
                temperature=0.1,
            )

            result = json.loads(response.choices[0].message.content)
            self.class_relationships = result.get("dependencies", {})
            return result

        except Exception as e:
            print(f"Error analyzing codebase: {e}")
            # Fallback to simple ordering
            return {
                "dependencies": {cls["name"]: [] for cls in classes},
                "processing_order": [cls["name"] for cls in classes],
            }

    def decompile_class_with_context(self, class_name: str) -> Dict[str, Any]:
        """Decompile a class with full context of related classes

        Args:
            class_name: Name of the class to decompile

        Returns:
            Decompilation result with Java code
        """
        if class_name not in self.all_classes:
            raise ValueError(f"Class {class_name} not found")

        target_class = self.all_classes[class_name]

        # Get dependencies for context
        dependencies = self.class_relationships.get(class_name, [])

        # Build context from related classes
        context_classes = []
        for dep_name in dependencies:
            if dep_name in self.all_classes:
                context_classes.append(self.all_classes[dep_name])

        # Also include already decompiled classes for reference
        decompiled_context = {}
        for dep_name in dependencies:
            if dep_name in self.decompiled_classes:
                decompiled_context[dep_name] = self.decompiled_classes[dep_name]

        result_generator = self._decompile_with_agent_generic(
            target_class, context_classes, decompiled_context, stream=False
        )
        return next(result_generator)

    def _decompile_with_agent_generic(
        self,
        target_class: Dict[str, Any],
        context_classes: List[Dict[str, Any]],
        decompiled_context: Dict[str, Any],
        stream: bool = False,
    ) -> Generator[Dict[str, Any], None, None]:
        """Generic agentic decompilation logic for both streaming and non-streaming"""
        # Function definitions for the AI to use
        functions = [
            {
                "name": "get_class_context",
                "description": "Get additional context about a specific class from the codebase",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "class_name": {
                            "type": "string",
                            "description": "Name of the class to get context for",
                        }
                    },
                    "required": ["class_name"],
                },
            },
            {
                "name": "get_decompiled_class",
                "description": "Get the already decompiled Java code for a class",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "class_name": {
                            "type": "string",
                            "description": "Name of the class to get decompiled code for",
                        }
                    },
                    "required": ["class_name"],
                },
            },
        ]

        system_prompt = prompts.DECOMPILER_SYSTEM_PROMPT

        # Format the target class for the prompt
        target_class_content = agent_utils.format_class_for_prompt(target_class)

        # Format context classes
        context_content = ""
        if context_classes:
            context_content = "\n\nRelated classes in codebase:\n"
            for ctx_class in context_classes:
                context_content += (
                    f"\n{agent_utils.format_class_for_prompt(ctx_class)}\n"
                )

        initial_prompt = f"""Convert this MapleIR SSA IR code to Java source code:

TARGET CLASS TO DECOMPILE:
{target_class_content}
{context_content}

Use the available functions to get additional context if needed. When you have sufficient context, provide the final JSON result."""
        if stream:
            initial_prompt = f"""Convert this MapleIR SSA IR code to Java source code:
TARGET CLASS TO DECOMPILE:
{target_class_content}
{context_content}

Provide ONLY the final JSON result with the decompiled Java code. Do not include any other text or comments."""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": initial_prompt},
        ]

        # Function call handlers
        def handle_get_class_context(class_name: str) -> str:
            if class_name in self.all_classes:
                return agent_utils.format_class_for_prompt(self.all_classes[class_name])
            return f"Class {class_name} not found in codebase"

        def handle_get_decompiled_class(class_name: str) -> str:
            if class_name in self.decompiled_classes:
                return self.decompiled_classes[class_name]["java_code"]
            return f"Class {class_name} has not been decompiled yet"

        function_handlers = {
            "get_class_context": handle_get_class_context,
            "get_decompiled_class": handle_get_decompiled_class,
        }

        if stream:
            try:
                # Use streaming completion
                stream_response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": initial_prompt},
                    ],
                    stream=True,
                    temperature=0.1,
                )

                full_response = ""
                for chunk in stream_response:
                    if chunk.choices[0].delta.content is not None:
                        content = chunk.choices[0].delta.content
                        full_response += content
                        yield content

                # Parse final result
                try:
                    # Clean up the response - remove markdown code blocks if present
                    cleaned_response = agent_utils.clean_json_response(full_response)
                    result = json.loads(cleaned_response)
                    self.decompiled_classes[target_class["name"]] = result
                    yield result
                except json.JSONDecodeError as e:
                    # Fallback if JSON parsing fails
                    print(f"JSON parsing failed for {target_class['name']}: {e}")
                    print(f"Raw response: {full_response[:200]}...")
                    result = {
                        "class_name": target_class["name"],
                        "package": "unknown",
                        "imports": [],
                        "java_code": f"// Error parsing decompilation result\n{full_response}",
                    }
                    self.decompiled_classes[target_class["name"]] = result
                    yield result

            except Exception as e:
                yield f"Error in streaming decompilation: {e}\n"
                result = {
                    "class_name": target_class["name"],
                    "package": "unknown",
                    "imports": [],
                    "java_code": f"// Error decompiling class: {str(e)}\n// Original MapleIR:\n/*\n{agent_utils.format_class_for_prompt(target_class)}\n*/",
                }
                self.decompiled_classes[target_class["name"]] = result
                yield result
            return

        max_iterations = 5
        iteration = 0

        while iteration < max_iterations:
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    functions=functions,
                    function_call="auto",
                    temperature=0.1,
                )

                message = response.choices[0].message

                if message.function_call:
                    # Handle function call
                    function_name = message.function_call.name
                    function_args = json.loads(message.function_call.arguments)

                    if function_name in function_handlers:
                        function_result = function_handlers[function_name](
                            **function_args
                        )

                        messages.append(
                            {
                                "role": "assistant",
                                "content": None,
                                "function_call": {
                                    "name": function_name,
                                    "arguments": message.function_call.arguments,
                                },
                            }
                        )
                        messages.append(
                            {
                                "role": "function",
                                "name": function_name,
                                "content": function_result,
                            }
                        )

                    iteration += 1
                    continue

                else:
                    # Parse final result
                    try:
                        # Clean up the response - remove markdown code blocks if present
                        cleaned_response = agent_utils.clean_json_response(
                            message.content
                        )
                        result = json.loads(cleaned_response)
                        # Store the decompiled class for future reference
                        self.decompiled_classes[target_class["name"]] = result
                        yield result
                        return
                    except json.JSONDecodeError:
                        # Fallback if JSON parsing fails
                        result = {
                            "class_name": target_class["name"],
                            "package": "unknown",
                            "imports": [],
                            "java_code": f"// Error parsing decompilation result\n{message.content}",
                        }
                        yield result
                        return

            except Exception as e:
                print(f"Error in agentic decompilation: {e}")
                result = {
                    "class_name": target_class["name"],
                    "package": "unknown",
                    "imports": [],
                    "java_code": f"// Error decompiling class: {str(e)}\n// Original MapleIR:\n/*\n{agent_utils.format_class_for_prompt(target_class)}\n*/",
                }
                yield result
                return

        # Max iterations reached
        result = {
            "class_name": target_class["name"],
            "package": "unknown",
            "imports": [],
            "java_code": f"// Max iterations reached during decompilation\n// Original MapleIR:\n/*\n{agent_utils.format_class_for_prompt(target_class)}\n*/",
        }
        yield result
        return

    def batch_decompile_with_context(
        self,
        classes: List[Dict[str, Any]],
        progress_callback: Optional[Callable] = None,
    ) -> List[Dict[str, Any]]:
        """Decompile all classes with full context awareness

        Args:
            classes: List of parsed class data
            progress_callback: Optional callback for progress updates

        Returns:
            List of decompilation results
        """
        # First analyze the codebase
        analysis = self.analyze_codebase(classes)
        processing_order = analysis.get(
            "processing_order", [cls["name"] for cls in classes]
        )

        results = []

        for i, class_name in enumerate(processing_order):
            if class_name in self.all_classes:
                if progress_callback:
                    progress_callback(
                        f"Decompiling class: {class_name}", i, len(processing_order)
                    )

                try:
                    result = self.decompile_class_with_context(class_name)
                    results.append(result)

                    if progress_callback:
                        progress_callback(
                            f"Successfully decompiled: {class_name}",
                            i + 1,
                            len(processing_order),
                        )
                except Exception as e:
                    if progress_callback:
                        progress_callback(
                            f"Error decompiling {class_name}: {e}",
                            i + 1,
                            len(processing_order),
                        )
                    # Add error result
                    results.append(
                        {
                            "class_name": class_name,
                            "package": "error",
                            "imports": [],
                            "java_code": f"// Error decompiling class: {str(e)}",
                        }
                    )

        return results

    def decompile_class_with_context_streaming(
        self, class_name: str
    ) -> Generator[str, None, Dict[str, Any]]:
        """Decompile a class with streaming response

        Args:
            class_name: Name of the class to decompile

        Yields:
            Streaming text chunks from AI response

        Returns:
            Final decompilation result
        """
        if class_name not in self.all_classes:
            raise ValueError(f"Class {class_name} not found")

        target_class = self.all_classes[class_name]
        dependencies = self.class_relationships.get(class_name, [])

        # Build context from related classes
        context_classes = []
        for dep_name in dependencies:
            if dep_name in self.all_classes:
                context_classes.append(self.all_classes[dep_name])

        # Also include already decompiled classes for reference
        decompiled_context = {}
        for dep_name in dependencies:
            if dep_name in self.decompiled_classes:
                decompiled_context[dep_name] = self.decompiled_classes[dep_name]

        # Call the streaming method and get the result
        result_generator = self._decompile_with_agent_generic(
            target_class, context_classes, decompiled_context, stream=True
        )
        final_result = None
        for result in result_generator:
            if isinstance(result, str):
                yield result
            else:
                final_result = result
        return final_result


# Legacy compatibility
AIClient = AgenticAIClient
