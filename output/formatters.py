"""
Output Formatters
=================
Various output format implementations with META 50/50 balance consideration.
"""

import json
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any


class OutputFormat(Enum):
    """Supported output formats."""

    TEXT = "text"
    JSON = "json"
    MARKDOWN = "markdown"
    TABLE = "table"
    HTML = "html"
    CSV = "csv"


@dataclass
class FormattedOutput:
    """Container for formatted output."""

    content: str
    format: OutputFormat
    metadata: dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)

    @property
    def length(self) -> int:
        return len(self.content)

    def to_dict(self) -> dict[str, Any]:
        return {
            "content": self.content,
            "format": self.format.value,
            "metadata": self.metadata,
            "timestamp": self.timestamp.isoformat(),
            "length": self.length,
        }


class Formatter(ABC):
    """Abstract base class for formatters."""

    def __init__(self):
        self._format = OutputFormat.TEXT

    @property
    def format(self) -> OutputFormat:
        return self._format

    @abstractmethod
    def format_data(self, data: Any) -> FormattedOutput:
        """Format data into output."""
        pass

    @abstractmethod
    def format_dict(self, data: dict[str, Any]) -> FormattedOutput:
        """Format dictionary data."""
        pass

    @abstractmethod
    def format_list(self, data: list[Any]) -> FormattedOutput:
        """Format list data."""
        pass

    def format_equilibrium(
        self, positive: float, negative: float, name: str = ""
    ) -> FormattedOutput:
        """Format equilibrium balance display."""
        data = {
            "type": "equilibrium",
            "name": name or "balance",
            "positive": positive,
            "negative": negative,
            "total": positive + negative,
            "balanced": abs(positive - 50) < 0.01,
        }
        return self.format_dict(data)

    def format_duality(
        self, positive_name: str, positive_value: float, negative_name: str, negative_value: float
    ) -> FormattedOutput:
        """Format duality display."""
        data = {
            "type": "duality",
            "positive": {"name": positive_name, "value": positive_value},
            "negative": {"name": negative_name, "value": negative_value},
            "balanced": abs(positive_value - 50) < 0.01,
        }
        return self.format_dict(data)


class TextFormatter(Formatter):
    """Plain text output formatter."""

    def __init__(self, indent: int = 2, width: int = 80):
        super().__init__()
        self._format = OutputFormat.TEXT
        self._indent = indent
        self._width = width

    def format_data(self, data: Any) -> FormattedOutput:
        """Format any data to text."""
        if isinstance(data, dict):
            return self.format_dict(data)
        elif isinstance(data, list):
            return self.format_list(data)
        else:
            return FormattedOutput(content=str(data), format=self._format)

    def format_dict(self, data: dict[str, Any], level: int = 0) -> FormattedOutput:
        """Format dictionary to text."""
        lines = []
        indent = " " * (self._indent * level)

        for key, value in data.items():
            if isinstance(value, dict):
                lines.append(f"{indent}{key}:")
                nested = self.format_dict(value, level + 1)
                lines.append(nested.content)
            elif isinstance(value, list):
                lines.append(f"{indent}{key}:")
                for item in value:
                    if isinstance(item, dict):
                        nested = self.format_dict(item, level + 1)
                        lines.append(nested.content)
                    else:
                        lines.append(f"{indent}  - {item}")
            else:
                lines.append(f"{indent}{key}: {value}")

        return FormattedOutput(content="\n".join(lines), format=self._format)

    def format_list(self, data: list[Any]) -> FormattedOutput:
        """Format list to text."""
        lines = []
        for i, item in enumerate(data, 1):
            if isinstance(item, dict):
                lines.append(f"{i}.")
                nested = self.format_dict(item, 1)
                lines.append(nested.content)
            else:
                lines.append(f"{i}. {item}")

        return FormattedOutput(content="\n".join(lines), format=self._format)

    def format_equilibrium(
        self, positive: float, negative: float, name: str = ""
    ) -> FormattedOutput:
        """Format equilibrium as text bar."""
        title = name or "Balance"
        bar_width = 50
        pos_width = int(bar_width * positive / 100)
        neg_width = bar_width - pos_width

        bar = f"[{'█' * pos_width}{'░' * neg_width}]"
        balance_status = "✓ BALANCED" if abs(positive - 50) < 0.01 else "⚠ IMBALANCED"

        lines = [
            f"═══ {title} ═══",
            f"  Positive: {positive:>6.2f}%",
            f"  Negative: {negative:>6.2f}%",
            f"  {bar}",
            f"  Status: {balance_status}",
            "═" * (len(title) + 8),
        ]

        return FormattedOutput(
            content="\n".join(lines),
            format=self._format,
            metadata={"balanced": abs(positive - 50) < 0.01},
        )

    def format_duality(
        self, positive_name: str, positive_value: float, negative_name: str, negative_value: float
    ) -> FormattedOutput:
        """Format duality as text."""
        bar_width = 40
        pos_width = int(bar_width * positive_value / 100)
        neg_width = bar_width - pos_width

        lines = [
            "┌─ Duality ─┐",
            f"│ {positive_name:<15} │ {negative_name:<15} │",
            f"│ {positive_value:>6.2f}%          │ {negative_value:>6.2f}%          │",
            f"│ {'█' * pos_width}{'░' * neg_width} │",
            f"└{'─' * 37}┘",
        ]

        return FormattedOutput(content="\n".join(lines), format=self._format)


