"""
Ecology Domain
==============
Ecological knowledge domain with META 50/50 equilibrium.
Fundamental duality: Growth/Decay (production vs decomposition).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class EcologyDomain(KnowledgeDomain):
    """
    Ecology knowledge domain.

    Fundamental Duality: Growth / Decay
    - Growth: Production, biomass accumulation, population increase
    - Decay: Decomposition, nutrient recycling, population decrease

    Secondary Dualities:
    - Producer / Consumer
    - Predator / Prey
    - Symbiosis / Parasitism
    - Native / Invasive
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Ecology",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of organisms and their interactions with the environment",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Growth/Decay duality."""
        self._domain.set_duality(
            positive_name="growth",
            positive_value=50,
            negative_name="decay",
            negative_value=50,
            duality_name="ecology_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental ecological principles."""
        principles = [
            (
                "Energy Flow",
                "Energy flows through ecosystems in one direction, from sun to decomposers",
            ),
            (
                "Nutrient Cycling",
                "Matter cycles through ecosystems in biogeochemical cycles",
            ),
            (
                "Competitive Exclusion",
                "Two species cannot occupy the same niche indefinitely",
            ),
            (
                "Limiting Factors",
                "Population growth is limited by the scarcest essential resource",
            ),
            (
                "Ecological Succession",
                "Ecosystems undergo predictable changes over time",
            ),
            (
                "Trophic Efficiency",
                "Only ~10% of energy transfers between trophic levels",
            ),
            (
                "Carrying Capacity",
                "Environments can support only a maximum population size",
            ),
            (
                "Biodiversity-Stability",
                "Greater biodiversity generally leads to ecosystem stability",
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
        """Get fundamental ecology concepts."""
        return [
            "Ecosystem",
            "Population",
            "Community",
            "Habitat",
            "Niche",
            "Food Web",
            "Biome",
            "Biodiversity",
            "Producer",
            "Consumer",
            "Decomposer",
            "Symbiosis",
            "Competition",
            "Succession",
            "Cycle",
        ]

    def initialize_branches(self) -> None:
        """Initialize major ecology branches."""
        branches = [
            (
                "Population Ecology",
                "Study of population dynamics and interactions",
                ConceptType.THEORY,
            ),
            (
                "Community Ecology",
                "Study of species interactions within communities",
                ConceptType.THEORY,
            ),
            (
                "Ecosystem Ecology",
                "Study of energy flow and nutrient cycling",
                ConceptType.THEORY,
            ),
            (
                "Landscape Ecology",
                "Study of spatial patterns and ecological processes",
                ConceptType.THEORY,
            ),
            (
                "Behavioral Ecology",
                "Study of ecological and evolutionary basis of behavior",
                ConceptType.THEORY,
            ),
            (
                "Conservation Ecology",
                "Study of biodiversity preservation and restoration",
                ConceptType.THEORY,
            ),
            (
                "Marine Ecology",
                "Study of ocean ecosystems and organisms",
                ConceptType.THEORY,
            ),
            (
                "Freshwater Ecology",
                "Study of lakes, rivers, and wetland ecosystems",
                ConceptType.THEORY,
            ),
            (
                "Microbial Ecology",
                "Study of microorganisms in ecosystems",
                ConceptType.THEORY,
            ),
            (
                "Urban Ecology",
                "Study of ecosystems in urban environments",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_trophic_levels(self) -> None:
        """Initialize trophic level classifications."""
        levels = [
            ("Primary Producer", "Autotrophs that create organic matter", 1, ["Plants", "Algae"]),
            ("Primary Consumer", "Herbivores that eat producers", 2, ["Deer", "Caterpillar"]),
            ("Secondary Consumer", "Carnivores that eat herbivores", 3, ["Snake", "Frog"]),
            ("Tertiary Consumer", "Top predators", 4, ["Eagle", "Shark"]),
            ("Decomposer", "Organisms that break down dead matter", 0, ["Fungi", "Bacteria"]),
        ]

        for name, description, level, examples in levels:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({"trophic_level": level, "examples": examples})

    def initialize_biomes(self) -> None:
        """Initialize major biome types."""
        biomes = [
            ("Tropical Rainforest", "Hot, wet, high biodiversity", 25, 2000),
            ("Temperate Forest", "Moderate climate, deciduous trees", 12, 1000),
            ("Boreal Forest", "Cold, coniferous, long winters", 0, 500),
            ("Grassland", "Dominated by grasses, moderate rainfall", 15, 600),
            ("Desert", "Arid, extreme temperatures", 25, 100),
            ("Tundra", "Cold, permafrost, low vegetation", -10, 250),
            ("Savanna", "Tropical grassland with scattered trees", 25, 900),
            ("Wetland", "Saturated soil, high productivity", 15, 1200),
            ("Coral Reef", "Marine, high biodiversity", 25, 0),
            ("Deep Ocean", "Dark, high pressure, cold", 4, 0),
        ]

        for name, description, avg_temp, rainfall in biomes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "average_temp_c": avg_temp,
                "rainfall_mm": rainfall,
            })

    def initialize_symbiotic_relationships(self) -> None:
        """Initialize types of symbiotic relationships."""
        relationships = [
            ("Mutualism", "Both species benefit", "+/+", "Bee and flower"),
            ("Commensalism", "One benefits, other unaffected", "+/0", "Barnacle on whale"),
            ("Parasitism", "One benefits, other harmed", "+/-", "Tick on dog"),
            ("Predation", "One kills and eats other", "+/-", "Lion and zebra"),
            ("Competition", "Both species harmed", "-/-", "Plants for sunlight"),
            ("Amensalism", "One harmed, other unaffected", "-/0", "Tree shading plants"),
        ]

        for name, description, effect, example in relationships:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({"effect": effect, "example": example})

    def initialize_biogeochemical_cycles(self) -> None:
        """Initialize major biogeochemical cycles."""
        cycles = [
            ("Carbon Cycle", "Movement of carbon through ecosystems", ["Photosynthesis", "Respiration"]),
            ("Nitrogen Cycle", "Transformation of nitrogen compounds", ["Fixation", "Denitrification"]),
            ("Water Cycle", "Circulation of water in the biosphere", ["Evaporation", "Precipitation"]),
            ("Phosphorus Cycle", "Movement of phosphorus through ecosystems", ["Weathering", "Uptake"]),
            ("Sulfur Cycle", "Cycling of sulfur compounds", ["Volcanic", "Bacterial"]),
        ]

        for name, description, key_processes in cycles:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["key_processes"] = key_processes

    def initialize_ecological_pairs(self) -> None:
        """Initialize fundamental ecological pairs with META 50/50 balance."""
        pairs = [
            ("Growth", "Decay", "Building vs breaking down"),
            ("Producer", "Consumer", "Creating vs using"),
            ("Predator", "Prey", "Hunter vs hunted"),
            ("Symbiosis", "Parasitism", "Mutual vs exploitative"),
            ("Native", "Invasive", "Indigenous vs foreign"),
            ("Abundance", "Scarcity", "Plentiful vs rare"),
            ("Biodiversity", "Monoculture", "Variety vs uniformity"),
            ("Succession", "Climax", "Changing vs stable"),
            ("Niche", "Habitat", "Role vs place"),
            ("Biotic", "Abiotic", "Living vs non-living"),
            ("Autotroph", "Heterotroph", "Self-feeding vs other-feeding"),
            ("Herbivore", "Carnivore", "Plant vs meat eater"),
            ("Decomposer", "Producer", "Breaking vs building"),
            ("Mutualism", "Competition", "Cooperation vs rivalry"),
            ("Migration", "Residence", "Moving vs staying"),
            ("Diurnal", "Nocturnal", "Day vs night active"),
            ("Terrestrial", "Aquatic", "Land vs water"),
            ("Tropical", "Polar", "Hot vs cold zone"),
            ("Endangered", "Thriving", "At risk vs flourishing"),
            ("Ecosystem", "Organism", "System vs individual"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Ecology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Ecology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def demonstrate_ecological_balance(self) -> dict[str, Any]:
        """Demonstrate ecological balance principles."""
        return {
            "concept": "Ecological Equilibrium",
            "dualities": {
                "growth_decay": {
                    "production": 50.0,
                    "decomposition": 50.0,
                    "meaning": "Biomass created equals biomass decomposed",
                },
                "predator_prey": {
                    "predator_population": 50.0,
                    "prey_population": 50.0,
                    "meaning": "Populations oscillate around equilibrium",
                },
                "energy_balance": {
                    "energy_input": 50.0,
                    "energy_output": 50.0,
                    "meaning": "Solar energy in equals heat dissipated",
                },
            },
            "nutrient_cycling": {
                "uptake": 50.0,
                "release": 50.0,
                "description": "Nutrients cycle in closed loops",
            },
            "meta_meaning": "Ecology demonstrates META 50/50 in all balanced ecosystems",
        }


def create_ecology_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> EcologyDomain:
    """
    Factory function to create a fully initialized ecology domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized EcologyDomain
    """
    domain = EcologyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_trophic_levels()
        domain.initialize_biomes()
        domain.initialize_symbiotic_relationships()
        domain.initialize_biogeochemical_cycles()
        domain.initialize_ecological_pairs()

    return domain
