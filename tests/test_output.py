"""
Tests for Output Module
=======================
Tests for formatters, display, and reporters.
"""

import pytest
import json
from datetime import datetime

from output.formatters import (
    OutputFormat,
    Formatter,
    FormattedOutput,
    TextFormatter,
    JsonFormatter,
    MarkdownFormatter,
    TableFormatter,
    create_formatter,
)
from output.display import (
    Display,
    ConsoleDisplay,
    BufferedDisplay,
    DisplayConfig,
    DisplayStyle,
    create_display,
)
from output.reporters import (
    Report,
    Reporter,
    DomainReporter,
    EquilibriumReporter,
    SystemReporter,
    create_reporter,
)


# =============================================================================
# FormattedOutput Tests
# =============================================================================

class TestFormattedOutput:
    """Tests for FormattedOutput container."""

    def test_creation(self):
        """Test basic creation."""
        output = FormattedOutput(
            content="test content",
            format=OutputFormat.TEXT
        )
        assert output.content == "test content"
        assert output.format == OutputFormat.TEXT

    def test_length(self):
        """Test length property."""
        output = FormattedOutput(content="12345", format=OutputFormat.TEXT)
        assert output.length == 5

    def test_to_dict(self):
        """Test dictionary conversion."""
        output = FormattedOutput(
            content="test",
            format=OutputFormat.JSON,
            metadata={"key": "value"}
        )
        d = output.to_dict()
        assert d["content"] == "test"
        assert d["format"] == "json"
        assert d["metadata"]["key"] == "value"
        assert "timestamp" in d

    def test_timestamp(self):
        """Test timestamp is set."""
        output = FormattedOutput(content="", format=OutputFormat.TEXT)
        assert isinstance(output.timestamp, datetime)


# =============================================================================
# TextFormatter Tests
# =============================================================================

class TestTextFormatter:
    """Tests for TextFormatter."""

    def test_creation(self):
        """Test formatter creation."""
        formatter = TextFormatter()
        assert formatter.format == OutputFormat.TEXT

    def test_format_string(self):
        """Test formatting a string."""
        formatter = TextFormatter()
        output = formatter.format_data("hello")
        assert output.content == "hello"

    def test_format_dict(self):
        """Test formatting a dictionary."""
        formatter = TextFormatter()
        data = {"name": "test", "value": 42}
        output = formatter.format_dict(data)
        assert "name: test" in output.content
        assert "value: 42" in output.content

    def test_format_nested_dict(self):
        """Test formatting nested dictionary."""
        formatter = TextFormatter()
        data = {
            "outer": {
                "inner": "value"
            }
        }
        output = formatter.format_dict(data)
        assert "outer:" in output.content
        assert "inner: value" in output.content

    def test_format_list(self):
        """Test formatting a list."""
        formatter = TextFormatter()
        data = ["item1", "item2", "item3"]
        output = formatter.format_list(data)
        assert "1. item1" in output.content
        assert "2. item2" in output.content

    def test_format_equilibrium(self):
        """Test formatting equilibrium."""
        formatter = TextFormatter()
        output = formatter.format_equilibrium(50, 50, "Test Balance")
        assert "Test Balance" in output.content
        assert "50.00%" in output.content
        assert "BALANCED" in output.content

    def test_format_imbalanced(self):
        """Test formatting imbalanced state."""
        formatter = TextFormatter()
        output = formatter.format_equilibrium(60, 40, "Imbalanced")
        assert "IMBALANCED" in output.content

    def test_format_duality(self):
        """Test formatting duality."""
        formatter = TextFormatter()
        output = formatter.format_duality("positive", 50, "negative", 50)
        assert "positive" in output.content
        assert "negative" in output.content


# =============================================================================
# JsonFormatter Tests
# =============================================================================

