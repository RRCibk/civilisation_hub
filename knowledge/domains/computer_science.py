"""
Computer Science Domain
=======================
Computer Science knowledge domain with META 50/50 equilibrium.
Fundamental duality: Hardware/Software (physical vs logical).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class ComputerScienceDomain(KnowledgeDomain):
    """
    Computer Science knowledge domain.

    Fundamental Duality: Hardware / Software
    - Hardware: Physical components, circuits, machines
    - Software: Programs, algorithms, data structures

    Secondary Dualities:
    - Theory / Practice
    - Sequential / Parallel
    - Centralized / Distributed
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="ComputerScience",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of computation, algorithms, and information processing",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Hardware/Software duality."""
        self._domain.set_duality(
            positive_name="hardware",
            positive_value=50,
            negative_name="software",
            negative_value=50,
            duality_name="computer_science_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental computer science principles."""
        principles = [
            (
                "Abstraction",
                "Hide complexity through layers of abstraction",
            ),
            (
                "Modularity",
                "Decompose systems into independent components",
            ),
            (
                "Correctness",
                "Programs must produce correct results",
            ),
            (
                "Efficiency",
                "Optimize use of computational resources",
            ),
            (
                "Scalability",
                "Systems should handle growth gracefully",
            ),
            (
                "Security",
                "Protect against unauthorized access and attacks",
            ),
            (
                "Reusability",
                "Design components for multiple uses",
            ),
            (
                "Maintainability",
                "Code should be easy to understand and modify",
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=90,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental computer science concepts."""
        return [
            "Algorithm",
            "Data Structure",
            "Computation",
            "Program",
            "Memory",
            "Processor",
            "Input",
            "Output",
            "Network",
            "Database",
            "Operating System",
            "Compiler",
            "Protocol",
            "Encryption",
            "Interface",
        ]

    def initialize_branches(self) -> None:
        """Initialize major computer science branches."""
        branches = [
            (
                "Algorithms",
                "Design and analysis of algorithms",
                ConceptType.THEORY,
            ),
            (
                "Data Structures",
                "Organization of data",
                ConceptType.THEORY,
            ),
            (
                "Computer Architecture",
                "Hardware design and organization",
                ConceptType.THEORY,
            ),
            (
                "Operating Systems",
                "System software management",
                ConceptType.THEORY,
            ),
            (
                "Databases",
                "Data storage and retrieval",
                ConceptType.THEORY,
            ),
            (
                "Networks",
                "Computer communication",
                ConceptType.THEORY,
            ),
            (
                "Programming Languages",
                "Language design and implementation",
                ConceptType.THEORY,
            ),
            (
                "Artificial Intelligence",
                "Intelligent systems",
                ConceptType.THEORY,
            ),
            (
                "Computer Graphics",
                "Visual computing",
                ConceptType.THEORY,
            ),
            (
                "Software Engineering",
                "Large-scale software development",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_complexity_classes(self) -> None:
        """Initialize computational complexity classes."""
        classes = [
            ("P", "Polynomial time", "Efficiently solvable"),
            ("NP", "Nondeterministic polynomial", "Verifiable in polynomial time"),
            ("NP-Complete", "Hardest in NP", "All NP reduces to these"),
            ("NP-Hard", "At least as hard as NP", "May not be in NP"),
            ("PSPACE", "Polynomial space", "Space-bounded"),
            ("EXPTIME", "Exponential time", "Very hard problems"),
        ]

        for name, description, meaning in classes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["meaning"] = meaning

    def initialize_paradigms(self) -> None:
        """Initialize programming paradigms."""
        paradigms = [
            ("Imperative", "Step-by-step commands", "How to do"),
            ("Declarative", "Describe what, not how", "What to do"),
            ("Object-Oriented", "Objects with state and behavior", "Encapsulation"),
            ("Functional", "Functions without side effects", "Immutability"),
            ("Logic", "Rules and inference", "Deduction"),
            ("Concurrent", "Parallel execution", "Simultaneity"),
        ]

        for name, description, key_concept in paradigms:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["key_concept"] = key_concept

    def initialize_cs_pairs(self) -> None:
        """Initialize fundamental computer science pairs with META 50/50 balance."""
        pairs = [
            ("Hardware", "Software", "Physical vs logical"),
            ("Theory", "Practice", "Abstract vs applied"),
            ("Sequential", "Parallel", "Serial vs concurrent"),
            ("Centralized", "Distributed", "Single vs multiple nodes"),
            ("Synchronous", "Asynchronous", "Blocking vs non-blocking"),
            ("Static", "Dynamic", "Compile-time vs runtime"),
            ("Compiled", "Interpreted", "Pre-translated vs on-the-fly"),
            ("Imperative", "Declarative", "How vs what"),
            ("Mutable", "Immutable", "Changeable vs fixed"),
            ("Eager", "Lazy", "Immediate vs deferred"),
            ("Breadth", "Depth", "Wide vs deep search"),
            ("Space", "Time", "Memory vs speed tradeoff"),
            ("Abstraction", "Implementation", "Interface vs detail"),
            ("Client", "Server", "Requester vs provider"),
            ("Encryption", "Decryption", "Encode vs decode"),
            ("Compression", "Decompression", "Shrink vs expand"),
            ("Virtual", "Physical", "Simulated vs real"),
            ("Syntax", "Semantics", "Form vs meaning"),
            ("Local", "Global", "Scoped vs universal"),
            ("Exact", "Approximate", "Precise vs estimated"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (CS)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (CS)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_big_o_complexities(self) -> dict[str, str]:
        """Get common Big-O complexity classes."""
        return {
            "O(1)": "Constant time",
            "O(log n)": "Logarithmic time",
            "O(n)": "Linear time",
            "O(n log n)": "Linearithmic time",
            "O(n^2)": "Quadratic time",
            "O(2^n)": "Exponential time",
        }

    def demonstrate_cs_balance(self) -> dict[str, Any]:
        """Demonstrate computer science balance principles."""
        return {
            "concept": "Computer Science Equilibrium",
            "dualities": {
                "hardware_software": {
                    "hardware": 50.0,
                    "software": 50.0,
                    "meaning": "Physical and logical systems are complementary",
                },
                "theory_practice": {
                    "theory": 50.0,
                    "practice": 50.0,
                    "meaning": "Foundations and applications equally important",
                },
                "space_time": {
                    "space": 50.0,
                    "time": 50.0,
                    "meaning": "Memory-speed tradeoffs are fundamental",
                },
            },
            "computing_balance": {
                "abstraction": 50.0,
                "implementation": 50.0,
                "description": "Interfaces and details must balance",
            },
            "meta_meaning": "Computer Science demonstrates META 50/50 in hardware-software unity",
        }


def create_computer_science_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> ComputerScienceDomain:
    """
    Factory function to create a fully initialized computer science domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized ComputerScienceDomain
    """
    domain = ComputerScienceDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_complexity_classes()
        domain.initialize_paradigms()
        domain.initialize_cs_pairs()

    return domain