class JsonFormatter(Formatter):
    """JSON output formatter."""

    def __init__(self, indent: int = 2, sort_keys: bool = False):
        super().__init__()
        self._format = OutputFormat.JSON
        self._indent = indent
        self._sort_keys = sort_keys

    def format_data(self, data: Any) -> FormattedOutput:
        """Format any data to JSON."""
        try:
            content = json.dumps(data, indent=self._indent, sort_keys=self._sort_keys, default=str)
        except (TypeError, ValueError) as e:
            content = json.dumps({"error": str(e), "data": str(data)})

        return FormattedOutput(content=content, format=self._format)

    def format_dict(self, data: dict[str, Any]) -> FormattedOutput:
        """Format dictionary to JSON."""
        return self.format_data(data)

    def format_list(self, data: list[Any]) -> FormattedOutput:
        """Format list to JSON."""
        return self.format_data(data)


class MarkdownFormatter(Formatter):
    """Markdown output formatter."""

    def __init__(self):
        super().__init__()
        self._format = OutputFormat.MARKDOWN

    def format_data(self, data: Any) -> FormattedOutput:
        """Format any data to Markdown."""
        if isinstance(data, dict):
            return self.format_dict(data)
        elif isinstance(data, list):
            return self.format_list(data)
        else:
            return FormattedOutput(content=f"`{data}`", format=self._format)

    def format_dict(self, data: dict[str, Any], level: int = 1) -> FormattedOutput:
        """Format dictionary to Markdown."""
        lines = []

        for key, value in data.items():
            if isinstance(value, dict):
                lines.append(f"{'#' * level} {key}\n")
                nested = self.format_dict(value, level + 1)
                lines.append(nested.content)
            elif isinstance(value, list):
                lines.append(f"{'#' * level} {key}\n")
                for item in value:
                    if isinstance(item, dict):
                        for k, v in item.items():
                            lines.append(f"- **{k}**: {v}")
                    else:
                        lines.append(f"- {item}")
                lines.append("")
            else:
                lines.append(f"**{key}**: {value}")

        return FormattedOutput(content="\n".join(lines), format=self._format)

    def format_list(self, data: list[Any]) -> FormattedOutput:
        """Format list to Markdown."""
        lines = []
        for item in data:
            if isinstance(item, dict):
                for key, value in item.items():
                    lines.append(f"- **{key}**: {value}")
            else:
                lines.append(f"- {item}")

        return FormattedOutput(content="\n".join(lines), format=self._format)

    def format_equilibrium(
        self, positive: float, negative: float, name: str = ""
    ) -> FormattedOutput:
        """Format equilibrium in Markdown."""
        title = name or "Balance"
        status = "✅ Balanced" if abs(positive - 50) < 0.01 else "⚠️ Imbalanced"

        lines = [
            f"## {title}",
            "",
            "| Component | Value |",
            "|-----------|-------|",
            f"| Positive | {positive:.2f}% |",
            f"| Negative | {negative:.2f}% |",
            f"| Status | {status} |",
            "",
        ]

        return FormattedOutput(content="\n".join(lines), format=self._format)

    def format_duality(
        self, positive_name: str, positive_value: float, negative_name: str, negative_value: float
    ) -> FormattedOutput:
        """Format duality in Markdown."""
        status = "✅" if abs(positive_value - 50) < 0.01 else "⚠️"

        lines = [
            "## Duality",
            "",
            f"| {positive_name} | {negative_name} | Status |",
            "|------------|------------|--------|",
            f"| {positive_value:.2f}% | {negative_value:.2f}% | {status} |",
            "",
        ]

        return FormattedOutput(content="\n".join(lines), format=self._format)


