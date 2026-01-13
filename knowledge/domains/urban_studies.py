"""
Urban Studies Domain
====================
Urban studies knowledge domain with META 50/50 equilibrium.
Fundamental duality: Urban/Rural (city vs countryside).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class UrbanStudiesDomain(KnowledgeDomain):
    """
    Urban Studies knowledge domain.

    Fundamental Duality: Urban / Rural
    - Urban: City, metropolitan, concentrated
    - Rural: Countryside, agricultural, dispersed

    Secondary Dualities:
    - Center / Periphery
    - Public / Private
    - Planned / Organic
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="UrbanStudies",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of cities, urbanization, and urban life",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Urban/Rural duality."""
        self._domain.set_duality(
            positive_name="urban",
            positive_value=50,
            negative_name="rural",
            negative_value=50,
            duality_name="urban_studies_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental urban principles."""
        principles = [
            (
                "Agglomeration Effects",
                "Concentration creates economic advantages",
            ),
            (
                "Urban Ecology",
                "Cities are ecosystems with zones and processes",
            ),
            (
                "Central Place Function",
                "Cities serve surrounding regions",
            ),
            (
                "Land Value Gradient",
                "Land value decreases with distance from center",
            ),
            (
                "Urban Metabolism",
                "Cities consume resources and produce waste",
            ),
            (
                "Social Heterogeneity",
                "Cities contain diverse populations",
            ),
            (
                "Spatial Segregation",
                "Different groups occupy different areas",
            ),
            (
                "Path Dependency",
                "Urban form reflects historical decisions",
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
        """Get fundamental urban studies concepts."""
        return [
            "City",
            "Urbanization",
            "Metropolitan",
            "Suburb",
            "Neighborhood",
            "Density",
            "Land Use",
            "Zoning",
            "Infrastructure",
            "Transportation",
            "Housing",
            "Gentrification",
            "Sprawl",
            "Renewal",
            "Public Space",
        ]

    def initialize_branches(self) -> None:
        """Initialize major urban studies branches."""
        branches = [
            (
                "Urban Geography",
                "Spatial aspects of cities",
                ConceptType.THEORY,
            ),
            (
                "Urban Sociology",
                "Social life in cities",
                ConceptType.THEORY,
            ),
            (
                "Urban Economics",
                "Economic functions of cities",
                ConceptType.THEORY,
            ),
            (
                "Urban Planning",
                "Design and management of cities",
                ConceptType.THEORY,
            ),
            (
                "Urban History",
                "Historical development of cities",
                ConceptType.THEORY,
            ),
            (
                "Urban Ecology",
                "Cities as ecosystems",
                ConceptType.THEORY,
            ),
            (
                "Urban Politics",
                "Governance of cities",
                ConceptType.THEORY,
            ),
            (
                "Urban Design",
                "Physical form of cities",
                ConceptType.THEORY,
            ),
            (
                "Transportation Planning",
                "Movement in cities",
                ConceptType.THEORY,
            ),
            (
                "Housing Studies",
                "Residential aspects of cities",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_urban_models(self) -> None:
        """Initialize urban structure models."""
        models = [
            ("Concentric Zone", "Burgess", "Rings from center"),
            ("Sector Model", "Hoyt", "Wedge-shaped sectors"),
            ("Multiple Nuclei", "Harris/Ullman", "Multiple centers"),
            ("Edge City", "Garreau", "Suburban employment centers"),
            ("Polycentric Model", "Various", "Many interconnected centers"),
        ]

        for name, founder, description in models:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.MODEL,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_urban_theories(self) -> None:
        """Initialize urban theories."""
        theories = [
            ("Chicago School", "Park", "Urban ecology approach"),
            ("Growth Machine", "Logan/Molotch", "Elite urban development"),
            ("Right to the City", "Lefebvre", "Urban as social product"),
            ("Creative Class", "Florida", "Talent drives urban growth"),
            ("Global Cities", "Sassen", "Command centers of economy"),
            ("New Urbanism", "Duany", "Traditional neighborhood design"),
        ]

        for name, founder, description in theories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_urban_processes(self) -> None:
        """Initialize urban processes."""
        processes = [
            ("Urbanization", "Rural to urban migration", "Growth of cities"),
            ("Suburbanization", "Movement to suburbs", "Decentralization"),
            ("Gentrification", "Neighborhood upgrading", "Displacement"),
            ("Urban Renewal", "Redevelopment programs", "Planned change"),
            ("Sprawl", "Low-density expansion", "Car-dependent"),
            ("Densification", "Increasing density", "Intensification"),
        ]

        for name, description, characteristic in processes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["characteristic"] = characteristic

    def initialize_urban_pairs(self) -> None:
        """Initialize fundamental urban pairs with META 50/50 balance."""
        pairs = [
            ("Urban", "Rural", "City vs countryside"),
            ("Center", "Periphery", "Core vs edge"),
            ("Public", "Private", "Common vs individual space"),
            ("Planned", "Organic", "Designed vs evolved"),
            ("Dense", "Sparse", "Concentrated vs spread"),
            ("Formal", "Informal", "Legal vs extra-legal"),
            ("Central", "Suburban", "Downtown vs outskirts"),
            ("Residential", "Commercial", "Living vs business"),
            ("Industrial", "Post-industrial", "Manufacturing vs service"),
            ("Mixed-use", "Single-use", "Combined vs separated"),
            ("Walkable", "Car-dependent", "Pedestrian vs auto"),
            ("Historic", "Modern", "Old vs new"),
            ("Gated", "Open", "Enclosed vs accessible"),
            ("Green", "Grey", "Nature vs built"),
            ("Affordable", "Expensive", "Accessible vs exclusive"),
            ("Growth", "Decline", "Expansion vs shrinkage"),
            ("Integration", "Segregation", "Mixed vs separated"),
            ("Local", "Global", "Place vs world city"),
            ("Top-down", "Bottom-up", "Official vs grassroots"),
            ("Compact", "Sprawling", "Dense vs spread"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Urban Studies)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Urban Studies)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_urban_zones(self) -> dict[str, str]:
        """Get Burgess concentric zone model."""
        return {
            "zone_1": "Central Business District (CBD)",
            "zone_2": "Zone of Transition",
            "zone_3": "Working Class Residential",
            "zone_4": "Middle Class Residential",
            "zone_5": "Commuter Zone",
        }

    def demonstrate_urban_balance(self) -> dict[str, Any]:
        """Demonstrate urban studies balance principles."""
        return {
            "concept": "Urban Equilibrium",
            "dualities": {
                "urban_rural": {
                    "urban": 50.0,
                    "rural": 50.0,
                    "meaning": "Cities and countryside are interdependent",
                },
                "center_periphery": {
                    "center": 50.0,
                    "periphery": 50.0,
                    "meaning": "Core and edge define each other",
                },
                "public_private": {
                    "public": 50.0,
                    "private": 50.0,
                    "meaning": "Both spheres essential to urban life",
                },
            },
            "spatial_balance": {
                "centralization": 50.0,
                "decentralization": 50.0,
                "description": "Cities balance concentration and dispersion",
            },
            "meta_meaning": "Urban Studies demonstrates META 50/50 in urban-rural balance",
        }


def create_urban_studies_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> UrbanStudiesDomain:
    """
    Factory function to create a fully initialized urban studies domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized UrbanStudiesDomain
    """
    domain = UrbanStudiesDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_urban_models()
        domain.initialize_urban_theories()
        domain.initialize_urban_processes()
        domain.initialize_urban_pairs()

    return domain