class TestJsonFormatter:
    """Tests for JsonFormatter."""

    def test_creation(self):
        """Test formatter creation."""
        formatter = JsonFormatter()
        assert formatter.format == OutputFormat.JSON

    def test_format_dict(self):
        """Test formatting dictionary to JSON."""
        formatter = JsonFormatter()
        data = {"key": "value", "number": 42}
        output = formatter.format_dict(data)

        parsed = json.loads(output.content)
        assert parsed["key"] == "value"
        assert parsed["number"] == 42

    def test_format_list(self):
        """Test formatting list to JSON."""
        formatter = JsonFormatter()
        data = [1, 2, 3, "four"]
        output = formatter.format_list(data)

        parsed = json.loads(output.content)
        assert parsed == [1, 2, 3, "four"]

    def test_format_with_indent(self):
        """Test JSON indentation."""
        formatter = JsonFormatter(indent=4)
        data = {"key": "value"}
        output = formatter.format_dict(data)
        assert "    " in output.content  # 4-space indent

    def test_format_sorted_keys(self):
        """Test sorted keys option."""
        formatter = JsonFormatter(sort_keys=True)
        data = {"z": 1, "a": 2, "m": 3}
        output = formatter.format_dict(data)
        # Keys should appear in sorted order
        a_pos = output.content.find('"a"')
        m_pos = output.content.find('"m"')
        z_pos = output.content.find('"z"')
        assert a_pos < m_pos < z_pos


# =============================================================================
# MarkdownFormatter Tests
# =============================================================================

class TestMarkdownFormatter:
    """Tests for MarkdownFormatter."""

    def test_creation(self):
        """Test formatter creation."""
        formatter = MarkdownFormatter()
        assert formatter.format == OutputFormat.MARKDOWN

    def test_format_dict(self):
        """Test formatting dict to markdown."""
        formatter = MarkdownFormatter()
        data = {"title": "Test", "value": 100}
        output = formatter.format_dict(data)
        assert "**title**" in output.content
        assert "**value**" in output.content

    def test_format_list(self):
        """Test formatting list to markdown."""
        formatter = MarkdownFormatter()
        data = ["item1", "item2"]
        output = formatter.format_list(data)
        assert "- item1" in output.content
        assert "- item2" in output.content

    def test_format_equilibrium(self):
        """Test equilibrium markdown table."""
        formatter = MarkdownFormatter()
        output = formatter.format_equilibrium(50, 50, "Balance")
        assert "## Balance" in output.content
        assert "| Component | Value |" in output.content
        assert "✅ Balanced" in output.content


# =============================================================================
# TableFormatter Tests
# =============================================================================

class TestTableFormatter:
    """Tests for TableFormatter."""

    def test_creation(self):
        """Test formatter creation."""
        formatter = TableFormatter()
        assert formatter.format == OutputFormat.TABLE

    def test_format_dict(self):
        """Test formatting dict as table."""
        formatter = TableFormatter()
        data = {"Name": "Test", "Value": 42}
        output = formatter.format_dict(data)
        assert "Name" in output.content
        assert "Value" in output.content
        assert "─" in output.content  # Border characters

    def test_format_empty_dict(self):
        """Test formatting empty dict."""
        formatter = TableFormatter()
        output = formatter.format_dict({})
        assert "(empty)" in output.content

    def test_format_list(self):
        """Test formatting list as table."""
        formatter = TableFormatter()
        data = ["a", "b", "c"]
        output = formatter.format_list(data)
        assert "1. a" in output.content
        assert "2. b" in output.content

    def test_format_dict_list(self):
        """Test formatting list of dicts."""
        formatter = TableFormatter()
        data = [
            {"id": 1, "name": "A"},
            {"id": 2, "name": "B"},
        ]
        output = formatter.format_list(data)
        assert "id" in output.content
        assert "name" in output.content


# =============================================================================
# create_formatter Tests
# =============================================================================

class TestCreateFormatter:
    """Tests for formatter factory."""

    def test_create_text(self):
        """Test creating text formatter."""
        formatter = create_formatter(OutputFormat.TEXT)
        assert isinstance(formatter, TextFormatter)

    def test_create_json(self):
        """Test creating JSON formatter."""
        formatter = create_formatter(OutputFormat.JSON)
        assert isinstance(formatter, JsonFormatter)

    def test_create_markdown(self):
        """Test creating markdown formatter."""
        formatter = create_formatter(OutputFormat.MARKDOWN)
        assert isinstance(formatter, MarkdownFormatter)

    def test_create_table(self):
        """Test creating table formatter."""
        formatter = create_formatter(OutputFormat.TABLE)
        assert isinstance(formatter, TableFormatter)

    def test_create_from_string(self):
        """Test creating formatter from string."""
        formatter = create_formatter("json")
        assert isinstance(formatter, JsonFormatter)


