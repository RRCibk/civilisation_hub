"""
Management Science Domain
=========================
Management science knowledge domain with META 50/50 equilibrium.
Fundamental duality: Strategy/Operations (planning vs execution).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class ManagementScienceDomain(KnowledgeDomain):
    """
    Management Science knowledge domain.

    Fundamental Duality: Strategy / Operations
    - Strategy: Long-term planning, direction, goals
    - Operations: Day-to-day execution, processes, efficiency

    Secondary Dualities:
    - Quantitative / Qualitative
    - Optimization / Satisficing
    - Centralized / Distributed
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="ManagementScience",
            domain_type=DomainType.FUNDAMENTAL,
            description="The application of scientific methods to management decisions",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Strategy/Operations duality."""
        self._domain.set_duality(
            positive_name="strategy",
            positive_value=50,
            negative_name="operations",
            negative_value=50,
            duality_name="management_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental management science principles."""
        principles = [
            (
                "Systems Approach",
                "Organizations are complex systems",
            ),
            (
                "Data-Driven Decisions",
                "Decisions based on evidence and analysis",
            ),
            (
                "Optimization",
                "Seek best solutions within constraints",
            ),
            (
                "Trade-offs",
                "Resources are limited, choices required",
            ),
            (
                "Continuous Improvement",
                "Always seek to improve processes",
            ),
            (
                "Stakeholder Balance",
                "Consider all stakeholder interests",
            ),
            (
                "Uncertainty Management",
                "Account for risk and uncertainty",
            ),
            (
                "Feedback Loops",
                "Monitor and adjust based on results",
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
        """Get fundamental management science concepts."""
        return [
            "Decision",
            "Optimization",
            "Model",
            "Constraint",
            "Objective",
            "Resource",
            "Process",
            "System",
            "Performance",
            "Efficiency",
            "Strategy",
            "Operations",
            "Risk",
            "Stakeholder",
            "Value",
        ]

    def initialize_branches(self) -> None:
        """Initialize major management science branches."""
        branches = [
            (
                "Operations Research",
                "Mathematical optimization",
                ConceptType.THEORY,
            ),
            (
                "Decision Analysis",
                "Structured decision making",
                ConceptType.THEORY,
            ),
            (
                "Supply Chain Management",
                "Material and information flow",
                ConceptType.THEORY,
            ),
            (
                "Project Management",
                "Project planning and control",
                ConceptType.THEORY,
            ),
            (
                "Quality Management",
                "Quality improvement",
                ConceptType.THEORY,
            ),
            (
                "Financial Management",
                "Financial decisions",
                ConceptType.THEORY,
            ),
            (
                "Risk Management",
                "Risk identification and mitigation",
                ConceptType.THEORY,
            ),
            (
                "Strategic Management",
                "Long-term planning",
                ConceptType.THEORY,
            ),
            (
                "Operations Management",
                "Production and service operations",
                ConceptType.THEORY,
            ),
            (
                "Information Systems",
                "IT management",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_methods(self) -> None:
        """Initialize management science methods."""
        methods = [
            ("Linear Programming", "Optimization with constraints", "Optimization"),
            ("Simulation", "Modeling complex systems", "Analysis"),
            ("Queuing Theory", "Waiting line analysis", "Operations"),
            ("Game Theory", "Strategic interaction", "Strategy"),
            ("Decision Trees", "Sequential decisions", "Decision"),
            ("Forecasting", "Predicting future", "Planning"),
        ]

        for name, description, category in methods:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_frameworks(self) -> None:
        """Initialize management frameworks."""
        frameworks = [
            ("SWOT", "Strengths, Weaknesses, Opportunities, Threats", "Strategy"),
            ("Balanced Scorecard", "Multi-perspective performance", "Performance"),
            ("Six Sigma", "Quality improvement", "Quality"),
            ("Lean", "Waste elimination", "Operations"),
            ("Agile", "Iterative development", "Project"),
            ("PDCA", "Plan-Do-Check-Act cycle", "Improvement"),
        ]

        for name, description, category in frameworks:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_management_pairs(self) -> None:
        """Initialize fundamental management pairs with META 50/50 balance."""
        pairs = [
            ("Strategy", "Operations", "Planning vs execution"),
            ("Quantitative", "Qualitative", "Numbers vs judgment"),
            ("Optimization", "Satisficing", "Best vs good enough"),
            ("Centralized", "Distributed", "Concentrated vs spread"),
            ("Short-term", "Long-term", "Immediate vs future"),
            ("Efficiency", "Effectiveness", "Doing right vs right thing"),
            ("Cost", "Quality", "Cheap vs excellent"),
            ("Risk", "Reward", "Danger vs gain"),
            ("Planned", "Emergent", "Deliberate vs adaptive"),
            ("Internal", "External", "Inside vs outside focus"),
            ("Individual", "Team", "Person vs group"),
            ("Analysis", "Intuition", "Data vs gut"),
            ("Control", "Empowerment", "Direct vs delegate"),
            ("Standardization", "Flexibility", "Uniform vs adaptive"),
            ("Innovation", "Stability", "New vs proven"),
            ("Growth", "Profitability", "Size vs margin"),
            ("Competition", "Cooperation", "Rival vs partner"),
            ("Process", "Outcome", "How vs what"),
            ("Supply", "Demand", "Production vs consumption"),
            ("Theory", "Practice", "Academic vs applied"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Management)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Management)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_decision_criteria(self) -> dict[str, str]:
        """Get decision-making criteria."""
        return {
            "maximax": "Best of best outcomes (optimistic)",
            "maximin": "Best of worst outcomes (pessimistic)",
            "minimax_regret": "Minimize maximum regret",
            "expected_value": "Probability-weighted average",
            "hurwicz": "Balance optimism and pessimism",
            "laplace": "Equal probability assumption",
        }

    def demonstrate_management_balance(self) -> dict[str, Any]:
        """Demonstrate management science balance principles."""
        return {
            "concept": "Management Science Equilibrium",
            "dualities": {
                "strategy_operations": {
                    "strategy": 50.0,
                    "operations": 50.0,
                    "meaning": "Planning and execution equally important",
                },
                "efficiency_effectiveness": {
                    "efficiency": 50.0,
                    "effectiveness": 50.0,
                    "meaning": "Doing things right and doing right things",
                },
                "quantitative_qualitative": {
                    "quantitative": 50.0,
                    "qualitative": 50.0,
                    "meaning": "Numbers and judgment both inform decisions",
                },
            },
            "decision_balance": {
                "analysis": 50.0,
                "intuition": 50.0,
                "description": "Data and experience both valuable",
            },
            "meta_meaning": "Management Science demonstrates META 50/50 in strategy-operations synthesis",
        }


def create_management_science_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> ManagementScienceDomain:
    """
    Factory function to create a fully initialized management science domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized ManagementScienceDomain
    """
    domain = ManagementScienceDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_methods()
        domain.initialize_frameworks()
        domain.initialize_management_pairs()

    return domain
