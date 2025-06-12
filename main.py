#!/usr/bin/env python3
"""
MapleSeek: Agentic AI-powered MapleIR to Java decompiler

This is the main entry point for the MapleSeek decompiler, which uses
agentic AI techniques to provide context-aware decompilation of MapleIR
SSA IR dumps back to readable Java source code.

Features:
- Codebase relationship analysis
- Context-aware decompilation
- Function calling for additional context
- Dependency-ordered processing
- Support for complex class hierarchies
"""

from mapleseek.cli import main

if __name__ == "__main__":
    main()
