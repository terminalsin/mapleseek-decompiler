"""
Agentic framework for MapleSeek using OpenAI Agents SDK
"""

from typing import Dict, Any, List, Optional
from agents import Agent, ModelSettings
from . import prompts
from .tools import (
    get_class_context_tool,
    get_decompiled_class_tool,
    run_linter_tool,
    analyze_code_quality_tool,
    format_java_code_tool,
)
from agents.extensions.models.litellm_model import LitellmModel
from .mapleagents.agent_analyser import AgentAnalyser


class MapleSeekAgents:
    """Collection of specialized agents for decompilation tasks"""

    def __init__(self, model_settings: Dict[str, Any]):
        """Initialize all agents with shared model settings

        Args:
            model_settings: LiteLLM model configuration
        """
        self.model_settings = ModelSettings(
            temperature=model_settings.get("temperature", 0.1),
            max_tokens=model_settings.get("max_tokens", 4000),
            include_usage=model_settings.get("include_usage", True),
            extra_query=model_settings.get("extra_query", None),
            extra_body=model_settings.get("extra_body", None),
            extra_headers=model_settings.get("extra_headers", None),
        )
        self.config = {
            "model": model_settings.get("model"),
            "base_url": model_settings.get("base_url"),
            "api_key": model_settings.get("api_key"),
        }
        self._create_agents()

    def _create_agents(self):
        """Create all specialized agents"""

        # Codebase Analyzer Agent - analyzes class relationships
        self.analyzer_agent = AgentAnalyser(
            config=self.config,
        )

        # Main Decompiler Agent - converts MapleIR to Java
        self.decompiler_agent = Agent(
            name="JavaDecompiler",
            instructions=prompts.DECOMPILER_INSTRUCTIONS,
            model=LitellmModel(
                self.config["model"],
                # base_url=self.config["base_url"],
                api_key=self.config["api_key"],
            ),
            model_settings=self.model_settings,
            tools=[
                get_class_context_tool,
                get_decompiled_class_tool,
                format_java_code_tool,
            ],
        )

        # Code Quality Agent - handles linting and quality analysis
        self.quality_agent = Agent(
            name="CodeQualityAnalyzer",
            instructions=prompts.CODE_QUALITY_INSTRUCTIONS,
            model=LitellmModel(
                self.config["model"],
                # base_url=self.config["base_url"],
                api_key=self.config["api_key"],
            ),
            model_settings=self.model_settings,
            tools=[
                run_linter_tool,
                analyze_code_quality_tool,
                format_java_code_tool,
            ],
        )

        # Orchestrator Agent - coordinates between other agents
        self.orchestrator_agent = Agent(
            name="DecompilationOrchestrator",
            instructions=prompts.ORCHESTRATOR_INSTRUCTIONS,
            model=LitellmModel(
                self.config["model"],
                # base_url=self.config["base_url"],
                api_key=self.config["api_key"],
            ),
            model_settings=self.model_settings,
            tools=[],  # Orchestrator uses handoffs instead of direct tools
        )

    def get_analyzer_agent(self) -> AgentAnalyser:
        """Get the codebase analyzer agent"""
        return self.analyzer_agent

    def get_decompiler_agent(self) -> Agent:
        """Get the main decompiler agent"""
        return self.decompiler_agent

    def get_quality_agent(self) -> Agent:
        """Get the code quality agent"""
        return self.quality_agent

    def get_orchestrator_agent(self) -> Agent:
        """Get the orchestrator agent"""
        return self.orchestrator_agent

    def list_available_agents(self) -> List[str]:
        """List all available agent names"""
        return [
            "CodebaseAnalyzer",
            "JavaDecompiler",
            "CodeQualityAnalyzer",
            "DecompilationOrchestrator",
        ]

    def get_agent_by_name(self, name: str) -> Optional[Agent]:
        """Get an agent by name"""
        agent_map = {
            "CodebaseAnalyzer": self.analyzer_agent,
            "JavaDecompiler": self.decompiler_agent,
            "CodeQualityAnalyzer": self.quality_agent,
            "DecompilationOrchestrator": self.orchestrator_agent,
        }
        return agent_map.get(name)
