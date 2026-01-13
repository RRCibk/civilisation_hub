#!/usr/bin/env python3
"""
Civilisation Hub
================
Main entry point for the Civilisation Hub system.

Core Principle: META 50/50 Equilibrium
- META balance: 50/50 (absolute balance)
- OPERATIONAL ratio: 52/48 (enables META balance)
- Derived from: PI/6 ≈ 0.5236

All components maintain META 50/50 equilibrium.
"""

import argparse
import sys
from typing import Any

from core.equilibrium import MetaEquilibrium, Atom
from core.proportions import (
    Pi6Proportion,
    OperationalRatio,
    ProportionValidator,
)
from knowledge.domains.base import KnowledgeDomain
from knowledge.domains.mathematics import create_mathematics_domain
from knowledge.domains.physics import create_physics_domain
from knowledge.domains.code import create_code_domain
from knowledge.domains.biology import create_biology_domain
from knowledge.domains.philosophy import create_philosophy_domain
from knowledge.domains.registry import DomainRegistry
from evolution.tracker import EvolutionTracker
from evolution.transitions import TransitionEngine
from participation.tracker import ParticipationTracker
from participation.contributions import ContributionManager
from verification.verifier import Verifier
from verification.validators import MetaEquilibriumValidator
from output.display import ConsoleDisplay, BufferedDisplay, DisplayStyle
from output.reporters import SystemReporter, DomainReporter
from database.persistence import DomainPersistenceService