# =============================================================================
# DisplayConfig Tests
# =============================================================================

class TestDisplayConfig:
    """Tests for DisplayConfig."""

    def test_defaults(self):
        """Test default configuration."""
        config = DisplayConfig()
        assert config.style == DisplayStyle.STANDARD
        assert config.format == OutputFormat.TEXT
        assert config.show_timestamps is False
        assert config.show_balance_indicators is True

    def test_custom_config(self):
        """Test custom configuration."""
        config = DisplayConfig(
            style=DisplayStyle.DETAILED,
            format=OutputFormat.JSON,
            show_timestamps=True
        )
        assert config.style == DisplayStyle.DETAILED
        assert config.format == OutputFormat.JSON
        assert config.show_timestamps is True


# =============================================================================
# BufferedDisplay Tests
# =============================================================================

class TestBufferedDisplay:
    """Tests for BufferedDisplay."""

    def test_creation(self):
        """Test display creation."""
        display = BufferedDisplay()
        assert display is not None

    def test_render_to_buffer(self):
        """Test rendering captures to buffer."""
        display = BufferedDisplay()
        display.render("test line")
        assert "test line" in display.get_buffer()

    def test_get_buffer_content(self):
        """Test getting buffer as string."""
        display = BufferedDisplay()
        display.render("line 1")
        display.render("line 2")
        content = display.get_buffer_content()
        assert "line 1" in content
        assert "line 2" in content

    def test_clear_buffer(self):
        """Test clearing buffer."""
        display = BufferedDisplay()
        display.render("test")
        display.clear_buffer()
        assert len(display.get_buffer()) == 0

    def test_display_data(self):
        """Test displaying data."""
        display = BufferedDisplay()
        display.display({"key": "value"})
        assert "key" in display.get_buffer_content()

    def test_display_equilibrium(self):
        """Test displaying equilibrium."""
        display = BufferedDisplay()
        display.display_equilibrium(50, 50, "Test")
        content = display.get_buffer_content()
        assert "Test" in content
        assert "50" in content

    def test_display_balance_bar(self):
        """Test displaying balance bar."""
        display = BufferedDisplay()
        display.display_balance_bar(50, 50, label="Balance")
        content = display.get_buffer_content()
        assert "Balance" in content
        assert "█" in content or "50" in content


# =============================================================================
# ConsoleDisplay Tests
# =============================================================================

class TestConsoleDisplay:
    """Tests for ConsoleDisplay."""

    def test_creation(self):
        """Test display creation."""
        display = ConsoleDisplay()
        assert display is not None
        assert display.config.format == OutputFormat.TEXT

    def test_display_title(self):
        """Test title display (use buffered for testing)."""
        display = BufferedDisplay()
        display.display_title("Test Title", level=1)
        content = display.get_buffer_content()
        assert "Test Title" in content
        assert "═" in content

    def test_display_section(self):
        """Test section display."""
        display = BufferedDisplay()
        display.display_section("Section", {"key": "value"})
        content = display.get_buffer_content()
        assert "Section" in content

    def test_display_meta_50_50(self):
        """Test META 50/50 display."""
        display = BufferedDisplay()
        display.display_meta_50_50()
        content = display.get_buffer_content()
        assert "META" in content
        assert "50" in content


# =============================================================================
# create_display Tests
# =============================================================================

class TestCreateDisplay:
    """Tests for display factory."""

    def test_create_default(self):
        """Test creating default display."""
        display = create_display()
        assert isinstance(display, ConsoleDisplay)

    def test_create_buffered(self):
        """Test creating buffered display."""
        display = create_display(buffered=True)
        assert isinstance(display, BufferedDisplay)

    def test_create_with_style(self):
        """Test creating with style."""
        display = create_display(style=DisplayStyle.DETAILED)
        assert display.config.style == DisplayStyle.DETAILED


# =============================================================================
# Report Tests
# =============================================================================

