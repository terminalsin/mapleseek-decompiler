#!/usr/bin/env python3
"""
Demo script to showcase the enhanced MapleSeek CLI with streaming and pretty UI
"""

import os
import sys
import tempfile
from pathlib import Path

# Add the mapleseek package to the path
sys.path.insert(0, str(Path(__file__).parent))

from mapleseek.ui import EnhancedUI
import time
import threading
from queue import Queue


def demo_streaming_display():
    """Demo the streaming display functionality"""
    ui = EnhancedUI()

    # Show banner
    ui.show_banner()

    # Show config
    ui.show_config(
        input_file="sample_input.mapleir",
        output_dir="./workspace/output",
        provider="deepseek",
        verbose=True,
    )

    # Demo analysis phase
    ui.show_analysis_phase(3)
    time.sleep(2)
    ui.show_success("Codebase analysis complete!")

    # Demo decompilation phase
    ui.show_decompilation_phase(3)
    time.sleep(1)

    # Demo streaming for each class
    sample_classes = [
        "com.example.MainClass",
        "com.example.UtilClass",
        "com.example.DataClass",
    ]

    for i, class_name in enumerate(sample_classes):
        ui.show_info(f"Starting decompilation of {class_name}...")

        # Start streaming display
        ui.start_class_streaming(class_name)

        # Simulate streaming AI response
        sample_response_parts = [
            "{\n",
            '  "class_name": "' + class_name + '",\n',
            '  "package": "com.example",\n',
            '  "imports": ["java.util.List", "java.io.IOException"],\n',
            '  "java_code": "package com.example;\\n\\n',
            "import java.util.List;\\n",
            "import java.io.IOException;\\n\\n",
            "public class " + class_name.split(".")[-1] + " {\\n",
            "    private String name;\\n\\n",
            "    public " + class_name.split(".")[-1] + "() {\\n",
            '        this.name = \\"default\\";\\n',
            "    }\\n\\n",
            "    public String getName() {\\n",
            "        return this.name;\\n",
            "    }\\n\\n",
            "    public void setName(String name) {\\n",
            "        this.name = name;\\n",
            "    }\\n",
            '}"\n',
            "}",
        ]

        # Stream the response parts with realistic timing
        for part in sample_response_parts:
            ui.add_stream_content(part)
            time.sleep(0.1)  # Simulate network delay

        time.sleep(1)  # Let the user see the final result

        # Stop streaming
        ui.stop_streaming()

        # Show result
        ui.show_class_result(class_name, True)
        time.sleep(0.5)

    # Demo final summary
    written_files = [
        "./workspace/output/com/example/MainClass.java",
        "./workspace/output/com/example/UtilClass.java",
        "./workspace/output/com/example/DataClass.java",
    ]

    ui.show_final_summary(
        total_classes=3,
        written_files=written_files,
        output_dir="./workspace/output",
        summary_file="./workspace/output/decompilation_summary.md",
        processing_time=45.2,
    )


def demo_progress_bars():
    """Demo the progress bar functionality"""
    ui = EnhancedUI()

    ui.show_info("Demonstrating progress bars...")

    # Demo class processing progress
    progress, task_id = ui.create_progress_bar("Processing classes", 5)

    with progress:
        for i in range(5):
            time.sleep(0.5)
            progress.update(task_id, advance=1)
            ui.show_info(f"Processed class {i + 1}")

    ui.show_success("Progress bar demo complete!")


def demo_ui_components():
    """Demo various UI components"""
    ui = EnhancedUI()

    # Banner
    ui.show_banner()

    # Different message types
    ui.show_info("This is an info message")
    ui.show_success("This is a success message")
    ui.show_error("This is an error message")

    # Configuration display
    ui.show_config("test.mapleir", "./output", "deepseek", True)

    # Phase displays
    ui.show_analysis_phase(10)
    ui.show_decompilation_phase(10)

    # Class results
    ui.show_class_result("TestClass", True)
    ui.show_class_result("FailedClass", False, "Parsing error")


if __name__ == "__main__":
    print("MapleSeek Enhanced CLI Demo")
    print("===========================")

    if len(sys.argv) > 1:
        demo_type = sys.argv[1]

        if demo_type == "streaming":
            print("Demonstrating streaming display...")
            demo_streaming_display()
        elif demo_type == "progress":
            print("Demonstrating progress bars...")
            demo_progress_bars()
        elif demo_type == "components":
            print("Demonstrating UI components...")
            demo_ui_components()
        else:
            print(f"Unknown demo type: {demo_type}")
            print("Available demos: streaming, progress, components")
    else:
        print("Choose a demo to run:")
        print("  python demo_enhanced_cli.py streaming    - Show streaming display")
        print("  python demo_enhanced_cli.py progress     - Show progress bars")
        print("  python demo_enhanced_cli.py components   - Show UI components")
