"""
Output module for writing decompiled Java files
"""

import os
import re
from pathlib import Path
from typing import Dict, Any, List


class JavaFileWriter:
    """Handles writing decompiled Java code to files"""

    def __init__(self, output_dir: str):
        """Initialize with output directory

        Args:
            output_dir: Directory to write Java files to
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def write_class(self, decompilation_result: Dict[str, Any]) -> str:
        """Write a single Java class to file

        Args:
            decompilation_result: Result from AI decompilation containing class info

        Returns:
            Path to the written file
        """
        class_name = decompilation_result.get("class_name", "UnknownClass")
        package = decompilation_result.get("package", "")
        java_code = decompilation_result.get("java_code", "")

        # Extract simple class name from fully qualified name
        simple_class_name = self._extract_simple_class_name(class_name)

        # Create package directory structure
        if package and package != "unknown" and package != "error":
            package_path = self.output_dir / package.replace(".", "/")
            package_path.mkdir(parents=True, exist_ok=True)
            file_path = package_path / f"{simple_class_name}.java"
        else:
            file_path = self.output_dir / f"{simple_class_name}.java"

        # Clean up java_code - handle escaped newlines
        if java_code:
            # Replace literal \n with actual newlines
            java_code = java_code.replace("\\n", "\n")
            # Replace literal \t with actual tabs
            java_code = java_code.replace("\\t", "\t")

        # Write the Java code to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(java_code)

        return str(file_path)

    def write_classes(self, decompilation_results: List[Dict[str, Any]]) -> List[str]:
        """Write multiple Java classes to files

        Args:
            decompilation_results: List of decompilation results

        Returns:
            List of written file paths
        """
        written_files = []

        for result in decompilation_results:
            try:
                file_path = self.write_class(result)
                written_files.append(file_path)
                print(f"Written: {file_path}")
            except Exception as e:
                print(f"Error writing class {result.get('class_name', 'Unknown')}: {e}")

        return written_files

    def _extract_simple_class_name(self, full_class_name: str) -> str:
        """Extract simple class name from fully qualified name

        Args:
            full_class_name: Fully qualified class name (with . or / separators)

        Returns:
            Simple class name
        """
        if not full_class_name or full_class_name == "UnknownClass":
            return "UnknownClass"

        # Handle inner classes ($ separator)
        if "$" in full_class_name:
            # For inner classes, take the part after the last . or /
            if "." in full_class_name:
                simple_name = full_class_name.split(".")[-1]
            else:
                simple_name = full_class_name.split("/")[-1]
            # Clean up any invalid characters for filenames
            simple_name = re.sub(r'[<>:"/\\|?*]', "_", simple_name)
            return simple_name

        # Handle both dot-separated (dev.sim0n.Class) and slash-separated (dev/sim0n/Class) names
        if "." in full_class_name:
            # Dot-separated: take the last part after .
            simple_name = full_class_name.split(".")[-1]
        elif "/" in full_class_name:
            # Slash-separated: take the last part after /
            simple_name = full_class_name.split("/")[-1]
        else:
            # No separators, use as-is
            simple_name = full_class_name

        # Clean up any invalid characters for filenames
        simple_name = re.sub(r'[<>:"/\\|?*]', "_", simple_name)

        return simple_name

    def create_summary(
        self, decompilation_results: List[Dict[str, Any]], written_files: List[str]
    ) -> str:
        """Create a summary file of the decompilation process

        Args:
            decompilation_results: List of decompilation results
            written_files: List of successfully written files

        Returns:
            Path to the summary file
        """
        summary_path = self.output_dir / "decompilation_summary.txt"

        with open(summary_path, "w", encoding="utf-8") as f:
            f.write("MapleSeek Decompilation Summary\n")
            f.write("=" * 40 + "\n\n")
            f.write(f"Total classes processed: {len(decompilation_results)}\n")
            f.write(f"Successfully written files: {len(written_files)}\n\n")

            f.write("Written files:\n")
            for file_path in written_files:
                f.write(f"  - {file_path}\n")

            f.write("\nClass details:\n")
            for i, result in enumerate(decompilation_results):
                f.write(f"  {i + 1}. {result.get('class_name', 'Unknown')}\n")
                f.write(f"     Package: {result.get('package', 'None')}\n")
                f.write(f"     Imports: {len(result.get('imports', []))}\n\n")

        return str(summary_path)