class TableFormatter(Formatter):
    """Table output formatter."""

    def __init__(self, border: str = "│", header_sep: str = "─"):
        super().__init__()
        self._format = OutputFormat.TABLE
        self._border = border
        self._header_sep = header_sep

    def format_data(self, data: Any) -> FormattedOutput:
        """Format any data to table."""
        if isinstance(data, dict):
            return self.format_dict(data)
        elif isinstance(data, list):
            return self.format_list(data)
        else:
            return FormattedOutput(content=str(data), format=self._format)

    def format_dict(self, data: dict[str, Any]) -> FormattedOutput:
        """Format dictionary as key-value table."""
        if not data:
            return FormattedOutput(content="(empty)", format=self._format)

        # Calculate column widths
        key_width = max(len(str(k)) for k in data.keys()) + 2
        val_width = max(len(str(v)) for v in data.values() if not isinstance(v, (dict, list))) + 2
        val_width = max(val_width, 10)

        lines = []
        header = f"┌{'─' * key_width}┬{'─' * val_width}┐"
        lines.append(header)
        lines.append(f"│{'Key':^{key_width}}│{'Value':^{val_width}}│")
        lines.append(f"├{'─' * key_width}┼{'─' * val_width}┤")

        for key, value in data.items():
            if isinstance(value, (dict, list)):
                value = f"[{type(value).__name__}]"
            lines.append(f"│{str(key):<{key_width}}│{str(value):<{val_width}}│")

        lines.append(f"└{'─' * key_width}┴{'─' * val_width}┘")

        return FormattedOutput(content="\n".join(lines), format=self._format)

    def format_list(self, data: list[Any]) -> FormattedOutput:
        """Format list as table."""
        if not data:
            return FormattedOutput(content="(empty)", format=self._format)

        # If list of dicts, create proper table
        if all(isinstance(item, dict) for item in data):
            return self._format_dict_list(data)

        # Simple list
        lines = []
        width = max(len(str(item)) for item in data) + 4

        lines.append(f"┌{'─' * width}┐")
        for i, item in enumerate(data, 1):
            lines.append(f"│ {i}. {str(item):<{width - 4}} │")
        lines.append(f"└{'─' * width}┘")

        return FormattedOutput(content="\n".join(lines), format=self._format)

    def _format_dict_list(self, data: list[dict[str, Any]]) -> FormattedOutput:
        """Format list of dicts as table with columns."""
        if not data:
            return FormattedOutput(content="(empty)", format=self._format)

        # Get all keys
        all_keys = []
        for item in data:
            for key in item.keys():
                if key not in all_keys:
                    all_keys.append(key)

        # Calculate column widths
        widths = {}
        for key in all_keys:
            max_width = len(key)
            for item in data:
                val = item.get(key, "")
                if not isinstance(val, (dict, list)):
                    max_width = max(max_width, len(str(val)))
            widths[key] = max_width + 2

        # Build table
        lines = []

        # Header
        header_border = "┌" + "┬".join("─" * widths[k] for k in all_keys) + "┐"
        header_row = "│" + "│".join(f"{k:^{widths[k]}}" for k in all_keys) + "│"
        header_sep = "├" + "┼".join("─" * widths[k] for k in all_keys) + "┤"

        lines.append(header_border)
        lines.append(header_row)
        lines.append(header_sep)

        # Data rows
        for item in data:
            row_vals = []
            for key in all_keys:
                val = item.get(key, "")
                if isinstance(val, (dict, list)):
                    val = f"[{type(val).__name__}]"
                row_vals.append(f"{str(val):<{widths[key]}}")
            lines.append("│" + "│".join(row_vals) + "│")

        # Footer
        footer = "└" + "┴".join("─" * widths[k] for k in all_keys) + "┘"
        lines.append(footer)

        return FormattedOutput(content="\n".join(lines), format=self._format)

    def format_equilibrium(
        self, positive: float, negative: float, name: str = ""
    ) -> FormattedOutput:
        """Format equilibrium as table."""
        title = name or "Equilibrium"
        balanced = "Yes" if abs(positive - 50) < 0.01 else "No"

        data = {
            "Name": title,
            "Positive": f"{positive:.2f}%",
            "Negative": f"{negative:.2f}%",
            "Balanced": balanced,
        }
        return self.format_dict(data)


def create_formatter(format_type: OutputFormat | str) -> Formatter:
    """
    Factory function to create appropriate formatter.

    Args:
        format_type: Output format type

    Returns:
        Formatter instance
    """
    if isinstance(format_type, str):
        format_type = OutputFormat(format_type.lower())

    formatters = {
        OutputFormat.TEXT: TextFormatter,
        OutputFormat.JSON: JsonFormatter,
        OutputFormat.MARKDOWN: MarkdownFormatter,
        OutputFormat.TABLE: TableFormatter,
    }

    formatter_class = formatters.get(format_type, TextFormatter)
    return formatter_class()
