"""
Geology Domain
==============
Geological knowledge domain with META 50/50 equilibrium.
Fundamental duality: Formation/Erosion (building vs wearing processes).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class GeologyDomain(KnowledgeDomain):
    """
    Geology knowledge domain.

    Fundamental Duality: Formation / Erosion
    - Formation: Constructive processes, mountain building, crystallization
    - Erosion: Destructive processes, weathering, breakdown

    Secondary Dualities:
    - Igneous / Sedimentary
    - Continental / Oceanic
    - Uplift / Subsidence
    - Tectonic / Volcanic
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Geology",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of Earth's solid matter, rocks, and processes",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Formation/Erosion duality."""
        self._domain.set_duality(
            positive_name="formation",
            positive_value=50,
            negative_name="erosion",
            negative_value=50,
            duality_name="geology_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental geological principles."""
        principles = [
            (
                "Uniformitarianism",
                "Present geological processes are the key to understanding the past",
            ),
            (
                "Superposition",
                "In undisturbed strata, older layers lie below younger layers",
            ),
            (
                "Original Horizontality",
                "Sedimentary layers are originally deposited horizontally",
            ),
            (
                "Lateral Continuity",
                "Sedimentary layers extend laterally in all directions",
            ),
            (
                "Cross-Cutting Relations",
                "Geological features that cut across others are younger",
            ),
            (
                "Faunal Succession",
                "Fossil assemblages succeed one another in predictable order",
            ),
            (
                "Plate Tectonics",
                "Earth's surface consists of moving lithospheric plates",
            ),
            (
                "Isostasy",
                "Earth's crust floats in gravitational equilibrium on the mantle",
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
        """Get fundamental geology concepts."""
        return [
            "Rock",
            "Mineral",
            "Plate",
            "Fault",
            "Fold",
            "Volcano",
            "Earthquake",
            "Sediment",
            "Magma",
            "Mantle",
            "Crust",
            "Core",
            "Fossil",
            "Stratum",
            "Erosion",
        ]

    def initialize_branches(self) -> None:
        """Initialize major geology branches."""
        branches = [
            (
                "Mineralogy",
                "Study of minerals, their composition and properties",
                ConceptType.THEORY,
            ),
            (
                "Petrology",
                "Study of rocks, their origin and composition",
                ConceptType.THEORY,
            ),
            (
                "Structural Geology",
                "Study of rock deformation and geological structures",
                ConceptType.THEORY,
            ),
            (
                "Sedimentology",
                "Study of sediments and sedimentary processes",
                ConceptType.THEORY,
            ),
            (
                "Volcanology",
                "Study of volcanoes and volcanic phenomena",
                ConceptType.THEORY,
            ),
            (
                "Seismology",
                "Study of earthquakes and seismic waves",
                ConceptType.THEORY,
            ),
            (
                "Geomorphology",
                "Study of landforms and landscape evolution",
                ConceptType.THEORY,
            ),
            (
                "Hydrogeology",
                "Study of groundwater and aquifer systems",
                ConceptType.THEORY,
            ),
            (
                "Paleontology",
                "Study of ancient life through fossils",
                ConceptType.THEORY,
            ),
            (
                "Geochemistry",
                "Study of chemical composition of Earth materials",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_rock_types(self) -> None:
        """Initialize rock classifications."""
        rocks = [
            ("Igneous", "Formed from cooled magma or lava", ["Granite", "Basalt", "Obsidian"]),
            ("Sedimentary", "Formed from accumulated sediments", ["Sandstone", "Limestone", "Shale"]),
            ("Metamorphic", "Transformed by heat and pressure", ["Marble", "Slate", "Quartzite"]),
        ]

        for name, description, examples in rocks:
            concept = self.create_concept(
                name=f"{name} Rock",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_plate_boundaries(self) -> None:
        """Initialize tectonic plate boundary types."""
        boundaries = [
            ("Divergent", "Plates moving apart", "Mid-Atlantic Ridge", "Rift valleys, new crust"),
            ("Convergent", "Plates moving together", "Himalayas", "Mountains, subduction"),
            ("Transform", "Plates sliding past", "San Andreas Fault", "Earthquakes"),
        ]

        for name, description, example, result in boundaries:
            concept = self.create_concept(
                name=f"{name} Boundary",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({"example": example, "geological_result": result})

    def initialize_earth_layers(self) -> None:
        """Initialize Earth's internal structure."""
        layers = [
            ("Inner Core", "Solid iron-nickel center", 1220, 5500),
            ("Outer Core", "Liquid iron-nickel layer", 2180, 4500),
            ("Lower Mantle", "Solid silicate layer", 2180, 3000),
            ("Upper Mantle", "Partially molten layer", 660, 1500),
            ("Asthenosphere", "Ductile flowing layer", 200, 1300),
            ("Lithosphere", "Rigid outer shell", 100, 500),
            ("Crust", "Thin outer layer", 35, 400),
        ]

        for name, description, thickness_km, temp_c in layers:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "thickness_km": thickness_km,
                "temperature_c": temp_c,
            })

    def initialize_geological_time(self) -> None:
        """Initialize geological time periods."""
        periods = [
            ("Hadean", 4600, 4000, "Formation of Earth"),
            ("Archean", 4000, 2500, "First life, no oxygen"),
            ("Proterozoic", 2500, 541, "Oxygen rise, complex cells"),
            ("Cambrian", 541, 485, "Explosion of life"),
            ("Ordovician", 485, 444, "Marine diversification"),
            ("Silurian", 444, 419, "First land plants"),
            ("Devonian", 419, 359, "Age of fishes"),
            ("Carboniferous", 359, 299, "Coal forests"),
            ("Permian", 299, 252, "Pangaea forms"),
            ("Triassic", 252, 201, "First dinosaurs"),
            ("Jurassic", 201, 145, "Dinosaur dominance"),
            ("Cretaceous", 145, 66, "Flowering plants"),
            ("Paleogene", 66, 23, "Mammal diversification"),
            ("Neogene", 23, 2.6, "Human ancestors"),
            ("Quaternary", 2.6, 0, "Ice ages, humans"),
        ]

        for name, start_mya, end_mya, key_event in periods:
            concept = self.create_concept(
                name=f"{name} Period",
                concept_type=ConceptType.DEFINITION,
                description=f"Geological period: {key_event}",
            )
            concept.metadata.update({
                "start_mya": start_mya,
                "end_mya": end_mya,
                "key_event": key_event,
            })

    def initialize_geological_pairs(self) -> None:
        """Initialize fundamental geological pairs with META 50/50 balance."""
        pairs = [
            ("Formation", "Erosion", "Building vs wearing"),
            ("Igneous", "Sedimentary", "Fire-formed vs deposited"),
            ("Continental", "Oceanic", "Land vs sea crust"),
            ("Tectonic", "Volcanic", "Plate vs eruption"),
            ("Mountain", "Valley", "Peak vs depression"),
            ("Uplift", "Subsidence", "Rising vs sinking"),
            ("Crystallization", "Weathering", "Forming vs breaking"),
            ("Intrusive", "Extrusive", "Underground vs surface"),
            ("Fault", "Fold", "Break vs bend"),
            ("Mineral", "Rock", "Pure vs aggregate"),
            ("Metamorphic", "Sedimentary", "Transformed vs layered"),
            ("Seismic", "Stable", "Shaking vs still"),
            ("Permeable", "Impermeable", "Porous vs solid"),
            ("Aquifer", "Aquitard", "Water-bearing vs blocking"),
            ("Stalactite", "Stalagmite", "Hanging vs rising"),
            ("Mantle", "Crust", "Deep vs surface"),
            ("Core", "Surface", "Center vs outer"),
            ("Magma", "Solid Rock", "Molten vs solid"),
            ("Fossil", "Living", "Ancient vs current"),
            ("Stratum", "Intrusion", "Layer vs injection"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Geology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Geology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_mohs_hardness_scale(self) -> dict[int, str]:
        """Get Mohs hardness scale for minerals."""
        return {
            1: "Talc",
            2: "Gypsum",
            3: "Calcite",
            4: "Fluorite",
            5: "Apatite",
            6: "Orthoclase",
            7: "Quartz",
            8: "Topaz",
            9: "Corundum",
            10: "Diamond",
        }

    def demonstrate_geological_balance(self) -> dict[str, Any]:
        """Demonstrate geological balance principles."""
        return {
            "concept": "Geological Equilibrium",
            "dualities": {
                "formation_erosion": {
                    "formation": 50.0,
                    "erosion": 50.0,
                    "meaning": "Mountains rise as fast as they erode over geological time",
                },
                "tectonic_balance": {
                    "crust_created": 50.0,
                    "crust_destroyed": 50.0,
                    "meaning": "Seafloor spreading equals subduction",
                },
                "rock_cycle": {
                    "creation": 50.0,
                    "destruction": 50.0,
                    "meaning": "Rocks continuously transform",
                },
            },
            "isostatic_equilibrium": {
                "uplift": 50.0,
                "subsidence": 50.0,
                "description": "Crust floats in gravitational balance",
            },
            "meta_meaning": "Geology demonstrates META 50/50 in Earth's dynamic balance",
        }


def create_geology_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> GeologyDomain:
    """
    Factory function to create a fully initialized geology domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized GeologyDomain
    """
    domain = GeologyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_rock_types()
        domain.initialize_plate_boundaries()
        domain.initialize_earth_layers()
        domain.initialize_geological_time()
        domain.initialize_geological_pairs()

    return domain
