"""
Paleontology Domain
===================
Paleontological knowledge domain with META 50/50 equilibrium.
Fundamental duality: Extinction/Emergence (ending vs beginning of species).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class PaleontologyDomain(KnowledgeDomain):
    """
    Paleontology knowledge domain.

    Fundamental Duality: Extinction / Emergence
    - Extinction: Species ending, disappearance, mass death events
    - Emergence: Species origin, diversification, radiation events

    Secondary Dualities:
    - Fossil / Living
    - Prehistoric / Historic
    - Evolution / Stasis
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Paleontology",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of ancient life through fossils",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Extinction/Emergence duality."""
        self._domain.set_duality(
            positive_name="extinction",
            positive_value=50,
            negative_name="emergence",
            negative_value=50,
            duality_name="paleontology_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental paleontological principles."""
        principles = [
            (
                "Faunal Succession",
                "Fossil assemblages succeed one another in predictable order",
            ),
            (
                "Biotic Replacement",
                "Extinction of one group often allows radiation of another",
            ),
            (
                "Punctuated Equilibrium",
                "Evolution occurs in rapid bursts between periods of stasis",
            ),
            (
                "Uniformitarianism",
                "Past geological processes operated as they do today",
            ),
            (
                "Index Fossil Principle",
                "Certain fossils indicate specific geological time periods",
            ),
            (
                "Extinction Inevitability",
                "All species eventually go extinct",
            ),
            (
                "Common Descent",
                "All life shares common ancestors",
            ),
            (
                "Taphonomic Bias",
                "Fossil record is incomplete and biased by preservation",
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
        """Get fundamental paleontology concepts."""
        return [
            "Fossil",
            "Extinction",
            "Evolution",
            "Stratigraphy",
            "Taphonomy",
            "Morphology",
            "Taxonomy",
            "Phylogeny",
            "Adaptation",
            "Speciation",
            "Radiation",
            "Dinosaur",
            "Trilobite",
            "Ammonite",
            "Mammoth",
        ]

    def initialize_branches(self) -> None:
        """Initialize major paleontology branches."""
        branches = [
            (
                "Vertebrate Paleontology",
                "Study of ancient vertebrates",
                ConceptType.THEORY,
            ),
            (
                "Invertebrate Paleontology",
                "Study of ancient invertebrates",
                ConceptType.THEORY,
            ),
            (
                "Paleobotany",
                "Study of ancient plants",
                ConceptType.THEORY,
            ),
            (
                "Micropaleontology",
                "Study of microscopic fossils",
                ConceptType.THEORY,
            ),
            (
                "Paleoecology",
                "Study of ancient ecosystems",
                ConceptType.THEORY,
            ),
            (
                "Paleoclimatology",
                "Study of ancient climates",
                ConceptType.THEORY,
            ),
            (
                "Biostratigraphy",
                "Dating rocks using fossils",
                ConceptType.THEORY,
            ),
            (
                "Taphonomy",
                "Study of fossilization processes",
                ConceptType.THEORY,
            ),
            (
                "Paleoanthropology",
                "Study of human evolution",
                ConceptType.THEORY,
            ),
            (
                "Paleogenetics",
                "Study of ancient DNA",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_geological_eras(self) -> None:
        """Initialize geological eras."""
        eras = [
            ("Hadean Eon", 4600, 4000, "Formation of Earth, no life"),
            ("Archean Eon", 4000, 2500, "First life, stromatolites"),
            ("Proterozoic Eon", 2500, 541, "Oxygen rise, first eukaryotes"),
            ("Paleozoic Era", 541, 252, "Cambrian explosion to Permian extinction"),
            ("Mesozoic Era", 252, 66, "Age of dinosaurs"),
            ("Cenozoic Era", 66, 0, "Age of mammals"),
        ]

        for name, start_mya, end_mya, key_events in eras:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=key_events,
            )
            concept.metadata.update({
                "start_mya": start_mya,
                "end_mya": end_mya,
            })

    def initialize_mass_extinctions(self) -> None:
        """Initialize major mass extinction events."""
        extinctions = [
            ("Ordovician-Silurian", 445, 85, "Glaciation, sea level change"),
            ("Late Devonian", 375, 75, "Possible volcanism, anoxia"),
            ("Permian-Triassic", 252, 96, "Siberian Traps volcanism"),
            ("Triassic-Jurassic", 201, 80, "Central Atlantic Magmatic Province"),
            ("Cretaceous-Paleogene", 66, 76, "Asteroid impact, Deccan Traps"),
        ]

        for name, mya, species_lost_percent, cause in extinctions:
            concept = self.create_concept(
                name=f"{name} Extinction",
                concept_type=ConceptType.DEFINITION,
                description=f"Mass extinction {mya} million years ago",
            )
            concept.metadata.update({
                "mya": mya,
                "species_lost_percent": species_lost_percent,
                "probable_cause": cause,
            })

    def initialize_fossil_types(self) -> None:
        """Initialize fossil type classifications."""
        fossils = [
            ("Body Fossil", "Preserved remains of organism", ["Bones", "Shells", "Teeth"]),
            ("Trace Fossil", "Evidence of organism activity", ["Footprints", "Burrows", "Coprolites"]),
            ("Mold Fossil", "Impression left by organism", ["External mold", "Internal mold"]),
            ("Cast Fossil", "Mold filled with minerals", ["Mineral replacement"]),
            ("Permineralization", "Minerals fill cellular spaces", ["Petrified wood"]),
            ("Compression Fossil", "Flattened remains", ["Plant leaves", "Fish"]),
            ("Amber", "Organism preserved in tree resin", ["Insects", "Feathers"]),
            ("Frozen", "Preserved in ice", ["Mammoths", "Ice age fauna"]),
        ]

        for name, description, examples in fossils:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_iconic_fossils(self) -> None:
        """Initialize iconic fossil organisms."""
        fossils = [
            ("Trilobite", "Paleozoic arthropod", "Cambrian-Permian", 521),
            ("Ammonite", "Coiled cephalopod", "Devonian-Cretaceous", 400),
            ("Tyrannosaurus rex", "Apex theropod dinosaur", "Late Cretaceous", 68),
            ("Triceratops", "Horned ceratopsian dinosaur", "Late Cretaceous", 68),
            ("Archaeopteryx", "Early feathered dinosaur/bird", "Late Jurassic", 150),
            ("Australopithecus", "Early hominin", "Pliocene", 4),
            ("Mammuthus", "Woolly mammoth", "Pleistocene", 0.01),
            ("Dimetrodon", "Early synapsid", "Permian", 295),
        ]

        for name, description, period, mya in fossils:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "period": period,
                "mya": mya,
            })

    def initialize_paleontological_pairs(self) -> None:
        """Initialize fundamental paleontological pairs with META 50/50 balance."""
        pairs = [
            ("Extinction", "Emergence", "Ending vs beginning"),
            ("Fossil", "Living", "Ancient vs current"),
            ("Prehistoric", "Historic", "Before vs after records"),
            ("Evolution", "Stasis", "Changing vs stable"),
            ("Mass Extinction", "Radiation", "Dying vs diversifying"),
            ("Ancestor", "Descendant", "Earlier vs later"),
            ("Primitive", "Derived", "Original vs evolved"),
            ("Terrestrial", "Marine", "Land vs sea"),
            ("Vertebrate", "Invertebrate", "Backbone vs none"),
            ("Mesozoic", "Cenozoic", "Reptile vs mammal age"),
            ("Permineralization", "Compression", "Mineral vs flattened"),
            ("Index Fossil", "Trace Fossil", "Body vs activity"),
            ("Stratigraphy", "Morphology", "Layers vs form"),
            ("Adaptive", "Maladaptive", "Surviving vs failing"),
            ("Convergent", "Divergent", "Similar vs different"),
            ("Endemic", "Cosmopolitan", "Local vs widespread"),
            ("Herbivore", "Carnivore", "Plant vs meat"),
            ("Giant", "Dwarf", "Large vs small"),
            ("Warm Period", "Ice Age", "Hot vs cold"),
            ("Fossil Record", "Gap", "Evidence vs missing"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Paleontology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Paleontology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_geological_time_scale(self) -> dict[str, dict[str, Any]]:
        """Get geological time scale summary."""
        return {
            "precambrian": {
                "duration_my": 4059,
                "percent_earth_history": 88,
                "key_events": ["Origin of life", "Oxygenation"],
            },
            "paleozoic": {
                "duration_my": 289,
                "percent_earth_history": 6.3,
                "key_events": ["Cambrian explosion", "Land colonization"],
            },
            "mesozoic": {
                "duration_my": 186,
                "percent_earth_history": 4.0,
                "key_events": ["Dinosaur dominance", "Flowering plants"],
            },
            "cenozoic": {
                "duration_my": 66,
                "percent_earth_history": 1.4,
                "key_events": ["Mammal radiation", "Human evolution"],
            },
        }

    def demonstrate_paleontological_balance(self) -> dict[str, Any]:
        """Demonstrate paleontological balance principles."""
        return {
            "concept": "Paleontological Equilibrium",
            "dualities": {
                "extinction_emergence": {
                    "extinctions": 50.0,
                    "emergences": 50.0,
                    "meaning": "Species lost are replaced by new species",
                },
                "background_mass": {
                    "background_extinction": 50.0,
                    "mass_extinction": 50.0,
                    "meaning": "Normal turnover punctuated by crises",
                },
                "stability_change": {
                    "stasis": 50.0,
                    "evolution": 50.0,
                    "meaning": "Punctuated equilibrium pattern",
                },
            },
            "diversity_balance": {
                "species_origination": 50.0,
                "species_extinction": 50.0,
                "description": "Long-term biodiversity is relatively stable",
            },
            "meta_meaning": "Paleontology demonstrates META 50/50 in extinction-emergence cycles",
        }


def create_paleontology_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> PaleontologyDomain:
    """
    Factory function to create a fully initialized paleontology domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized PaleontologyDomain
    """
    domain = PaleontologyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_geological_eras()
        domain.initialize_mass_extinctions()
        domain.initialize_fossil_types()
        domain.initialize_iconic_fossils()
        domain.initialize_paleontological_pairs()

    return domain
