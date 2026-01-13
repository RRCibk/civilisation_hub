"""
Systems Science Domain
======================
Systems science knowledge domain with META 50/50 equilibrium.
Fundamental duality: Whole/Parts (system vs components).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class SystemsScienceDomain(KnowledgeDomain):
    """
    Systems Science knowledge domain.

    Fundamental Duality: Whole / Parts
    - Whole: System, emergent properties, holistic view
    - Parts: Components, elements, reductionist view

    Secondary Dualities:
    - Open / Closed
    - Linear / Nonlinear
    - Order / Chaos
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="SystemsScience",
            domain_type=DomainType.FUNDAMENTAL,
            description="The interdisciplinary study of systems and complexity",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Whole/Parts duality."""
        self._domain.set_duality(
            positive_name="whole",
            positive_value=50,
            negative_name="parts",
            negative_value=50,
            duality_name="systems_science_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental systems science principles."""
        principles = [
            (
                "Emergence",
                "Wholes have properties parts lack",
            ),
            (
                "Feedback",
                "Outputs affect inputs",
            ),
            (
                "Interconnection",
                "Everything is connected",
            ),
            (
                "Hierarchy",
                "Systems within systems",
            ),
            (
                "Nonlinearity",
                "Small causes can have large effects",
            ),
            (
                "Adaptation",
                "Systems change with environment",
            ),
            (
                "Self-Organization",
                "Order arises spontaneously",
            ),
            (
                "Equifinality",
                "Multiple paths to same outcome",
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=85,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental systems science concepts."""
        return [
            "System",
            "Feedback",
            "Emergence",
            "Complexity",
            "Network",
            "Hierarchy",
            "Boundary",
            "Environment",
            "State",
            "Dynamics",
            "Equilibrium",
            "Adaptation",
            "Evolution",
            "Control",
            "Information",
        ]

    def initialize_branches(self) -> None:
        """Initialize major systems science branches."""
        branches = [
            (
                "General Systems Theory",
                "Universal system principles",
                ConceptType.THEORY,
            ),
            (
                "Cybernetics",
                "Control and communication",
                ConceptType.THEORY,
            ),
            (
                "Complexity Science",
                "Complex adaptive systems",
                ConceptType.THEORY,
            ),
            (
                "Network Science",
                "Network structure and dynamics",
                ConceptType.THEORY,
            ),
            (
                "Chaos Theory",
                "Deterministic chaos",
                ConceptType.THEORY,
            ),
            (
                "Systems Dynamics",
                "Feedback-driven behavior",
                ConceptType.THEORY,
            ),
            (
                "Control Theory",
                "System control",
                ConceptType.THEORY,
            ),
            (
                "Information Theory",
                "Information in systems",
                ConceptType.THEORY,
            ),
            (
                "Agent-Based Modeling",
                "Individual-based simulation",
                ConceptType.THEORY,
            ),
            (
                "Soft Systems Methodology",
                "Human activity systems",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_properties(self) -> None:
        """Initialize system properties."""
        properties = [
            ("Emergence", "Novel properties arise", "Whole"),
            ("Feedback", "Self-regulation", "Dynamics"),
            ("Resilience", "Recovery from disturbance", "Stability"),
            ("Adaptability", "Response to change", "Evolution"),
            ("Modularity", "Separable components", "Structure"),
            ("Redundancy", "Backup elements", "Robustness"),
        ]

        for name, description, category in properties:
            concept = self.create_concept(
                name=f"System {name}",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_archetypes(self) -> None:
        """Initialize system archetypes."""
        archetypes = [
            ("Limits to Growth", "Growth hits constraints", "Growth"),
            ("Shifting the Burden", "Short-term fixes worsen long-term", "Behavior"),
            ("Tragedy of Commons", "Individual vs collective", "Resource"),
            ("Fixes That Fail", "Unintended consequences", "Intervention"),
            ("Success to Successful", "Rich get richer", "Competition"),
            ("Escalation", "Arms race dynamics", "Competition"),
        ]

        for name, description, category in archetypes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_systems_pairs(self) -> None:
        """Initialize fundamental systems science pairs with META 50/50 balance."""
        pairs = [
            ("Whole", "Parts", "System vs components"),
            ("Open", "Closed", "Exchanging vs isolated"),
            ("Linear", "Nonlinear", "Proportional vs disproportional"),
            ("Order", "Chaos", "Structured vs unpredictable"),
            ("Stability", "Change", "Persistent vs evolving"),
            ("Simple", "Complex", "Few vs many elements"),
            ("Positive", "Negative", "Amplifying vs dampening feedback"),
            ("Centralized", "Distributed", "Concentrated vs spread"),
            ("Deterministic", "Stochastic", "Certain vs random"),
            ("Discrete", "Continuous", "Separate vs flowing"),
            ("Static", "Dynamic", "Fixed vs changing"),
            ("Autonomous", "Controlled", "Self vs externally governed"),
            ("Resilient", "Fragile", "Robust vs vulnerable"),
            ("Efficient", "Redundant", "Lean vs backup"),
            ("Top-Down", "Bottom-Up", "Macro vs micro driven"),
            ("Reductionist", "Holistic", "Parts vs whole focus"),
            ("Equilibrium", "Far-from-Equilibrium", "Balanced vs driven"),
            ("Local", "Global", "Nearby vs system-wide"),
            ("Short-term", "Long-term", "Immediate vs delayed effects"),
            ("Structure", "Function", "Form vs purpose"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Systems)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Systems)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_system_types(self) -> dict[str, str]:
        """Get types of systems."""
        return {
            "simple": "Few elements, predictable",
            "complicated": "Many elements, predictable",
            "complex": "Many elements, unpredictable",
            "chaotic": "Sensitive to initial conditions",
        }

    def demonstrate_systems_balance(self) -> dict[str, Any]:
        """Demonstrate systems science balance principles."""
        return {
            "concept": "Systems Science Equilibrium",
            "dualities": {
                "whole_parts": {
                    "whole": 50.0,
                    "parts": 50.0,
                    "meaning": "System and components equally important",
                },
                "order_chaos": {
                    "order": 50.0,
                    "chaos": 50.0,
                    "meaning": "Structure and unpredictability coexist",
                },
                "stability_change": {
                    "stability": 50.0,
                    "change": 50.0,
                    "meaning": "Persistence and evolution balance",
                },
            },
            "feedback_balance": {
                "positive": 50.0,
                "negative": 50.0,
                "description": "Amplifying and dampening balance",
            },
            "meta_meaning": "Systems Science demonstrates META 50/50 in whole-parts synthesis",
        }


def create_systems_science_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> SystemsScienceDomain:
    """
    Factory function to create a fully initialized systems science domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized SystemsScienceDomain
    """
    domain = SystemsScienceDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_properties()
        domain.initialize_archetypes()
        domain.initialize_systems_pairs()

    return domain
