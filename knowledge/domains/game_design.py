"""
Game Design Domain
==================
Game Design knowledge domain with META 50/50 equilibrium.
Fundamental duality: Challenge/Reward (difficulty vs satisfaction).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class GameDesignDomain(KnowledgeDomain):
    """
    Game Design knowledge domain.

    Fundamental Duality: Challenge / Reward
    - Challenge: Difficulty, obstacles, skill requirements
    - Reward: Satisfaction, progression, achievement

    Secondary Dualities:
    - Mechanics / Aesthetics
    - Player / Designer
    - Freedom / Structure
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="GameDesign",
            domain_type=DomainType.FUNDAMENTAL,
            description="The art and science of creating interactive experiences",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Challenge/Reward duality."""
        self._domain.set_duality(
            positive_name="challenge",
            positive_value=50,
            negative_name="reward",
            negative_value=50,
            duality_name="game_design_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental game design principles."""
        principles = [
            ("Fun", "Games should be enjoyable"),
            ("Engagement", "Keep players invested"),
            ("Balance", "Fair and competitive"),
            ("Feedback", "Clear response to actions"),
            ("Flow", "Optimal challenge level"),
            ("Agency", "Player choices matter"),
            ("Iteration", "Test and refine"),
            ("Accessibility", "Playable by intended audience"),
        ]

        for name, description in principles:
            self.create_concept(name, ConceptType.PRINCIPLE, description, certainty=85)

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental game design concepts."""
        return ["Mechanics", "Dynamics", "Aesthetics", "Rules", "Goals", "Feedback",
                "Challenge", "Balance", "Flow", "Player", "Level", "Progression",
                "Narrative", "Reward", "Engagement"]

    def initialize_branches(self) -> None:
        """Initialize major game design branches."""
        branches = [
            ("Level Design", "Environment creation", ConceptType.THEORY),
            ("Systems Design", "Game mechanics", ConceptType.THEORY),
            ("Narrative Design", "Story integration", ConceptType.THEORY),
            ("UX Design", "Player experience", ConceptType.THEORY),
            ("Economy Design", "Resource systems", ConceptType.THEORY),
            ("Combat Design", "Battle systems", ConceptType.THEORY),
            ("Multiplayer Design", "Social features", ConceptType.THEORY),
            ("Mobile Design", "Mobile games", ConceptType.THEORY),
            ("Serious Games", "Educational games", ConceptType.THEORY),
            ("Gamification", "Game elements in non-games", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_elements(self) -> None:
        """Initialize game elements (MDA framework)."""
        elements = [
            ("Mechanics", "Rules and systems", "Foundation"),
            ("Dynamics", "Emergent behavior", "Interaction"),
            ("Aesthetics", "Emotional response", "Experience"),
            ("Technology", "Technical platform", "Implementation"),
            ("Story", "Narrative elements", "Context"),
            ("Art", "Visual design", "Presentation"),
        ]

        for name, description, role in elements:
            concept = self.create_concept(name, ConceptType.DEFINITION, description)
            concept.metadata["role"] = role

    def initialize_game_design_pairs(self) -> None:
        """Initialize fundamental game design pairs with META 50/50 balance."""
        pairs = [
            ("Challenge", "Reward", "Difficulty vs satisfaction"),
            ("Mechanics", "Aesthetics", "Systems vs feelings"),
            ("Player", "Designer", "User vs creator"),
            ("Freedom", "Structure", "Open vs guided"),
            ("Skill", "Luck", "Ability vs chance"),
            ("Competition", "Cooperation", "Versus vs together"),
            ("Single", "Multi", "Solo vs social"),
            ("Casual", "Hardcore", "Light vs intense"),
            ("Linear", "Open", "Path vs exploration"),
            ("Narrative", "Gameplay", "Story vs action"),
            ("Simulation", "Abstraction", "Realistic vs stylized"),
            ("Intrinsic", "Extrinsic", "Internal vs external reward"),
            ("Short", "Long", "Quick vs extended play"),
            ("Easy", "Hard", "Simple vs difficult"),
            ("Physical", "Digital", "Tabletop vs electronic"),
            ("Synchronous", "Asynchronous", "Real-time vs turn-based"),
            ("Deterministic", "Probabilistic", "Certain vs random"),
            ("Theme", "Mechanics", "Setting vs rules"),
            ("Depth", "Accessibility", "Complex vs approachable"),
            ("Innovation", "Familiarity", "New vs known"),
        ]

        for positive, negative, description in pairs:
            pos = self.create_concept(f"{positive} (Game)", ConceptType.DEFINITION,
                                       f"Positive pole: {description.split(' vs ')[0]}")
            neg = self.create_concept(f"{negative} (Game)", ConceptType.DEFINITION,
                                       f"Negative pole: {description.split(' vs ')[1]}")
            self.create_relation(pos, neg, RelationType.CONTRADICTS, strength=50)

    def demonstrate_game_balance(self) -> dict[str, Any]:
        """Demonstrate game design balance principles."""
        return {
            "concept": "Game Design Equilibrium",
            "dualities": {
                "challenge_reward": {"challenge": 50.0, "reward": 50.0,
                    "meaning": "Balance difficulty with satisfaction"},
                "freedom_structure": {"freedom": 50.0, "structure": 50.0,
                    "meaning": "Balance player agency with guided experience"},
            },
            "meta_meaning": "Game Design demonstrates META 50/50 in challenge-reward balance",
        }


def create_game_design_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> GameDesignDomain:
    domain = GameDesignDomain(meta_equilibrium)
    if initialize_all:
        domain.initialize_branches()
        domain.initialize_elements()
        domain.initialize_game_design_pairs()
    return domain
