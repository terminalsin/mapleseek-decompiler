"""
Enhanced UI components for MapleSeek CLI with streaming support
"""

import threading
import time
from typing import Optional, Callable, Any
from queue import Queue, Empty

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, TaskID, BarColumn, TextColumn, TimeElapsedColumn
from rich.live import Live
from rich.layout import Layout
from rich.text import Text
from rich.table import Table
from rich.align import Align
from rich.columns import Columns
from rich.syntax import Syntax


class StreamingDisplay:
    """Real-time streaming display for AI responses"""

    def __init__(self, console: Console):
        self.console = console
        self.content_queue = Queue()
        self.is_streaming = False
        self.display_thread = None
        self.accumulated_text = ""
        self.current_class = ""

    def start_streaming(self, class_name: str):
        """Start streaming display for a class"""
        # Stop any existing streaming first
        self.stop_streaming()

        self.current_class = class_name
        self.accumulated_text = ""
        self.is_streaming = True

        # Clear the queue
        while not self.content_queue.empty():
            try:
                self.content_queue.get_nowait()
            except Empty:
                break

        # Show initial message
        self.console.print(
            f"\n🤖 [cyan]Starting AI decompilation of {class_name}...[/cyan]"
        )

        # Start simple display thread that doesn't use Live to avoid conflicts
        self.display_thread = threading.Thread(
            target=self._simple_display_loop, daemon=True
        )
        self.display_thread.start()

    def add_content(self, content: str):
        """Add streaming content"""
        if self.is_streaming:
            self.content_queue.put(content)

    def stop_streaming(self):
        """Stop streaming display"""
        self.is_streaming = False
        if self.display_thread and self.display_thread.is_alive():
            self.display_thread.join(timeout=2.0)

        # Clear the streaming line properly
        print("\r" + " " * 100, end="", flush=True)  # Clear full line
        print("\r", end="", flush=True)  # Reset cursor

        # Show final content summary
        if self.accumulated_text:
            self._show_final_content()

    def _simple_display_loop(self):
        """Simple display loop without Live to avoid conflicts"""
        last_length = 0
        last_preview = ""

        while self.is_streaming:
            try:
                # Get new content from queue
                new_content = False
                while not self.content_queue.empty():
                    try:
                        content = self.content_queue.get_nowait()
                        self.accumulated_text += content
                        new_content = True
                    except Empty:
                        break

                # Show live content preview when we have significant new content
                if new_content and len(self.accumulated_text) > last_length + 50:
                    chars_received = len(self.accumulated_text)

                    # Extract a meaningful preview of current content
                    preview = self._extract_preview(self.accumulated_text)

                    # Only update if preview changed significantly
                    if preview != last_preview:
                        # Clear previous line properly and show new preview
                        print("\r" + " " * 100, end="", flush=True)  # Clear full line
                        print(
                            f"\r📡 [Chars: {chars_received}] {preview}",
                            end="",
                            flush=True,
                        )
                        last_preview = preview

                    last_length = chars_received

                time.sleep(0.2)  # Faster polling for better responsiveness

            except Exception as e:
                print(f"\n[ERROR] Streaming error: {e}")
                break

    def _extract_preview(self, text: str) -> str:
        """Extract a meaningful preview from the streaming text"""
        if not text:
            return "Waiting..."

        # Clean up text
        text = text.strip()

        # If it looks like JSON is starting, show JSON preview
        if text.startswith("{"):
            # Try to extract key fields
            if '"class_name"' in text:
                # Look for class name
                try:
                    import re

                    match = re.search(r'"class_name":\s*"([^"]+)"', text)
                    if match:
                        return f"JSON: class_name={match.group(1)[:30]}..."
                except:
                    pass

            if '"java_code"' in text:
                return "JSON: building java_code..."

            return "JSON: building response..."

        # If it looks like Java code
        if any(
            keyword in text
            for keyword in ["package ", "import ", "class ", "public ", "private "]
        ):
            # Extract first meaningful line
            lines = [line.strip() for line in text.split("\n") if line.strip()]
            if lines:
                first_line = lines[0][:40]
                return f"Java: {first_line}..."

        # For other content, show a safe preview
        clean_text = text.replace("\n", " ").replace("\r", "")[:40]
        return f"{clean_text}..."

    def _show_final_content(self):
        """Show the final accumulated content"""
        if not self.accumulated_text:
            return

        self.console.print(
            f"✅ [green]Completed streaming for {self.current_class}[/green]"
        )
        self.console.print(
            f"📊 [dim]Total received: {len(self.accumulated_text)} characters[/dim]"
        )

        # Try to show formatted JSON if it looks like JSON
        if (
            self.accumulated_text.strip().startswith("{")
            and "java_code" in self.accumulated_text
        ):
            try:
                # Show a compact preview of the JSON structure
                preview_text = self.accumulated_text[:300]
                if len(self.accumulated_text) > 300:
                    preview_text += "\n... (truncated)"

                syntax = Syntax(
                    preview_text,
                    "json",
                    theme="monokai",
                    line_numbers=False,
                )
                self.console.print(
                    Panel(
                        syntax,
                        title=f"🤖 AI Response Preview - {self.current_class}",
                        border_style="green",
                        expand=False,
                    )
                )
            except Exception:
                # Fallback to plain text preview
                preview = (
                    self.accumulated_text[:150] + "..."
                    if len(self.accumulated_text) > 150
                    else self.accumulated_text
                )
                self.console.print(
                    Panel(
                        preview,
                        title=f"🤖 AI Response Preview - {self.current_class}",
                        border_style="green",
                        expand=False,
                    )
                )

    def _display_loop(self):
        """Legacy display loop - not used to avoid Live conflicts"""
        pass

    def _update_layout(self, layout):
        """Update the streaming display layout"""
        # Header
        header_table = Table.grid(padding=1)
        header_table.add_column(style="cyan", justify="left")
        header_table.add_column(style="magenta", justify="right")
        header_table.add_row(
            f"🤖 AI Decompiling: {self.current_class}", "Press Ctrl+C to cancel"
        )
        layout["header"].update(Panel(header_table, style="blue"))

        # Stream content
        if self.accumulated_text:
            # Try to format as syntax if it looks like code
            if (
                self.accumulated_text.strip().startswith("{")
                and "java_code" in self.accumulated_text
            ):
                try:
                    # Show as JSON syntax
                    syntax = Syntax(
                        self.accumulated_text,
                        "json",
                        theme="monokai",
                        line_numbers=False,
                    )
                    layout["stream"].update(
                        Panel(syntax, title="AI Response Stream", border_style="green")
                    )
                except:
                    # Fallback to plain text
                    layout["stream"].update(
                        Panel(
                            Text(self.accumulated_text, style="white"),
                            title="AI Response Stream",
                            border_style="green",
                        )
                    )
            else:
                layout["stream"].update(
                    Panel(
                        Text(self.accumulated_text, style="white"),
                        title="AI Response Stream",
                        border_style="green",
                    )
                )
        else:
            layout["stream"].update(
                Panel(
                    Align.center("⏳ Waiting for AI response...", vertical="middle"),
                    title="AI Response Stream",
                    border_style="yellow",
                )
            )

        # Footer
        footer_text = f"📝 Accumulated: {len(self.accumulated_text)} chars"
        layout["footer"].update(Text(footer_text, style="dim"))


