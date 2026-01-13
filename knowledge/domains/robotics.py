"""
Robotics Domain
===============
Robotics knowledge domain with META 50/50 equilibrium.
Fundamental duality: Autonomy/Control (independence vs direction).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class RoboticsDomain(KnowledgeDomain):
    """
    Robotics knowledge domain.

    Fundamental Duality: Autonomy / Control
    - Autonomy: Independent operation, self-direction
    - Control: Human direction, programmed behavior

    Secondary Dualities:
    - Hardware / Software
    - Perception / Action
    - Planning / Execution
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Robotics",
            domain_type=DomainType.FUNDAMENTAL,
            description="The design, construction, and operation of robots",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Autonomy/Control duality."""
        self._domain.set_duality(
            positive_name="autonomy",
            positive_value=50,
            negative_name="control",
            negative_value=50,
            duality_name="robotics_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental robotics principles."""
        principles = [
            (
                "Sense-Think-Act",
                "Robots perceive, process, and respond",
            ),
            (
                "Embodiment",
                "Physical form affects intelligence",
            ),
            (
                "Feedback Control",
                "Control systems use feedback loops",
            ),
            (
                "Task Decomposition",
                "Complex tasks broken into simpler ones",
            ),
            (
                "Safety Critical",
                "Robot safety is paramount",
            ),
            (
                "Human-Robot Interaction",
                "Robots must work with humans",
            ),
            (
                "Real-Time Operation",
                "Many tasks require real-time response",
            ),
            (
                "Robustness",
                "Robots must handle uncertainty",
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
        """Get fundamental robotics concepts."""
        return [
            "Robot",
            "Actuator",
            "Sensor",
            "Controller",
            "Manipulator",
            "Kinematics",
            "Dynamics",
            "Navigation",
            "Localization",
            "Path Planning",
            "Gripper",
            "End Effector",
            "Degrees of Freedom",
            "Workspace",
            "Trajectory",
        ]

    def initialize_branches(self) -> None:
        """Initialize major robotics branches."""
        branches = [
            (
                "Industrial Robotics",
                "Manufacturing robots",
                ConceptType.THEORY,
            ),
            (
                "Mobile Robotics",
                "Autonomous vehicles",
                ConceptType.THEORY,
            ),
            (
                "Humanoid Robotics",
                "Human-like robots",
                ConceptType.THEORY,
            ),
            (
                "Medical Robotics",
                "Healthcare robots",
                ConceptType.THEORY,
            ),
            (
                "Service Robotics",
                "Service and assistive robots",
                ConceptType.THEORY,
            ),
            (
                "Swarm Robotics",
                "Multi-robot systems",
                ConceptType.THEORY,
            ),
            (
                "Soft Robotics",
                "Compliant materials robots",
                ConceptType.THEORY,
            ),
            (
                "Aerial Robotics",
                "Drones and UAVs",
                ConceptType.THEORY,
            ),
            (
                "Underwater Robotics",
                "Marine robots",
                ConceptType.THEORY,
            ),
            (
                "Space Robotics",
                "Planetary and orbital robots",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_components(self) -> None:
        """Initialize robot components."""
        components = [
            ("Actuators", "Create motion", "Motors, hydraulics"),
            ("Sensors", "Gather information", "Cameras, encoders"),
            ("Controllers", "Process information", "Computers, PLCs"),
            ("End Effectors", "Interact with world", "Grippers, tools"),
            ("Power Systems", "Provide energy", "Batteries, pneumatics"),
            ("Structure", "Physical form", "Links, joints"),
        ]

        for name, function, examples in components:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=function,
            )
            concept.metadata["examples"] = examples

    def initialize_algorithms(self) -> None:
        """Initialize robotics algorithms."""
        algorithms = [
            ("SLAM", "Simultaneous localization and mapping", "Navigation"),
            ("Path Planning", "Finding routes", "Motion"),
            ("Inverse Kinematics", "Joint angle calculation", "Control"),
            ("PID Control", "Feedback control", "Control"),
            ("Motion Planning", "Trajectory generation", "Planning"),
            ("Obstacle Avoidance", "Collision prevention", "Safety"),
        ]

        for name, description, category in algorithms:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_robotics_pairs(self) -> None:
        """Initialize fundamental robotics pairs with META 50/50 balance."""
        pairs = [
            ("Autonomy", "Control", "Independence vs direction"),
            ("Hardware", "Software", "Physical vs logical"),
            ("Perception", "Action", "Sensing vs moving"),
            ("Planning", "Execution", "Thinking vs doing"),
            ("Open Loop", "Closed Loop", "No feedback vs feedback"),
            ("Serial", "Parallel", "Chain vs platform"),
            ("Mobile", "Fixed", "Moving vs stationary"),
            ("Teleoperated", "Autonomous", "Remote vs self"),
            ("Rigid", "Soft", "Stiff vs compliant"),
            ("Single", "Swarm", "One vs many"),
            ("Deterministic", "Probabilistic", "Certain vs uncertain"),
            ("Kinematic", "Dynamic", "Position vs force"),
            ("Local", "Global", "Immediate vs overall"),
            ("Reactive", "Deliberative", "Quick vs planned"),
            ("Manipulation", "Locomotion", "Handling vs moving"),
            ("Indoor", "Outdoor", "Structured vs unstructured"),
            ("Contact", "Non-contact", "Touching vs sensing"),
            ("Task", "Motion", "What vs how"),
            ("Safety", "Performance", "Safe vs fast"),
            ("Simulation", "Reality", "Virtual vs physical"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Robotics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Robotics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_asimov_laws(self) -> dict[str, str]:
        """Get Asimov's Three Laws of Robotics."""
        return {
            "first": "A robot may not injure a human being",
            "second": "A robot must obey human orders",
            "third": "A robot must protect its own existence",
            "zeroth": "A robot may not harm humanity",
        }

    def demonstrate_robotics_balance(self) -> dict[str, Any]:
        """Demonstrate robotics balance principles."""
        return {
            "concept": "Robotics Equilibrium",
            "dualities": {
                "autonomy_control": {
                    "autonomy": 50.0,
                    "control": 50.0,
                    "meaning": "Balance independence and human direction",
                },
                "hardware_software": {
                    "hardware": 50.0,
                    "software": 50.0,
                    "meaning": "Physical and computational equally important",
                },
                "perception_action": {
                    "perception": 50.0,
                    "action": 50.0,
                    "meaning": "Sensing and moving are complementary",
                },
            },
            "operation_balance": {
                "planning": 50.0,
                "execution": 50.0,
                "description": "Thinking and doing must balance",
            },
            "meta_meaning": "Robotics demonstrates META 50/50 in autonomy-control synthesis",
        }


def create_robotics_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> RoboticsDomain:
    """
    Factory function to create a fully initialized robotics domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized RoboticsDomain
    """
    domain = RoboticsDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_components()
        domain.initialize_algorithms()
        domain.initialize_robotics_pairs()

    return domain
