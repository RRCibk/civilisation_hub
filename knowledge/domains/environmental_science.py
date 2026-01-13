"""
Environmental Science Domain
============================
Environmental science knowledge domain with META 50/50 equilibrium.
Fundamental duality: Natural/Anthropogenic (nature vs human impact).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class EnvironmentalScienceDomain(KnowledgeDomain):
    """
    Environmental Science knowledge domain.

    Fundamental Duality: Natural / Anthropogenic
    - Natural: Earth systems, natural processes
    - Anthropogenic: Human impacts, modifications

    Secondary Dualities:
    - Conservation / Development
    - Local / Global
    - Mitigation / Adaptation
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="EnvironmentalScience",
            domain_type=DomainType.FUNDAMENTAL,
            description="The interdisciplinary study of environmental systems and human impacts",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Natural/Anthropogenic duality."""
        self._domain.set_duality(
            positive_name="natural",
            positive_value=50,
            negative_name="anthropogenic",
            negative_value=50,
            duality_name="environmental_science_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental environmental science principles."""
        principles = [
            (
                "Systems Thinking",
                "Environment is interconnected system",
            ),
            (
                "Carrying Capacity",
                "Ecosystems have limits to support life",
            ),
            (
                "Sustainability",
                "Meet present needs without compromising future",
            ),
            (
                "Precautionary Principle",
                "Act to prevent harm despite uncertainty",
            ),
            (
                "Polluter Pays",
                "Those who cause damage bear costs",
            ),
            (
                "Interdependence",
                "All species and systems are connected",
            ),
            (
                "Biodiversity Value",
                "Biological diversity essential for resilience",
            ),
            (
                "Intergenerational Equity",
                "Future generations have environmental rights",
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
        """Get fundamental environmental science concepts."""
        return [
            "Ecosystem",
            "Biodiversity",
            "Climate",
            "Pollution",
            "Conservation",
            "Sustainability",
            "Resources",
            "Energy",
            "Water",
            "Air Quality",
            "Soil",
            "Carbon Cycle",
            "Habitat",
            "Waste",
            "Remediation",
        ]

    def initialize_branches(self) -> None:
        """Initialize major environmental science branches."""
        branches = [
            (
                "Climate Science",
                "Climate systems and change",
                ConceptType.THEORY,
            ),
            (
                "Conservation Biology",
                "Species and habitat preservation",
                ConceptType.THEORY,
            ),
            (
                "Environmental Chemistry",
                "Chemical processes in environment",
                ConceptType.THEORY,
            ),
            (
                "Environmental Toxicology",
                "Pollutant effects on organisms",
                ConceptType.THEORY,
            ),
            (
                "Hydrology",
                "Water systems and cycles",
                ConceptType.THEORY,
            ),
            (
                "Atmospheric Science",
                "Atmosphere composition and dynamics",
                ConceptType.THEORY,
            ),
            (
                "Soil Science",
                "Soil systems and processes",
                ConceptType.THEORY,
            ),
            (
                "Environmental Policy",
                "Environmental governance",
                ConceptType.THEORY,
            ),
            (
                "Restoration Ecology",
                "Ecosystem restoration",
                ConceptType.THEORY,
            ),
            (
                "Environmental Engineering",
                "Technical solutions to environmental problems",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_environmental_issues(self) -> None:
        """Initialize major environmental issues."""
        issues = [
            ("Climate Change", "Global warming effects", "Global"),
            ("Biodiversity Loss", "Species extinction", "Ecological"),
            ("Air Pollution", "Atmospheric contamination", "Health"),
            ("Water Pollution", "Aquatic contamination", "Resource"),
            ("Deforestation", "Forest loss", "Land use"),
            ("Ocean Acidification", "Sea chemistry change", "Marine"),
        ]

        for name, description, category in issues:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_solutions(self) -> None:
        """Initialize environmental solutions."""
        solutions = [
            ("Renewable Energy", "Clean energy sources", "Mitigation"),
            ("Conservation Areas", "Protected habitats", "Protection"),
            ("Waste Recycling", "Material recovery", "Circular economy"),
            ("Carbon Capture", "CO2 removal", "Technology"),
            ("Sustainable Agriculture", "Eco-friendly farming", "Food"),
            ("Green Infrastructure", "Nature-based solutions", "Urban"),
        ]

        for name, description, category in solutions:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_environmental_pairs(self) -> None:
        """Initialize fundamental environmental pairs with META 50/50 balance."""
        pairs = [
            ("Natural", "Anthropogenic", "Nature vs human impact"),
            ("Conservation", "Development", "Preserve vs use"),
            ("Local", "Global", "Site vs planetary"),
            ("Mitigation", "Adaptation", "Prevent vs adjust"),
            ("Renewable", "Non-renewable", "Sustainable vs finite"),
            ("Source", "Sink", "Origin vs destination"),
            ("Biotic", "Abiotic", "Living vs non-living"),
            ("Terrestrial", "Aquatic", "Land vs water"),
            ("Pristine", "Degraded", "Intact vs damaged"),
            ("Prevention", "Remediation", "Avoid vs clean up"),
            ("Point Source", "Non-point", "Localized vs diffuse"),
            ("Short-term", "Long-term", "Immediate vs future"),
            ("Economy", "Environment", "Wealth vs nature"),
            ("Growth", "Sustainability", "Expansion vs balance"),
            ("Risk", "Safety", "Harm vs protection"),
            ("Extraction", "Restoration", "Taking vs giving back"),
            ("Urban", "Rural", "City vs countryside"),
            ("Production", "Consumption", "Making vs using"),
            ("Pollution", "Purification", "Contaminating vs cleaning"),
            ("Fragmentation", "Connectivity", "Broken vs linked"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Environmental)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Environmental)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_planetary_boundaries(self) -> dict[str, str]:
        """Get planetary boundaries framework."""
        return {
            "climate_change": "CO2 concentration limits",
            "biodiversity_loss": "Species extinction rate",
            "nitrogen_cycle": "Nitrogen fixation limits",
            "phosphorus_cycle": "Phosphorus flow to oceans",
            "ozone_depletion": "Stratospheric ozone",
            "ocean_acidification": "Carbonate saturation state",
        }

    def demonstrate_environmental_balance(self) -> dict[str, Any]:
        """Demonstrate environmental science balance principles."""
        return {
            "concept": "Environmental Science Equilibrium",
            "dualities": {
                "natural_anthropogenic": {
                    "natural": 50.0,
                    "anthropogenic": 50.0,
                    "meaning": "Understanding both natural systems and human impacts",
                },
                "conservation_development": {
                    "conservation": 50.0,
                    "development": 50.0,
                    "meaning": "Balancing preservation and use",
                },
                "mitigation_adaptation": {
                    "mitigation": 50.0,
                    "adaptation": 50.0,
                    "meaning": "Both preventing and adjusting to change",
                },
            },
            "sustainability_balance": {
                "present": 50.0,
                "future": 50.0,
                "description": "Current needs and future generations equally important",
            },
            "meta_meaning": "Environmental Science demonstrates META 50/50 in natural-anthropogenic harmony",
        }


def create_environmental_science_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> EnvironmentalScienceDomain:
    """
    Factory function to create a fully initialized environmental science domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized EnvironmentalScienceDomain
    """
    domain = EnvironmentalScienceDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_environmental_issues()
        domain.initialize_solutions()
        domain.initialize_environmental_pairs()

    return domain
