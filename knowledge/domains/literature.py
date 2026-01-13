"""
Literature Domain
=================
Literature knowledge domain with META 50/50 equilibrium.
Fundamental duality: Text/Reader (work vs interpretation).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class LiteratureDomain(KnowledgeDomain):
    """
    Literature knowledge domain.

    Fundamental Duality: Text / Reader
    - Text: Written work, author's creation, fixed form
    - Reader: Interpretation, reception, meaning-making

    Secondary Dualities:
    - Form / Content
    - Author / Audience
    - Fiction / Reality
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Literature",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of written works of artistic merit",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Text/Reader duality."""
        self._domain.set_duality(
            positive_name="text",
            positive_value=50,
            negative_name="reader",
            negative_value=50,
            duality_name="literature_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental literary principles."""
        principles = [
            (
                "Intentional Fallacy",
                "Author's intent doesn't determine meaning",
            ),
            (
                "Affective Fallacy",
                "Reader's response doesn't determine value",
            ),
            (
                "Death of the Author",
                "Text exists independently of author",
            ),
            (
                "Intertextuality",
                "Texts reference other texts",
            ),
            (
                "Defamiliarization",
                "Literature makes the familiar strange",
            ),
            (
                "Implied Reader",
                "Text constructs its ideal reader",
            ),
            (
                "Narrative Reliability",
                "Narrators can be unreliable",
            ),
            (
                "Literary Canon",
                "Certain works are deemed exemplary",
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=80,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental literature concepts."""
        return [
            "Text",
            "Author",
            "Reader",
            "Narrative",
            "Character",
            "Plot",
            "Theme",
            "Style",
            "Genre",
            "Interpretation",
            "Metaphor",
            "Symbol",
            "Imagery",
            "Voice",
            "Canon",
        ]

    def initialize_branches(self) -> None:
        """Initialize major literature branches."""
        branches = [
            (
                "Literary Theory",
                "Frameworks for interpreting literature",
                ConceptType.THEORY,
            ),
            (
                "Literary Criticism",
                "Analysis and evaluation of texts",
                ConceptType.THEORY,
            ),
            (
                "Comparative Literature",
                "Literature across cultures",
                ConceptType.THEORY,
            ),
            (
                "Genre Studies",
                "Study of literary genres",
                ConceptType.THEORY,
            ),
            (
                "Narratology",
                "Theory of narrative",
                ConceptType.THEORY,
            ),
            (
                "Poetics",
                "Theory of poetry",
                ConceptType.THEORY,
            ),
            (
                "Rhetoric",
                "Art of persuasion in texts",
                ConceptType.THEORY,
            ),
            (
                "Stylistics",
                "Study of literary style",
                ConceptType.THEORY,
            ),
            (
                "Reception Theory",
                "How readers interpret texts",
                ConceptType.THEORY,
            ),
            (
                "Postcolonial Literature",
                "Literature and colonialism",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_genres(self) -> None:
        """Initialize literary genres."""
        genres = [
            ("Poetry", "Verse, rhythm, imagery", "Sonnets, epics, lyrics"),
            ("Fiction", "Imagined narrative", "Novels, short stories"),
            ("Drama", "Performance text", "Tragedy, comedy"),
            ("Non-fiction", "Factual prose", "Essays, biography"),
            ("Epic", "Long heroic narrative", "Homer, Milton"),
            ("Novel", "Extended prose fiction", "19th century form"),
        ]

        for name, description, examples in genres:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_theories(self) -> None:
        """Initialize literary theories."""
        theories = [
            ("Formalism", "Russian Formalists", "Focus on form and technique"),
            ("Structuralism", "Barthes", "Underlying structures"),
            ("Post-structuralism", "Derrida", "Decentered meaning"),
            ("New Criticism", "Brooks", "Close reading of text"),
            ("Reader-Response", "Iser", "Reader creates meaning"),
            ("Feminist Criticism", "Showalter", "Gender in literature"),
            ("Marxist Criticism", "Eagleton", "Class and ideology"),
            ("Psychoanalytic", "Lacan", "Unconscious in texts"),
        ]

        for name, founder, description in theories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_literary_devices(self) -> None:
        """Initialize literary devices."""
        devices = [
            ("Metaphor", "Implicit comparison", "Life is a journey"),
            ("Simile", "Explicit comparison", "Like a red rose"),
            ("Irony", "Contrast intended/expressed", "Dramatic, verbal"),
            ("Symbol", "Object representing idea", "White whale"),
            ("Allegory", "Extended symbolism", "Animal Farm"),
            ("Foreshadowing", "Hints at future", "Building tension"),
        ]

        for name, description, example in devices:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["example"] = example

    def initialize_literary_pairs(self) -> None:
        """Initialize fundamental literary pairs with META 50/50 balance."""
        pairs = [
            ("Text", "Reader", "Work vs interpretation"),
            ("Form", "Content", "How vs what"),
            ("Author", "Audience", "Creator vs receiver"),
            ("Fiction", "Reality", "Imagined vs actual"),
            ("Surface", "Depth", "Literal vs symbolic"),
            ("Showing", "Telling", "Scene vs summary"),
            ("Plot", "Character", "Action vs person"),
            ("Poetry", "Prose", "Verse vs continuous"),
            ("Literal", "Figurative", "Direct vs indirect"),
            ("Comedy", "Tragedy", "Happy vs sad ending"),
            ("Narrator", "Character", "Teller vs actor"),
            ("First Person", "Third Person", "I vs he/she"),
            ("Dialogue", "Monologue", "Exchange vs solo"),
            ("Written", "Oral", "Text vs speech"),
            ("Classic", "Modern", "Old vs new"),
            ("High", "Low", "Elite vs popular"),
            ("Canonical", "Marginal", "Center vs periphery"),
            ("Mimesis", "Diegesis", "Show vs tell"),
            ("Denotation", "Connotation", "Literal vs associated"),
            ("Explicit", "Implicit", "Stated vs implied"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Literature)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Literature)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_narrative_elements(self) -> dict[str, str]:
        """Get narrative elements."""
        return {
            "plot": "Sequence of events",
            "character": "Persons in the story",
            "setting": "Time and place",
            "point_of_view": "Narrative perspective",
            "theme": "Central idea",
            "style": "Author's use of language",
        }

    def demonstrate_literature_balance(self) -> dict[str, Any]:
        """Demonstrate literature balance principles."""
        return {
            "concept": "Literature Equilibrium",
            "dualities": {
                "text_reader": {
                    "text": 50.0,
                    "reader": 50.0,
                    "meaning": "Meaning emerges from text-reader interaction",
                },
                "form_content": {
                    "form": 50.0,
                    "content": 50.0,
                    "meaning": "How something is said matters as much as what",
                },
                "author_audience": {
                    "author": 50.0,
                    "audience": 50.0,
                    "meaning": "Creation and reception equally important",
                },
            },
            "interpretive_balance": {
                "objective": 50.0,
                "subjective": 50.0,
                "description": "Text constrains but doesn't determine meaning",
            },
            "meta_meaning": "Literature demonstrates META 50/50 in text-reader dialogue",
        }


def create_literature_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> LiteratureDomain:
    """
    Factory function to create a fully initialized literature domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized LiteratureDomain
    """
    domain = LiteratureDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_genres()
        domain.initialize_theories()
        domain.initialize_literary_devices()
        domain.initialize_literary_pairs()

    return domain
