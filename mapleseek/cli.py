"""
Command-line interface for MapleSeek with enhanced UI and streaming
"""

import os
import sys
import time
from pathlib import Path
import click

from .parser import MapleIRParser
from .ai_client import AgenticAIClient
from .output import JavaFileWriter
from .ui import EnhancedUI


@click.command()
@click.argument("input_file", type=click.Path(exists=True, readable=True))
@click.argument("output_dir", type=click.Path())
@click.option(
    "--provider",
    "-p",
    default="deepseek",
    type=click.Choice(["deepseek", "openai", "gemini"]),
    help="AI provider to use (default: deepseek)",
)
@click.option(
    "--api-key", "-k", help="API key (or use DEEPSEEK_API_KEY/OPENAI_API_KEY env var)"
)
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.option(
    "--stream/--no-stream",
    default=True,
    help="Enable/disable streaming display (default: enabled)",
)
@click.option(
    "--show-info",
    is_flag=True,
    help="Show agent and MCP server information",
)
def main(
    input_file: str,
    output_dir: str,
    provider: str,
    api_key: str,
    verbose: bool,
    stream: bool,
    show_info: bool,
):
    """
    MapleSeek: Convert MapleIR SSA IR dumps to Java source code using AI.

    INPUT_FILE: Path to the MapleIR formatted file
    OUTPUT_DIR: Directory to write the decompiled Java files
    """

    start_time = time.time()
    ui = EnhancedUI()

    # Show welcome banner
    ui.show_banner()

    # Show agent and MCP info if requested
    if show_info:
        ui.show_info("🤖 Agent Information:")
        try:
            from .mcp_integration import get_mcp_server_info

            mcp_info = get_mcp_server_info()

            ui.show_info(
                f"Available Agents: CodebaseAnalyzer, JavaDecompiler, CodeQualityAnalyzer, DecompilationOrchestrator"
            )
            ui.show_info(f"MCP Server: {mcp_info['name']} v{mcp_info['version']}")
            ui.show_info(
                f"MCP Available: {'✅' if mcp_info['mcp_available'] else '❌'}"
            )
            ui.show_info(f"Tools Count: {len(mcp_info.get('tools', []))}")

            if mcp_info["mcp_available"]:
                ui.show_info("MCP Tools:")
                for tool in mcp_info.get("tools", []):
                    ui.show_info(f"  • {tool['name']}: {tool['description']}")

        except Exception as e:
            ui.show_error(f"Error getting agent info: {e}")

        return  # Exit after showing info

    # Show configuration
    ui.show_config(input_file, output_dir, provider, verbose)

    try:
        # Initialize components
        if verbose:
            ui.show_info("Initializing mapleir parser...")
        parser = MapleIRParser()

        if verbose:
            ui.show_info(
                f"Initializing {provider} agentic AI client with OpenAI Agents SDK..."
            )
        ai_client = AgenticAIClient(
            provider_config={
                "model": provider,
            },
            api_key=api_key,
        )

        if verbose:
            ui.show_info("Setting up output directory...")
        writer = JavaFileWriter(output_dir)

        # Parse input file
        if verbose:
            ui.show_info("Parsing MapleIR file...")

        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Parse all classes into dictionaries for AI processing
        if verbose:
            ui.show_info("Parsing classes...")
        classes = parser.parse_content_to_dicts(content)

        if not classes:
            ui.show_error("No classes found in input file")
            sys.exit(1)

        ui.show_success(f"Found {len(classes)} classes to process")

        # Phase 1: Codebase Analysis
        ui.show_analysis_phase(len(classes))

        # Analyze relationships (this part doesn't stream, so we just show progress)
        analysis = ai_client.analyze_codebase(classes)
        processing_order = analysis.get(
            "processing_order", [cls["name"] for cls in classes]
        )

        # Ensure processing_order is not None
        if processing_order is None:
            processing_order = [cls["name"] for cls in classes]

        ui.show_success("Codebase analysis complete!")

        # Phase 2: Decompilation with streaming
        ui.show_decompilation_phase(len(processing_order))

        if stream:
            # Use streaming decompilation with immediate file writing
            decompilation_results = []
            written_files = []

            for i, class_name in enumerate(processing_order):
                # Check if class exists in the context store
                from .tools import get_context_store

                context_store = get_context_store()
                all_classes = context_store.get("all_classes", {})

                if class_name in all_classes:
                    try:
                        # Show current progress
                        ui.show_info(
                            f"[{i + 1}/{len(processing_order)}] Processing {class_name}"
                        )

                        # Start streaming display for this class
                        if verbose:
                            ui.start_class_streaming(class_name)

                        # Stream the decompilation and collect the result
                        full_content = ""
                        result = None

                        # Create a generator from the streaming method
                        stream_gen = ai_client.decompile_class_with_context_streaming(
                            class_name
                        )

                        try:
                            # Process all streaming content
                            while True:
                                try:
                                    content_chunk = next(stream_gen)
                                    if isinstance(content_chunk, dict):
                                        # This is the final result
                                        result = content_chunk
                                        break
                                    else:
                                        # This is streaming content
                                        full_content += content_chunk
                                        if verbose:
                                            ui.add_stream_content(content_chunk)
                                except StopIteration as e:
                                    # Generator finished, get the return value
                                    if hasattr(e, "value") and e.value:
                                        result = e.value
                                    break
                        except Exception as gen_error:
                            if verbose:
                                ui.show_error(f"Generator error: {gen_error}")

                        # Stop streaming display
                        if verbose:
                            ui.stop_streaming()

                        if result:
                            decompilation_results.append(result)

                            # Write the file immediately
                            try:
                                file_path = writer.write_class(result)
                                written_files.append(file_path)

                                ui.show_class_result(class_name, True)
                                if verbose:
                                    ui.show_info(f"✍️ Written: {file_path}")

                            except Exception as write_error:
                                ui.show_error(
                                    f"Error writing {class_name}: {write_error}"
                                )
                                ui.show_class_result(
                                    class_name, False, f"Write error: {write_error}"
                                )
                        else:
                            ui.show_class_result(
                                class_name, False, "No result returned from AI"
                            )
                            # Add error result for summary
                            decompilation_results.append(
                                {
                                    "class_name": class_name,
                                    "package": "error",
                                    "imports": [],
                                    "java_code": f"// Error: No result returned from AI\n// Streaming content:\n/*\n{full_content[:500]}...\n*/",
                                }
                            )

                    except Exception as e:
                        if verbose:
                            ui.stop_streaming()
                        ui.show_class_result(class_name, False, str(e))
                        # Add error result
                        decompilation_results.append(
                            {
                                "class_name": class_name,
                                "package": "error",
                                "imports": [],
                                "java_code": f"// Error decompiling class: {str(e)}",
                            }
                        )
        else:
            # Use traditional batch processing with progress callback
            def progress_callback(message: str, current: int, total: int):
                if verbose:
                    ui.show_info(f"[{current}/{total}] {message}")

            decompilation_results = ai_client.batch_decompile_with_context(
                classes, progress_callback=progress_callback
            )

            # Write results to files for batch mode
            ui.show_info("Writing decompiled classes to files...")
            written_files = []

            # Create progress bar for writing
            write_progress, write_task_id = ui.create_progress_bar(
                "Writing Java files", len(decompilation_results)
            )

            with write_progress:
                for result in decompilation_results:
                    try:
                        file_path = writer.write_class(result)
                        written_files.append(file_path)

                        if verbose:
                            class_name = result.get("class_name", "Unknown")
                            ui.show_info(f"Written: {class_name} -> {file_path}")

                    except Exception as e:
                        ui.show_error(
                            f"Error writing class {result.get('class_name', 'Unknown')}: {e}"
                        )

                    write_progress.update(write_task_id, advance=1)

        # Create summary (this now happens after all processing)
        if written_files:  # Only create summary if we have files
            summary_file = writer.create_summary(decompilation_results, written_files)
        else:
            summary_file = "No files written"

        # Calculate processing time
        processing_time = time.time() - start_time

        # Final report
        ui.show_final_summary(
            total_classes=len(classes),
            written_files=written_files,
            output_dir=output_dir,
            summary_file=summary_file,
            processing_time=processing_time,
        )

        if verbose:
            ui.show_info("Decompilation approach:")
            ui.show_info("  - Analyzed class relationships and dependencies")
            ui.show_info("  - Processed classes in optimal order")
            if stream:
                ui.show_info("  - Used real-time streaming decompilation")
            ui.show_info(
                "  - AI used context-aware decompilation with function calling"
            )

    except KeyboardInterrupt:
        ui.show_error("Operation cancelled by user")
        sys.exit(1)

    except Exception as e:
        ui.show_error(f"Fatal error: {e}")
        if verbose:
            import traceback

            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
