"""
AI client for communicating with LLMs using OpenAI Agents SDK with agentic decompilation capabilities
"""

import json
import os
from typing import Optional, Dict, Any, List, Callable, Generator
import litellm
from agents import Runner
from agents.extensions.models.litellm_model import LitellmModel
from .mapleagents.agent_analyser import AgentAnalyser
from .agents import MapleSeekAgents
from .tools import (
    update_context_store,
    get_context_store,
    clear_context_store,
    get_mcp_tools,
)
from . import agent_utils


class AgenticAIClient:
    """Agentic AI client using OpenAI Agents SDK with LiteLLM backend"""

    def __init__(
        self, provider_config: Dict[str, Any], api_key: Optional[str] = None, **kwargs
    ):
        """Initialize AI client with LiteLLM model configuration

        Args:
            provider: Model provider (deepseek, openai, anthropic, etc.)
            api_key: API key for the service
            **kwargs: Additional model configuration
        """
        self.provider_config = provider_config
        self.model_config = self._setup_model_config(
            provider_config["model"], api_key, **kwargs
        )

        # Initialize the agents
        self.agents = MapleSeekAgents(self.model_config)

        # Clear context store on initialization
        clear_context_store()

    def _setup_model_config(
        self,
        provider: str,
        api_key: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """Setup LiteLLM model configuration"""

        # Map provider names to LiteLLM model names
        analyser_models = {
            "deepseek": "deepseek/deepseek-chat",
            "openai": "gpt-4o",
            "anthropic": "claude-3-5-sonnet-20240620",
            "gemini": "gemini/gemini-2.5-flash-preview-05-20",
            "cohere": "command-r-plus",
            "ollama": "ollama/llama3:latest",
        }
        provider_models = {
            "deepseek": "deepseek/deepseek-reasoner",
            "openai": "gpt-4",
            "anthropic": "claude-3-sonnet-20240229",
            "gemini": "gemini/gemini-2.5-flash-preview-05-20",
            "cohere": "cohere/command-r-plus",
            "ollama": "ollama/llama3:latest",
        }

        # Setup API key environment variables for LiteLLM
        base_url = kwargs.get("base_url", "")
        if api_key:
            if provider == "deepseek":
                os.environ["DEEPSEEK_API_KEY"] = api_key
            elif provider == "openai":
                os.environ["OPENAI_API_KEY"] = api_key
            elif provider == "anthropic":
                os.environ["ANTHROPIC_API_KEY"] = api_key
            elif provider == "gemini":
                os.environ["GEMINI_API_KEY"] = api_key
            elif provider == "cohere":
                os.environ["COHERE_API_KEY"] = api_key

        # Base model configuration
        config = {
            "model": provider,
            "api_key": api_key,
            "base_url": base_url,
            "temperature": kwargs.get("temperature", 0.1),
            "max_tokens": kwargs.get("max_tokens", 4000),
            "timeout": kwargs.get("timeout", 60),
        }

        return config

    def analyze_codebase(self, classes: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        """Analyze all classes to understand relationships and dependencies using agents

        Args:
            classes: List of parsed class data

        Returns:
            Dictionary mapping class names to their dependencies
        """
        print("🔍 Analyzing codebase relationships with AI agents...")

        # Update context store with all classes
        all_classes = {cls["name"]: cls for cls in classes}
        update_context_store("all_classes", all_classes)

        # Prepare analysis prompt
        class_summaries = []
        for cls in classes:
            summary = f"Class: {cls['name']}\n"
            summary += f"Super: {cls.get('super_class', '')}\n"
            summary += f"Interfaces: {cls.get('interfaces', [])}\n"
            summary += f"Methods: {[m['name'] for m in cls.get('methods', [])]}\n"
            class_summaries.append(summary)

        analysis_prompt = f"""Analyze these MapleIR class definitions:

{chr(10).join(class_summaries)}

Identify the dependencies and optimal processing order. Return a JSON object with:
- dependencies: mapping of class names to their dependency lists
- processing_order: list of classes in dependency order (base classes first)"""

        try:
            # Use the analyzer agent
            print(f"Using model: {self.model_config['model']}")
            analyzer_agent: AgentAnalyser = self.agents.get_analyzer_agent()

            # Run the analysis
            print(
                f"Running analysis using agent {analyzer_agent.name} and model {self.model_config['model']}..."
            )
            result = Runner.run_sync(analyzer_agent, analysis_prompt)
            print(f"Analysis result: {result}")
            # Parse the result
            response_content = result.final_output

            try:
                # Clean and parse JSON response
                cleaned_response = agent_utils.clean_json_response(response_content)
                analysis_result = json.loads(cleaned_response)

                # Update context store with relationships
                update_context_store(
                    "class_relationships", analysis_result.get("dependencies", {})
                )

                return analysis_result

            except json.JSONDecodeError as e:
                print(f"⚠️ Error parsing analysis result: {e}")
                # Fallback to simple ordering
                fallback_result = {
                    "dependencies": {cls["name"]: [] for cls in classes},
                    "processing_order": [cls["name"] for cls in classes],
                }
                update_context_store(
                    "class_relationships", fallback_result["dependencies"]
                )
                return fallback_result

        except Exception as e:
            print(f"❌ Error in codebase analysis: {e}")

            # Fallback to simple ordering
            fallback_result = {
                "dependencies": {cls["name"]: [] for cls in classes},
                "processing_order": [cls["name"] for cls in classes],
            }
            update_context_store("class_relationships", fallback_result["dependencies"])
            raise e

    def decompile_class_with_context(self, class_name: str) -> Dict[str, Any]:
        """Decompile a class with full context using agents

        Args:
            class_name: Name of the class to decompile

        Returns:
            Decompilation result with Java code
        """
        context_store = get_context_store()
        all_classes = context_store.get("all_classes", {})

        if class_name not in all_classes:
            raise ValueError(f"Class {class_name} not found")

        target_class = all_classes[class_name]

        # Format the target class for the prompt
        target_class_content = agent_utils.format_class_for_prompt(target_class)

        decompile_prompt = f"""Convert this MapleIR SSA IR code to Java source code:

TARGET CLASS TO DECOMPILE:
{target_class_content}

When you have all the context you need, return a JSON object with this exact structure:
"class_name": "fully.qualified.ClassName",
    "package": "com.example.package", 
    "imports": ["java.util.List", "java.io.IOException"],
    "java_code": "complete Java class source code as a string"
    
"""

        try:
            # Use the decompiler agent
            decompiler_agent = self.agents.get_decompiler_agent()

            # Run the decompilation
            result = Runner.run_sync(decompiler_agent, decompile_prompt)

            # Parse the result
            response_content = result.final_output

            try:
                # Clean and parse JSON response
                cleaned_response = agent_utils.clean_json_response(response_content)
                decompile_result = json.loads(cleaned_response)

                # Store the decompiled class for future reference
                decompiled_classes = context_store.get("decompiled_classes", {})
                decompiled_classes[class_name] = decompile_result
                update_context_store("decompiled_classes", decompiled_classes)

                return decompile_result

            except json.JSONDecodeError as e:
                print(f"⚠️ Error parsing decompilation result for {class_name}: {e}")
                # Return error result
                return {
                    "class_name": class_name,
                    "package": "error",
                    "imports": [],
                    "java_code": f"// Error parsing decompilation result: {str(e)}\n// Raw response:\n/*\n{response_content[:500]}...\n*/",
                }

        except Exception as e:
            print(f"❌ Error decompiling {class_name}: {e}")
            return {
                "class_name": class_name,
                "package": "error",
                "imports": [],
                "java_code": f"// Error decompiling class: {str(e)}\n// Original MapleIR:\n/*\n{target_class_content[:500]}...\n*/",
            }

    def decompile_class_with_context_streaming(
        self, class_name: str
    ) -> Generator[str, None, Dict[str, Any]]:
        """Decompile a class with streaming response using agents

        Args:
            class_name: Name of the class to decompile

        Yields:
            Streaming text chunks from AI response

        Returns:
            Final decompilation result
        """
        context_store = get_context_store()
        all_classes = context_store.get("all_classes", {})

        if class_name not in all_classes:
            raise ValueError(f"Class {class_name} not found")

        target_class = all_classes[class_name]
        target_class_content = agent_utils.format_class_for_prompt(target_class)

        decompile_prompt = f"""Convert this MapleIR SSA IR code to Java source code:

TARGET CLASS TO DECOMPILE:
{target_class_content}

Provide ONLY the final JSON result with the decompiled Java code. Format:
{{"class_name": "...", "package": "...", "imports": [...], "java_code": "..."}}"""

        try:
            # Use the decompiler agent with streaming
            decompiler_agent = self.agents.get_decompiler_agent()

            # Create a streaming model configuration
            streaming_config = self.model_config.copy()
            streaming_config["stream"] = True

            # Use LiteLLM directly for streaming since Agents SDK might not support it yet
            response = litellm.completion(
                model=streaming_config["model"],
                messages=[
                    {"role": "system", "content": decompiler_agent.instructions},
                    {"role": "user", "content": decompile_prompt},
                ],
                stream=True,
                temperature=streaming_config.get("temperature", 0.1),
                max_tokens=streaming_config.get("max_tokens", 4000),
            )

            full_response = ""
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    content = chunk.choices[0].delta.content
                    full_response += content
                    yield content

            # Parse final result
            try:
                cleaned_response = agent_utils.clean_json_response(full_response)
                result = json.loads(cleaned_response)

                # Store the decompiled class
                decompiled_classes = context_store.get("decompiled_classes", {})
                decompiled_classes[class_name] = result
                update_context_store("decompiled_classes", decompiled_classes)

                yield result
                return result

            except json.JSONDecodeError as e:
                print(f"⚠️ JSON parsing failed for {class_name}: {e}")
                result = {
                    "class_name": class_name,
                    "package": "error",
                    "imports": [],
                    "java_code": f"// Error parsing decompilation result\n{full_response}",
                }
                yield result
                return result

        except Exception as e:
            error_msg = f"Error in streaming decompilation: {e}"
            yield error_msg
            result = {
                "class_name": class_name,
                "package": "error",
                "imports": [],
                "java_code": f"// {error_msg}\n// Original MapleIR:\n/*\n{target_class_content}\n*/",
            }
            yield result
            return result

    def batch_decompile_with_context(
        self,
        classes: List[Dict[str, Any]],
        progress_callback: Optional[Callable] = None,
    ) -> List[Dict[str, Any]]:
        """Decompile all classes with full context awareness using agents

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
            context_store = get_context_store()
            all_classes = context_store.get("all_classes", {})

            if class_name in all_classes:
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

    def analyze_code_quality(self, java_code: str, class_name: str) -> Dict[str, Any]:
        """Analyze code quality using the quality agent

        Args:
            java_code: Java source code to analyze
            class_name: Name of the class being analyzed

        Returns:
            Quality analysis results
        """
        try:
            quality_agent = self.agents.get_quality_agent()

            quality_prompt = f"""Analyze the code quality of this Java class:

Class: {class_name}

```java
{java_code}
```

Provide a comprehensive quality analysis including:
- Code complexity metrics
- Maintainability assessment  
- Style and formatting issues
- Suggestions for improvement

Use available tools for detailed analysis."""

            result = Runner.run_sync(quality_agent, quality_prompt)

            try:
                # Try to parse as JSON, fallback to text analysis
                cleaned_response = agent_utils.clean_json_response(result.final_output)
                return json.loads(cleaned_response)
            except json.JSONDecodeError:
                # Return as text analysis if not JSON
                return {
                    "class_name": class_name,
                    "analysis": result.final_output,
                    "format": "text",
                }

        except Exception as e:
            return {
                "class_name": class_name,
                "error": str(e),
                "analysis": "Failed to analyze code quality",
            }

    def get_mcp_tools_info(self) -> List[Dict[str, Any]]:
        """Get information about available MCP tools"""
        return get_mcp_tools()

    def get_available_agents(self) -> List[str]:
        """Get list of available agent names"""
        return self.agents.list_available_agents()


# Legacy compatibility
AIClient = AgenticAIClient
