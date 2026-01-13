"""
Display Module
==============
Console display and output rendering with META 50/50 balance awareness.
"""

import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, TextIO

from output.formatters import (
    OutputFormat,
    Formatter,
    FormattedOutput,
    create_formatter,
)


class DisplayStyle(Enum):
    """Display style presets."""
    MINIMAL = "minimal"
    STANDARD = "standard"
    DETAILED = "detailed"
    BALANCED = "balanced"  # Special style for META 50/50 display


@dataclass
class DisplayConfig:
    """Configuration for display output."""
    style: DisplayStyle = DisplayStyle.STANDARD
    format: OutputFormat = OutputFormat.TEXT
    show_timestamps: bool = False
    show_balance_indicators: bool = True
    color_enabled: bool = True
    indent_size: int = 2
    max_width: int = 120


class Display(ABC):
    """Abstract base class for display output."""

    def __init__(self, config: DisplayConfig | None = None):
        self._config = config or DisplayConfig()
        self._formatter = create_formatter(self._config.format)
        self._output_history: list[FormattedOutput] = []

    @property
    def config(self) -> DisplayConfig:
        return self._config

    @property
    def formatter(self) -> Formatter:
        return self._formatter

    @abstractmethod
    def render(self, content: str) -> None:
        """Render content to display."""
        pass

    @abstractmethod
    def render_formatted(self, output: FormattedOutput) -> None:
        """Render formatted output."""
        pass

    def display(self, data: Any) -> None:
        """Format and display data."""
        formatted = self._formatter.format_data(data)
        self._output_history.append(formatted)
        self.render_formatted(formatted)

    def display_dict(self, data: dict[str, Any]) -> None:
        """Format and display dictionary."""
        formatted = self._formatter.format_dict(data)
        self._output_history.append(formatted)
        self.render_formatted(formatted)

    def display_list(self, data: list[Any]) -> None:
        """Format and display list."""
        formatted = self._formatter.format_list(data)
        self._output_history.append(formatted)
        self.render_formatted(formatted)

    def display_equilibrium(
        self,
        positive: float,
        negative: float,
        name: str = ""
    ) -> None:
        """Display equilibrium balance."""
        formatted = self._formatter.format_equilibrium(positive, negative, name)
        self._output_history.append(formatted)
        self.render_formatted(formatted)

    def display_duality(
        self,
        positive_name: str,
        positive_value: float,
        negative_name: str,
        negative_value: float
    ) -> None:
        """Display duality balance."""
        formatted = self._formatter.format_duality(
            positive_name, positive_value,
            negative_name, negative_value
        )
        self._output_history.append(formatted)
        self.render_formatted(formatted)

    def clear_history(self) -> None:
        """Clear output history."""
        self._output_history.clear()

    def get_history(self) -> list[FormattedOutput]:
        """Get output history."""
        return self._output_history.copy()


