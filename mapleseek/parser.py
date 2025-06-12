"""
MapleIR parser to extract class information and methods
"""

import re
from typing import List, Dict, Any
from dataclasses import dataclass


@dataclass
class Method:
    name: str
    access: str
    ssa_code: str


@dataclass
class JavaClass:
    name: str
    super_class: str
    interfaces: List[str]
    access: str
    methods: List[Method]


class MapleIRParser:
    """Parser for MapleIR SSA IR dump format"""

    def __init__(self):
        pass

    def parse_file(self, file_path: str) -> List[JavaClass]:
        """Parse a MapleIR file and return list of classes"""
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        return self.parse_content(content)

    def parse_content(self, content: str) -> List[JavaClass]:
        """Parse MapleIR content and return list of classes"""
        classes = []

        # Split content by class definitions
        class_pattern = r"^## Class: (.+?)$"
        class_splits = re.split(class_pattern, content, flags=re.MULTILINE)

        # Skip the header part
        if class_splits:
            class_splits = class_splits[1:]  # Remove everything before first class

        # Process pairs of (class_name, class_content)
        for i in range(0, len(class_splits), 2):
            if i + 1 < len(class_splits):
                class_name = class_splits[i].strip()
                class_content = class_splits[i + 1]

                java_class = self._parse_class(class_name, class_content)
                if java_class:
                    classes.append(java_class)

        return classes

    def parse_content_to_dicts(self, content: str) -> List[Dict[str, Any]]:
        """Parse MapleIR content and return list of class dictionaries"""
        classes = self.parse_content(content)
        return [self._class_to_dict(cls) for cls in classes]

    def _class_to_dict(self, java_class: JavaClass) -> Dict[str, Any]:
        """Convert JavaClass to dictionary"""
        return {
            "name": java_class.name,
            "super_class": java_class.super_class,
            "interfaces": java_class.interfaces,
            "access": java_class.access,
            "methods": [
                {
                    "name": method.name,
                    "access": method.access,
                    "ssa_code": method.ssa_code,
                }
                for method in java_class.methods
            ],
        }

    def _parse_class(self, class_name: str, class_content: str) -> JavaClass:
        """Parse individual class content"""
        lines = class_content.strip().split("\n")

        super_class = ""
        interfaces = []
        access = ""
        methods = []

        current_method = None
        current_ssa = []
        in_ssa = False

        for line in lines:
            line = line.strip()

            if line.startswith("Super:"):
                super_class = line[6:].strip()
            elif line.startswith("Interfaces:"):
                interfaces_str = line[11:].strip()
                if interfaces_str and interfaces_str != "[]":
                    # Parse interface list
                    interfaces_str = interfaces_str.strip("[]")
                    interfaces = [
                        i.strip() for i in interfaces_str.split(",") if i.strip()
                    ]
            elif line.startswith("Access:"):
                access = line[7:].strip()
            elif line.startswith("### Method:"):
                # Save previous method if exists
                if current_method and current_ssa:
                    current_method.ssa_code = "\n".join(current_ssa)
                    methods.append(current_method)

                # Start new method
                method_sig = line[11:].strip()
                current_method = Method(name=method_sig, access="", ssa_code="")
                current_ssa = []
                in_ssa = False
            elif line.startswith("Access:") and current_method:
                current_method.access = line[7:].strip()
            elif line == "```ssa":
                in_ssa = True
                current_ssa = []
            elif line == "```" and in_ssa:
                in_ssa = False
            elif in_ssa:
                current_ssa.append(line)

        # Save last method
        if current_method and current_ssa:
            current_method.ssa_code = "\n".join(current_ssa)
            methods.append(current_method)

        return JavaClass(
            name=class_name,
            super_class=super_class,
            interfaces=interfaces,
            access=access,
            methods=methods,
        )

    def split_classes(self, content: str) -> List[str]:
        """Split MapleIR content into individual class chunks"""
        classes = self.parse_content(content)
        class_chunks = []

        for java_class in classes:
            chunk = self._format_class_chunk(java_class)
            class_chunks.append(chunk)

        return class_chunks

    def _format_class_chunk(self, java_class: JavaClass) -> str:
        """Format a single class back into MapleIR format for processing"""
        chunk_lines = [
            f"## Class: {java_class.name}",
            f"Super: {java_class.super_class}",
            f"Interfaces: {java_class.interfaces}",
            f"Access: {java_class.access}",
            "",
        ]

        for method in java_class.methods:
            chunk_lines.extend(
                [
                    f"### Method: {method.name}",
                    f"Access: {method.access}",
                    "",
                    "```ssa",
                    method.ssa_code,
                    "```",
                    "",
                ]
            )

        return "\n".join(chunk_lines)
