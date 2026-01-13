"""
Actuarial Science Domain
========================
Actuarial Science knowledge domain with META 50/50 equilibrium.
Fundamental duality: Risk/Return (uncertainty vs reward).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class ActuarialScienceDomain(KnowledgeDomain):
    """
    Actuarial Science knowledge domain.

    Fundamental Duality: Risk / Return
    - Risk: Uncertainty, potential loss, variability
    - Return: Reward, gain, expected value

    Secondary Dualities:
    - Premium / Benefit
    - Short-term / Long-term
    - Individual / Portfolio
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="ActuarialScience",
            domain_type=DomainType.FUNDAMENTAL,
            description="The discipline of assessing and managing financial risk",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Risk/Return duality."""
        self._domain.set_duality(
            positive_name="risk",
            positive_value=50,
            negative_name="return",
            negative_value=50,
            duality_name="actuarial_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental actuarial principles."""
        principles = [
            ("Risk Assessment", "Quantify uncertainty systematically"),
            ("Time Value", "Money has temporal value"),
            ("Pooling", "Spread risk across many"),
            ("Equivalence", "Premium equals expected claims"),
            ("Solvency", "Maintain ability to pay"),
            ("Prudence", "Conservative assumptions"),
            ("Consistency", "Stable methodology over time"),
            ("Transparency", "Clear communication of methods"),
        ]

        for name, description in principles:
            self.create_concept(name, ConceptType.PRINCIPLE, description, certainty=95)

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental actuarial concepts."""
        return ["Risk", "Premium", "Reserve", "Mortality", "Probability",
                "Interest", "Annuity", "Liability", "Solvency", "Experience",
                "Underwriting", "Claims", "Exposure", "Loss", "Contingency"]

    def initialize_branches(self) -> None:
        """Initialize major actuarial branches."""
        branches = [
            ("Life Insurance", "Mortality risk", ConceptType.THEORY),
            ("Health Insurance", "Medical costs", ConceptType.THEORY),
            ("Property/Casualty", "Asset protection", ConceptType.THEORY),
            ("Pension", "Retirement funding", ConceptType.THEORY),
            ("Enterprise Risk", "Corporate risk", ConceptType.THEORY),
            ("Investment", "Asset-liability matching", ConceptType.THEORY),
            ("Reinsurance", "Risk transfer", ConceptType.THEORY),
            ("Predictive Modeling", "Statistical forecasting", ConceptType.THEORY),
            ("Financial Economics", "Market valuation", ConceptType.THEORY),
            ("Regulatory", "Compliance standards", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_tables(self) -> None:
        """Initialize actuarial tables and models."""
        tables = [
            ("Mortality Table", "Death rates by age", "Life"),
            ("Morbidity Table", "Illness rates", "Health"),
            ("Interest Rate", "Discount factors", "All"),
            ("Loss Distribution", "Claim frequencies", "P&C"),
            ("Survival Function", "Remaining lifetime", "Life"),
            ("Hazard Rate", "Instantaneous failure", "All"),
        ]

        for name, description, application in tables:
            concept = self.create_concept(name, ConceptType.DEFINITION, description)
            concept.metadata["application"] = application

    def initialize_actuarial_pairs(self) -> None:
        """Initialize fundamental actuarial pairs with META 50/50 balance."""
        pairs = [
            ("Risk", "Return", "Uncertainty vs reward"),
            ("Premium", "Benefit", "Payment vs payout"),
            ("Short-term", "Long-term", "Near vs far horizon"),
            ("Individual", "Portfolio", "Single vs aggregate"),
            ("Assets", "Liabilities", "Own vs owe"),
            ("Frequency", "Severity", "How often vs how much"),
            ("Expected", "Actual", "Predicted vs realized"),
            ("Gross", "Net", "Before vs after reinsurance"),
            ("Earned", "Unearned", "Past vs future premium"),
            ("Incurred", "Paid", "Recognized vs settled"),
            ("Static", "Dynamic", "Fixed vs changing assumptions"),
            ("Deterministic", "Stochastic", "Fixed vs random model"),
            ("Best Estimate", "Margin", "Expected vs cushion"),
            ("Retrospective", "Prospective", "Past vs future"),
            ("Nominal", "Real", "Face vs inflation-adjusted"),
            ("Term", "Whole", "Temporary vs permanent"),
            ("Level", "Increasing", "Flat vs growing"),
            ("Guaranteed", "Participating", "Fixed vs variable"),
            ("Insured", "Self-Insured", "Transfer vs retain"),
            ("Adverse", "Favorable", "Bad vs good experience"),
        ]

        for positive, negative, description in pairs:
            pos = self.create_concept(f"{positive} (Actuarial)", ConceptType.DEFINITION,
                                       f"Positive pole: {description.split(' vs ')[0]}")
            neg = self.create_concept(f"{negative} (Actuarial)", ConceptType.DEFINITION,
                                       f"Negative pole: {description.split(' vs ')[1]}")
            self.create_relation(pos, neg, RelationType.CONTRADICTS, strength=50)

    def demonstrate_actuarial_balance(self) -> dict[str, Any]:
        """Demonstrate actuarial balance principles."""
        return {
            "concept": "Actuarial Equilibrium",
            "dualities": {
                "risk_return": {"risk": 50.0, "return": 50.0,
                    "meaning": "Balance uncertainty with reward"},
                "premium_benefit": {"premium": 50.0, "benefit": 50.0,
                    "meaning": "Payment equals expected payout"},
            },
            "meta_meaning": "Actuarial Science demonstrates META 50/50 in risk-return balance",
        }


def create_actuarial_science_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> ActuarialScienceDomain:
    domain = ActuarialScienceDomain(meta_equilibrium)
    if initialize_all:
        domain.initialize_branches()
        domain.initialize_tables()
        domain.initialize_actuarial_pairs()
    return domain
