"""
Extensible tools for MapleSeek agents with MCP integration
"""

from typing import Dict, Any, List, Optional, Union
from functools import wraps
import json
from pydantic import BaseModel, Field
from agents import function_tool

# Store for shared context between tools
_context_store = {
    "all_classes": {},
    "class_relationships": {},
    "decompiled_classes": {},
    "analysis_results": {},
}


class ToolResult(BaseModel):
    """Standard result format for tools"""

    success: bool
    data: Any = None
    message: str = ""
    error: Optional[str] = None


@function_tool(
    name_override="get_class_context",
    description_override="Get detailed context about a specific class from the codebase",
)
def get_class_context_tool(class_name: str) -> ToolResult:
    """Get additional context about a specific class from the codebase

    Args:
        class_name: Name of the class to get context for

    Returns:
        ToolResult with class information
    """
    try:
        all_classes = _context_store["all_classes"]

        if class_name not in all_classes:
            return ToolResult(
                success=False,
                error=f"Class {class_name} not found in codebase",
                message=f"Available classes: {list(all_classes.keys())[:10]}",
            )

        class_data = all_classes[class_name]
        formatted_data = _format_class_for_context(class_data)

        return ToolResult(
            success=True,
            data=formatted_data,
            message=f"Retrieved context for class {class_name}",
        )

    except Exception as e:
        return ToolResult(
            success=False, error=str(e), message="Error retrieving class context"
        )


@function_tool(
    name_override="get_decompiled_class",
    description_override="Get already decompiled Java code for a class",
)
def get_decompiled_class_tool(class_name: str) -> ToolResult:
    """Get the already decompiled Java code for a class

    Args:
        class_name: Name of the class to get decompiled code for

    Returns:
        ToolResult with decompiled Java code
    """
    try:
        decompiled_classes = _context_store["decompiled_classes"]

        if class_name not in decompiled_classes:
            return ToolResult(
                success=False,
                error=f"Class {class_name} has not been decompiled yet",
                message=f"Decompiled classes: {list(decompiled_classes.keys())}",
            )

        decompiled_data = decompiled_classes[class_name]

        return ToolResult(
            success=True,
            data=decompiled_data,
            message=f"Retrieved decompiled code for {class_name}",
        )

    except Exception as e:
        return ToolResult(
            success=False, error=str(e), message="Error retrieving decompiled class"
        )


@function_tool(
    name_override="run_linter",
    description_override="Run code linting and static analysis on Java code",
)
def run_linter_tool(java_code: str, linter_type: str = "checkstyle") -> ToolResult:
    """Run linting analysis on Java code (STUB - to be implemented)

    Args:
        java_code: Java source code to analyze
        linter_type: Type of linter to use (checkstyle, spotbugs, pmd)

    Returns:
        ToolResult with linting results
    """
    # STUB: This would integrate with actual Java linting tools
    try:
        # Simulate basic checks
        issues = []

        if "public class" not in java_code:
            issues.append(
                {
                    "severity": "warning",
                    "message": "No public class declaration found",
                    "line": 1,
                }
            )

        if java_code.count("{") != java_code.count("}"):
            issues.append(
                {"severity": "error", "message": "Mismatched braces", "line": -1}
            )

        result = {
            "linter": linter_type,
            "issues_found": len(issues),
            "issues": issues,
            "status": "error"
            if any(i["severity"] == "error" for i in issues)
            else "clean",
        }

        return ToolResult(
            success=True,
            data=result,
            message=f"Linting completed with {len(issues)} issues found",
        )

    except Exception as e:
        return ToolResult(success=False, error=str(e), message="Error running linter")


