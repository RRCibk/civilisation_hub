"""
Botany Domain
=============
Botanical knowledge domain with META 50/50 equilibrium.
Fundamental duality: Growth/Dormancy (active vs resting states).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class BotanyDomain(KnowledgeDomain):
    """
    Botany knowledge domain.

    Fundamental Duality: Growth / Dormancy
    - Growth: Active metabolism, cell division, development
    - Dormancy: Suspended growth, energy conservation, survival mode

    Secondary Dualities:
    - Photosynthesis / Respiration
    - Root / Shoot
    - Flower / Seed
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Botany",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of plants, their structure, growth, and classification",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Growth/Dormancy duality."""
        self._domain.set_duality(
            positive_name="growth",
            positive_value=50,
            negative_name="dormancy",
            negative_value=50,
            duality_name="botany_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental botanical principles."""
        principles = [
            (
                "Photosynthesis",
                "Plants convert light energy to chemical energy using CO2 and water",
            ),
            (
                "Cellular Respiration",
                "Plants release energy from glucose through respiration",
            ),
            (
                "Tropism",
                "Plants grow in response to environmental stimuli",
            ),
            (
                "Alternation of Generations",
                "Plants alternate between sporophyte and gametophyte phases",
            ),
            (
                "Apical Dominance",
                "Main stem suppresses growth of lateral branches",
            ),
            (
                "Photoperiodism",
                "Plants respond to day length for flowering and growth",
            ),
            (
                "Transpiration",
                "Water moves from roots to leaves and evaporates",
            ),
            (
                "Nutrient Uptake",
                "Plants absorb minerals through roots via active transport",
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
        """Get fundamental botany concepts."""
        return [
            "Cell",
            "Chloroplast",
            "Root",
            "Stem",
            "Leaf",
            "Flower",
            "Seed",
            "Fruit",
            "Xylem",
            "Phloem",
            "Stomata",
            "Chlorophyll",
            "Photosynthesis",
            "Pollination",
            "Germination",
        ]

    def initialize_branches(self) -> None:
        """Initialize major botany branches."""
        branches = [
            (
                "Plant Anatomy",
                "Study of internal plant structure",
                ConceptType.THEORY,
            ),
            (
                "Plant Physiology",
                "Study of plant functions and processes",
                ConceptType.THEORY,
            ),
            (
                "Plant Taxonomy",
                "Classification and naming of plants",
                ConceptType.THEORY,
            ),
            (
                "Plant Ecology",
                "Plants in relation to environment",
                ConceptType.THEORY,
            ),
            (
                "Plant Genetics",
                "Heredity and variation in plants",
                ConceptType.THEORY,
            ),
            (
                "Phytopathology",
                "Study of plant diseases",
                ConceptType.THEORY,
            ),
            (
                "Ethnobotany",
                "Traditional plant uses by humans",
                ConceptType.THEORY,
            ),
            (
                "Paleobotany",
                "Study of fossil plants",
                ConceptType.THEORY,
            ),
            (
                "Mycology",
                "Study of fungi",
                ConceptType.THEORY,
            ),
            (
                "Phycology",
                "Study of algae",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_plant_groups(self) -> None:
        """Initialize major plant groups."""
        groups = [
            ("Bryophytes", "Non-vascular plants", ["Mosses", "Liverworts", "Hornworts"]),
            ("Pteridophytes", "Seedless vascular plants", ["Ferns", "Horsetails", "Clubmosses"]),
            ("Gymnosperms", "Naked seed plants", ["Conifers", "Cycads", "Ginkgo"]),
            ("Angiosperms", "Flowering plants", ["Monocots", "Dicots"]),
        ]

        for name, description, examples in groups:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_plant_tissues(self) -> None:
        """Initialize plant tissue types."""
        tissues = [
            ("Epidermis", "Outer protective layer", "Protection"),
            ("Parenchyma", "Ground tissue for storage", "Storage, photosynthesis"),
            ("Collenchyma", "Flexible support tissue", "Support"),
            ("Sclerenchyma", "Rigid support tissue", "Support"),
            ("Xylem", "Water conducting tissue", "Water transport"),
            ("Phloem", "Sugar conducting tissue", "Nutrient transport"),
            ("Meristem", "Growth tissue", "Cell division"),
            ("Cork", "Protective outer bark", "Protection"),
        ]

        for name, description, function in tissues:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["function"] = function

    def initialize_plant_organs(self) -> None:
        """Initialize plant organ systems."""
        organs = [
            ("Root", "Underground organ for absorption and anchorage", ["Taproot", "Fibrous"]),
            ("Stem", "Support structure connecting roots and leaves", ["Herbaceous", "Woody"]),
            ("Leaf", "Photosynthetic organ", ["Simple", "Compound"]),
            ("Flower", "Reproductive organ", ["Complete", "Incomplete"]),
            ("Fruit", "Mature ovary containing seeds", ["Fleshy", "Dry"]),
            ("Seed", "Embryo with stored food", ["Monocot", "Dicot"]),
        ]

        for name, description, types in organs:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["types"] = types

    def initialize_photosynthesis_process(self) -> None:
        """Initialize photosynthesis components."""
        components = [
            ("Light Reactions", "Light-dependent reactions in thylakoid", "ATP and NADPH"),
            ("Calvin Cycle", "Light-independent carbon fixation", "Glucose"),
            ("Chlorophyll", "Primary photosynthetic pigment", "Light absorption"),
            ("Carotenoids", "Accessory pigments", "Light absorption"),
            ("Rubisco", "Carbon-fixing enzyme", "CO2 fixation"),
            ("ATP Synthase", "Energy-producing enzyme", "ATP synthesis"),
        ]

        for name, description, function in components:
            concept = self.create_concept(
                name=f"{name} (Photosynthesis)",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["function"] = function

    def initialize_botanical_pairs(self) -> None:
        """Initialize fundamental botanical pairs with META 50/50 balance."""
        pairs = [
            ("Growth", "Dormancy", "Active vs resting"),
            ("Photosynthesis", "Respiration", "Building vs breaking"),
            ("Root", "Shoot", "Below vs above ground"),
            ("Flower", "Seed", "Reproduction vs propagation"),
            ("Deciduous", "Evergreen", "Shedding vs keeping"),
            ("Annual", "Perennial", "One year vs many"),
            ("Vascular", "Nonvascular", "Tubes vs no tubes"),
            ("Monocot", "Dicot", "One vs two seed leaves"),
            ("Pollination", "Fertilization", "Transfer vs fusion"),
            ("Germination", "Senescence", "Starting vs ending"),
            ("Xylem", "Phloem", "Water up vs sugar down"),
            ("Stomata Open", "Stomata Closed", "Gas exchange on vs off"),
            ("Tropism", "Nastic", "Directional vs non-directional"),
            ("Herbaceous", "Woody", "Soft vs hard stem"),
            ("Native", "Cultivated", "Wild vs farmed"),
            ("Parasite", "Host", "Taking vs giving"),
            ("Nitrogen Fixing", "Nitrogen Using", "Creating vs consuming"),
            ("Sun", "Shade", "Light vs dark tolerant"),
            ("Drought Resistant", "Water Loving", "Dry vs wet adapted"),
            ("Fruit", "Vegetable", "Seed bearing vs not"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Botany)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Botany)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_photosynthesis_equation(self) -> dict[str, str]:
        """Get photosynthesis equation components."""
        return {
            "overall": "6CO2 + 6H2O + light -> C6H12O6 + 6O2",
            "reactants": "Carbon dioxide, Water, Light energy",
            "products": "Glucose, Oxygen",
            "location": "Chloroplast",
        }

    def demonstrate_plant_balance(self) -> dict[str, Any]:
        """Demonstrate plant balance principles."""
        return {
            "concept": "Plant Equilibrium",
            "dualities": {
                "growth_dormancy": {
                    "growth_phase": 50.0,
                    "dormancy_phase": 50.0,
                    "meaning": "Plants cycle between growth and rest",
                },
                "photosynthesis_respiration": {
                    "carbon_fixed": 50.0,
                    "carbon_released": 50.0,
                    "meaning": "Net carbon exchange in balance",
                },
                "water_balance": {
                    "water_uptake": 50.0,
                    "water_loss": 50.0,
                    "meaning": "Transpiration balanced by absorption",
                },
            },
            "nutrient_balance": {
                "uptake": 50.0,
                "utilization": 50.0,
                "description": "Nutrients absorbed equal nutrients used",
            },
            "meta_meaning": "Botany demonstrates META 50/50 in plant life cycles",
        }


def create_botany_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> BotanyDomain:
    """
    Factory function to create a fully initialized botany domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized BotanyDomain
    """
    domain = BotanyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_plant_groups()
        domain.initialize_plant_tissues()
        domain.initialize_plant_organs()
        domain.initialize_photosynthesis_process()
        domain.initialize_botanical_pairs()

    return domain
