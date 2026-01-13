"""
Economics Domain
================
Economics knowledge domain with META 50/50 equilibrium.
Fundamental duality: Supply/Demand (production vs consumption).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class EconomicsDomain(KnowledgeDomain):
    """
    Economics knowledge domain.

    Fundamental Duality: Supply / Demand
    - Supply: Production, sellers, quantity available
    - Demand: Consumption, buyers, quantity desired

    Secondary Dualities:
    - Scarcity / Abundance
    - Public / Private
    - Micro / Macro
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Economics",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of production, distribution, and consumption of goods and services",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Supply/Demand duality."""
        self._domain.set_duality(
            positive_name="supply",
            positive_value=50,
            negative_name="demand",
            negative_value=50,
            duality_name="economics_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental economic principles."""
        principles = [
            (
                "Law of Supply and Demand",
                "Price adjusts to balance supply and demand",
            ),
            (
                "Scarcity Principle",
                "Resources are limited relative to wants",
            ),
            (
                "Rational Choice",
                "Agents maximize utility given constraints",
            ),
            (
                "Opportunity Cost",
                "True cost includes foregone alternatives",
            ),
            (
                "Diminishing Returns",
                "Marginal output decreases with added input",
            ),
            (
                "Comparative Advantage",
                "Trade benefits all through specialization",
            ),
            (
                "Market Equilibrium",
                "Markets tend toward clearing prices",
            ),
            (
                "Incentives Matter",
                "People respond to incentives predictably",
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.LAW,
                description=description,
                certainty=90,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental economics concepts."""
        return [
            "Market",
            "Price",
            "Supply",
            "Demand",
            "Equilibrium",
            "Scarcity",
            "Trade",
            "Capital",
            "Labor",
            "Production",
            "Consumption",
            "Utility",
            "Cost",
            "Profit",
            "Money",
        ]

    def initialize_branches(self) -> None:
        """Initialize major economics branches."""
        branches = [
            (
                "Microeconomics",
                "Individual and firm behavior",
                ConceptType.THEORY,
            ),
            (
                "Macroeconomics",
                "Economy-wide phenomena",
                ConceptType.THEORY,
            ),
            (
                "Behavioral Economics",
                "Psychology of economic decisions",
                ConceptType.THEORY,
            ),
            (
                "Development Economics",
                "Economic growth in developing countries",
                ConceptType.THEORY,
            ),
            (
                "International Economics",
                "Trade and finance across borders",
                ConceptType.THEORY,
            ),
            (
                "Labor Economics",
                "Markets for work and wages",
                ConceptType.THEORY,
            ),
            (
                "Public Economics",
                "Government role in economy",
                ConceptType.THEORY,
            ),
            (
                "Financial Economics",
                "Financial markets and instruments",
                ConceptType.THEORY,
            ),
            (
                "Environmental Economics",
                "Economic analysis of environment",
                ConceptType.THEORY,
            ),
            (
                "Health Economics",
                "Economics of healthcare systems",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_market_structures(self) -> None:
        """Initialize market structure types."""
        structures = [
            ("Perfect Competition", "Many sellers, identical products", "Price takers"),
            ("Monopoly", "Single seller", "Price maker"),
            ("Oligopoly", "Few sellers", "Strategic behavior"),
            ("Monopolistic Competition", "Many sellers, differentiated products", "Some price power"),
            ("Monopsony", "Single buyer", "Buyer power"),
        ]

        for name, description, characteristic in structures:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["characteristic"] = characteristic

    def initialize_economic_indicators(self) -> None:
        """Initialize economic indicators."""
        indicators = [
            ("GDP", "Gross Domestic Product", "Total output value"),
            ("Inflation", "Price level increase", "Purchasing power"),
            ("Unemployment", "Labor force without jobs", "Labor utilization"),
            ("Interest Rate", "Cost of borrowing", "Monetary policy"),
            ("Exchange Rate", "Currency value ratio", "International trade"),
            ("Balance of Trade", "Exports minus imports", "External balance"),
        ]

        for name, full_name, description in indicators:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["full_name"] = full_name

    def initialize_schools_of_thought(self) -> None:
        """Initialize economic schools of thought."""
        schools = [
            ("Classical Economics", "Smith/Ricardo", "Free markets, labor theory"),
            ("Keynesian Economics", "Keynes", "Government intervention, demand management"),
            ("Monetarism", "Friedman", "Money supply importance"),
            ("Austrian Economics", "Mises/Hayek", "Individual action, market process"),
            ("Marxian Economics", "Marx", "Class struggle, exploitation"),
            ("Neoclassical Economics", "Marshall", "Marginal analysis, equilibrium"),
        ]

        for name, founder, description in schools:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_economic_pairs(self) -> None:
        """Initialize fundamental economic pairs with META 50/50 balance."""
        pairs = [
            ("Supply", "Demand", "Production vs consumption"),
            ("Scarcity", "Abundance", "Limited vs plentiful"),
            ("Public", "Private", "Government vs individual"),
            ("Micro", "Macro", "Individual vs aggregate"),
            ("Production", "Consumption", "Making vs using"),
            ("Saving", "Spending", "Defer vs use now"),
            ("Export", "Import", "Sell vs buy abroad"),
            ("Inflation", "Deflation", "Rising vs falling prices"),
            ("Growth", "Recession", "Expansion vs contraction"),
            ("Employment", "Unemployment", "Working vs seeking"),
            ("Revenue", "Cost", "Income vs expense"),
            ("Profit", "Loss", "Gain vs deficit"),
            ("Asset", "Liability", "Owned vs owed"),
            ("Credit", "Debt", "Lending vs borrowing"),
            ("Fixed", "Variable", "Constant vs changing cost"),
            ("Short-run", "Long-run", "Immediate vs eventual"),
            ("Nominal", "Real", "Stated vs adjusted value"),
            ("Progressive", "Regressive", "Higher vs lower rate"),
            ("Efficiency", "Equity", "Optimal vs fair"),
            ("Buyer", "Seller", "Purchaser vs vendor"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Economics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Economics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_supply_demand_formulas(self) -> dict[str, str]:
        """Get supply and demand formulas."""
        return {
            "demand_curve": "Qd = a - bP",
            "supply_curve": "Qs = c + dP",
            "equilibrium": "Qd = Qs",
            "elasticity": "E = (%ΔQ) / (%ΔP)",
            "consumer_surplus": "Area below demand, above price",
            "producer_surplus": "Area above supply, below price",
        }

    def demonstrate_economics_balance(self) -> dict[str, Any]:
        """Demonstrate economics balance principles."""
        return {
            "concept": "Economics Equilibrium",
            "dualities": {
                "supply_demand": {
                    "supply": 50.0,
                    "demand": 50.0,
                    "meaning": "Market clears when supply equals demand",
                },
                "production_consumption": {
                    "production": 50.0,
                    "consumption": 50.0,
                    "meaning": "What is produced must be consumed",
                },
                "saving_investment": {
                    "saving": 50.0,
                    "investment": 50.0,
                    "meaning": "Savings fund investment in economy",
                },
            },
            "market_balance": {
                "buyers": 50.0,
                "sellers": 50.0,
                "description": "Exchange requires both sides",
            },
            "meta_meaning": "Economics demonstrates META 50/50 in supply-demand equilibrium",
        }


def create_economics_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> EconomicsDomain:
    """
    Factory function to create a fully initialized economics domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized EconomicsDomain
    """
    domain = EconomicsDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_market_structures()
        domain.initialize_economic_indicators()
        domain.initialize_schools_of_thought()
        domain.initialize_economic_pairs()

    return domain
