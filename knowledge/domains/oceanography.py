"""
Oceanography Domain
===================
Oceanographic knowledge domain with META 50/50 equilibrium.
Fundamental duality: Surface/Deep (ocean layers and processes).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class OceanographyDomain(KnowledgeDomain):
    """
    Oceanography knowledge domain.

    Fundamental Duality: Surface / Deep
    - Surface: Photic zone, waves, currents, warm waters
    - Deep: Aphotic zone, pressure, cold, abyssal plains

    Secondary Dualities:
    - Coastal / Pelagic
    - Warm / Cold
    - Saline / Fresh
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Oceanography",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of oceans, their processes, and marine life",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Surface/Deep duality."""
        self._domain.set_duality(
            positive_name="surface",
            positive_value=50,
            negative_name="deep",
            negative_value=50,
            duality_name="oceanography_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental oceanographic principles."""
        principles = [
            (
                "Thermohaline Circulation",
                "Ocean circulation driven by temperature and salinity differences",
            ),
            (
                "Ekman Transport",
                "Wind-driven water movement deflected by Coriolis effect",
            ),
            (
                "Conservation of Salt",
                "Total ocean salt content remains relatively constant",
            ),
            (
                "Hydrostatic Pressure",
                "Pressure increases linearly with depth",
            ),
            (
                "Wave Energy Transfer",
                "Waves transfer energy, not water mass",
            ),
            (
                "Tidal Periodicity",
                "Tides follow predictable cycles based on lunar and solar positions",
            ),
            (
                "Upwelling Nutrient Transport",
                "Deep nutrients rise to surface in upwelling zones",
            ),
            (
                "Marine Stratification",
                "Oceans are stratified by temperature and density",
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
        """Get fundamental oceanography concepts."""
        return [
            "Ocean",
            "Current",
            "Wave",
            "Tide",
            "Salinity",
            "Thermocline",
            "Upwelling",
            "Reef",
            "Trench",
            "Continental Shelf",
            "Abyssal Plain",
            "Plankton",
            "Nekton",
            "Benthos",
            "Marine Ecosystem",
        ]

    def initialize_branches(self) -> None:
        """Initialize major oceanography branches."""
        branches = [
            (
                "Physical Oceanography",
                "Study of ocean physics and dynamics",
                ConceptType.THEORY,
            ),
            (
                "Chemical Oceanography",
                "Study of ocean chemistry and composition",
                ConceptType.THEORY,
            ),
            (
                "Biological Oceanography",
                "Study of marine life and ecosystems",
                ConceptType.THEORY,
            ),
            (
                "Geological Oceanography",
                "Study of ocean floor and coastal geology",
                ConceptType.THEORY,
            ),
            (
                "Marine Geophysics",
                "Study of physical properties of ocean floor",
                ConceptType.THEORY,
            ),
            (
                "Paleoceanography",
                "Study of ancient ocean conditions",
                ConceptType.THEORY,
            ),
            (
                "Coastal Oceanography",
                "Study of coastal waters and processes",
                ConceptType.THEORY,
            ),
            (
                "Fisheries Science",
                "Study of fish populations and harvesting",
                ConceptType.THEORY,
            ),
            (
                "Marine Acoustics",
                "Study of sound in the ocean",
                ConceptType.THEORY,
            ),
            (
                "Polar Oceanography",
                "Study of Arctic and Antarctic oceans",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_ocean_zones(self) -> None:
        """Initialize ocean depth zones."""
        zones = [
            ("Epipelagic", "Sunlit zone, 0-200m", 200, True),
            ("Mesopelagic", "Twilight zone, 200-1000m", 1000, False),
            ("Bathypelagic", "Midnight zone, 1000-4000m", 4000, False),
            ("Abyssopelagic", "Abyssal zone, 4000-6000m", 6000, False),
            ("Hadopelagic", "Hadal zone, >6000m", 11000, False),
        ]

        for name, description, max_depth, has_light in zones:
            concept = self.create_concept(
                name=f"{name} Zone",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "max_depth_m": max_depth,
                "has_light": has_light,
            })

    def initialize_ocean_features(self) -> None:
        """Initialize major ocean features."""
        features = [
            ("Continental Shelf", "Shallow underwater extension of continent", 200),
            ("Continental Slope", "Steep descent from shelf to deep ocean", 3000),
            ("Continental Rise", "Gradual transition to abyssal plain", 4000),
            ("Abyssal Plain", "Flat deep ocean floor", 5000),
            ("Mid-Ocean Ridge", "Underwater mountain range", 2500),
            ("Ocean Trench", "Deep depression in ocean floor", 11000),
            ("Seamount", "Underwater volcanic mountain", 3000),
            ("Guyot", "Flat-topped seamount", 2000),
            ("Hydrothermal Vent", "Hot water emission from seafloor", 3000),
            ("Cold Seep", "Methane and sulfide release site", 2000),
        ]

        for name, description, typical_depth in features:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["typical_depth_m"] = typical_depth

    def initialize_ocean_currents(self) -> None:
        """Initialize major ocean currents."""
        currents = [
            ("Gulf Stream", "Warm Atlantic current from Gulf of Mexico", "Warm", "North Atlantic"),
            ("Kuroshio", "Warm Pacific current near Japan", "Warm", "North Pacific"),
            ("Humboldt", "Cold current along South America", "Cold", "South Pacific"),
            ("Benguela", "Cold current along Africa", "Cold", "South Atlantic"),
            ("North Atlantic Deep Water", "Deep cold current", "Cold", "Atlantic"),
            ("Antarctic Circumpolar", "Largest current, encircles Antarctica", "Cold", "Southern Ocean"),
            ("California Current", "Cold eastern Pacific current", "Cold", "North Pacific"),
            ("Agulhas", "Warm current off South Africa", "Warm", "Indian Ocean"),
        ]

        for name, description, temperature, location in currents:
            concept = self.create_concept(
                name=f"{name} Current",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "temperature_type": temperature,
                "location": location,
            })

    def initialize_marine_life_zones(self) -> None:
        """Initialize marine life habitat zones."""
        life_zones = [
            ("Plankton", "Drifting organisms", ["Phytoplankton", "Zooplankton"]),
            ("Nekton", "Active swimmers", ["Fish", "Whales", "Squid"]),
            ("Benthos", "Bottom dwellers", ["Crabs", "Starfish", "Worms"]),
            ("Intertidal", "Between tides", ["Barnacles", "Mussels", "Seaweed"]),
            ("Coral Reef", "Tropical reef communities", ["Coral", "Clownfish", "Sea Anemone"]),
            ("Deep Sea", "Abyssal life forms", ["Anglerfish", "Giant Squid", "Tube Worms"]),
        ]

        for name, description, examples in life_zones:
            concept = self.create_concept(
                name=f"{name} Zone",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_oceanographic_pairs(self) -> None:
        """Initialize fundamental oceanographic pairs with META 50/50 balance."""
        pairs = [
            ("Surface", "Deep", "Top vs bottom"),
            ("Coastal", "Pelagic", "Shore vs open ocean"),
            ("Warm", "Cold", "Tropical vs polar water"),
            ("Saline", "Fresh", "Salty vs pure"),
            ("Current", "Still", "Flowing vs static"),
            ("Tidal", "Constant", "Rhythmic vs steady"),
            ("Photic", "Aphotic", "Light vs dark zone"),
            ("Upwelling", "Downwelling", "Rising vs sinking"),
            ("Plankton", "Nekton", "Drifting vs swimming"),
            ("Benthic", "Pelagic", "Bottom vs water column"),
            ("Reef", "Abyss", "Shallow life vs deep void"),
            ("Estuary", "Ocean", "Mixed vs pure salt"),
            ("Wave", "Calm", "Turbulent vs still"),
            ("Erosion", "Deposition", "Wearing vs building"),
            ("Thermocline", "Mixed", "Layered vs uniform temp"),
            ("Nutrient Rich", "Nutrient Poor", "Fertile vs barren"),
            ("Coral", "Sand", "Living vs inert bottom"),
            ("Marine", "Freshwater", "Salt vs fresh habitat"),
            ("Tsunami", "Ripple", "Massive vs small wave"),
            ("Trench", "Ridge", "Depression vs elevation"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Oceanography)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Oceanography)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_ocean_facts(self) -> dict[str, Any]:
        """Get key ocean facts and statistics."""
        return {
            "coverage": {
                "percent_earth": 71,
                "total_area_km2": 361000000,
            },
            "volume": {
                "total_km3": 1335000000,
                "percent_water": 97,
            },
            "depth": {
                "average_m": 3688,
                "maximum_m": 10994,
                "location": "Mariana Trench",
            },
            "salinity": {
                "average_ppt": 35,
                "range": "33-37 ppt",
            },
            "temperature": {
                "surface_avg_c": 17,
                "deep_avg_c": 4,
            },
        }

    def demonstrate_ocean_balance(self) -> dict[str, Any]:
        """Demonstrate oceanic balance principles."""
        return {
            "concept": "Ocean Equilibrium",
            "dualities": {
                "surface_deep": {
                    "surface_layer": 50.0,
                    "deep_layer": 50.0,
                    "meaning": "Energy exchange between surface and deep",
                },
                "upwelling_downwelling": {
                    "upwelling": 50.0,
                    "downwelling": 50.0,
                    "meaning": "Water rising equals water sinking",
                },
                "evaporation_precipitation": {
                    "evaporation": 50.0,
                    "precipitation": 50.0,
                    "meaning": "Ocean water cycle in balance",
                },
            },
            "thermohaline_balance": {
                "heat_transport_poleward": 50.0,
                "cold_return_equatorward": 50.0,
                "description": "Global conveyor belt circulation",
            },
            "meta_meaning": "Oceanography demonstrates META 50/50 in ocean dynamics",
        }


def create_oceanography_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> OceanographyDomain:
    """
    Factory function to create a fully initialized oceanography domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized OceanographyDomain
    """
    domain = OceanographyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_ocean_zones()
        domain.initialize_ocean_features()
        domain.initialize_ocean_currents()
        domain.initialize_marine_life_zones()
        domain.initialize_oceanographic_pairs()

    return domain
