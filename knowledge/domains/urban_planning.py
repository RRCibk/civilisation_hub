"""
Urban Planning Domain
=====================
Urban Planning knowledge domain with META 50/50 equilibrium.
Fundamental duality: Built/Natural (constructed vs green).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class UrbanPlanningDomain(KnowledgeDomain):
    """
    Urban Planning knowledge domain.

    Fundamental Duality: Built / Natural
    - Built: Constructed environment, buildings, infrastructure
    - Natural: Green space, ecosystems, environment

    Secondary Dualities:
    - Public / Private
    - Density / Sprawl
    - Conservation / Development
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="UrbanPlanning",
            domain_type=DomainType.FUNDAMENTAL,
            description="The design and organization of urban environments",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Built/Natural duality."""
        self._domain.set_duality(
            positive_name="built",
            positive_value=50,
            negative_name="natural",
            negative_value=50,
            duality_name="urban_planning_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental urban planning principles."""
        principles = [
            ("Public Interest", "Planning serves the community"),
            ("Sustainability", "Balance present and future needs"),
            ("Equity", "Fair distribution of resources"),
            ("Participation", "Include community in decisions"),
            ("Efficiency", "Optimize land use"),
            ("Connectivity", "Link places and people"),
            ("Diversity", "Mix of uses and people"),
            ("Resilience", "Withstand and adapt to change"),
        ]

        for name, description in principles:
            self.create_concept(name, ConceptType.PRINCIPLE, description, certainty=85)

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental urban planning concepts."""
        return ["Zoning", "Land Use", "Density", "Infrastructure", "Transportation",
                "Housing", "Open Space", "Community", "Development", "Regulation",
                "Design", "Policy", "Growth", "Sustainability", "Equity"]

    def initialize_branches(self) -> None:
        """Initialize major urban planning branches."""
        branches = [
            ("Land Use Planning", "Zoning and development", ConceptType.THEORY),
            ("Transportation Planning", "Mobility systems", ConceptType.THEORY),
            ("Environmental Planning", "Ecological considerations", ConceptType.THEORY),
            ("Housing Policy", "Residential development", ConceptType.THEORY),
            ("Urban Design", "Physical form", ConceptType.THEORY),
            ("Economic Development", "Growth strategies", ConceptType.THEORY),
            ("Community Development", "Social planning", ConceptType.THEORY),
            ("Regional Planning", "Multi-jurisdiction", ConceptType.THEORY),
            ("Historic Preservation", "Heritage conservation", ConceptType.THEORY),
            ("Disaster Planning", "Hazard mitigation", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_zones(self) -> None:
        """Initialize zoning types."""
        zones = [
            ("Residential", "Housing areas", "Living"),
            ("Commercial", "Business areas", "Working"),
            ("Industrial", "Manufacturing areas", "Production"),
            ("Mixed-Use", "Combined uses", "Integration"),
            ("Open Space", "Parks and green", "Recreation"),
            ("Institutional", "Public facilities", "Services"),
        ]

        for name, description, function in zones:
            concept = self.create_concept(name, ConceptType.DEFINITION, description)
            concept.metadata["function"] = function

    def initialize_urban_planning_pairs(self) -> None:
        """Initialize fundamental urban planning pairs with META 50/50 balance."""
        pairs = [
            ("Built", "Natural", "Constructed vs green"),
            ("Public", "Private", "Common vs individual"),
            ("Density", "Sprawl", "Compact vs spread"),
            ("Conservation", "Development", "Preserve vs build"),
            ("Top-Down", "Bottom-Up", "Authority vs community"),
            ("Short-term", "Long-term", "Immediate vs future"),
            ("Local", "Regional", "Neighborhood vs area"),
            ("Formal", "Informal", "Planned vs organic"),
            ("Vehicular", "Pedestrian", "Cars vs walking"),
            ("Historic", "Modern", "Old vs new"),
            ("Affordable", "Market-Rate", "Subsidized vs full-price"),
            ("Growth", "Stability", "Expansion vs maintenance"),
            ("Centralized", "Decentralized", "Core vs distributed"),
            ("Regulation", "Flexibility", "Rules vs adaptation"),
            ("Function", "Form", "Use vs appearance"),
            ("Efficiency", "Equity", "Optimal vs fair"),
            ("Supply", "Demand", "Build vs need"),
            ("Infill", "Greenfield", "Inside vs edge development"),
            ("Transit", "Auto", "Public vs private transport"),
            ("Generic", "Contextual", "Standard vs site-specific"),
        ]

        for positive, negative, description in pairs:
            pos = self.create_concept(f"{positive} (Urban)", ConceptType.DEFINITION,
                                       f"Positive pole: {description.split(' vs ')[0]}")
            neg = self.create_concept(f"{negative} (Urban)", ConceptType.DEFINITION,
                                       f"Negative pole: {description.split(' vs ')[1]}")
            self.create_relation(pos, neg, RelationType.CONTRADICTS, strength=50)

    def demonstrate_urban_balance(self) -> dict[str, Any]:
        """Demonstrate urban planning balance principles."""
        return {
            "concept": "Urban Planning Equilibrium",
            "dualities": {
                "built_natural": {"built": 50.0, "natural": 50.0,
                    "meaning": "Balance construction with green space"},
                "density_sprawl": {"density": 50.0, "sprawl": 50.0,
                    "meaning": "Balance compact and spread development"},
            },
            "meta_meaning": "Urban Planning demonstrates META 50/50 in built-natural balance",
        }


def create_urban_planning_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> UrbanPlanningDomain:
    domain = UrbanPlanningDomain(meta_equilibrium)
    if initialize_all:
        domain.initialize_branches()
        domain.initialize_zones()
        domain.initialize_urban_planning_pairs()
    return domain
