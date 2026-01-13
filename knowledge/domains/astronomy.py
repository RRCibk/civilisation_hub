"""
Astronomy Domain
================
Astronomical knowledge domain with META 50/50 equilibrium.
Fundamental duality: Light/Dark (visible radiation vs cosmic void).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class AstronomyDomain(KnowledgeDomain):
    """
    Astronomy knowledge domain.

    Fundamental Duality: Light / Dark
    - Light: Electromagnetic radiation, visible matter, stellar emission
    - Dark: Cosmic void, dark matter, dark energy, absence of radiation

    Secondary Dualities:
    - Matter / Antimatter
    - Expansion / Contraction
    - Star / Void
    - Gravity / Antigravity
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Astronomy",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of celestial objects, space, and the physical universe",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Light/Dark duality."""
        self._domain.set_duality(
            positive_name="light",
            positive_value=50,
            negative_name="dark",
            negative_value=50,
            duality_name="astronomy_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental astronomical principles."""
        principles = [
            (
                "Cosmological Principle",
                "The universe is homogeneous and isotropic on large scales",
            ),
            (
                "Hubble's Law",
                "Galaxies recede at velocities proportional to their distance",
            ),
            (
                "Copernican Principle",
                "Earth does not occupy a special position in the universe",
            ),
            (
                "Stellar Nucleosynthesis",
                "Elements are forged in the cores of stars",
            ),
            (
                "Conservation of Angular Momentum",
                "Rotating systems maintain angular momentum",
            ),
            (
                "Gravitational Binding",
                "Massive objects are bound by gravitational attraction",
            ),
            (
                "Cosmic Microwave Background",
                "Remnant radiation from the early universe pervades all space",
            ),
            (
                "Dark Matter Hypothesis",
                "Unseen matter accounts for gravitational effects",
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
        """Get fundamental astronomy concepts."""
        return [
            "Star",
            "Galaxy",
            "Planet",
            "Moon",
            "Asteroid",
            "Comet",
            "Black Hole",
            "Nebula",
            "Supernova",
            "Quasar",
            "Pulsar",
            "Dark Matter",
            "Dark Energy",
            "Cosmos",
            "Universe",
        ]

    def initialize_branches(self) -> None:
        """Initialize major astronomy branches."""
        branches = [
            (
                "Astrophysics",
                "Physics of celestial objects and phenomena",
                ConceptType.THEORY,
            ),
            (
                "Cosmology",
                "Study of the origin and evolution of the universe",
                ConceptType.THEORY,
            ),
            (
                "Planetary Science",
                "Study of planets and planetary systems",
                ConceptType.THEORY,
            ),
            (
                "Stellar Astronomy",
                "Study of stars, their formation and evolution",
                ConceptType.THEORY,
            ),
            (
                "Galactic Astronomy",
                "Study of the Milky Way and its components",
                ConceptType.THEORY,
            ),
            (
                "Extragalactic Astronomy",
                "Study of objects beyond the Milky Way",
                ConceptType.THEORY,
            ),
            (
                "Astrometry",
                "Measurement of positions and motions of celestial objects",
                ConceptType.THEORY,
            ),
            (
                "Radio Astronomy",
                "Study of celestial objects using radio waves",
                ConceptType.THEORY,
            ),
            (
                "X-ray Astronomy",
                "Study of X-ray emissions from celestial objects",
                ConceptType.THEORY,
            ),
            (
                "Astrobiology",
                "Study of life in the universe",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_celestial_objects(self) -> None:
        """Initialize types of celestial objects."""
        objects = [
            ("Star", "Luminous sphere of plasma held by gravity", "Sun"),
            ("Planet", "Celestial body orbiting a star", "Earth"),
            ("Moon", "Natural satellite orbiting a planet", "Luna"),
            ("Asteroid", "Rocky minor planet", "Ceres"),
            ("Comet", "Icy body with tail when near Sun", "Halley"),
            ("Meteoroid", "Small rocky debris in space", "Various"),
            ("Black Hole", "Region of spacetime with extreme gravity", "Sagittarius A*"),
            ("Neutron Star", "Collapsed stellar core of extreme density", "PSR B1919+21"),
            ("White Dwarf", "Remnant of low-mass star", "Sirius B"),
            ("Nebula", "Cloud of gas and dust in space", "Orion Nebula"),
            ("Galaxy", "System of stars, gas, dust bound by gravity", "Milky Way"),
            ("Quasar", "Extremely luminous active galactic nucleus", "3C 273"),
            ("Pulsar", "Rotating neutron star emitting radiation", "Crab Pulsar"),
            ("Supernova", "Explosive death of a massive star", "SN 1987A"),
        ]

        for name, description, example in objects:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["example"] = example

    def initialize_stellar_evolution(self) -> None:
        """Initialize stellar evolution stages."""
        stages = [
            ("Protostar", "Initial stage of star formation from gas cloud", 1),
            ("Main Sequence", "Stable hydrogen-burning phase", 2),
            ("Red Giant", "Expanded star burning helium", 3),
            ("Planetary Nebula", "Outer layers expelled by dying star", 4),
            ("White Dwarf", "Final state of low-mass stars", 5),
            ("Supergiant", "Massive star in late evolutionary stage", 3),
            ("Supernova", "Explosive death of massive star", 4),
            ("Neutron Star", "Ultra-dense remnant of supernova", 5),
            ("Black Hole", "Gravitational collapse of massive star", 5),
        ]

        for name, description, stage_order in stages:
            concept = self.create_concept(
                name=f"Stellar {name}",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["evolution_stage"] = stage_order

    def initialize_cosmic_scales(self) -> None:
        """Initialize cosmic distance scales."""
        scales = [
            ("Astronomical Unit", "Earth-Sun distance", 1.496e11, "m"),
            ("Light Year", "Distance light travels in one year", 9.461e15, "m"),
            ("Parsec", "Distance at which 1 AU subtends 1 arcsecond", 3.086e16, "m"),
            ("Kiloparsec", "One thousand parsecs", 3.086e19, "m"),
            ("Megaparsec", "One million parsecs", 3.086e22, "m"),
        ]

        for name, description, value, unit in scales:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({"value": value, "unit": unit})

    def initialize_cosmic_pairs(self) -> None:
        """Initialize fundamental cosmic pairs with META 50/50 balance."""
        pairs = [
            ("Light", "Dark", "Visible vs invisible"),
            ("Matter", "Antimatter", "Positive vs negative existence"),
            ("Star", "Void", "Radiant vs empty"),
            ("Expansion", "Contraction", "Universe growing vs shrinking"),
            ("Gravity", "Dark Energy", "Attraction vs repulsion"),
            ("Visible Matter", "Dark Matter", "Detectable vs hidden mass"),
            ("Solar", "Interstellar", "Star system vs between stars"),
            ("Planet", "Moon", "Primary vs satellite body"),
            ("Stellar", "Planetary", "Star vs planet scale"),
            ("Nebula", "Black Hole", "Birth cloud vs death singularity"),
            ("Red Shift", "Blue Shift", "Receding vs approaching"),
            ("Perihelion", "Aphelion", "Nearest vs farthest"),
            ("Zenith", "Nadir", "Highest vs lowest point"),
            ("Waxing", "Waning", "Growing vs shrinking phase"),
            ("Corona", "Core", "Outer vs inner sun"),
            ("Terrestrial", "Jovian", "Rocky vs gaseous"),
            ("Asteroid", "Comet", "Rocky vs icy body"),
            ("Quasar", "Pulsar", "Active galaxy vs spinning star"),
            ("Supernova", "White Dwarf", "Explosive vs quiet death"),
            ("Cosmic", "Local", "Universal vs nearby scale"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Astronomy)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Astronomy)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_astronomical_constants(self) -> dict[str, dict[str, Any]]:
        """Get important astronomical constants."""
        return {
            "speed_of_light": {
                "value": 299792458,
                "unit": "m/s",
                "symbol": "c",
            },
            "gravitational_constant": {
                "value": 6.674e-11,
                "unit": "m^3/(kg·s^2)",
                "symbol": "G",
            },
            "solar_mass": {
                "value": 1.989e30,
                "unit": "kg",
                "symbol": "M☉",
            },
            "solar_radius": {
                "value": 6.957e8,
                "unit": "m",
                "symbol": "R☉",
            },
            "hubble_constant": {
                "value": 70,
                "unit": "km/s/Mpc",
                "symbol": "H0",
            },
            "age_of_universe": {
                "value": 13.8e9,
                "unit": "years",
                "symbol": "t0",
            },
        }

    def demonstrate_cosmic_balance(self) -> dict[str, Any]:
        """Demonstrate cosmic balance principles."""
        return {
            "concept": "Cosmic Equilibrium",
            "dualities": {
                "light_dark": {
                    "visible_matter": 5.0,
                    "dark_matter": 27.0,
                    "dark_energy": 68.0,
                    "meaning": "Universe is 95% dark (matter + energy)",
                },
                "expansion_gravity": {
                    "expansion_force": 50.0,
                    "gravitational_attraction": 50.0,
                    "meaning": "Cosmic expansion balanced against gravity",
                },
                "matter_antimatter": {
                    "matter": 50.0,
                    "antimatter": 50.0,
                    "meaning": "Created equally, asymmetry unexplained",
                },
            },
            "stellar_balance": {
                "radiation_pressure": 50.0,
                "gravitational_collapse": 50.0,
                "description": "Stars maintain hydrostatic equilibrium",
            },
            "meta_meaning": "The cosmos demonstrates META 50/50 in fundamental forces",
        }


def create_astronomy_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> AstronomyDomain:
    """
    Factory function to create a fully initialized astronomy domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized AstronomyDomain
    """
    domain = AstronomyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_celestial_objects()
        domain.initialize_stellar_evolution()
        domain.initialize_cosmic_scales()
        domain.initialize_cosmic_pairs()

    return domain
