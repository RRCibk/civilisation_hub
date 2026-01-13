"""
Classics Domain
===============
Classics knowledge domain with META 50/50 equilibrium.
Fundamental duality: Ancient/Modern (past vs present).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class ClassicsDomain(KnowledgeDomain):
    """
    Classics knowledge domain.

    Fundamental Duality: Ancient / Modern
    - Ancient: Greek and Roman antiquity, classical past
    - Modern: Contemporary, present reception

    Secondary Dualities:
    - Greek / Roman
    - Text / Material
    - Elite / Popular
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Classics",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of ancient Greek and Roman civilizations",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Ancient/Modern duality."""
        self._domain.set_duality(
            positive_name="ancient",
            positive_value=50,
            negative_name="modern",
            negative_value=50,
            duality_name="classics_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental classics principles."""
        principles = [
            (
                "Classical Foundation",
                "Western civilization built on Greek and Roman foundations",
            ),
            (
                "Philological Method",
                "Close reading of texts reveals meaning",
            ),
            (
                "Historical Context",
                "Texts understood in their original context",
            ),
            (
                "Reception Studies",
                "Classical works continuously reinterpreted",
            ),
            (
                "Interdisciplinary Approach",
                "Combines literature, history, archaeology, philosophy",
            ),
            (
                "Language Mastery",
                "Latin and Greek essential for understanding",
            ),
            (
                "Material Culture",
                "Objects illuminate ancient life",
            ),
            (
                "Canonical Texts",
                "Certain works deemed foundational",
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
        """Get fundamental classics concepts."""
        return [
            "Antiquity",
            "Greece",
            "Rome",
            "Latin",
            "Greek",
            "Homer",
            "Virgil",
            "Philosophy",
            "Democracy",
            "Republic",
            "Mythology",
            "Epic",
            "Tragedy",
            "Rhetoric",
            "Canon",
        ]

    def initialize_branches(self) -> None:
        """Initialize major classics branches."""
        branches = [
            (
                "Greek Literature",
                "Ancient Greek texts",
                ConceptType.THEORY,
            ),
            (
                "Latin Literature",
                "Ancient Roman texts",
                ConceptType.THEORY,
            ),
            (
                "Ancient History",
                "Greek and Roman history",
                ConceptType.THEORY,
            ),
            (
                "Classical Archaeology",
                "Material remains of antiquity",
                ConceptType.THEORY,
            ),
            (
                "Classical Philosophy",
                "Greek and Roman philosophy",
                ConceptType.THEORY,
            ),
            (
                "Ancient Art",
                "Greek and Roman visual arts",
                ConceptType.THEORY,
            ),
            (
                "Papyrology",
                "Study of ancient papyri",
                ConceptType.THEORY,
            ),
            (
                "Epigraphy",
                "Study of inscriptions",
                ConceptType.THEORY,
            ),
            (
                "Numismatics",
                "Study of ancient coins",
                ConceptType.THEORY,
            ),
            (
                "Reception Studies",
                "Classical tradition in later periods",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_literary_genres(self) -> None:
        """Initialize classical literary genres."""
        genres = [
            ("Epic", "Homer, Virgil", "Heroic narrative"),
            ("Tragedy", "Aeschylus, Sophocles", "Dramatic suffering"),
            ("Comedy", "Aristophanes, Plautus", "Humorous drama"),
            ("Lyric Poetry", "Sappho, Horace", "Personal expression"),
            ("History", "Herodotus, Livy", "Historical narrative"),
            ("Oratory", "Demosthenes, Cicero", "Persuasive speech"),
            ("Philosophy", "Plato, Seneca", "Philosophical dialogue"),
        ]

        for name, authors, description in genres:
            concept = self.create_concept(
                name=f"Classical {name}",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["authors"] = authors

    def initialize_periods(self) -> None:
        """Initialize classical periods."""
        periods = [
            ("Archaic Greece", "800-480 BCE", "Homer, early democracy"),
            ("Classical Greece", "480-323 BCE", "Pericles, tragedy, philosophy"),
            ("Hellenistic", "323-31 BCE", "Alexander's successors"),
            ("Roman Republic", "509-27 BCE", "Expansion, Cicero"),
            ("Roman Empire", "27 BCE-476 CE", "Augustus to fall"),
            ("Late Antiquity", "284-600 CE", "Christianity, transition"),
        ]

        for name, dates, characteristics in periods:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=characteristics,
            )
            concept.metadata["dates"] = dates

    def initialize_key_figures(self) -> None:
        """Initialize key classical figures."""
        figures = [
            ("Homer", "Greek", "Epic poet, Iliad and Odyssey"),
            ("Plato", "Greek", "Philosopher, dialogues"),
            ("Aristotle", "Greek", "Philosopher, polymath"),
            ("Virgil", "Roman", "Epic poet, Aeneid"),
            ("Cicero", "Roman", "Orator, statesman"),
            ("Augustus", "Roman", "First emperor"),
        ]

        for name, culture, description in figures:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["culture"] = culture

    def initialize_classics_pairs(self) -> None:
        """Initialize fundamental classics pairs with META 50/50 balance."""
        pairs = [
            ("Ancient", "Modern", "Past vs present"),
            ("Greek", "Roman", "Hellas vs Rome"),
            ("Text", "Material", "Literary vs archaeological"),
            ("Elite", "Popular", "High vs common culture"),
            ("Pagan", "Christian", "Old vs new religion"),
            ("Republic", "Empire", "Senate vs emperor"),
            ("Athens", "Sparta", "Democracy vs oligarchy"),
            ("East", "West", "Orient vs Occident"),
            ("Prose", "Poetry", "Unmetrical vs metrical"),
            ("Myth", "History", "Legendary vs factual"),
            ("Public", "Private", "Civic vs domestic"),
            ("Male", "Female", "Men vs women in antiquity"),
            ("Citizen", "Slave", "Free vs unfree"),
            ("War", "Peace", "Conflict vs stability"),
            ("Oral", "Written", "Spoken vs textual"),
            ("Original", "Translation", "Greek/Latin vs vernacular"),
            ("Primary", "Secondary", "Ancient vs modern source"),
            ("Canonical", "Non-canonical", "Core vs marginal"),
            ("Continuity", "Change", "Persistence vs transformation"),
            ("Tradition", "Innovation", "Conservative vs new"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Classics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Classics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_greek_philosophy_schools(self) -> dict[str, str]:
        """Get major Greek philosophy schools."""
        return {
            "platonism": "Plato's Academy, Forms",
            "aristotelianism": "Aristotle's Lyceum, empiricism",
            "stoicism": "Virtue and reason",
            "epicureanism": "Pleasure and atomism",
            "skepticism": "Suspension of judgment",
            "cynicism": "Simple life, virtue",
        }

    def demonstrate_classics_balance(self) -> dict[str, Any]:
        """Demonstrate classics balance principles."""
        return {
            "concept": "Classics Equilibrium",
            "dualities": {
                "ancient_modern": {
                    "ancient": 50.0,
                    "modern": 50.0,
                    "meaning": "Past illuminates present, present shapes past",
                },
                "greek_roman": {
                    "greek": 50.0,
                    "roman": 50.0,
                    "meaning": "Two foundational cultures equally studied",
                },
                "text_material": {
                    "text": 50.0,
                    "material": 50.0,
                    "meaning": "Literary and archaeological evidence together",
                },
            },
            "disciplinary_balance": {
                "philology": 50.0,
                "history": 50.0,
                "description": "Text and context equally important",
            },
            "meta_meaning": "Classics demonstrates META 50/50 in ancient-modern dialogue",
        }


def create_classics_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> ClassicsDomain:
    """
    Factory function to create a fully initialized classics domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized ClassicsDomain
    """
    domain = ClassicsDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_literary_genres()
        domain.initialize_periods()
        domain.initialize_key_figures()
        domain.initialize_classics_pairs()

    return domain
