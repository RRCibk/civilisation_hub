"""
Reporters Module
================
Specialized reporters for different system components.
All reports maintain META 50/50 awareness.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from output.display import ConsoleDisplay, Display


@dataclass
class Report:
    """Container for a generated report."""

    title: str
    sections: dict[str, Any] = field(default_factory=dict)
    summary: str = ""
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "sections": self.sections,
            "summary": self.summary,
            "timestamp": self.timestamp.isoformat(),
            "metadata": self.metadata,
        }

    def add_section(self, name: str, content: Any) -> None:
        self.sections[name] = content


class Reporter(ABC):
    """Abstract base class for reporters."""

    def __init__(self, display: Display | None = None):
        self._display = display or ConsoleDisplay()
        self._reports: list[Report] = []

    @property
    def display(self) -> Display:
        return self._display

    @abstractmethod
    def generate_report(self, data: Any) -> Report:
        """Generate a report from data."""
        pass

    def render_report(self, report: Report) -> None:
        """Render a report to display."""
        self._display.display_title(report.title, level=1)

        for section_name, section_content in report.sections.items():
            self._display.display_section(section_name, section_content)

        if report.summary:
            self._display.display_title("Summary", level=2)
            self._display.render(report.summary)

    def save_report(self, report: Report) -> None:
        """Save report to history."""
        self._reports.append(report)

    def get_reports(self) -> list[Report]:
        """Get all saved reports."""
        return self._reports.copy()


class DomainReporter(Reporter):
    """Reporter for knowledge domains."""

    def generate_report(self, domain: Any) -> Report:
        """Generate domain report."""
        stats = domain.get_domain_stats()
        proof = domain.prove_meta_meaning()

        report = Report(
            title=f"Domain Report: {domain.name}", metadata={"domain_id": str(domain.id)}
        )

        report.add_section(
            "Overview",
            {
                "Name": domain.name,
                "Type": domain.domain_type.value,
                "Description": domain.description,
            },
        )

        report.add_section(
            "Statistics",
            {
                "Total Concepts": stats["concepts"],
                "Axioms": stats["axioms"],
                "Relations": stats["relations"],
                "Average Certainty": f"{stats['average_certainty']:.1f}%",
            },
        )

        if stats.get("concepts_by_type"):
            report.add_section("Concepts by Type", stats["concepts_by_type"])

        if proof.get("duality"):
            duality = proof["duality"]
            report.add_section(
                "Duality",
                {
                    "Positive Pole": duality["positive"],
                    "Negative Pole": duality["negative"],
                    "Balanced": "Yes" if duality["balanced"] else "No",
                },
            )

        report.summary = proof.get("proof", "")
        report.metadata["balanced"] = stats["balanced"]

        return report

    def render_report(self, report: Report) -> None:
        """Render domain report with balance visualization."""
        super().render_report(report)

        if report.metadata.get("balanced"):
            self._display.display_balance_bar(50, 50, label="Domain Balance")


class EquilibriumReporter(Reporter):
    """Reporter for equilibrium states."""

    def generate_report(self, equilibrium: Any) -> Report:
        """Generate equilibrium report."""
        report = Report(title="Equilibrium Report")

        # META Balance
        meta_balance = equilibrium.get_meta_balance()
        report.add_section(
            "META Balance",
            {
                "Positive": f"{meta_balance['positive']:.2f}%",
                "Negative": f"{meta_balance['negative']:.2f}%",
                "Balanced": "Yes" if meta_balance["balanced"] else "No",
            },
        )

        # Operational Ratio
        op_ratio = equilibrium.get_operational_ratio()
        report.add_section(
            "Operational Ratio",
            {
                "Structure": f"{op_ratio['structure']:.2f}%",
                "Flexibility": f"{op_ratio['flexibility']:.2f}%",
                "Ratio": f"{op_ratio['ratio']:.4f}",
            },
        )

        # Validation
        report.add_section(
            "Validation",
            {
                "META Valid": "Yes" if equilibrium.validate_meta() else "No",
                "Operational Valid": "Yes" if equilibrium.validate_operational() else "No",
            },
        )

        report.summary = "META 50/50 equilibrium enables balanced system operation."
        report.metadata["meta_valid"] = equilibrium.validate_meta()

        return report

    def render_report(self, report: Report) -> None:
        """Render equilibrium report with visual bars."""
        self._display.display_title(report.title, level=1)

        # META section
        if "META Balance" in report.sections:
            self._display.display_title("META Balance", level=2)
            self._display.display_balance_bar(50, 50, label="META 50/50")

        # Operational section
        if "Operational Ratio" in report.sections:
            self._display.display_title("Operational Ratio", level=2)
            self._display.display_balance_bar(52, 48, label="Operational 52/48")

        for section_name, section_content in report.sections.items():
            if section_name not in ["META Balance", "Operational Ratio"]:
                self._display.display_section(section_name, section_content)

        if report.summary:
            self._display.render(f"\n{report.summary}")


class EvolutionReporter(Reporter):
    """Reporter for evolution tracking."""

    def generate_report(self, tracker: Any) -> Report:
        """Generate evolution report."""
        report = Report(title="Evolution Report")

        # Current state
        current = tracker.get_current_state()
        report.add_section(
            "Current State",
            {
                "Phase": current.phase.value,
                "Progress": f"{current.progress:.1f}%",
                "Generation": current.generation,
            },
        )

        # Metrics
        metrics = tracker.get_metrics()
        report.add_section(
            "Metrics",
            {
                "Total Transitions": metrics.total_transitions,
                "Phase Distribution": metrics.phase_distribution,
                "Average Progress": f"{metrics.average_progress:.1f}%",
            },
        )

        # Recent changes
        recent = tracker.get_recent_deltas(5)
        if recent:
            report.add_section(
                "Recent Changes",
                [
                    {
                        "From": d.from_state.phase.value if d.from_state else "None",
                        "To": d.to_state.phase.value,
                        "Delta": f"{d.progress_delta:+.1f}%",
                    }
                    for d in recent
                ],
            )

        report.summary = (
            f"Evolution at generation {current.generation}, phase {current.phase.value}"
        )
        return report


class ParticipationReporter(Reporter):
    """Reporter for participation tracking."""

    def generate_report(self, tracker: Any) -> Report:
        """Generate participation report."""
        report = Report(title="Participation Report")

        # Overall stats
        metrics = tracker.get_metrics()
        report.add_section(
            "Overview",
            {
                "Total Participants": metrics.total_participants,
                "Active Participants": metrics.active_participants,
                "Overall Engagement": f"{metrics.overall_engagement:.1f}%",
            },
        )

        # Distribution
        report.add_section("Level Distribution", metrics.level_distribution)

        # Balance
        balance = metrics.give_receive_balance
        report.add_section(
            "Give/Receive Balance",
            {
                "Give": f"{balance['give']:.2f}%",
                "Receive": f"{balance['receive']:.2f}%",
                "Balanced": "Yes" if balance["balanced"] else "No",
            },
        )

        report.summary = (
            f"{metrics.active_participants} active of {metrics.total_participants} total"
        )
        return report


class VerificationReporter(Reporter):
    """Reporter for verification results."""

    def generate_report(self, verifier: Any) -> Report:
        """Generate verification report."""
        report = Report(title="Verification Report")

        # Results summary
        results = verifier.get_all_results()
        passed = sum(1 for r in results if r.is_valid)
        failed = len(results) - passed

        report.add_section(
            "Summary",
            {
                "Total Claims": len(results),
                "Passed": passed,
                "Failed": failed,
                "Pass Rate": f"{(passed / len(results) * 100) if results else 0:.1f}%",
            },
        )

        # Failed claims
        failed_results = [r for r in results if not r.is_valid]
        if failed_results:
            report.add_section(
                "Failed Claims",
                [{"Claim": r.claim.name, "Reason": r.message} for r in failed_results[:10]],
            )

        # Balance verification
        balance_results = [r for r in results if "balance" in r.claim.name.lower()]
        if balance_results:
            report.add_section(
                "Balance Verifications",
                [
                    {
                        "Claim": r.claim.name,
                        "Status": "✓" if r.is_valid else "✗",
                        "Confidence": f"{r.confidence:.1f}%",
                    }
                    for r in balance_results
                ],
            )

        report.summary = f"Verification: {passed}/{len(results)} passed ({failed} failed)"
        report.metadata["all_passed"] = failed == 0

        return report


class SystemReporter(Reporter):
    """Comprehensive system reporter combining all aspects."""

    def __init__(self, display: Display | None = None):
        super().__init__(display)
        self._domain_reporter = DomainReporter(display)
        self._equilibrium_reporter = EquilibriumReporter(display)
        self._evolution_reporter = EvolutionReporter(display)
        self._participation_reporter = ParticipationReporter(display)
        self._verification_reporter = VerificationReporter(display)

    def generate_report(self, system: Any) -> Report:
        """Generate comprehensive system report."""
        report = Report(title="Civilisation Hub System Report")

        # System overview
        report.add_section(
            "System Overview",
            {
                "Name": "Civilisation Hub",
                "Version": "1.0.0",
                "Principle": "META 50/50 Equilibrium",
            },
        )

        # META Foundation
        report.add_section(
            "META Foundation",
            {
                "META Balance": "50/50 (Absolute)",
                "Operational Ratio": "52/48 (Enabling)",
                "Derived From": "PI/6 ≈ 0.5236",
            },
        )

        # Components
        if hasattr(system, "domains"):
            report.add_section(
                "Domains",
                {
                    "Count": len(system.domains),
                    "Active": sum(1 for d in system.domains if d.validate_balance()),
                },
            )

        report.summary = "System maintains META 50/50 equilibrium across all components."
        return report

    def generate_full_report(
        self,
        domains: list[Any] | None = None,
        equilibrium: Any | None = None,
        evolution: Any | None = None,
        participation: Any | None = None,
        verification: Any | None = None,
    ) -> Report:
        """Generate full system report with all components."""
        report = Report(title="Full System Report")

        # System section
        report.add_section(
            "System",
            {
                "Name": "Civilisation Hub",
                "Principle": "META 50/50",
                "Timestamp": datetime.now().isoformat(),
            },
        )

        # Domains section
        if domains:
            domain_summaries = []
            for domain in domains:
                domain_summaries.append(
                    {
                        "Name": domain.name,
                        "Concepts": domain.concept_count,
                        "Balanced": domain.validate_balance(),
                    }
                )
            report.add_section("Domains", domain_summaries)

        # Equilibrium section
        if equilibrium:
            eq_report = self._equilibrium_reporter.generate_report(equilibrium)
            report.add_section("Equilibrium", eq_report.sections)

        # Evolution section
        if evolution:
            evo_report = self._evolution_reporter.generate_report(evolution)
            report.add_section("Evolution", evo_report.sections)

        # Participation section
        if participation:
            part_report = self._participation_reporter.generate_report(participation)
            report.add_section("Participation", part_report.sections)

        # Verification section
        if verification:
            ver_report = self._verification_reporter.generate_report(verification)
            report.add_section("Verification", ver_report.sections)

        # Overall status
        all_balanced = all(d.validate_balance() for d in (domains or []))
        report.metadata["all_balanced"] = all_balanced
        report.summary = (
            "All systems balanced and operational."
            if all_balanced
            else "Some systems require balance adjustment."
        )

        return report

    def render_report(self, report: Report) -> None:
        """Render full system report."""
        self._display.display_meta_50_50()
        super().render_report(report)


def create_reporter(reporter_type: str, display: Display | None = None) -> Reporter:
    """
    Factory function to create appropriate reporter.

    Args:
        reporter_type: Type of reporter
        display: Display instance to use

    Returns:
        Reporter instance
    """
    reporters = {
        "domain": DomainReporter,
        "equilibrium": EquilibriumReporter,
        "evolution": EvolutionReporter,
        "participation": ParticipationReporter,
        "verification": VerificationReporter,
        "system": SystemReporter,
    }

    reporter_class = reporters.get(reporter_type.lower(), SystemReporter)
    return reporter_class(display)
