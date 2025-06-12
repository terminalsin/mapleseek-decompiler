"""
Utility functions for the agentic AI client
"""

import json
from typing import Dict, Any


def format_class_for_prompt(java_class: Dict[str, Any]) -> str:
    """Format a class for inclusion in prompts"""
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


def clean_json_response(response: str) -> str:
    """Clean up AI response to extract valid JSON

    Args:
        response: Raw AI response that may contain markdown code blocks

    Returns:
        Cleaned JSON string
    """
    response = response.strip()

    # Remove markdown code blocks if present
    if response.startswith("```json"):
        response = response[7:]  # Remove ```json
    elif response.startswith("```"):
        response = response[3:]  # Remove ```

    if response.endswith("```"):
        response = response[:-3]  # Remove closing ```

    # Find JSON object boundaries
    # Look for the first { and last }
    start_idx = response.find("{")
    end_idx = response.rfind("}")

    if start_idx != -1 and end_idx != -1 and end_idx > start_idx:
        response = response[start_idx : end_idx + 1]

    return response.strip()
