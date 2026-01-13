"""
Physics Domain
==============
Physical science knowledge domain with META 50/50 equilibrium.
Fundamental duality: Energy/Matter (wave/particle, potential/kinetic).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    Concept,
    ConceptType,
    KnowledgeDomain,
)
from models.domain import DomainType


class PhysicsDomain(KnowledgeDomain):
    """
    Physics knowledge domain.

    Fundamental Duality: Energy / Matter
    - Energy: Capacity to do work, force, motion
    - Matter: Physical substance, mass, particles

    Secondary Dualities:
    - Wave / Particle (quantum duality)
    - Potential / Kinetic (energy forms)
    - Space / Time (spacetime)
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Physics",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of matter, energy, and their interactions",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Energy/Matter duality."""
        self._domain.set_duality(
            positive_name="energy",
            positive_value=50,
            negative_name="matter",
            negative_value=50,
            duality_name="physics_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental physical laws as axioms."""
        laws = [
            ("Conservation of Energy", "Energy cannot be created or destroyed, only transformed"),
            ("Conservation of Momentum", "Total momentum in an isolated system remains constant"),
            (
                "Conservation of Mass-Energy",
                "Total mass-energy in an isolated system is conserved (E=mc²)",
            ),
            (
                "Newton's First Law",
                "An object remains at rest or in uniform motion unless acted upon",
            ),
            ("Newton's Second Law", "Force equals mass times acceleration (F=ma)"),
            ("Newton's Third Law", "Every action has an equal and opposite reaction"),
            ("Thermodynamic First Law", "Energy is conserved in thermodynamic processes"),
            ("Thermodynamic Second Law", "Entropy of an isolated system never decreases"),
            (
                "Speed of Light Constancy",
                "The speed of light in vacuum is constant for all observers",
            ),
            ("Uncertainty Principle", "Position and momentum cannot both be precisely known"),
        ]

        for name, description in laws:
            self.create_concept(
                name=name, concept_type=ConceptType.LAW, description=description, certainty=100
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental physics concepts."""
        return [
            "Mass",
            "Energy",
            "Force",
            "Momentum",
            "Velocity",
            "Acceleration",
            "Space",
            "Time",
            "Charge",
            "Field",
            "Wave",
            "Particle",
            "Quantum",
            "Relativity",
            "Entropy",
        ]

    def initialize_branches(self) -> None:
        """Initialize major physics branches."""
        branches = [
            ("Classical Mechanics", "Study of motion of macroscopic objects", ConceptType.THEORY),
            ("Thermodynamics", "Study of heat, energy, and work", ConceptType.THEORY),
            ("Electromagnetism", "Study of electric and magnetic phenomena", ConceptType.THEORY),
            ("Quantum Mechanics", "Study of atomic and subatomic systems", ConceptType.THEORY),
            ("Relativity", "Study of space, time, and gravity", ConceptType.THEORY),
            ("Optics", "Study of light and its interactions", ConceptType.THEORY),
            ("Acoustics", "Study of sound waves", ConceptType.THEORY),
            ("Nuclear Physics", "Study of atomic nuclei", ConceptType.THEORY),
            ("Particle Physics", "Study of fundamental particles", ConceptType.THEORY),
            ("Astrophysics", "Physics of celestial objects", ConceptType.THEORY),
            ("Condensed Matter", "Study of solid and liquid phases", ConceptType.THEORY),
            ("Plasma Physics", "Study of ionized gases", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_fundamental_particles(self) -> None:
        """Initialize fundamental particles."""
        # Fermions (matter particles)
        quarks = [
            ("Up Quark", "u", 2 / 3, 2.2),
            ("Down Quark", "d", -1 / 3, 4.7),
            ("Charm Quark", "c", 2 / 3, 1270),
            ("Strange Quark", "s", -1 / 3, 96),
            ("Top Quark", "t", 2 / 3, 173000),
            ("Bottom Quark", "b", -1 / 3, 4180),
        ]

        leptons = [
            ("Electron", "e⁻", -1, 0.511),
            ("Muon", "μ⁻", -1, 105.7),
            ("Tau", "τ⁻", -1, 1777),
            ("Electron Neutrino", "νₑ", 0, 0),
            ("Muon Neutrino", "νμ", 0, 0),
            ("Tau Neutrino", "ντ", 0, 0),
        ]

        # Bosons (force carriers)
        bosons = [
            ("Photon", "γ", 0, 0, "Electromagnetic"),
            ("W Boson", "W±", 1, 80400, "Weak"),  # ±1 charge
            ("Z Boson", "Z⁰", 0, 91200, "Weak"),
            ("Gluon", "g", 0, 0, "Strong"),
            ("Higgs Boson", "H⁰", 0, 125000, "Mass"),
        ]

        for name, symbol, charge, mass in quarks:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=f"Fundamental quark with charge {charge}",
            )
            concept.metadata.update(
                {"symbol": symbol, "charge": charge, "mass_mev": mass, "category": "quark"}
            )

        for name, symbol, charge, mass in leptons:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=f"Fundamental lepton with charge {charge}",
            )
            concept.metadata.update(
                {"symbol": symbol, "charge": charge, "mass_mev": mass, "category": "lepton"}
            )

        for name, symbol, charge, mass, force in bosons:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=f"Gauge boson mediating {force} force",
            )
            concept.metadata.update(
                {
                    "symbol": symbol,
                    "charge": charge,
                    "mass_mev": mass,
                    "force": force,
                    "category": "boson",
                }
            )

    def initialize_fundamental_forces(self) -> None:
        """Initialize the four fundamental forces."""
        forces = [
            (
                "Gravitational Force",
                "Attractive force between masses",
                "Graviton (hypothetical)",
                1e-38,  # Relative strength
            ),
            (
                "Electromagnetic Force",
                "Force between charged particles",
                "Photon",
                1 / 137,  # Fine structure constant
            ),
            (
                "Strong Nuclear Force",
                "Force binding quarks in nucleons",
                "Gluon",
                1.0,  # Reference strength
            ),
            (
                "Weak Nuclear Force",
                "Force responsible for radioactive decay",
                "W and Z Bosons",
                1e-6,  # Relative strength
            ),
        ]

        for name, description, mediator, strength in forces:
            concept = self.create_concept(
                name=name, concept_type=ConceptType.PRINCIPLE, description=description
            )
            concept.metadata.update({"mediator": mediator, "relative_strength": strength})

    def add_equation(
        self, name: str, equation: str, description: str, variables: dict[str, str]
    ) -> Concept:
        """Add a physics equation."""
        concept = self.create_concept(
            name=name, concept_type=ConceptType.LAW, description=description
        )
        concept.metadata.update({"equation": equation, "variables": variables})
        return concept

    def initialize_key_equations(self) -> None:
        """Initialize key physics equations."""
        equations = [
            (
                "Mass-Energy Equivalence",
                "E = mc²",
                "Energy equals mass times speed of light squared",
                {"E": "Energy", "m": "Mass", "c": "Speed of light"},
            ),
            (
                "Newton's Second Law",
                "F = ma",
                "Force equals mass times acceleration",
                {"F": "Force", "m": "Mass", "a": "Acceleration"},
            ),
            (
                "Kinetic Energy",
                "KE = ½mv²",
                "Energy of motion",
                {"KE": "Kinetic energy", "m": "Mass", "v": "Velocity"},
            ),
            (
                "Gravitational Force",
                "F = Gm₁m₂/r²",
                "Newton's law of gravitation",
                {"F": "Force", "G": "Gravitational constant", "m": "Mass", "r": "Distance"},
            ),
            (
                "Coulomb's Law",
                "F = kq₁q₂/r²",
                "Electrostatic force between charges",
                {"F": "Force", "k": "Coulomb constant", "q": "Charge", "r": "Distance"},
            ),
            (
                "Schrödinger Equation",
                "iℏ∂ψ/∂t = Ĥψ",
                "Fundamental equation of quantum mechanics",
                {"ψ": "Wave function", "Ĥ": "Hamiltonian", "ℏ": "Reduced Planck constant"},
            ),
            (
                "Heisenberg Uncertainty",
                "ΔxΔp ≥ ℏ/2",
                "Fundamental limit on precision of measurements",
                {
                    "Δx": "Position uncertainty",
                    "Δp": "Momentum uncertainty",
                    "ℏ": "Reduced Planck constant",
                },
            ),
        ]

        for name, eq, desc, vars in equations:
            self.add_equation(name, eq, desc, vars)

    def get_physical_constants(self) -> dict[str, dict[str, Any]]:
        """Get fundamental physical constants."""
        return {
            "speed_of_light": {"value": 299792458, "unit": "m/s", "symbol": "c"},
            "planck_constant": {"value": 6.62607015e-34, "unit": "J·s", "symbol": "h"},
            "gravitational_constant": {"value": 6.67430e-11, "unit": "m³/(kg·s²)", "symbol": "G"},
            "elementary_charge": {"value": 1.602176634e-19, "unit": "C", "symbol": "e"},
            "electron_mass": {"value": 9.1093837015e-31, "unit": "kg", "symbol": "mₑ"},
            "proton_mass": {"value": 1.67262192369e-27, "unit": "kg", "symbol": "mₚ"},
            "boltzmann_constant": {"value": 1.380649e-23, "unit": "J/K", "symbol": "k"},
            "avogadro_number": {"value": 6.02214076e23, "unit": "mol⁻¹", "symbol": "Nₐ"},
        }

    def demonstrate_wave_particle_duality(self) -> dict[str, Any]:
        """
        Demonstrate wave-particle duality balance.
        Shows META 50/50 in quantum mechanics.
        """
        return {
            "concept": "Wave-Particle Duality",
            "wave_properties": {"interference": True, "diffraction": True, "wavelength": "λ = h/p"},
            "particle_properties": {
                "localization": True,
                "discrete_energy": True,
                "momentum": "p = h/λ",
            },
            "balance": {"wave_aspect": 50.0, "particle_aspect": 50.0, "total": 100.0},
            "meta_meaning": "Quantum systems exhibit balanced wave-particle nature",
        }


def create_physics_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> PhysicsDomain:
    """
    Factory function to create a fully initialized physics domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized PhysicsDomain
    """
    domain = PhysicsDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_fundamental_particles()
        domain.initialize_fundamental_forces()
        domain.initialize_key_equations()

    return domain
