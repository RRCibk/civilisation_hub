"""
Theater Domain
==============
Theater knowledge domain with META 50/50 equilibrium.
Fundamental duality: Performance/Audience (stage vs spectator).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class TheaterDomain(KnowledgeDomain):
    """
    Theater knowledge domain.

    Fundamental Duality: Performance / Audience
    - Performance: Stage action, actors, production
    - Audience: Spectators, reception, response

    Secondary Dualities:
    - Text / Performance
    - Actor / Character
    - Real / Fictional
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Theater",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of dramatic performance and theatrical arts",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Performance/Audience duality."""
        self._domain.set_duality(
            positive_name="performance",
            positive_value=50,
            negative_name="audience",
            negative_value=50,
            duality_name="theater_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental theater principles."""
        principles = [
            (
                "Liveness",
                "Theater happens in real time with live presence",
            ),
            (
                "Mimesis",
                "Theater imitates action",
            ),
            (
                "Catharsis",
                "Theater purges emotion",
            ),
            (
                "Willing Suspension of Disbelief",
                "Audience accepts theatrical conventions",
            ),
            (
                "The Fourth Wall",
                "Invisible barrier between stage and audience",
            ),
            (
                "Theatrical Convention",
                "Agreed-upon practices understood by all",
            ),
            (
                "Presence",
                "Actor's energy and immediacy",
            ),
            (
                "Ensemble",
                "Company works as unified whole",
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
        """Get fundamental theater concepts."""
        return [
            "Performance",
            "Audience",
            "Actor",
            "Character",
            "Script",
            "Director",
            "Stage",
            "Scene",
            "Act",
            "Dialogue",
            "Action",
            "Costume",
            "Set",
            "Lighting",
            "Sound",
        ]

    def initialize_branches(self) -> None:
        """Initialize major theater branches."""
        branches = [
            (
                "Drama",
                "Written plays for performance",
                ConceptType.THEORY,
            ),
            (
                "Performance Studies",
                "Broad study of performance",
                ConceptType.THEORY,
            ),
            (
                "Acting",
                "Art of the performer",
                ConceptType.THEORY,
            ),
            (
                "Directing",
                "Interpretation and staging",
                ConceptType.THEORY,
            ),
            (
                "Dramaturgy",
                "Play structure and context",
                ConceptType.THEORY,
            ),
            (
                "Scenic Design",
                "Visual environment",
                ConceptType.THEORY,
            ),
            (
                "Theater History",
                "Historical development",
                ConceptType.THEORY,
            ),
            (
                "Playwriting",
                "Creating dramatic texts",
                ConceptType.THEORY,
            ),
            (
                "Stage Management",
                "Production coordination",
                ConceptType.THEORY,
            ),
            (
                "Applied Theater",
                "Theater for social change",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_genres(self) -> None:
        """Initialize theatrical genres."""
        genres = [
            ("Tragedy", "Serious, protagonist falls", "Catharsis"),
            ("Comedy", "Humorous, happy ending", "Social critique"),
            ("Tragicomedy", "Mixed elements", "Blended form"),
            ("Melodrama", "Heightened emotion", "Clear morality"),
            ("Farce", "Physical comedy", "Absurd situations"),
            ("Musical Theater", "Song and dance", "Integrated form"),
        ]

        for name, description, characteristic in genres:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["characteristic"] = characteristic

    def initialize_acting_methods(self) -> None:
        """Initialize acting methods."""
        methods = [
            ("Stanislavski System", "Stanislavski", "Emotional truth"),
            ("Method Acting", "Strasberg", "Affective memory"),
            ("Meisner Technique", "Meisner", "Living truthfully"),
            ("Physical Theater", "Lecoq", "Body-based performance"),
            ("Brechtian", "Brecht", "Alienation effect"),
            ("Viewpoints", "Bogart", "Composition-based"),
        ]

        for name, founder, focus in methods:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=focus,
            )
            concept.metadata["founder"] = founder

    def initialize_production_elements(self) -> None:
        """Initialize production elements."""
        elements = [
            ("Set Design", "Physical environment", "Scenic elements"),
            ("Costume Design", "Character clothing", "Visual identity"),
            ("Lighting Design", "Illumination", "Mood and focus"),
            ("Sound Design", "Audio elements", "Atmosphere"),
            ("Props", "Stage objects", "Hand props, set dressing"),
        ]

        for name, description, function in elements:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["function"] = function

    def initialize_theater_pairs(self) -> None:
        """Initialize fundamental theater pairs with META 50/50 balance."""
        pairs = [
            ("Performance", "Audience", "Stage vs spectator"),
            ("Text", "Performance", "Script vs enactment"),
            ("Actor", "Character", "Person vs role"),
            ("Real", "Fictional", "Actual vs imagined"),
            ("Tragedy", "Comedy", "Serious vs humorous"),
            ("Speech", "Action", "Words vs movement"),
            ("Stage", "Backstage", "Visible vs hidden"),
            ("Rehearsal", "Performance", "Practice vs show"),
            ("Director", "Actor", "Vision vs execution"),
            ("Playwright", "Director", "Text vs interpretation"),
            ("Representation", "Presentation", "Mimetic vs direct"),
            ("Illusion", "Reality", "Theatrical vs actual"),
            ("Fourth Wall", "Direct Address", "Closed vs open"),
            ("Protagonist", "Antagonist", "Hero vs opponent"),
            ("Main Plot", "Subplot", "Primary vs secondary"),
            ("Climax", "Resolution", "Peak vs ending"),
            ("Exposition", "Action", "Setup vs events"),
            ("Monologue", "Dialogue", "Solo vs exchange"),
            ("Professional", "Amateur", "Career vs hobby"),
            ("Realism", "Stylization", "Naturalistic vs theatrical"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Theater)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Theater)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_aristotle_elements(self) -> dict[str, str]:
        """Get Aristotle's six elements of drama."""
        return {
            "plot": "Arrangement of incidents",
            "character": "Agents of the action",
            "thought": "Ideas expressed",
            "diction": "Expression in words",
            "spectacle": "Visual elements",
            "song": "Musical elements",
        }

    def demonstrate_theater_balance(self) -> dict[str, Any]:
        """Demonstrate theater balance principles."""
        return {
            "concept": "Theater Equilibrium",
            "dualities": {
                "performance_audience": {
                    "performance": 50.0,
                    "audience": 50.0,
                    "meaning": "Theater requires both performers and viewers",
                },
                "actor_character": {
                    "actor": 50.0,
                    "character": 50.0,
                    "meaning": "Performance is both real person and role",
                },
                "text_performance": {
                    "text": 50.0,
                    "performance": 50.0,
                    "meaning": "Script and enactment equally important",
                },
            },
            "dramatic_balance": {
                "tragedy": 50.0,
                "comedy": 50.0,
                "description": "Both modes essential to theater",
            },
            "meta_meaning": "Theater demonstrates META 50/50 in performance-audience co-creation",
        }


def create_theater_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> TheaterDomain:
    """
    Factory function to create a fully initialized theater domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized TheaterDomain
    """
    domain = TheaterDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_genres()
        domain.initialize_acting_methods()
        domain.initialize_production_elements()
        domain.initialize_theater_pairs()

    return domain