class EnhancedUI:
    """Enhanced UI manager for MapleSeek CLI"""

    def __init__(self):
        self.console = Console()
        self.streaming_display = StreamingDisplay(self.console)

    def show_banner(self):
        """Display welcome banner"""
        banner_text = """
   __  __             _      ____            _    
  |  \/  | __ _ _ __ | | ___/ ___|  ___  ___| | __
  | |\/| |/ _` | '_ \| |/ _ \___ \ / _ \/ _ \ |/ /
  | |  | | (_| | |_) | |  __/___) |  __/  __/   < 
  |_|  |_|\__,_| .__/|_|\___|____/ \___|\___|_|\_\\
               |_|                                 
        """

        banner_panel = Panel(
            Align.center(banner_text, vertical="middle"),
            title="🚀 MapleSeek v2.0.0 - Agentic Decompiler",
            subtitle="Convert MapleIR SSA IR dumps to Java source code using AI",
            style="bold blue",
            padding=(1, 2),
        )

        self.console.print(banner_panel)
        self.console.print()

    def show_config(
        self, input_file: str, output_dir: str, provider: str, verbose: bool
    ):
        """Display configuration information"""
        config_table = Table(title="🔧 Configuration", show_header=False, box=None)
        config_table.add_column("Key", style="cyan", width=15)
        config_table.add_column("Value", style="white")

        config_table.add_row("Input File", input_file)
        config_table.add_row("Output Dir", output_dir)
        config_table.add_row("AI Provider", f"🤖 {provider.upper()}")
        config_table.add_row("Verbose Mode", "✅ Enabled" if verbose else "❌ Disabled")

        config_panel = Panel(config_table, style="green")
        self.console.print(config_panel)
        self.console.print()

    def create_progress_bar(
        self, description: str, total: int
    ) -> tuple[Progress, TaskID]:
        """Create a progress bar with custom styling"""
        progress = Progress(
            TextColumn("[bold blue]{task.description}", justify="right"),
            BarColumn(bar_width=None),
            "[progress.percentage]{task.percentage:>3.1f}%",
            "•",
            TextColumn("({task.completed}/{task.total})"),
            "•",
            TimeElapsedColumn(),
            console=self.console,
            expand=True,
        )

        task_id = progress.add_task(description, total=total)
        return progress, task_id

    def show_analysis_phase(self, classes_count: int):
        """Show codebase analysis phase"""
        analysis_panel = Panel(
            f"🔍 Analyzing relationships between {classes_count} classes...\n"
            "• Identifying inheritance hierarchies\n"
            "• Mapping class dependencies\n"
            "• Determining optimal processing order",
            title="Phase 1: Codebase Analysis",
            style="yellow",
        )
        self.console.print(analysis_panel)

    def show_decompilation_phase(self, total_classes: int):
        """Show decompilation phase start"""
        decompile_panel = Panel(
            f"⚙️ Starting agentic decompilation of {total_classes} classes...\n"
            "• Context-aware processing\n"
            "• Real-time AI streaming\n"
            "• Dependency-ordered execution",
            title="Phase 2: Agentic Decompilation",
            style="green",
        )
        self.console.print(decompile_panel)

    def start_class_streaming(self, class_name: str):
        """Start streaming display for a class"""
        self.streaming_display.start_streaming(class_name)

    def add_stream_content(self, content: str):
        """Add content to streaming display"""
        self.streaming_display.add_content(content)

    def stop_streaming(self):
        """Stop streaming display"""
        self.streaming_display.stop_streaming()

    def show_class_result(
        self, class_name: str, success: bool, error_msg: Optional[str] = None
    ):
        """Show result for a single class"""
        if success:
            self.console.print(
                f"✅ [bold green]{class_name}[/bold green] - Decompiled successfully"
            )
        else:
            self.console.print(
                f"❌ [bold red]{class_name}[/bold red] - Error: {error_msg}"
            )

    def show_final_summary(
        self,
        total_classes: int,
        written_files: list,
        output_dir: str,
        summary_file: str,
        processing_time: float,
    ):
        """Show final decompilation summary"""

        # Success/failure stats
        success_count = len(written_files)
        failure_count = total_classes - success_count

        stats_table = Table(title="📊 Decompilation Statistics", show_header=False)
        stats_table.add_column("Metric", style="cyan", width=20)
        stats_table.add_column("Value", style="white")

        stats_table.add_row("Total Classes", str(total_classes))
        stats_table.add_row(
            "✅ Successful", f"[bold green]{success_count}[/bold green]"
        )
        if failure_count > 0:
            stats_table.add_row("❌ Failed", f"[bold red]{failure_count}[/bold red]")
        stats_table.add_row("⏱️ Processing Time", f"{processing_time:.2f}s")
        stats_table.add_row("📁 Output Directory", output_dir)
        stats_table.add_row("📄 Summary File", summary_file)

        summary_panel = Panel(stats_table, style="blue")
        self.console.print(summary_panel)

        # Show file list if not too many
        if len(written_files) <= 10:
            self.console.print("\n[bold cyan]Generated Files:[/bold cyan]")
            for file_path in written_files:
                self.console.print(f"  📄 {file_path}")
        elif len(written_files) > 10:
            self.console.print(
                f"\n[bold cyan]Generated {len(written_files)} files in:[/bold cyan] {output_dir}"
            )

    def show_error(self, message: str):
        """Show error message"""
        error_panel = Panel(f"💥 {message}", title="Error", style="bold red")
        self.console.print(error_panel)

    def show_info(self, message: str):
        """Show info message"""
        self.console.print(f"ℹ️  [cyan]{message}[/cyan]")

    def show_success(self, message: str):
        """Show success message"""
        self.console.print(f"✅ [bold green]{message}[/bold green]")