class TestReport:
    """Tests for Report class."""

    def test_creation(self):
        """Test report creation."""
        report = Report(title="Test Report")
        assert report.title == "Test Report"
        assert len(report.sections) == 0

    def test_add_section(self):
        """Test adding sections."""
        report = Report(title="Test")
        report.add_section("Overview", {"key": "value"})
        assert "Overview" in report.sections
        assert report.sections["Overview"]["key"] == "value"

    def test_to_dict(self):
        """Test dictionary conversion."""
        report = Report(
            title="Test",
            summary="Test summary"
        )
        report.add_section("Data", {"x": 1})

        d = report.to_dict()
        assert d["title"] == "Test"
        assert d["summary"] == "Test summary"
        assert "Data" in d["sections"]


# =============================================================================
# DomainReporter Tests
# =============================================================================

class TestDomainReporter:
    """Tests for DomainReporter."""

    def test_creation(self):
        """Test reporter creation."""
        display = BufferedDisplay()
        reporter = DomainReporter(display)
        assert reporter.display is display

    def test_generate_report(self):
        """Test report generation with mock domain."""
        from unittest.mock import MagicMock
        from uuid import uuid4

        # Create mock domain
        mock_domain = MagicMock()
        mock_domain.name = "TestDomain"
        mock_domain.id = uuid4()
        mock_domain.domain_type.value = "fundamental"
        mock_domain.description = "Test description"
        mock_domain.get_domain_stats.return_value = {
            "concepts": 10,
            "axioms": 2,
            "relations": 5,
            "average_certainty": 75.0,
            "balanced": True,
            "concepts_by_type": {"definition": 5, "theorem": 5}
        }
        mock_domain.prove_meta_meaning.return_value = {
            "duality": {
                "positive": "pos",
                "negative": "neg",
                "balanced": True
            },
            "proof": "Domain is balanced"
        }

        reporter = DomainReporter(BufferedDisplay())
        report = reporter.generate_report(mock_domain)

        assert "TestDomain" in report.title
        assert "Overview" in report.sections
        assert "Statistics" in report.sections


# =============================================================================
# SystemReporter Tests
# =============================================================================

class TestSystemReporter:
    """Tests for SystemReporter."""

    def test_creation(self):
        """Test reporter creation."""
        reporter = SystemReporter()
        assert reporter is not None

    def test_generate_report(self):
        """Test system report generation."""
        from unittest.mock import MagicMock

        mock_system = MagicMock()
        mock_system.domains = []

        reporter = SystemReporter(BufferedDisplay())
        report = reporter.generate_report(mock_system)

        assert "System" in report.title
        assert "System Overview" in report.sections


# =============================================================================
# create_reporter Tests
# =============================================================================

class TestCreateReporter:
    """Tests for reporter factory."""

    def test_create_domain(self):
        """Test creating domain reporter."""
        reporter = create_reporter("domain")
        assert isinstance(reporter, DomainReporter)

    def test_create_system(self):
        """Test creating system reporter."""
        reporter = create_reporter("system")
        assert isinstance(reporter, SystemReporter)

    def test_create_with_display(self):
        """Test creating with custom display."""
        display = BufferedDisplay()
        reporter = create_reporter("domain", display)
        assert reporter.display is display


# =============================================================================
# Integration Tests
# =============================================================================

class TestOutputIntegration:
    """Integration tests for output module."""

    def test_format_and_display(self):
        """Test formatting and displaying data."""
        display = BufferedDisplay()
        formatter = TextFormatter()

        data = {"name": "Test", "value": 42}
        output = formatter.format_dict(data)
        display.render_formatted(output)

        content = display.get_buffer_content()
        assert "name" in content
        assert "42" in content

    def test_equilibrium_display_chain(self):
        """Test equilibrium display through full chain."""
        display = BufferedDisplay()

        display.display_equilibrium(50, 50, "META Balance")
        content = display.get_buffer_content()

        assert "META" in content
        assert "50" in content
        assert "BALANCED" in content

    def test_report_render_chain(self):
        """Test report rendering chain."""
        display = BufferedDisplay()
        reporter = SystemReporter(display)

        from unittest.mock import MagicMock
        mock_system = MagicMock()
        mock_system.domains = []

        report = reporter.generate_report(mock_system)
        reporter.render_report(report)

        content = display.get_buffer_content()
        assert len(content) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
