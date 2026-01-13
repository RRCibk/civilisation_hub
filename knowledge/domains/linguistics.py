"""
Linguistics Domain
==================
Linguistics knowledge domain with META 50/50 equilibrium.
Fundamental duality: Signifier/Signified (form vs meaning).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class LinguisticsDomain(KnowledgeDomain):
    """
    Linguistics knowledge domain.

    Fundamental Duality: Signifier / Signified
    - Signifier: Sound pattern, written form, expression
    - Signified: Concept, meaning, content

    Secondary Dualities:
    - Langue / Parole
    - Synchronic / Diachronic
    - Competence / Performance
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Linguistics",
            domain_type=DomainType.FUNDAMENTAL,
            description="The scientific study of language structure, use, and change",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Signifier/Signified duality."""
        self._domain.set_duality(
            positive_name="signifier",
            positive_value=50,
            negative_name="signified",
            negative_value=50,
            duality_name="linguistics_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental linguistic principles."""
        principles = [
            (
                "Arbitrariness of Sign",
                "The link between signifier and signified is arbitrary",
            ),
            (
                "Duality of Patterning",
                "Language has two levels: meaningless sounds form meaningful units",
            ),
            (
                "Productivity",
                "Infinite sentences from finite rules",
            ),
            (
                "Displacement",
                "Language can refer to absent things",
            ),
            (
                "Universal Grammar",
                "All languages share underlying principles",
            ),
            (
                "Language Acquisition",
                "Children acquire language naturally",
            ),
            (
                "Language Change",
                "All living languages change over time",
            ),
            (
                "Systematicity",
                "Language is a structured system",
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
        """Get fundamental linguistics concepts."""
        return [
            "Language",
            "Grammar",
            "Phoneme",
            "Morpheme",
            "Syntax",
            "Semantics",
            "Pragmatics",
            "Discourse",
            "Sign",
            "Symbol",
            "Meaning",
            "Reference",
            "Speech",
            "Writing",
            "Communication",
        ]

    def initialize_branches(self) -> None:
        """Initialize major linguistics branches."""
        branches = [
            (
                "Phonetics",
                "Physical sounds of speech",
                ConceptType.THEORY,
            ),
            (
                "Phonology",
                "Sound systems of languages",
                ConceptType.THEORY,
            ),
            (
                "Morphology",
                "Word structure and formation",
                ConceptType.THEORY,
            ),
            (
                "Syntax",
                "Sentence structure",
                ConceptType.THEORY,
            ),
            (
                "Semantics",
                "Meaning in language",
                ConceptType.THEORY,
            ),
            (
                "Pragmatics",
                "Language use in context",
                ConceptType.THEORY,
            ),
            (
                "Sociolinguistics",
                "Language and society",
                ConceptType.THEORY,
            ),
            (
                "Psycholinguistics",
                "Language and mind",
                ConceptType.THEORY,
            ),
            (
                "Historical Linguistics",
                "Language change over time",
                ConceptType.THEORY,
            ),
            (
                "Computational Linguistics",
                "Computer processing of language",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_linguistic_units(self) -> None:
        """Initialize linguistic unit types."""
        units = [
            ("Phone", "Physical sound", "Smallest speech unit"),
            ("Phoneme", "Distinctive sound unit", "/p/, /b/, /t/"),
            ("Morpheme", "Smallest meaningful unit", "un-, -ed, cat"),
            ("Word", "Free-standing unit", "Lexical item"),
            ("Phrase", "Group of words", "Syntactic unit"),
            ("Clause", "Subject-predicate unit", "Proposition"),
            ("Sentence", "Complete thought", "Grammatical unit"),
        ]

        for name, description, example in units:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["example"] = example

    def initialize_theories(self) -> None:
        """Initialize linguistic theories."""
        theories = [
            ("Structuralism", "Saussure", "Language as system of differences"),
            ("Generative Grammar", "Chomsky", "Innate language faculty"),
            ("Functionalism", "Halliday", "Language serves functions"),
            ("Cognitive Linguistics", "Lakoff", "Language reflects cognition"),
            ("Construction Grammar", "Goldberg", "Constructions are basic units"),
            ("Usage-Based Theory", "Langacker", "Usage shapes grammar"),
        ]

        for name, founder, description in theories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_language_families(self) -> None:
        """Initialize major language families."""
        families = [
            ("Indo-European", "3 billion speakers", "English, Hindi, Spanish"),
            ("Sino-Tibetan", "1.5 billion speakers", "Mandarin, Burmese"),
            ("Afro-Asiatic", "500 million speakers", "Arabic, Hebrew, Amharic"),
            ("Niger-Congo", "700 million speakers", "Swahili, Yoruba, Zulu"),
            ("Austronesian", "400 million speakers", "Indonesian, Tagalog"),
            ("Dravidian", "250 million speakers", "Tamil, Telugu, Malayalam"),
        ]

        for name, speakers, examples in families:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=f"Language family with {speakers}",
            )
            concept.metadata["examples"] = examples

    def initialize_linguistic_pairs(self) -> None:
        """Initialize fundamental linguistic pairs with META 50/50 balance."""
        pairs = [
            ("Signifier", "Signified", "Form vs meaning"),
            ("Langue", "Parole", "System vs use"),
            ("Synchronic", "Diachronic", "Snapshot vs historical"),
            ("Competence", "Performance", "Knowledge vs use"),
            ("Phonetics", "Phonology", "Physical vs abstract"),
            ("Syntax", "Semantics", "Structure vs meaning"),
            ("Morpheme", "Phoneme", "Meaningful vs distinctive"),
            ("Deep", "Surface", "Underlying vs visible"),
            ("Prescriptive", "Descriptive", "Should vs does"),
            ("Written", "Spoken", "Text vs speech"),
            ("Standard", "Dialect", "Official vs regional"),
            ("Native", "Foreign", "First vs learned"),
            ("Productive", "Receptive", "Speaking vs understanding"),
            ("Content", "Function", "Meaning vs grammar words"),
            ("Derivation", "Inflection", "New word vs form change"),
            ("Paradigmatic", "Syntagmatic", "Selection vs combination"),
            ("Marked", "Unmarked", "Special vs default"),
            ("Bound", "Free", "Attached vs independent"),
            ("Animate", "Inanimate", "Living vs non-living"),
            ("Vowel", "Consonant", "Open vs obstructed"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Linguistics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Linguistics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_saussure_dichotomies(self) -> dict[str, str]:
        """Get Saussure's fundamental dichotomies."""
        return {
            "langue_parole": "Language system vs individual speech acts",
            "signifier_signified": "Sound pattern vs concept",
            "synchronic_diachronic": "Static vs historical analysis",
            "paradigmatic_syntagmatic": "Selection vs combination",
        }

    def demonstrate_linguistics_balance(self) -> dict[str, Any]:
        """Demonstrate linguistics balance principles."""
        return {
            "concept": "Linguistics Equilibrium",
            "dualities": {
                "signifier_signified": {
                    "signifier": 50.0,
                    "signified": 50.0,
                    "meaning": "Sign unites form and meaning",
                },
                "langue_parole": {
                    "langue": 50.0,
                    "parole": 50.0,
                    "meaning": "System and use are interdependent",
                },
                "competence_performance": {
                    "competence": 50.0,
                    "performance": 50.0,
                    "meaning": "Knowledge and use co-exist",
                },
            },
            "sign_balance": {
                "expression": 50.0,
                "content": 50.0,
                "description": "Two sides of the linguistic sign",
            },
            "meta_meaning": "Linguistics demonstrates META 50/50 in signifier-signified unity",
        }


def create_linguistics_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> LinguisticsDomain:
    """
    Factory function to create a fully initialized linguistics domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized LinguisticsDomain
    """
    domain = LinguisticsDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_linguistic_units()
        domain.initialize_theories()
        domain.initialize_language_families()
        domain.initialize_linguistic_pairs()

    return domain
