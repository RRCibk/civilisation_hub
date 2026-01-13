"""
Engineering Domain
==================
Engineering knowledge domain with META 50/50 equilibrium.
Fundamental duality: Theory/Practice (design vs build).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class EngineeringDomain(KnowledgeDomain):
    """
    Engineering knowledge domain.

    Fundamental Duality: Theory / Practice
    - Theory: Design, analysis, modeling
    - Practice: Building, implementation, testing

    Secondary Dualities:
    - Innovation / Reliability
    - Efficiency / Safety
    - Cost / Quality
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Engineering",
            domain_type=DomainType.FUNDAMENTAL,
            description="The application of science to design and build systems",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Theory/Practice duality."""
        self._domain.set_duality(
            positive_name="theory",
            positive_value=50,
            negative_name="practice",
            negative_value=50,
            duality_name="engineering_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental engineering principles."""
        principles = [
            (
                "Requirements First",
                "Design begins with understanding requirements",
            ),
            (
                "Safety Critical",
                "Human safety takes precedence over other factors",
            ),
            (
                "Trade-off Analysis",
                "Every design involves balancing competing factors",
            ),
            (
                "Iterative Design",
                "Solutions improve through cycles of testing and refinement",
            ),
            (
                "Systems Thinking",
                "Components interact in complex ways",
            ),
            (
                "Optimization",
                "Seek best solution within constraints",
            ),
            (
                "Failure Analysis",
                "Learn from failures to improve designs",
            ),
            (
                "Standards Compliance",
                "Follow established standards and codes",
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
        """Get fundamental engineering concepts."""
        return [
            "Design",
            "System",
            "Requirements",
            "Specifications",
            "Analysis",
            "Optimization",
            "Testing",
            "Validation",
            "Safety",
            "Reliability",
            "Efficiency",
            "Cost",
            "Quality",
            "Standards",
            "Innovation",
        ]

    def initialize_branches(self) -> None:
        """Initialize major engineering branches."""
        branches = [
            (
                "Mechanical Engineering",
                "Design of mechanical systems",
                ConceptType.THEORY,
            ),
            (
                "Electrical Engineering",
                "Electrical and electronic systems",
                ConceptType.THEORY,
            ),
            (
                "Civil Engineering",
                "Infrastructure and structures",
                ConceptType.THEORY,
            ),
            (
                "Chemical Engineering",
                "Chemical processes at scale",
                ConceptType.THEORY,
            ),
            (
                "Aerospace Engineering",
                "Aircraft and spacecraft",
                ConceptType.THEORY,
            ),
            (
                "Biomedical Engineering",
                "Medical devices and systems",
                ConceptType.THEORY,
            ),
            (
                "Software Engineering",
                "Software development processes",
                ConceptType.THEORY,
            ),
            (
                "Industrial Engineering",
                "Process optimization",
                ConceptType.THEORY,
            ),
            (
                "Environmental Engineering",
                "Environmental protection systems",
                ConceptType.THEORY,
            ),
            (
                "Systems Engineering",
                "Complex system integration",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_design_process(self) -> None:
        """Initialize engineering design process stages."""
        stages = [
            ("Problem Definition", "Clarify the problem", "Start"),
            ("Research", "Gather information", "Analysis"),
            ("Ideation", "Generate solutions", "Creative"),
            ("Prototyping", "Build models", "Development"),
            ("Testing", "Validate solutions", "Verification"),
            ("Implementation", "Build final product", "Delivery"),
        ]

        for name, description, phase in stages:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["phase"] = phase

    def initialize_analysis_methods(self) -> None:
        """Initialize engineering analysis methods."""
        methods = [
            ("Finite Element Analysis", "Structural analysis", "Simulation"),
            ("Computational Fluid Dynamics", "Fluid flow analysis", "Simulation"),
            ("Failure Mode Analysis", "Risk identification", "Safety"),
            ("Root Cause Analysis", "Problem investigation", "Quality"),
            ("Trade Study", "Option comparison", "Decision"),
            ("Cost-Benefit Analysis", "Economic evaluation", "Planning"),
        ]

        for name, description, category in methods:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_engineering_pairs(self) -> None:
        """Initialize fundamental engineering pairs with META 50/50 balance."""
        pairs = [
            ("Theory", "Practice", "Design vs implementation"),
            ("Innovation", "Reliability", "New vs proven"),
            ("Efficiency", "Safety", "Performance vs security"),
            ("Cost", "Quality", "Economy vs excellence"),
            ("Simple", "Complex", "Minimal vs comprehensive"),
            ("Analysis", "Synthesis", "Breaking down vs building up"),
            ("Ideal", "Real", "Perfect vs practical"),
            ("General", "Specific", "Universal vs particular"),
            ("Centralized", "Distributed", "Unified vs spread"),
            ("Rigid", "Flexible", "Fixed vs adaptable"),
            ("Standard", "Custom", "Common vs specialized"),
            ("Manual", "Automated", "Human vs machine"),
            ("Hardware", "Software", "Physical vs logical"),
            ("Modular", "Integrated", "Separate vs unified"),
            ("Top-Down", "Bottom-Up", "Whole to parts vs parts to whole"),
            ("Deterministic", "Probabilistic", "Certain vs uncertain"),
            ("Linear", "Nonlinear", "Proportional vs disproportional"),
            ("Static", "Dynamic", "Fixed vs changing"),
            ("Open", "Closed", "Accessible vs contained"),
            ("Robust", "Optimal", "Resilient vs best-case"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Engineering)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Engineering)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_engineering_disciplines(self) -> dict[str, str]:
        """Get major engineering disciplines."""
        return {
            "mechanical": "Motion, energy, and force systems",
            "electrical": "Electrical and electronic systems",
            "civil": "Infrastructure and construction",
            "chemical": "Chemical processes and materials",
            "computer": "Hardware and software systems",
            "aerospace": "Flight and space vehicles",
        }

    def demonstrate_engineering_balance(self) -> dict[str, Any]:
        """Demonstrate engineering balance principles."""
        return {
            "concept": "Engineering Equilibrium",
            "dualities": {
                "theory_practice": {
                    "theory": 50.0,
                    "practice": 50.0,
                    "meaning": "Design and implementation are equally essential",
                },
                "innovation_reliability": {
                    "innovation": 50.0,
                    "reliability": 50.0,
                    "meaning": "Progress and stability must balance",
                },
                "cost_quality": {
                    "cost": 50.0,
                    "quality": 50.0,
                    "meaning": "Economy and excellence require trade-offs",
                },
            },
            "design_balance": {
                "analysis": 50.0,
                "synthesis": 50.0,
                "description": "Understanding and building are complementary",
            },
            "meta_meaning": "Engineering demonstrates META 50/50 in theory-practice synthesis",
        }


def create_engineering_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> EngineeringDomain:
    """
    Factory function to create a fully initialized engineering domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized EngineeringDomain
    """
    domain = EngineeringDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_design_process()
        domain.initialize_analysis_methods()
        domain.initialize_engineering_pairs()

    return domain
