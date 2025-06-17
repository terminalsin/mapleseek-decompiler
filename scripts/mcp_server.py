#!/usr/bin/env python3
"""
Standalone MCP server for MapleSeek tools
"""

import asyncio
import sys
import os

# Add the parent directory to the path so we can import mapleseek
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mapleseek.mcp_integration import run_mcp_server, get_mcp_server_info


def main():
    """Main entry point for MCP server"""
    if len(sys.argv) > 1 and sys.argv[1] == "--info":
        # Show server information
        info = get_mcp_server_info()
        print(f"MapleSeek MCP Server v{info['version']}")
        print(f"Description: {info['description']}")
        print(f"MCP Available: {info['mcp_available']}")

        if info["mcp_available"]:
            print(f"\nAvailable Tools ({len(info.get('tools', []))}):")
            for tool in info.get("tools", []):
                print(f"  • {tool['name']}: {tool['description']}")
        else:
            print(f"Error: {info.get('error', 'MCP not available')}")

        return

    # Run the MCP server
    try:
        asyncio.run(run_mcp_server())
    except KeyboardInterrupt:
        print("\n👋 MCP server stopped")
    except Exception as e:
        print(f"❌ Error running MCP server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
