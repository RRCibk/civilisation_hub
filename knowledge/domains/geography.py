"""
Geography Domain
================
Geography knowledge domain with META 50/50 equilibrium.
Fundamental duality: Physical/Human (natural vs social).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class GeographyDomain(KnowledgeDomain):
    """
    Geography knowledge domain.

    Fundamental Duality: Physical / Human
    - Physical: Natural environment, landforms, climate
    - Human: Social, cultural, economic aspects of space

    Secondary Dualities:
    - Space / Place
    - Local / Global
    - Urban / Rural
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Geography",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of places, spaces, and human-environment interactions",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Physical/Human duality."""
        self._domain.set_duality(
            positive_name="physical",
            positive_value=50,
            negative_name="human",
            negative_value=50,
            duality_name="geography_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental geographical principles."""
        principles = [
            (
                "Location Matters",
                "Where things are affects what they are",
            ),
            (
                "Spatial Interaction",
                "Places are connected through flows and movement",
            ),
            (
                "Scale Dependency",
                "Patterns differ across scales",
            ),
            (
                "Human-Environment Interaction",
                "Humans and environment mutually influence each other",
            ),
            (
                "Regional Differentiation",
                "Earth's surface varies from place to place",
            ),
            (
                "Distance Decay",
                "Interaction decreases with distance",
            ),
            (
                "Spatial Association",
                "Phenomena are often clustered in space",
            ),
            (
                "Place Uniqueness",
                "Every place has distinctive characteristics",
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
        """Get fundamental geography concepts."""
        return [
            "Location",
            "Place",
            "Space",
            "Region",
            "Scale",
            "Movement",
            "Environment",
            "Landscape",
            "Territory",
            "Distance",
            "Pattern",
            "Distribution",
            "Diffusion",
            "Interaction",
            "Flow",
        ]

    def initialize_branches(self) -> None:
        """Initialize major geography branches."""
        branches = [
            (
                "Physical Geography",
                "Natural systems and processes",
                ConceptType.THEORY,
            ),
            (
                "Human Geography",
                "Human activities in space",
                ConceptType.THEORY,
            ),
            (
                "Economic Geography",
                "Spatial distribution of economic activities",
                ConceptType.THEORY,
            ),
            (
                "Cultural Geography",
                "Spatial aspects of culture",
                ConceptType.THEORY,
            ),
            (
                "Political Geography",
                "Spatial aspects of politics",
                ConceptType.THEORY,
            ),
            (
                "Urban Geography",
                "Cities and urban systems",
                ConceptType.THEORY,
            ),
            (
                "Biogeography",
                "Distribution of living things",
                ConceptType.THEORY,
            ),
            (
                "Geomorphology",
                "Landforms and processes",
                ConceptType.THEORY,
            ),
            (
                "Climatology",
                "Climate patterns and processes",
                ConceptType.THEORY,
            ),
            (
                "GIScience",
                "Geographic information systems",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_spatial_concepts(self) -> None:
        """Initialize spatial concept types."""
        concepts = [
            ("Absolute Location", "Fixed coordinates", "Latitude/longitude"),
            ("Relative Location", "Position relative to other places", "Near, far"),
            ("Site", "Internal characteristics of place", "Physical attributes"),
            ("Situation", "External relations of place", "Regional context"),
            ("Formal Region", "Uniform characteristics", "Climate zones"),
            ("Functional Region", "Organized around a node", "Metropolitan area"),
            ("Vernacular Region", "Perceived identity", "The South"),
        ]

        for name, description, example in concepts:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["example"] = example

    def initialize_geographic_models(self) -> None:
        """Initialize geographic models."""
        models = [
            ("Von Thünen Model", "Agricultural land use rings", "Distance from market"),
            ("Weber Model", "Industrial location", "Transport costs"),
            ("Central Place Theory", "Urban hierarchies", "Christaller"),
            ("Gravity Model", "Interaction between places", "Size and distance"),
            ("Core-Periphery Model", "Uneven development", "Wallerstein"),
            ("Demographic Transition", "Population change stages", "Birth/death rates"),
        ]

        for name, description, key_concept in models:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.MODEL,
                description=description,
            )
            concept.metadata["key_concept"] = key_concept

    def initialize_landform_types(self) -> None:
        """Initialize landform types."""
        landforms = [
            ("Mountain", "Elevated landform", "Tectonic uplift"),
            ("Plain", "Flat land", "Deposition"),
            ("Plateau", "Elevated flat area", "Uplift and erosion"),
            ("Valley", "Low area between heights", "River erosion"),
            ("Delta", "Sediment deposit at river mouth", "Deposition"),
            ("Glacier", "Moving ice mass", "Accumulation zone"),
        ]

        for name, description, formation in landforms:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["formation"] = formation

    def initialize_geographical_pairs(self) -> None:
        """Initialize fundamental geographical pairs with META 50/50 balance."""
        pairs = [
            ("Physical", "Human", "Natural vs social"),
            ("Space", "Place", "Abstract vs meaningful"),
            ("Local", "Global", "Small vs large scale"),
            ("Urban", "Rural", "City vs country"),
            ("Site", "Situation", "Internal vs external"),
            ("Absolute", "Relative", "Fixed vs contextual"),
            ("Core", "Periphery", "Center vs margin"),
            ("Formal", "Functional", "Uniform vs organized"),
            ("Push", "Pull", "Repel vs attract factors"),
            ("Dispersed", "Clustered", "Spread vs concentrated"),
            ("Intensive", "Extensive", "High vs low input"),
            ("Commercial", "Subsistence", "Market vs self use"),
            ("Developed", "Developing", "Rich vs poor regions"),
            ("Centripetal", "Centrifugal", "Unifying vs dividing"),
            ("Permanent", "Temporary", "Fixed vs mobile"),
            ("Internal", "External", "Inside vs outside"),
            ("Natural", "Cultural", "Environment vs society"),
            ("Horizontal", "Vertical", "Lateral vs hierarchical"),
            ("Distribution", "Diffusion", "Pattern vs spread"),
            ("Conservation", "Development", "Preserve vs change"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Geography)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Geography)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_five_themes(self) -> dict[str, str]:
        """Get the five themes of geography."""
        return {
            "location": "Where is it? Absolute and relative position",
            "place": "What is it like? Physical and human characteristics",
            "human_environment": "How do humans and environment interact?",
            "movement": "How are places connected?",
            "region": "How are areas similar and different?",
        }

    def demonstrate_geography_balance(self) -> dict[str, Any]:
        """Demonstrate geography balance principles."""
        return {
            "concept": "Geography Equilibrium",
            "dualities": {
                "physical_human": {
                    "physical": 50.0,
                    "human": 50.0,
                    "meaning": "Natural and social worlds interconnected",
                },
                "space_place": {
                    "space": 50.0,
                    "place": 50.0,
                    "meaning": "Abstract geometry and meaningful location",
                },
                "local_global": {
                    "local": 50.0,
                    "global": 50.0,
                    "meaning": "All scales matter equally",
                },
            },
            "environmental_balance": {
                "determinism": 50.0,
                "possibilism": 50.0,
                "description": "Environment shapes but does not determine",
            },
            "meta_meaning": "Geography demonstrates META 50/50 in physical-human synthesis",
        }


def create_geography_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> GeographyDomain:
    """
    Factory function to create a fully initialized geography domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized GeographyDomain
    """
    domain = GeographyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_spatial_concepts()
        domain.initialize_geographic_models()
        domain.initialize_landform_types()
        domain.initialize_geographical_pairs()

    return domain
