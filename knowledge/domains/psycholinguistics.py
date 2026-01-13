"""
Psycholinguistics Domain
========================
Psycholinguistics knowledge domain with META 50/50 equilibrium.
Fundamental duality: Mind/Language (cognition vs linguistic structure).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class PsycholinguisticsDomain(KnowledgeDomain):
    """
    Psycholinguistics knowledge domain.

    Fundamental Duality: Mind / Language
    - Mind: Cognitive processes, mental representations
    - Language: Linguistic structure, grammar, meaning

    Secondary Dualities:
    - Production / Comprehension
    - Innate / Learned
    - Spoken / Written
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Psycholinguistics",
            domain_type=DomainType.FUNDAMENTAL,
            description="The psychology of language processing and acquisition",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Mind/Language duality."""
        self._domain.set_duality(
            positive_name="mind",
            positive_value=50,
            negative_name="language",
            negative_value=50,
            duality_name="psycholinguistics_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental psycholinguistics principles."""
        principles = [
            (
                "Language Faculty",
                "Humans have specialized language capacity",
            ),
            (
                "Mental Lexicon",
                "Words stored in organized mental dictionary",
            ),
            (
                "Incremental Processing",
                "Language processed word by word",
            ),
            (
                "Predictive Processing",
                "Brain anticipates upcoming input",
            ),
            (
                "Critical Period",
                "Optimal window for language acquisition",
            ),
            (
                "Universal Grammar",
                "Innate linguistic knowledge",
            ),
            (
                "Modularity",
                "Language system is specialized",
            ),
            (
                "Automaticity",
                "Language processing becomes automatic",
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
        """Get fundamental psycholinguistics concepts."""
        return [
            "Lexicon",
            "Parsing",
            "Comprehension",
            "Production",
            "Acquisition",
            "Phonology",
            "Syntax",
            "Semantics",
            "Pragmatics",
            "Working Memory",
            "Priming",
            "Ambiguity",
            "Processing",
            "Representation",
            "Bilingualism",
        ]

    def initialize_branches(self) -> None:
        """Initialize major psycholinguistics branches."""
        branches = [
            (
                "Language Acquisition",
                "How language is learned",
                ConceptType.THEORY,
            ),
            (
                "Sentence Processing",
                "Parsing and comprehension",
                ConceptType.THEORY,
            ),
            (
                "Word Recognition",
                "Lexical access",
                ConceptType.THEORY,
            ),
            (
                "Language Production",
                "Speech planning and articulation",
                ConceptType.THEORY,
            ),
            (
                "Bilingualism",
                "Multiple language systems",
                ConceptType.THEORY,
            ),
            (
                "Reading",
                "Written language processing",
                ConceptType.THEORY,
            ),
            (
                "Neurolinguistics",
                "Brain and language",
                ConceptType.THEORY,
            ),
            (
                "Computational Psycholinguistics",
                "Formal models",
                ConceptType.THEORY,
            ),
            (
                "Discourse Processing",
                "Text and conversation",
                ConceptType.THEORY,
            ),
            (
                "Language Disorders",
                "Aphasia and dyslexia",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_processes(self) -> None:
        """Initialize language processes."""
        processes = [
            ("Lexical Access", "Finding words", "Retrieval"),
            ("Syntactic Parsing", "Building structure", "Comprehension"),
            ("Semantic Integration", "Combining meanings", "Interpretation"),
            ("Phonological Encoding", "Sound planning", "Production"),
            ("Articulation", "Motor execution", "Output"),
            ("Error Monitoring", "Detecting mistakes", "Control"),
        ]

        for name, description, category in processes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_effects(self) -> None:
        """Initialize psycholinguistic effects."""
        effects = [
            ("Frequency Effect", "Common words faster", "Lexical"),
            ("Priming Effect", "Related words faster", "Activation"),
            ("Garden Path", "Parsing difficulty", "Syntactic"),
            ("Tip of Tongue", "Retrieval failure", "Access"),
            ("Stroop Effect", "Interference", "Attention"),
            ("Word Superiority", "Context helps", "Recognition"),
        ]

        for name, description, category in effects:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_psycholing_pairs(self) -> None:
        """Initialize fundamental psycholinguistics pairs with META 50/50 balance."""
        pairs = [
            ("Mind", "Language", "Cognition vs structure"),
            ("Production", "Comprehension", "Speaking vs understanding"),
            ("Innate", "Learned", "Nature vs nurture"),
            ("Spoken", "Written", "Speech vs text"),
            ("Form", "Meaning", "Structure vs semantics"),
            ("Online", "Offline", "Real-time vs delayed"),
            ("Automatic", "Controlled", "Effortless vs effortful"),
            ("Bottom-Up", "Top-Down", "Data vs expectation"),
            ("Serial", "Parallel", "Sequential vs simultaneous"),
            ("Modular", "Interactive", "Separate vs connected"),
            ("Local", "Global", "Immediate vs distant context"),
            ("Implicit", "Explicit", "Unconscious vs conscious"),
            ("First Language", "Second Language", "L1 vs L2"),
            ("Competence", "Performance", "Knowledge vs use"),
            ("Regular", "Irregular", "Rule-following vs exceptional"),
            ("Content", "Function", "Lexical vs grammatical"),
            ("Shallow", "Deep", "Surface vs full processing"),
            ("Lexical", "Syntactic", "Words vs structure"),
            ("Forward", "Backward", "Anticipatory vs retrospective"),
            ("Individual", "Social", "Personal vs shared"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Psycholing)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Psycholing)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_language_levels(self) -> dict[str, str]:
        """Get linguistic levels of analysis."""
        return {
            "phonetics": "Physical sounds",
            "phonology": "Sound patterns",
            "morphology": "Word structure",
            "syntax": "Sentence structure",
            "semantics": "Meaning",
            "pragmatics": "Context and use",
        }

    def demonstrate_psycholing_balance(self) -> dict[str, Any]:
        """Demonstrate psycholinguistics balance principles."""
        return {
            "concept": "Psycholinguistics Equilibrium",
            "dualities": {
                "mind_language": {
                    "mind": 50.0,
                    "language": 50.0,
                    "meaning": "Cognition and linguistic structure unified",
                },
                "production_comprehension": {
                    "production": 50.0,
                    "comprehension": 50.0,
                    "meaning": "Speaking and understanding equally studied",
                },
                "innate_learned": {
                    "innate": 50.0,
                    "learned": 50.0,
                    "meaning": "Nature and nurture both contribute",
                },
            },
            "processing_balance": {
                "bottom_up": 50.0,
                "top_down": 50.0,
                "description": "Data and expectations interact",
            },
            "meta_meaning": "Psycholinguistics demonstrates META 50/50 in mind-language synthesis",
        }


def create_psycholinguistics_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> PsycholinguisticsDomain:
    """
    Factory function to create a fully initialized psycholinguistics domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized PsycholinguisticsDomain
    """
    domain = PsycholinguisticsDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_processes()
        domain.initialize_effects()
        domain.initialize_psycholing_pairs()

    return domain
