from agents import Agent
from typing import Dict, Any
from agents.extensions.models.litellm_model import LitellmModel
from ..tools import (
    get_class_context_tool,
    get_decompiled_class_tool,
    format_java_code_tool,
)

SYSTEM_PROMPT = """

You are a Java codebase analyzer. Your task is to analyze MapleIR class definitions and identify relationships between classes.

For each class, identify:
1. Superclasses (inheritance hierarchy)
2. Referenced classes (in method signatures, field types, etc.)
3. Inner classes
4. Classes that should be decompiled together for context

Return ONLY a JSON object with this structure:
{
    "dependencies": {
        "ClassName1": ["SuperClass", "ReferencedClass1", "ReferencedClass2"],
        "ClassName2": ["SuperClass", "ReferencedClass3"]
    },
    "processing_order": ["BaseClass", "DerivedClass1", "DerivedClass2"]
}

The processing_order should list classes in dependency order (base classes first).
"""


class AgentAnalyser(Agent):
    def __init__(self, config: Dict[str, Any]):
        super().__init__(
            name=f"AgentAnalyser ({config['model']} @ {config['base_url']})",
            model=LitellmModel(
                self.model_name(config["model"]),
                # base_url=config["base_url"],
                api_key=config["api_key"],
            ),
            instructions=SYSTEM_PROMPT,
            tools=[get_class_context_tool],
        )

    def model_name(self, base_name: str = "deepseek"):
        analyser_models = {
            "deepseek": "deepseek/deepseek-chat",
            "openai": "gpt-4o",
            "anthropic": "claude-3-5-sonnet-20240620",
            "gemini": "gemini/gemini-2.5-flash-preview-05-20",
            "cohere": "command-r-plus",
            "ollama": "ollama/llama3:latest",
        }
        return analyser_models.get(base_name, base_name)
