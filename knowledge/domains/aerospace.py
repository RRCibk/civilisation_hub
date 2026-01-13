"""
Aerospace Domain
================
Aerospace knowledge domain with META 50/50 equilibrium.
Fundamental duality: Atmosphere/Space (aeronautics vs astronautics).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class AerospaceDomain(KnowledgeDomain):
    """
    Aerospace knowledge domain.

    Fundamental Duality: Atmosphere / Space
    - Atmosphere: Aeronautics, aircraft, atmospheric flight
    - Space: Astronautics, spacecraft, orbital and beyond

    Secondary Dualities:
    - Lift / Thrust
    - Fixed / Rotary
    - Manned / Unmanned
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Aerospace",
            domain_type=DomainType.FUNDAMENTAL,
            description="The science and engineering of flight in atmosphere and space",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Atmosphere/Space duality."""
        self._domain.set_duality(
            positive_name="atmosphere",
            positive_value=50,
            negative_name="space",
            negative_value=50,
            duality_name="aerospace_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental aerospace principles."""
        principles = [
            (
                "Bernoulli's Principle",
                "Faster flow creates lower pressure",
            ),
            (
                "Newton's Third Law",
                "Action and reaction for propulsion",
            ),
            (
                "Orbital Mechanics",
                "Gravity determines trajectories",
            ),
            (
                "Weight Minimization",
                "Every gram counts in flight",
            ),
            (
                "Aerodynamic Efficiency",
                "Minimize drag, maximize lift",
            ),
            (
                "Safety Critical",
                "Redundancy and reliability essential",
            ),
            (
                "Systems Integration",
                "Complex systems must work together",
            ),
            (
                "Testing and Certification",
                "Rigorous testing ensures safety",
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=95,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental aerospace concepts."""
        return [
            "Lift",
            "Drag",
            "Thrust",
            "Weight",
            "Airfoil",
            "Propulsion",
            "Orbit",
            "Trajectory",
            "Attitude",
            "Aerodynamics",
            "Spacecraft",
            "Satellite",
            "Launch",
            "Reentry",
            "Navigation",
        ]

    def initialize_branches(self) -> None:
        """Initialize major aerospace branches."""
        branches = [
            (
                "Aerodynamics",
                "Air flow and forces",
                ConceptType.THEORY,
            ),
            (
                "Propulsion",
                "Engines and thrust",
                ConceptType.THEORY,
            ),
            (
                "Structures",
                "Airframe design",
                ConceptType.THEORY,
            ),
            (
                "Avionics",
                "Flight electronics",
                ConceptType.THEORY,
            ),
            (
                "Flight Mechanics",
                "Vehicle dynamics",
                ConceptType.THEORY,
            ),
            (
                "Orbital Mechanics",
                "Space trajectories",
                ConceptType.THEORY,
            ),
            (
                "Spacecraft Design",
                "Space vehicle engineering",
                ConceptType.THEORY,
            ),
            (
                "Rocket Science",
                "Rocket propulsion",
                ConceptType.THEORY,
            ),
            (
                "Guidance and Control",
                "Navigation systems",
                ConceptType.THEORY,
            ),
            (
                "Space Systems",
                "Satellites and probes",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_vehicle_types(self) -> None:
        """Initialize aerospace vehicle types."""
        vehicles = [
            ("Fixed-Wing", "Conventional aircraft", "Lift from wings"),
            ("Rotorcraft", "Helicopters", "Rotating lift"),
            ("Rocket", "Launch vehicles", "Reaction propulsion"),
            ("Satellite", "Orbital spacecraft", "Earth orbit"),
            ("Space Probe", "Deep space craft", "Exploration"),
            ("Spaceplane", "Hybrid vehicle", "Runway to orbit"),
        ]

        for name, description, characteristic in vehicles:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["characteristic"] = characteristic

    def initialize_propulsion_types(self) -> None:
        """Initialize propulsion systems."""
        propulsion = [
            ("Piston Engine", "Internal combustion", "Light aircraft"),
            ("Turbofan", "Gas turbine", "Airliners"),
            ("Turbojet", "Jet propulsion", "Fast aircraft"),
            ("Solid Rocket", "Solid fuel", "Boosters"),
            ("Liquid Rocket", "Liquid fuel", "Main stages"),
            ("Ion Engine", "Electric propulsion", "Deep space"),
        ]

        for name, description, application in propulsion:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["application"] = application

    def initialize_aerospace_pairs(self) -> None:
        """Initialize fundamental aerospace pairs with META 50/50 balance."""
        pairs = [
            ("Atmosphere", "Space", "Air vs vacuum"),
            ("Lift", "Thrust", "Aerodynamic vs propulsive"),
            ("Fixed", "Rotary", "Wings vs rotors"),
            ("Manned", "Unmanned", "Crewed vs autonomous"),
            ("Subsonic", "Supersonic", "Below vs above sound speed"),
            ("Civil", "Military", "Commercial vs defense"),
            ("Expendable", "Reusable", "Single-use vs multiple"),
            ("Orbit", "Suborbital", "Complete vs partial path"),
            ("Ascent", "Descent", "Launch vs reentry"),
            ("Aerodynamic", "Ballistic", "Lift vs gravity"),
            ("Stable", "Maneuverable", "Steady vs agile"),
            ("Light", "Heavy", "Small vs large aircraft"),
            ("Low", "High", "Near vs far altitude"),
            ("Short", "Long", "Short range vs long range"),
            ("Single", "Multi", "One vs multiple engines"),
            ("Pressurized", "Unpressurized", "Pressurized vs unpressurized cabin"),
            ("Ground", "Flight", "Ground testing vs flight testing"),
            ("Design", "Operation", "Building vs flying"),
            ("Theory", "Test", "Calculation vs measurement"),
            ("Safety", "Performance", "Reliability vs capability"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Aerospace)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Aerospace)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_four_forces(self) -> dict[str, str]:
        """Get four forces of flight."""
        return {
            "lift": "Upward force from airfoil",
            "weight": "Downward gravitational force",
            "thrust": "Forward propulsive force",
            "drag": "Backward resistance force",
        }

    def demonstrate_aerospace_balance(self) -> dict[str, Any]:
        """Demonstrate aerospace balance principles."""
        return {
            "concept": "Aerospace Equilibrium",
            "dualities": {
                "atmosphere_space": {
                    "atmosphere": 50.0,
                    "space": 50.0,
                    "meaning": "Both atmospheric and space flight equally important",
                },
                "lift_thrust": {
                    "lift": 50.0,
                    "thrust": 50.0,
                    "meaning": "Aerodynamic and propulsive forces complement",
                },
                "safety_performance": {
                    "safety": 50.0,
                    "performance": 50.0,
                    "meaning": "Reliability and capability must balance",
                },
            },
            "flight_balance": {
                "lift": 50.0,
                "weight": 50.0,
                "description": "Steady flight requires force balance",
            },
            "meta_meaning": "Aerospace demonstrates META 50/50 in atmosphere-space synthesis",
        }


def create_aerospace_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> AerospaceDomain:
    """
    Factory function to create a fully initialized aerospace domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized AerospaceDomain
    """
    domain = AerospaceDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_vehicle_types()
        domain.initialize_propulsion_types()
        domain.initialize_aerospace_pairs()

    return domain
