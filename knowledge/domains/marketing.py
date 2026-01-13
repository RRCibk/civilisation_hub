"""
Marketing Domain
================
Marketing knowledge domain with META 50/50 equilibrium.
Fundamental duality: Supply/Demand (seller vs buyer).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class MarketingDomain(KnowledgeDomain):
    """
    Marketing knowledge domain.

    Fundamental Duality: Supply / Demand
    - Supply: Producer perspective, offerings
    - Demand: Consumer perspective, needs

    Secondary Dualities:
    - Product / Customer
    - Push / Pull
    - Traditional / Digital
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Marketing",
            domain_type=DomainType.FUNDAMENTAL,
            description="The science of creating and delivering value to customers",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Supply/Demand duality."""
        self._domain.set_duality(
            positive_name="supply",
            positive_value=50,
            negative_name="demand",
            negative_value=50,
            duality_name="marketing_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental marketing principles."""
        principles = [
            ("Customer Focus", "Customer needs drive marketing"),
            ("Value Creation", "Marketing creates and delivers value"),
            ("Exchange", "Marketing facilitates exchanges"),
            ("Segmentation", "Markets consist of distinct segments"),
            ("Positioning", "Brands occupy mental positions"),
            ("Integration", "All marketing elements must align"),
            ("Relationship", "Long-term relationships over transactions"),
            ("Measurement", "Marketing effectiveness must be measured"),
        ]

        for name, description in principles:
            self.create_concept(name, ConceptType.PRINCIPLE, description, certainty=85)

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental marketing concepts."""
        return ["Market", "Customer", "Brand", "Product", "Price", "Promotion",
                "Place", "Segmentation", "Targeting", "Positioning", "Value",
                "Demand", "Competition", "Channel", "Campaign"]

    def initialize_branches(self) -> None:
        """Initialize major marketing branches."""
        branches = [
            ("Digital Marketing", "Online channels", ConceptType.THEORY),
            ("Brand Management", "Brand equity", ConceptType.THEORY),
            ("Consumer Behavior", "Buyer psychology", ConceptType.THEORY),
            ("Marketing Research", "Data collection", ConceptType.THEORY),
            ("Content Marketing", "Valuable content", ConceptType.THEORY),
            ("Social Media Marketing", "Social platforms", ConceptType.THEORY),
            ("B2B Marketing", "Business markets", ConceptType.THEORY),
            ("Services Marketing", "Intangible offerings", ConceptType.THEORY),
            ("International Marketing", "Global markets", ConceptType.THEORY),
            ("Retail Marketing", "Consumer retail", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_four_ps(self) -> None:
        """Initialize the marketing mix (4Ps)."""
        ps = [
            ("Product", "What is offered", "Core offering"),
            ("Price", "What is charged", "Value exchange"),
            ("Place", "Where sold", "Distribution"),
            ("Promotion", "How communicated", "Communication"),
        ]

        for name, description, role in ps:
            concept = self.create_concept(name, ConceptType.DEFINITION, description)
            concept.metadata["role"] = role

    def initialize_marketing_pairs(self) -> None:
        """Initialize fundamental marketing pairs with META 50/50 balance."""
        pairs = [
            ("Supply", "Demand", "Seller vs buyer"),
            ("Product", "Customer", "Offering vs need"),
            ("Push", "Pull", "Outbound vs inbound"),
            ("Traditional", "Digital", "Offline vs online"),
            ("Mass", "Niche", "Broad vs targeted"),
            ("Acquisition", "Retention", "New vs existing"),
            ("Brand", "Performance", "Awareness vs conversion"),
            ("Rational", "Emotional", "Logic vs feeling"),
            ("Price", "Value", "Cost vs worth"),
            ("Short-term", "Long-term", "Tactical vs strategic"),
            ("Local", "Global", "Regional vs worldwide"),
            ("B2B", "B2C", "Business vs consumer"),
            ("Owned", "Paid", "Your media vs bought"),
            ("Quantitative", "Qualitative", "Numbers vs insights"),
            ("Offensive", "Defensive", "Attack vs protect"),
            ("Standardized", "Customized", "Same vs tailored"),
            ("Online", "Offline", "Digital vs physical"),
            ("Inbound", "Outbound", "Attract vs reach out"),
            ("Awareness", "Conversion", "Know vs buy"),
            ("Art", "Science", "Creative vs analytical"),
        ]

        for positive, negative, description in pairs:
            pos = self.create_concept(f"{positive} (Marketing)", ConceptType.DEFINITION,
                                       f"Positive pole: {description.split(' vs ')[0]}")
            neg = self.create_concept(f"{negative} (Marketing)", ConceptType.DEFINITION,
                                       f"Negative pole: {description.split(' vs ')[1]}")
            self.create_relation(pos, neg, RelationType.CONTRADICTS, strength=50)

    def demonstrate_marketing_balance(self) -> dict[str, Any]:
        """Demonstrate marketing balance principles."""
        return {
            "concept": "Marketing Equilibrium",
            "dualities": {
                "supply_demand": {"supply": 50.0, "demand": 50.0,
                    "meaning": "Market clears when supply meets demand"},
                "product_customer": {"product": 50.0, "customer": 50.0,
                    "meaning": "Balance offering with needs"},
            },
            "meta_meaning": "Marketing demonstrates META 50/50 in supply-demand equilibrium",
        }


def create_marketing_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> MarketingDomain:
    domain = MarketingDomain(meta_equilibrium)
    if initialize_all:
        domain.initialize_branches()
        domain.initialize_four_ps()
        domain.initialize_marketing_pairs()
    return domain
