"""
Zoology Domain
==============
Zoological knowledge domain with META 50/50 equilibrium.
Fundamental duality: Predator/Prey (ecological roles in food webs).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class ZoologyDomain(KnowledgeDomain):
    """
    Zoology knowledge domain.

    Fundamental Duality: Predator / Prey
    - Predator: Hunter, consumer, top of food chain
    - Prey: Hunted, consumed, supports predator population

    Secondary Dualities:
    - Vertebrate / Invertebrate
    - Warm-blooded / Cold-blooded
    - Carnivore / Herbivore
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Zoology",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of animals, their behavior, physiology, and classification",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Predator/Prey duality."""
        self._domain.set_duality(
            positive_name="predator",
            positive_value=50,
            negative_name="prey",
            negative_value=50,
            duality_name="zoology_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental zoological principles."""
        principles = [
            (
                "Cell Theory",
                "All animals are composed of cells",
            ),
            (
                "Evolution by Natural Selection",
                "Animals evolve through differential reproductive success",
            ),
            (
                "Homeostasis",
                "Animals maintain internal stability despite external changes",
            ),
            (
                "Energy Flow",
                "Energy flows from prey to predator through food webs",
            ),
            (
                "Adaptation",
                "Animals are adapted to their environments",
            ),
            (
                "Behavior-Ecology Link",
                "Animal behavior is shaped by ecological pressures",
            ),
            (
                "Phylogenetic Relationship",
                "All animals share common ancestry",
            ),
            (
                "Structure-Function Correlation",
                "Animal structure is related to its function",
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
        """Get fundamental zoology concepts."""
        return [
            "Animal",
            "Cell",
            "Tissue",
            "Organ",
            "System",
            "Behavior",
            "Adaptation",
            "Evolution",
            "Reproduction",
            "Metabolism",
            "Locomotion",
            "Predation",
            "Migration",
            "Communication",
            "Taxonomy",
        ]

    def initialize_branches(self) -> None:
        """Initialize major zoology branches."""
        branches = [
            (
                "Mammalogy",
                "Study of mammals",
                ConceptType.THEORY,
            ),
            (
                "Ornithology",
                "Study of birds",
                ConceptType.THEORY,
            ),
            (
                "Herpetology",
                "Study of reptiles and amphibians",
                ConceptType.THEORY,
            ),
            (
                "Ichthyology",
                "Study of fish",
                ConceptType.THEORY,
            ),
            (
                "Entomology",
                "Study of insects",
                ConceptType.THEORY,
            ),
            (
                "Arachnology",
                "Study of spiders and scorpions",
                ConceptType.THEORY,
            ),
            (
                "Malacology",
                "Study of mollusks",
                ConceptType.THEORY,
            ),
            (
                "Ethology",
                "Study of animal behavior",
                ConceptType.THEORY,
            ),
            (
                "Comparative Anatomy",
                "Comparison of animal structures",
                ConceptType.THEORY,
            ),
            (
                "Parasitology",
                "Study of parasitic animals",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_animal_phyla(self) -> None:
        """Initialize major animal phyla."""
        phyla = [
            ("Porifera", "Sponges", False, ["Sea sponge"]),
            ("Cnidaria", "Jellyfish and corals", False, ["Jellyfish", "Coral"]),
            ("Platyhelminthes", "Flatworms", False, ["Planaria", "Tapeworm"]),
            ("Nematoda", "Roundworms", False, ["C. elegans", "Hookworm"]),
            ("Annelida", "Segmented worms", False, ["Earthworm", "Leech"]),
            ("Mollusca", "Mollusks", False, ["Snail", "Octopus", "Clam"]),
            ("Arthropoda", "Jointed-leg animals", False, ["Insect", "Spider", "Crab"]),
            ("Echinodermata", "Spiny-skinned animals", False, ["Starfish", "Sea urchin"]),
            ("Chordata", "Animals with notochord", True, ["Fish", "Mammals", "Birds"]),
        ]

        for name, description, has_vertebrates, examples in phyla:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "has_vertebrates": has_vertebrates,
                "examples": examples,
            })

    def initialize_vertebrate_classes(self) -> None:
        """Initialize vertebrate classes."""
        classes = [
            ("Fish", "Aquatic vertebrates with gills", "Cold-blooded", ["Salmon", "Shark"]),
            ("Amphibians", "Dual life vertebrates", "Cold-blooded", ["Frog", "Salamander"]),
            ("Reptiles", "Scaly cold-blooded vertebrates", "Cold-blooded", ["Snake", "Lizard"]),
            ("Birds", "Feathered vertebrates", "Warm-blooded", ["Eagle", "Penguin"]),
            ("Mammals", "Fur-bearing milk producers", "Warm-blooded", ["Human", "Whale"]),
        ]

        for name, description, thermoreg, examples in classes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "thermoregulation": thermoreg,
                "examples": examples,
            })

    def initialize_animal_systems(self) -> None:
        """Initialize animal organ systems."""
        systems = [
            ("Nervous System", "Signal transmission and control", ["Brain", "Nerves"]),
            ("Circulatory System", "Blood and nutrient transport", ["Heart", "Blood vessels"]),
            ("Respiratory System", "Gas exchange", ["Lungs", "Gills"]),
            ("Digestive System", "Food processing", ["Stomach", "Intestines"]),
            ("Excretory System", "Waste removal", ["Kidneys", "Bladder"]),
            ("Skeletal System", "Support and protection", ["Bones", "Cartilage"]),
            ("Muscular System", "Movement", ["Skeletal muscle", "Cardiac muscle"]),
            ("Endocrine System", "Hormone regulation", ["Glands", "Hormones"]),
            ("Reproductive System", "Offspring production", ["Gonads", "Gametes"]),
            ("Immune System", "Disease defense", ["White blood cells", "Antibodies"]),
        ]

        for name, description, components in systems:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["components"] = components

    def initialize_animal_behaviors(self) -> None:
        """Initialize animal behavior types."""
        behaviors = [
            ("Instinct", "Innate, unlearned behavior", "Web building in spiders"),
            ("Learning", "Behavior modified by experience", "Bird song learning"),
            ("Migration", "Seasonal long-distance movement", "Salmon returning to spawn"),
            ("Hibernation", "Winter dormancy", "Bear hibernation"),
            ("Courtship", "Mate attraction displays", "Peacock tail display"),
            ("Territoriality", "Defense of area", "Wolf pack territories"),
            ("Altruism", "Self-sacrifice for others", "Bee defending hive"),
            ("Communication", "Information transfer", "Whale songs"),
        ]

        for name, description, example in behaviors:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["example"] = example

    def initialize_zoological_pairs(self) -> None:
        """Initialize fundamental zoological pairs with META 50/50 balance."""
        pairs = [
            ("Predator", "Prey", "Hunter vs hunted"),
            ("Vertebrate", "Invertebrate", "Backbone vs no backbone"),
            ("Warm-blooded", "Cold-blooded", "Internal vs external heat"),
            ("Carnivore", "Herbivore", "Meat vs plant eater"),
            ("Diurnal", "Nocturnal", "Day vs night active"),
            ("Solitary", "Social", "Alone vs group"),
            ("Migratory", "Sedentary", "Moving vs staying"),
            ("Aquatic", "Terrestrial", "Water vs land"),
            ("Flying", "Flightless", "Aerial vs ground"),
            ("Oviparous", "Viviparous", "Egg vs live birth"),
            ("Camouflage", "Display", "Hiding vs showing"),
            ("Venomous", "Harmless", "Toxic vs safe"),
            ("Wild", "Domestic", "Free vs tamed"),
            ("Endangered", "Common", "Rare vs abundant"),
            ("Mammal", "Reptile", "Fur vs scales"),
            ("Insect", "Arachnid", "Six vs eight legs"),
            ("Larva", "Adult", "Immature vs mature"),
            ("Male", "Female", "Sperm vs egg producer"),
            ("Territorial", "Nomadic", "Fixed vs roaming"),
            ("Apex", "Base", "Top vs bottom of chain"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Zoology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Zoology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_animal_kingdom_stats(self) -> dict[str, Any]:
        """Get animal kingdom statistics."""
        return {
            "total_species": 1500000,
            "invertebrates_percent": 97,
            "vertebrates_percent": 3,
            "insects_species": 1000000,
            "mammals_species": 6500,
            "birds_species": 10000,
            "fish_species": 35000,
            "reptiles_species": 10000,
            "amphibians_species": 8000,
        }

    def demonstrate_animal_balance(self) -> dict[str, Any]:
        """Demonstrate animal balance principles."""
        return {
            "concept": "Animal Equilibrium",
            "dualities": {
                "predator_prey": {
                    "predator_population": 50.0,
                    "prey_population": 50.0,
                    "meaning": "Populations oscillate around equilibrium",
                },
                "birth_death": {
                    "birth_rate": 50.0,
                    "death_rate": 50.0,
                    "meaning": "Population stability through balance",
                },
                "energy_balance": {
                    "energy_intake": 50.0,
                    "energy_expenditure": 50.0,
                    "meaning": "Metabolic equilibrium",
                },
            },
            "ecological_balance": {
                "competition": 50.0,
                "cooperation": 50.0,
                "description": "Balance of competitive and cooperative behaviors",
            },
            "meta_meaning": "Zoology demonstrates META 50/50 in predator-prey dynamics",
        }


def create_zoology_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> ZoologyDomain:
    """
    Factory function to create a fully initialized zoology domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized ZoologyDomain
    """
    domain = ZoologyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_animal_phyla()
        domain.initialize_vertebrate_classes()
        domain.initialize_animal_systems()
        domain.initialize_animal_behaviors()
        domain.initialize_zoological_pairs()

    return domain