class ConsoleDisplay(Display):
    """Console/terminal display implementation."""

    # ANSI color codes
    COLORS = {
        "reset": "\033[0m",
        "bold": "\033[1m",
        "dim": "\033[2m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
    }

    def __init__(
        self,
        config: DisplayConfig | None = None,
        output: TextIO | None = None
    ):
        super().__init__(config)
        self._output = output or sys.stdout

    def render(self, content: str) -> None:
        """Render content to console."""
        self._output.write(content)
        self._output.write("\n")
        self._output.flush()

    def render_formatted(self, output: FormattedOutput) -> None:
        """Render formatted output to console."""
        content = output.content

        if self._config.show_timestamps:
            timestamp = output.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            content = f"[{timestamp}]\n{content}"

        # Add balance indicator if applicable
        if self._config.show_balance_indicators and output.metadata.get("balanced") is not None:
            if output.metadata["balanced"]:
                indicator = self._colorize("✓", "green") if self._config.color_enabled else "✓"
            else:
                indicator = self._colorize("⚠", "yellow") if self._config.color_enabled else "⚠"
            content = f"{indicator} {content}"

        self.render(content)

    def _colorize(self, text: str, color: str) -> str:
        """Apply color to text if enabled."""
        if not self._config.color_enabled:
            return text
        color_code = self.COLORS.get(color, "")
        reset = self.COLORS["reset"]
        return f"{color_code}{text}{reset}"

    def display_title(self, title: str, level: int = 1) -> None:
        """Display a title with formatting."""
        if level == 1:
            border = "═" * len(title)
            if self._config.color_enabled:
                title = self._colorize(title, "bold")
            self.render(f"\n{border}\n{title}\n{border}")
        elif level == 2:
            border = "─" * len(title)
            self.render(f"\n{title}\n{border}")
        else:
            self.render(f"\n{title}")

    def display_section(self, title: str, content: Any) -> None:
        """Display a section with title and content."""
        self.display_title(title, level=2)
        self.display(content)

    def display_balance_bar(
        self,
        positive: float,
        negative: float,
        width: int = 50,
        label: str = ""
    ) -> None:
        """Display a visual balance bar."""
        pos_width = int(width * positive / 100)
        neg_width = width - pos_width

        pos_char = self._colorize("█", "green") if self._config.color_enabled else "█"
        neg_char = self._colorize("░", "red") if self._config.color_enabled else "░"

        bar = f"[{pos_char * pos_width}{neg_char * neg_width}]"

        if label:
            self.render(f"{label}: {bar} ({positive:.1f}% / {negative:.1f}%)")
        else:
            self.render(f"{bar} ({positive:.1f}% / {negative:.1f}%)")

    def display_meta_50_50(self) -> None:
        """Display META 50/50 equilibrium state."""
        title = "META 50/50 EQUILIBRIUM"
        self.display_title(title, level=1)

        content = [
            "The fundamental principle of perfect balance:",
            "",
            "  Positive: 50%  ←→  Negative: 50%",
            "",
            "  All systems derive from this balance.",
            "  OPERATIONAL 52/48 enables META 50/50.",
            ""
        ]

        self.display_balance_bar(50, 50, label="META Balance")
        for line in content:
            self.render(line)

    def display_operational_52_48(self) -> None:
        """Display OPERATIONAL 52/48 ratio."""
        title = "OPERATIONAL 52/48"
        self.display_title(title, level=2)

        content = [
            "The enabling ratio for META 50/50:",
            "",
            "  Structure: 52%  ←→  Flexibility: 48%",
            "",
            "  Derived from PI/6 ≈ 0.5236",
            ""
        ]

        self.display_balance_bar(52, 48, label="Operational")
        for line in content:
            self.render(line)

    def display_proof(
        self,
        claim: str,
        evidence: list[str],
        conclusion: str,
        balanced: bool
    ) -> None:
        """Display a proof structure."""
        self.display_title("Proof", level=2)

        status = self._colorize("✓ VALID", "green") if balanced else self._colorize("✗ INVALID", "red")
        if not self._config.color_enabled:
            status = "✓ VALID" if balanced else "✗ INVALID"

        self.render(f"Claim: {claim}")
        self.render("\nEvidence:")
        for i, e in enumerate(evidence, 1):
            self.render(f"  {i}. {e}")
        self.render(f"\nConclusion: {conclusion}")
        self.render(f"\nStatus: {status}")

    def display_domain_summary(
        self,
        name: str,
        duality: tuple[str, str],
        concepts: int,
        balanced: bool
    ) -> None:
        """Display domain summary."""
        self.display_title(f"Domain: {name}", level=2)

        status = "✓ Balanced" if balanced else "⚠ Imbalanced"
        if self._config.color_enabled:
            status = self._colorize(status, "green" if balanced else "yellow")

        self.render(f"  Duality: {duality[0]} ↔ {duality[1]}")
        self.render(f"  Concepts: {concepts}")
        self.render(f"  Status: {status}")
        self.display_balance_bar(50, 50, width=30, label="  Balance")


class BufferedDisplay(ConsoleDisplay):
    """Buffered display that captures output."""

    def __init__(self, config: DisplayConfig | None = None):
        super().__init__(config)
        self._buffer: list[str] = []

    def render(self, content: str) -> None:
        """Capture content to buffer."""
        self._buffer.append(content)

    def get_buffer(self) -> list[str]:
        """Get buffered content."""
        return self._buffer.copy()

    def get_buffer_content(self) -> str:
        """Get all buffered content as string."""
        return "\n".join(self._buffer)

    def clear_buffer(self) -> None:
        """Clear the buffer."""
        self._buffer.clear()

    def flush_to_console(self) -> None:
        """Flush buffer to actual console."""
        for line in self._buffer:
            print(line)
        self._buffer.clear()


def create_display(
    style: DisplayStyle = DisplayStyle.STANDARD,
    format_type: OutputFormat = OutputFormat.TEXT,
    buffered: bool = False
) -> Display:
    """
    Factory function to create display instance.

    Args:
        style: Display style preset
        format_type: Output format
        buffered: Whether to use buffered display

    Returns:
        Display instance
    """
    config = DisplayConfig(style=style, format=format_type)

    if buffered:
        return BufferedDisplay(config)
    return ConsoleDisplay(config)
