"""
Translation Studies Domain
==========================
Translation Studies knowledge domain with META 50/50 equilibrium.
Fundamental duality: Source/Target (original vs translated).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class TranslationStudiesDomain(KnowledgeDomain):
    """
    Translation Studies knowledge domain.

    Fundamental Duality: Source / Target
    - Source: Original text, language, culture
    - Target: Translated text, receiving culture

    Secondary Dualities:
    - Fidelity / Fluency
    - Foreignization / Domestication
    - Form / Meaning
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="TranslationStudies",
            domain_type=DomainType.FUNDAMENTAL,
            description="The theory and practice of translation and interpreting",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Source/Target duality."""
        self._domain.set_duality(
            positive_name="source",
            positive_value=50,
            negative_name="target",
            negative_value=50,
            duality_name="translation_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental translation principles."""
        principles = [
            ("Equivalence", "Achieve equivalent effect"),
            ("Fidelity", "Stay true to the source"),
            ("Fluency", "Read naturally in target"),
            ("Context", "Consider cultural context"),
            ("Purpose", "Translation serves a function"),
            ("Competence", "Master both languages"),
            ("Ethics", "Impartial and confidential"),
            ("Invisibility", "Translator as transparent mediator"),
        ]

        for name, description in principles:
            self.create_concept(name, ConceptType.PRINCIPLE, description, certainty=85)

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental translation concepts."""
        return ["Translation", "Interpretation", "Source", "Target", "Equivalence",
                "Fidelity", "Fluency", "Localization", "Adaptation", "Transcreation",
                "Register", "Genre", "Context", "Culture", "Terminology"]

    def initialize_branches(self) -> None:
        """Initialize major translation branches."""
        branches = [
            ("Literary Translation", "Creative texts", ConceptType.THEORY),
            ("Technical Translation", "Specialized texts", ConceptType.THEORY),
            ("Legal Translation", "Law texts", ConceptType.THEORY),
            ("Medical Translation", "Healthcare texts", ConceptType.THEORY),
            ("Audiovisual Translation", "Media content", ConceptType.THEORY),
            ("Interpreting", "Oral translation", ConceptType.THEORY),
            ("Localization", "Product adaptation", ConceptType.THEORY),
            ("Machine Translation", "Automated translation", ConceptType.THEORY),
            ("Community Interpreting", "Public services", ConceptType.THEORY),
            ("Conference Interpreting", "Simultaneous translation", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_modes(self) -> None:
        """Initialize translation/interpreting modes."""
        modes = [
            ("Written", "Text translation", "Delayed"),
            ("Simultaneous", "Real-time interpreting", "Immediate"),
            ("Consecutive", "Turn-based interpreting", "Sequential"),
            ("Sight", "Written to oral", "Hybrid"),
            ("Whispered", "Chuchotage", "Quiet"),
            ("Relay", "Through pivot", "Indirect"),
        ]

        for name, description, timing in modes:
            concept = self.create_concept(name, ConceptType.DEFINITION, description)
            concept.metadata["timing"] = timing

    def initialize_translation_pairs(self) -> None:
        """Initialize fundamental translation pairs with META 50/50 balance."""
        pairs = [
            ("Source", "Target", "Original vs translated"),
            ("Fidelity", "Fluency", "Accurate vs natural"),
            ("Foreignization", "Domestication", "Keep foreign vs adapt"),
            ("Form", "Meaning", "Structure vs content"),
            ("Literal", "Free", "Word-for-word vs sense"),
            ("Written", "Oral", "Translation vs interpreting"),
            ("Human", "Machine", "Translator vs computer"),
            ("Specialized", "General", "Technical vs common"),
            ("Overt", "Covert", "Visible vs invisible translation"),
            ("Direct", "Indirect", "Straight vs via pivot"),
            ("Semantic", "Communicative", "Meaning vs effect"),
            ("Author", "Reader", "Source vs target oriented"),
            ("Local", "Global", "Specific vs universal"),
            ("Prescriptive", "Descriptive", "Should vs does"),
            ("Product", "Process", "Result vs method"),
            ("Adequacy", "Acceptability", "Source vs target norms"),
            ("Equivalence", "Correspondence", "Same vs similar"),
            ("Loss", "Gain", "Missing vs added"),
            ("Visible", "Invisible", "Marked vs unmarked"),
            ("Norm", "Deviation", "Standard vs creative"),
        ]

        for positive, negative, description in pairs:
            pos = self.create_concept(f"{positive} (Translation)", ConceptType.DEFINITION,
                                       f"Positive pole: {description.split(' vs ')[0]}")
            neg = self.create_concept(f"{negative} (Translation)", ConceptType.DEFINITION,
                                       f"Negative pole: {description.split(' vs ')[1]}")
            self.create_relation(pos, neg, RelationType.CONTRADICTS, strength=50)

    def demonstrate_translation_balance(self) -> dict[str, Any]:
        """Demonstrate translation balance principles."""
        return {
            "concept": "Translation Studies Equilibrium",
            "dualities": {
                "source_target": {"source": 50.0, "target": 50.0,
                    "meaning": "Balance original and translated"},
                "fidelity_fluency": {"fidelity": 50.0, "fluency": 50.0,
                    "meaning": "Balance accuracy with naturalness"},
            },
            "meta_meaning": "Translation Studies demonstrates META 50/50 in source-target balance",
        }


def create_translation_studies_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> TranslationStudiesDomain:
    domain = TranslationStudiesDomain(meta_equilibrium)
    if initialize_all:
        domain.initialize_branches()
        domain.initialize_modes()
        domain.initialize_translation_pairs()
    return domain