@function_tool(
    name_override="analyze_code_quality",
    description_override="Perform comprehensive code quality analysis",
)
def analyze_code_quality_tool(
    java_code: str, metrics: Optional[List[str]] = None
) -> ToolResult:
    """Analyze code quality metrics (STUB - to be implemented)

    Args:
        java_code: Java source code to analyze
        metrics: List of specific metrics to analyze

    Returns:
        ToolResult with quality analysis
    """
    # STUB: This would integrate with code analysis tools
    try:
        if metrics is None:
            metrics = ["complexity", "maintainability", "readability"]

        # Simulate quality analysis
        analysis = {
            "complexity": {
                "cyclomatic": min(
                    10,
                    max(
                        1,
                        java_code.count("if")
                        + java_code.count("for")
                        + java_code.count("while"),
                    ),
                ),
                "cognitive": min(15, len(java_code.split("\n")) // 10),
            },
            "maintainability": {
                "score": max(60, 100 - len(java_code) // 100),
                "factors": ["method_length", "class_coupling", "inheritance_depth"],
            },
            "readability": {
                "score": max(70, 100 - java_code.count("//") * 5),
                "factors": ["comments", "naming", "structure"],
            },
            "suggestions": [
                "Consider adding more documentation",
                "Extract complex methods into smaller ones",
                "Use more descriptive variable names",
            ],
        }

        return ToolResult(
            success=True, data=analysis, message="Code quality analysis completed"
        )

    except Exception as e:
        return ToolResult(
            success=False, error=str(e), message="Error analyzing code quality"
        )


@function_tool(
    name_override="format_java_code",
    description_override="Format and beautify Java source code",
)
def format_java_code_tool(java_code: str, style: str = "google") -> ToolResult:
    """Format Java code according to style guidelines (STUB - to be implemented)

    Args:
        java_code: Java source code to format
        style: Code style to apply (google, oracle, intellij)

    Returns:
        ToolResult with formatted code
    """
    # STUB: This would integrate with Java formatters like google-java-format
    try:
        # Simple formatting simulation
        lines = java_code.split("\n")
        formatted_lines = []
        indent_level = 0

        for line in lines:
            line = line.strip()
            if not line:
                formatted_lines.append("")
                continue

            # Decrease indent for closing braces
            if line.startswith("}"):
                indent_level = max(0, indent_level - 1)

            # Add indentation
            formatted_line = "    " * indent_level + line
            formatted_lines.append(formatted_line)

            # Increase indent for opening braces
            if line.endswith("{"):
                indent_level += 1

        formatted_code = "\n".join(formatted_lines)

        return ToolResult(
            success=True,
            data=formatted_code,
            message=f"Code formatted using {style} style",
        )

    except Exception as e:
        return ToolResult(success=False, error=str(e), message="Error formatting code")


def _format_class_for_context(java_class: Dict[str, Any]) -> str:
    """Format a class for inclusion in agent context"""
    lines = [
        f"## Class: {java_class['name']}",
        f"Super: {java_class.get('super_class', '')}",
        f"Interfaces: {java_class.get('interfaces', [])}",
        f"Access: {java_class.get('access', '')}",
        "",
    ]

    for method in java_class.get("methods", []):
        lines.extend(
            [
                f"### Method: {method['name']}",
                f"Access: {method.get('access', '')}",
                "",
                "```ssa",
                method.get("ssa_code", ""),
                "```",
                "",
            ]
        )

    return "\n".join(lines)


def update_context_store(key: str, data: Any) -> None:
    """Update the shared context store"""
    _context_store[key] = data


def get_context_store() -> Dict[str, Any]:
    """Get the current context store"""
    return _context_store.copy()


def clear_context_store() -> None:
    """Clear the context store"""
    _context_store.clear()
    _context_store.update(
        {
            "all_classes": {},
            "class_relationships": {},
            "decompiled_classes": {},
            "analysis_results": {},
        }
    )


def get_mcp_tools() -> List[Dict[str, Any]]:
    """Get list of MCP-enabled tools"""
    tools = []

    # Find all functions with MCP metadata
    for name, obj in globals().items():
        if callable(obj) and hasattr(obj, "_mcp_name"):
            tools.append(
                {
                    "name": obj._mcp_name,
                    "description": obj._mcp_description,
                    "function": obj,
                }
            )

    return tools
