"""
Astrophysics Domain
===================
Astrophysics knowledge domain with META 50/50 equilibrium.
Fundamental duality: Observation/Theory (empirical vs mathematical).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class AstrophysicsDomain(KnowledgeDomain):
    """
    Astrophysics knowledge domain.

    Fundamental Duality: Observation / Theory
    - Observation: Empirical data, measurements, detection
    - Theory: Mathematical models, physical laws, prediction

    Secondary Dualities:
    - Matter / Energy
    - Local / Cosmological
    - Classical / Relativistic
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Astrophysics",
            domain_type=DomainType.FUNDAMENTAL,
            description="The physics of celestial objects and the universe",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Observation/Theory duality."""
        self._domain.set_duality(
            positive_name="observation",
            positive_value=50,
            negative_name="theory",
            negative_value=50,
            duality_name="astrophysics_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental astrophysics principles."""
        principles = [
            (
                "Universality of Physics",
                "Same laws everywhere in universe",
            ),
            (
                "Gravity Dominates",
                "Gravity shapes cosmic structure",
            ),
            (
                "Light is Messenger",
                "Electromagnetic radiation carries information",
            ),
            (
                "Cosmic Evolution",
                "Universe and its contents evolve",
            ),
            (
                "Scale Hierarchy",
                "Structures exist at many scales",
            ),
            (
                "Conservation Laws",
                "Energy, momentum, charge conserved",
            ),
            (
                "Finite Speed of Light",
                "Looking far is looking back",
            ),
            (
                "Dark Sector",
                "Most matter and energy is dark",
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
        """Get fundamental astrophysics concepts."""
        return [
            "Star",
            "Galaxy",
            "Black Hole",
            "Gravity",
            "Radiation",
            "Spectrum",
            "Redshift",
            "Luminosity",
            "Mass",
            "Energy",
            "Spacetime",
            "Dark Matter",
            "Dark Energy",
            "Cosmology",
            "Nucleosynthesis",
        ]

    def initialize_branches(self) -> None:
        """Initialize major astrophysics branches."""
        branches = [
            (
                "Stellar Astrophysics",
                "Physics of stars",
                ConceptType.THEORY,
            ),
            (
                "Galactic Astrophysics",
                "Galaxy structure and dynamics",
                ConceptType.THEORY,
            ),
            (
                "Cosmology",
                "Universe origin and evolution",
                ConceptType.THEORY,
            ),
            (
                "High Energy Astrophysics",
                "Extreme phenomena",
                ConceptType.THEORY,
            ),
            (
                "Planetary Astrophysics",
                "Planetary systems",
                ConceptType.THEORY,
            ),
            (
                "Gravitational Physics",
                "Gravity and spacetime",
                ConceptType.THEORY,
            ),
            (
                "Nuclear Astrophysics",
                "Nuclear reactions in stars",
                ConceptType.THEORY,
            ),
            (
                "Plasma Astrophysics",
                "Cosmic plasmas",
                ConceptType.THEORY,
            ),
            (
                "Computational Astrophysics",
                "Numerical simulations",
                ConceptType.THEORY,
            ),
            (
                "Astroparticle Physics",
                "Particles from space",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_objects(self) -> None:
        """Initialize astrophysical objects."""
        objects = [
            ("Main Sequence Star", "Hydrogen-burning star", "Stellar"),
            ("White Dwarf", "Degenerate star", "Compact"),
            ("Neutron Star", "Collapsed core", "Compact"),
            ("Black Hole", "Spacetime singularity", "Compact"),
            ("Supernova", "Stellar explosion", "Transient"),
            ("Galaxy Cluster", "Gravitationally bound galaxies", "Large-scale"),
        ]

        for name, description, category in objects:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_phenomena(self) -> None:
        """Initialize astrophysical phenomena."""
        phenomena = [
            ("Gravitational Lensing", "Light bent by gravity", "Relativistic"),
            ("Cosmic Microwave Background", "Relic radiation", "Cosmological"),
            ("Gravitational Waves", "Spacetime ripples", "Relativistic"),
            ("Gamma Ray Bursts", "Extreme explosions", "High energy"),
            ("Quasars", "Active galactic nuclei", "Extragalactic"),
            ("Cosmic Expansion", "Universe stretching", "Cosmological"),
        ]

        for name, description, category in phenomena:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_astrophysics_pairs(self) -> None:
        """Initialize fundamental astrophysics pairs with META 50/50 balance."""
        pairs = [
            ("Observation", "Theory", "Empirical vs mathematical"),
            ("Matter", "Energy", "Mass vs radiation"),
            ("Local", "Cosmological", "Nearby vs universal"),
            ("Classical", "Relativistic", "Newtonian vs Einstein"),
            ("Visible", "Dark", "Observable vs hidden"),
            ("Luminous", "Non-luminous", "Emitting vs absorbing"),
            ("Bound", "Unbound", "Gravitationally trapped vs free"),
            ("Thermal", "Non-thermal", "Equilibrium vs accelerated"),
            ("Steady", "Transient", "Persistent vs temporary"),
            ("Point", "Extended", "Compact vs spread"),
            ("Active", "Passive", "Energetic vs quiet"),
            ("Normal", "Exotic", "Common vs rare"),
            ("Early", "Late", "Young vs old universe"),
            ("Baryonic", "Non-baryonic", "Normal vs dark matter"),
            ("Gravitational", "Electromagnetic", "Gravity vs light"),
            ("Ground", "Space", "Earth-based vs orbital"),
            ("Single", "Binary", "Isolated vs paired"),
            ("Stellar", "Interstellar", "Star vs between stars"),
            ("Nuclear", "Gravitational", "Fusion vs collapse"),
            ("Expanding", "Collapsing", "Growing vs shrinking"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Astro)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Astro)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_cosmic_distance_ladder(self) -> dict[str, str]:
        """Get cosmic distance measurement methods."""
        return {
            "parallax": "Geometric triangulation (nearby stars)",
            "cepheids": "Standard candles (galaxies)",
            "supernovae": "Type Ia brightness (distant)",
            "redshift": "Hubble law (cosmological)",
        }

    def demonstrate_astrophysics_balance(self) -> dict[str, Any]:
        """Demonstrate astrophysics balance principles."""
        return {
            "concept": "Astrophysics Equilibrium",
            "dualities": {
                "observation_theory": {
                    "observation": 50.0,
                    "theory": 50.0,
                    "meaning": "Data and models equally important",
                },
                "matter_energy": {
                    "matter": 50.0,
                    "energy": 50.0,
                    "meaning": "Mass and radiation interconvert",
                },
                "visible_dark": {
                    "visible": 50.0,
                    "dark": 50.0,
                    "meaning": "Observable and hidden sectors",
                },
            },
            "cosmic_balance": {
                "expansion": 50.0,
                "gravity": 50.0,
                "description": "Universe balances expansion and attraction",
            },
            "meta_meaning": "Astrophysics demonstrates META 50/50 in observation-theory synthesis",
        }


def create_astrophysics_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> AstrophysicsDomain:
    """
    Factory function to create a fully initialized astrophysics domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized AstrophysicsDomain
    """
    domain = AstrophysicsDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_objects()
        domain.initialize_phenomena()
        domain.initialize_astrophysics_pairs()

    return domain