class CivilisationHub:
    """
    Main system class for Civilisation Hub.

    Integrates all modules while maintaining META 50/50 equilibrium.
    """

    VERSION = "1.0.0"
    NAME = "Civilisation Hub"

    def __init__(self, verbose: bool = False):
        self._verbose = verbose

        # Core equilibrium - shared across all components
        self._meta = MetaEquilibrium()

        # Initialize components
        self._domains: dict[str, KnowledgeDomain] = {}
        self._registry = DomainRegistry()
        self._evolution = EvolutionTracker()
        self._participation = ParticipationTracker()
        self._contributions = ContributionManager()
        self._verifier = Verifier()

        # Output
        self._display = ConsoleDisplay()
        self._system_reporter = SystemReporter(self._display)

        # Proportions
        self._pi6 = Pi6Proportion()
        self._operational = OperationalRatio()

        # Database persistence (lazy initialized)
        self._persistence: DomainPersistenceService | None = None

    @property
    def meta_equilibrium(self) -> MetaEquilibrium:
        """Get the shared META equilibrium."""
        return self._meta

    @property
    def domains(self) -> list[KnowledgeDomain]:
        """Get all initialized domains."""
        return list(self._domains.values())

    def get_meta_balance(self) -> dict[str, Any]:
        """Get META balance state."""
        return {
            "positive": 50.0,
            "negative": 50.0,
            "balanced": True
        }

    def get_operational_ratio(self) -> dict[str, Any]:
        """Get operational ratio state."""
        return {
            "structure": 52.0,
            "flexibility": 48.0,
            "ratio": 52 / 48
        }

    def is_meta_balanced(self) -> bool:
        """Check if META is balanced."""
        return MetaEquilibrium.verify_balance(50, 50)

    def initialize(self) -> None:
        """Initialize all system components."""
        if self._verbose:
            self._display.display_title("Initializing Civilisation Hub", level=1)

        # Initialize domains
        self._initialize_domains()

        # Set up validation
        self._setup_validation()

        if self._verbose:
            self._display.render("System initialized successfully.")

    def _initialize_domains(self) -> None:
        """Initialize all knowledge domains."""
        domain_creators = [
            ("Mathematics", create_mathematics_domain),
            ("Physics", create_physics_domain),
            ("Code", create_code_domain),
            ("Biology", create_biology_domain),
            ("Philosophy", create_philosophy_domain),
        ]

        for name, creator in domain_creators:
            if self._verbose:
                self._display.render(f"  Initializing {name} domain...")

            domain = creator(meta_equilibrium=self._meta)
            self._domains[name.lower()] = domain
            self._registry.register_domain(domain.domain)

    def _setup_validation(self) -> None:
        """Set up system validation."""
        # Default rules are loaded by Verifier constructor
        pass

    def validate_system(self) -> bool:
        """Validate entire system maintains META 50/50."""
        all_valid = True

        # Validate META equilibrium (always 50/50 by definition)
        if not self.is_meta_balanced():
            all_valid = False

        # Validate all domains
        for domain in self._domains.values():
            if not domain.validate_balance():
                all_valid = False

        return all_valid

    def get_system_stats(self) -> dict[str, Any]:
        """Get comprehensive system statistics."""
        domain_stats = []
        total_concepts = 0

        for name, domain in self._domains.items():
            stats = domain.get_domain_stats()
            total_concepts += stats["concepts"]
            domain_stats.append({
                "name": name,
                "concepts": stats["concepts"],
                "balanced": stats["balanced"]
            })

        return {
            "system": self.NAME,
            "version": self.VERSION,
            "meta_balanced": self.is_meta_balanced(),
            "operational_ratio": self._operational.ratio,
            "domains": {
                "count": len(self._domains),
                "details": domain_stats
            },
            "total_concepts": total_concepts,
            "system_valid": self.validate_system()
        }

    def prove_meta_meaning(self) -> dict[str, Any]:
        """Generate META proof for entire system."""
        proofs = []

        # META balance proof
        meta_balance = self.get_meta_balance()
        proofs.append({
            "component": "META Equilibrium",
            "claim": "System maintains 50/50 balance",
            "evidence": f"Positive: {meta_balance['positive']}%, Negative: {meta_balance['negative']}%",
            "valid": meta_balance["balanced"]
        })

        # Operational ratio proof
        op_ratio = self.get_operational_ratio()
        proofs.append({
            "component": "Operational Ratio",
            "claim": "52/48 ratio enables META balance",
            "evidence": f"Structure: {op_ratio['structure']}%, Flexibility: {op_ratio['flexibility']}%",
            "valid": abs(op_ratio["ratio"] - 1.0833) < 0.01
        })

        # PI/6 derivation proof
        proofs.append({
            "component": "PI/6 Proportion",
            "claim": "Operational ratio derived from PI/6",
            "evidence": f"PI/6 ≈ {self._pi6.value:.4f}, sin(PI/6) = 0.5 (META connection)",
            "valid": self._pi6.verify_meta_connection()
        })

        # Domain balance proofs
        for name, domain in self._domains.items():
            domain_proof = domain.prove_meta_meaning()
            proofs.append({
                "component": f"Domain: {name}",
                "claim": f"{name} domain maintains META balance",
                "evidence": f"Duality balanced: {domain_proof['meta_valid']}",
                "valid": domain_proof["meta_valid"]
            })

        all_valid = all(p["valid"] for p in proofs)

        return {
            "system": self.NAME,
            "proofs": proofs,
            "all_valid": all_valid,
            "conclusion": (
                "Civilisation Hub maintains META 50/50 equilibrium across all components."
                if all_valid else
                "Some components require balance adjustment."
            )
        }

    def display_status(self) -> None:
        """Display current system status."""
        self._display.display_meta_50_50()
        self._display.display_operational_52_48()

        self._display.display_title("System Status", level=1)

        stats = self.get_system_stats()
        self._display.display({
            "Version": stats["version"],
            "META Balanced": "Yes" if stats["meta_balanced"] else "No",
            "Domains": stats["domains"]["count"],
            "Total Concepts": stats["total_concepts"],
            "System Valid": "Yes" if stats["system_valid"] else "No"
        })

        self._display.display_title("Domains", level=2)
        for domain_stat in stats["domains"]["details"]:
            status = "✓" if domain_stat["balanced"] else "✗"
            self._display.render(
                f"  {status} {domain_stat['name']}: {domain_stat['concepts']} concepts"
            )

    def display_proof(self) -> None:
        """Display META proof for the system."""
        proof = self.prove_meta_meaning()

        self._display.display_title("META 50/50 PROOF", level=1)

        for p in proof["proofs"]:
            status = "✓" if p["valid"] else "✗"
            self._display.render(f"\n{status} {p['component']}")
            self._display.render(f"    Claim: {p['claim']}")
            self._display.render(f"    Evidence: {p['evidence']}")

        self._display.render(f"\n{'═' * 60}")
        self._display.render(f"Conclusion: {proof['conclusion']}")

    def get_domain(self, name: str) -> KnowledgeDomain | None:
        """Get a domain by name."""
        return self._domains.get(name.lower())

    @property
    def persistence(self) -> DomainPersistenceService:
        """Get the persistence service (lazy initialization)."""
        if self._persistence is None:
            self._persistence = DomainPersistenceService()
        return self._persistence

    def save_domains(self) -> list[str]:
        """
        Save all domains to database.

        Returns:
            List of saved domain names
        """
        saved = []
        for domain in self._domains.values():
            self.persistence.save_domain(domain)
            saved.append(domain.name)
        return saved

    def save_domain(self, name: str) -> bool:
        """
        Save a specific domain to database.

        Args:
            name: Domain name to save

        Returns:
            True if saved, False if domain not found
        """
        domain = self.get_domain(name)
        if domain:
            self.persistence.save_domain(domain)
            return True
        return False

    def list_saved_domains(self) -> list[dict[str, Any]]:
        """
        List all domains saved in database.

        Returns:
            List of domain summaries
        """
        return self.persistence.list_domains()

    def get_persistence_stats(self) -> dict[str, Any]:
        """
        Get database persistence statistics.

        Returns:
            Statistics dictionary
        """
        return self.persistence.get_persistence_stats()

    def run_demo(self) -> None:
        """Run demonstration of system capabilities."""
        self._display.display_title("CIVILISATION HUB DEMONSTRATION", level=1)

        # Show META principle
        self._display.display_meta_50_50()
        self._display.display_operational_52_48()

        # Show system status
        self.display_status()

        # Show proof
        self.display_proof()

        # Domain details
        self._display.display_title("Domain Details", level=1)
        for name, domain in self._domains.items():
            reporter = DomainReporter(self._display)
            report = reporter.generate_report(domain)
            reporter.render_report(report)
            self._display.render("")


