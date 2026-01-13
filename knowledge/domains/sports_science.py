"""
Sports Science Domain
=====================
Sports Science knowledge domain with META 50/50 equilibrium.
Fundamental duality: Performance/Recovery (output vs restoration).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class SportsScienceDomain(KnowledgeDomain):
    """
    Sports Science knowledge domain.

    Fundamental Duality: Performance / Recovery
    - Performance: Output, exertion, competition
    - Recovery: Restoration, rest, regeneration

    Secondary Dualities:
    - Training / Rest
    - Physical / Mental
    - Individual / Team
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="SportsScience",
            domain_type=DomainType.FUNDAMENTAL,
            description="The science of athletic performance and human movement",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Performance/Recovery duality."""
        self._domain.set_duality(
            positive_name="performance",
            positive_value=50,
            negative_name="recovery",
            negative_value=50,
            duality_name="sports_science_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental sports science principles."""
        principles = [
            ("Specificity", "Training must match sport demands"),
            ("Overload", "Progressive stress for adaptation"),
            ("Recovery", "Rest is essential for growth"),
            ("Periodization", "Planned variation in training"),
            ("Individuality", "Each athlete responds differently"),
            ("Reversibility", "Detraining occurs without stimulus"),
            ("Adaptation", "Body adapts to imposed demands"),
            ("Diminishing Returns", "Gains decrease with advancement"),
        ]

        for name, description in principles:
            self.create_concept(name, ConceptType.PRINCIPLE, description, certainty=90)

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental sports science concepts."""
        return ["Training", "Fitness", "Fatigue", "Adaptation", "Performance",
                "Recovery", "Periodization", "Load", "Intensity", "Volume",
                "Technique", "Tactics", "Conditioning", "Biomechanics", "Physiology"]

    def initialize_branches(self) -> None:
        """Initialize major sports science branches."""
        branches = [
            ("Exercise Physiology", "Body during exercise", ConceptType.THEORY),
            ("Sports Biomechanics", "Movement mechanics", ConceptType.THEORY),
            ("Sports Psychology", "Mental aspects", ConceptType.THEORY),
            ("Sports Nutrition", "Dietary optimization", ConceptType.THEORY),
            ("Strength and Conditioning", "Physical preparation", ConceptType.THEORY),
            ("Sports Medicine", "Injury and health", ConceptType.THEORY),
            ("Motor Learning", "Skill acquisition", ConceptType.THEORY),
            ("Performance Analysis", "Game analysis", ConceptType.THEORY),
            ("Sports Technology", "Equipment and data", ConceptType.THEORY),
            ("Coaching Science", "Coach development", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_systems(self) -> None:
        """Initialize energy systems."""
        systems = [
            ("ATP-PC", "Immediate energy", "0-10 seconds"),
            ("Glycolytic", "Short-term energy", "10-90 seconds"),
            ("Oxidative", "Long-term energy", "90+ seconds"),
            ("Aerobic", "With oxygen", "Endurance"),
            ("Anaerobic", "Without oxygen", "Power"),
            ("Mixed", "Combined systems", "Most sports"),
        ]

        for name, description, duration in systems:
            concept = self.create_concept(name, ConceptType.DEFINITION, description)
            concept.metadata["duration"] = duration

    def initialize_sports_science_pairs(self) -> None:
        """Initialize fundamental sports science pairs with META 50/50 balance."""
        pairs = [
            ("Performance", "Recovery", "Output vs restoration"),
            ("Training", "Rest", "Work vs regeneration"),
            ("Physical", "Mental", "Body vs mind"),
            ("Individual", "Team", "Solo vs collective"),
            ("Aerobic", "Anaerobic", "Endurance vs power"),
            ("Strength", "Flexibility", "Force vs range"),
            ("Speed", "Endurance", "Fast vs sustained"),
            ("Technique", "Fitness", "Skill vs capacity"),
            ("Offense", "Defense", "Attack vs protect"),
            ("Practice", "Competition", "Training vs game"),
            ("Volume", "Intensity", "Amount vs effort"),
            ("General", "Specific", "Base vs sport"),
            ("Peak", "Maintenance", "Maximum vs sustain"),
            ("Central", "Peripheral", "Core vs limbs"),
            ("Concentric", "Eccentric", "Shorten vs lengthen"),
            ("Bilateral", "Unilateral", "Both vs single"),
            ("Open", "Closed", "Variable vs fixed skill"),
            ("Intrinsic", "Extrinsic", "Internal vs external motivation"),
            ("Talent", "Training", "Natural vs developed"),
            ("Art", "Science", "Intuition vs data"),
        ]

        for positive, negative, description in pairs:
            pos = self.create_concept(f"{positive} (Sports)", ConceptType.DEFINITION,
                                       f"Positive pole: {description.split(' vs ')[0]}")
            neg = self.create_concept(f"{negative} (Sports)", ConceptType.DEFINITION,
                                       f"Negative pole: {description.split(' vs ')[1]}")
            self.create_relation(pos, neg, RelationType.CONTRADICTS, strength=50)

    def demonstrate_sports_balance(self) -> dict[str, Any]:
        """Demonstrate sports science balance principles."""
        return {
            "concept": "Sports Science Equilibrium",
            "dualities": {
                "performance_recovery": {"performance": 50.0, "recovery": 50.0,
                    "meaning": "Balance output with restoration"},
                "training_rest": {"training": 50.0, "rest": 50.0,
                    "meaning": "Balance work with regeneration"},
            },
            "meta_meaning": "Sports Science demonstrates META 50/50 in performance-recovery balance",
        }


def create_sports_science_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> SportsScienceDomain:
    domain = SportsScienceDomain(meta_equilibrium)
    if initialize_all:
        domain.initialize_branches()
        domain.initialize_systems()
        domain.initialize_sports_science_pairs()
    return domain
