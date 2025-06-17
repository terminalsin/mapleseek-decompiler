#!/usr/bin/env python3
"""
Example: Basic usage of MapleSeek agentic API
"""

import os
import sys

# Add parent directory to path for development
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mapleseek.ai_client import AgenticAIClient
from mapleseek.parser import MapleIRParser
from mapleseek.output import JavaFileWriter


def main():
    """Demonstrate basic MapleSeek usage"""

    # 1. Setup the AI client with your preferred provider
    print("🚀 Initializing MapleSeek with DeepSeek...")
    ai_client = AgenticAIClient(
        provider="deepseek",  # or "openai", "anthropic", "gemini"
        # api_key="your_key_here"  # or set environment variable
    )

    # 2. Show available agents
    print(f"Available agents: {ai_client.get_available_agents()}")

    # 3. Show MCP tools
    mcp_tools = ai_client.get_mcp_tools_info()
    print(f"MCP tools available: {len(mcp_tools)}")
    for tool in mcp_tools:
        print(f"  • {tool['name']}: {tool['description']}")

    # 4. Parse a MapleIR file (you need to provide this)
    mapleir_file = "sample_input.mapleir"  # Update this path
    if not os.path.exists(mapleir_file):
        print(f"❌ Sample file {mapleir_file} not found")
        print("Please provide a MapleIR file to test with")
        return

    print(f"\n📄 Parsing {mapleir_file}...")
    parser = MapleIRParser()
    classes = parser.parse_content_to_dicts(open(mapleir_file).read())
    print(f"Found {len(classes)} classes")

    # 5. Analyze codebase relationships
    print("\n🔍 Analyzing codebase with AI agents...")
    analysis = ai_client.analyze_codebase(classes)
    print(f"Dependencies mapped: {len(analysis.get('dependencies', {}))}")
    print(f"Processing order: {analysis.get('processing_order', [])}")

    # 6. Decompile a single class
    if classes:
        class_name = classes[0]["name"]
        print(f"\n⚙️ Decompiling class: {class_name}")

        try:
            result = ai_client.decompile_class_with_context(class_name)
            print(f"✅ Successfully decompiled {result['class_name']}")
            print(f"Package: {result['package']}")
            print(f"Imports: {len(result['imports'])}")
            print(f"Java code length: {len(result['java_code'])} chars")

            # Show a preview of the decompiled code
            preview = (
                result["java_code"][:300] + "..."
                if len(result["java_code"]) > 300
                else result["java_code"]
            )
            print(f"\nPreview:\n{preview}")

        except Exception as e:
            print(f"❌ Error decompiling: {e}")

    # 7. Optional: Analyze code quality
    if classes:
        print(f"\n🔍 Analyzing code quality...")
        try:
            quality_result = ai_client.analyze_code_quality(
                result["java_code"], class_name
            )
            print(f"Quality analysis: {quality_result.get('format', 'completed')}")
        except Exception as e:
            print(f"⚠️ Quality analysis failed: {e}")

    # 8. Write to files
    print(f"\n📁 Writing results to output/...")
    writer = JavaFileWriter("output")
    if classes:
        try:
            file_path = writer.write_class(result)
            print(f"✅ Written to: {file_path}")
        except Exception as e:
            print(f"❌ Error writing file: {e}")

    print("\n🎉 Example completed!")


if __name__ == "__main__":
    main()