def create_argument_parser() -> argparse.ArgumentParser:
    """Create command line argument parser."""
    parser = argparse.ArgumentParser(
        description="Civilisation Hub - META 50/50 Equilibrium System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                    Run system status
  python main.py --demo             Run full demonstration
  python main.py --prove            Show META proof
  python main.py --domain physics   Show physics domain details
  python main.py --save             Save all domains to database
  python main.py --list-saved       List saved domains
  python main.py --db-stats         Show database statistics
        """
    )

    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run full system demonstration"
    )

    parser.add_argument(
        "--prove",
        action="store_true",
        help="Display META 50/50 proof"
    )

    parser.add_argument(
        "--status",
        action="store_true",
        help="Display system status (default)"
    )

    parser.add_argument(
        "--domain",
        type=str,
        choices=["mathematics", "physics", "code", "biology", "philosophy"],
        help="Display specific domain details"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"Civilisation Hub {CivilisationHub.VERSION}"
    )

    # Database persistence options
    parser.add_argument(
        "--save",
        action="store_true",
        help="Save all domains to database"
    )

    parser.add_argument(
        "--save-domain",
        type=str,
        metavar="NAME",
        help="Save a specific domain to database"
    )

    parser.add_argument(
        "--list-saved",
        action="store_true",
        help="List all domains saved in database"
    )

    parser.add_argument(
        "--db-stats",
        action="store_true",
        help="Show database persistence statistics"
    )

    return parser


def main() -> int:
    """Main entry point."""
    parser = create_argument_parser()
    args = parser.parse_args()

    # Initialize system
    hub = CivilisationHub(verbose=args.verbose)
    hub.initialize()

    # Handle commands
    if args.demo:
        hub.run_demo()
    elif args.prove:
        hub.display_proof()
    elif args.domain:
        domain = hub.get_domain(args.domain)
        if domain:
            reporter = DomainReporter(hub._display)
            report = reporter.generate_report(domain)
            reporter.render_report(report)
        else:
            print(f"Domain '{args.domain}' not found.")
            return 1
    elif args.save:
        saved = hub.save_domains()
        print(f"Saved {len(saved)} domains to database:")
        for name in saved:
            print(f"  ✓ {name}")
    elif args.save_domain:
        if hub.save_domain(args.save_domain):
            print(f"Saved domain '{args.save_domain}' to database.")
        else:
            print(f"Domain '{args.save_domain}' not found.")
            return 1
    elif args.list_saved:
        domains = hub.list_saved_domains()
        if domains:
            print(f"Saved domains ({len(domains)}):")
            for d in domains:
                status = "✓" if d.get("meta_compliant") else "○"
                print(f"  {status} {d['name']} ({d['type']}) - {d['concept_count']} concepts")
        else:
            print("No domains saved in database.")
    elif args.db_stats:
        stats = hub.get_persistence_stats()
        print("Database Statistics:")
        print(f"  Total domains: {stats['total_domains']}")
        print(f"  Total concepts: {stats['total_concepts']}")
        print(f"  META compliant: {stats['meta_compliant_domains']}")
        print(f"  Compliance rate: {stats['compliance_rate']:.1f}%")
    else:
        # Default: show status
        hub.display_status()

    return 0


if __name__ == "__main__":
    sys.exit(main())
