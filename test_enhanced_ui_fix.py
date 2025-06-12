#!/usr/bin/env python3
"""
Test script to verify the enhanced UI fixes work without Live display conflicts
"""

import sys
import time
from pathlib import Path

# Add the mapleseek package to the path
sys.path.insert(0, str(Path(__file__).parent))

from mapleseek.ui import EnhancedUI


def test_ui_without_conflicts():
    """Test the UI components without Live display conflicts"""
    ui = EnhancedUI()

    # Test banner
    ui.show_banner()

    # Test config
    ui.show_config("test.mapleir", "./output", "deepseek", True)

    # Test info messages
    ui.show_info("Testing info message")
    ui.show_success("Testing success message")

    # Test streaming without conflicts
    ui.show_info("Testing streaming display...")

    # Test multiple classes to ensure no conflicts
    test_classes = ["com.example.Class1", "com.example.Class2", "com.example.Class3"]

    for i, class_name in enumerate(test_classes):
        ui.show_info(f"[{i + 1}/{len(test_classes)}] Processing {class_name}")

        # Start streaming
        ui.start_class_streaming(class_name)

        # Simulate AI response
        sample_response = (
            '{"class_name": "'
            + class_name
            + '", "package": "com.example", "java_code": "public class '
            + class_name.split(".")[-1]
            + ' { }"}'
        )

        # Add content in chunks
        for chunk in [
            sample_response[i : i + 20] for i in range(0, len(sample_response), 20)
        ]:
            ui.add_stream_content(chunk)
            time.sleep(0.1)

        # Stop streaming
        ui.stop_streaming()

        # Show result
        ui.show_class_result(class_name, True)

        time.sleep(0.5)

    # Test final summary
    ui.show_final_summary(
        total_classes=3,
        written_files=[
            "./output/Class1.java",
            "./output/Class2.java",
            "./output/Class3.java",
        ],
        output_dir="./output",
        summary_file="./output/summary.md",
        processing_time=15.2,
    )

    ui.show_success("All tests completed without Live display conflicts!")


def test_progress_bars_separately():
    """Test progress bars in isolation"""
    ui = EnhancedUI()

    ui.show_info("Testing progress bars separately...")

    progress, task_id = ui.create_progress_bar("Test progress", 5)

    with progress:
        for i in range(5):
            time.sleep(0.5)
            progress.update(task_id, advance=1)

    ui.show_success("Progress bar test completed!")


if __name__ == "__main__":
    print("Enhanced UI Fix Test")
    print("===================")

    if len(sys.argv) > 1:
        test_type = sys.argv[1]

        if test_type == "streaming":
            test_ui_without_conflicts()
        elif test_type == "progress":
            test_progress_bars_separately()
        else:
            print(f"Unknown test type: {test_type}")
            print("Available tests: streaming, progress")
    else:
        print("Running all tests...")
        test_ui_without_conflicts()
        print("\n" + "=" * 50 + "\n")
        test_progress_bars_separately()
