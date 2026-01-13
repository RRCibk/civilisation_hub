"""
Philosophy Domain
=================
Philosophical knowledge domain with META 50/50 equilibrium.
Fundamental duality: Being/Non-Being (existence/void, thesis/antithesis).
"""

from typing import Any
from uuid import UUID

from models.domain import DomainType
from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    KnowledgeDomain,
    Concept,
    ConceptType,
    ConceptRelation,
    RelationType,
)


class PhilosophyDomain(KnowledgeDomain):
    """
    Philosophy knowledge domain.

    Fundamental Duality: Being / Non-Being
    - Being: Existence, presence, affirmation
    - Non-Being: Void, absence, negation

    Secondary Dualities:
    - Mind / Body (dualism)
    - Subject / Object (epistemology)
    - Good / Evil (ethics)
    - Order / Chaos (cosmology)
    - Thesis / Antithesis (dialectics)
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Philosophy",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of fundamental nature of reality, knowledge, and existence",
            meta_equilibrium=meta_equilibrium
        )

    def _initialize_duality(self) -> None:
        """Initialize Being/Non-Being duality."""
        self._domain.set_duality(
            positive_name="being",
            positive_value=50,
            negative_name="non_being",
            negative_value=50,
            duality_name="philosophy_duality"
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental philosophical principles as axioms."""
        principles = [
            (
                "Cogito Ergo Sum",
                "I think, therefore I am - the foundation of rational certainty"
            ),
            (
                "Principle of Sufficient Reason",
                "Everything must have a reason or cause for its existence"
            ),
            (
                "Law of Identity",
                "A thing is what it is (A = A)"
            ),
            (
                "Law of Non-Contradiction",
                "Nothing can both be and not be at the same time"
            ),
            (
                "Law of Excluded Middle",
                "Everything must either be or not be"
            ),
            (
                "Categorical Imperative",
                "Act only according to maxims universalizable as law"
            ),
            (
                "Unity of Opposites",
                "Reality arises from the tension of opposites"
            ),
            (
                "The Examined Life",
                "The unexamined life is not worth living"
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.AXIOM,
                description=description,
                certainty=75  # Philosophical principles are debated
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental philosophy concepts."""
        return [
            "Being", "Truth", "Knowledge", "Reality", "Mind",
            "Consciousness", "Free Will", "Ethics", "Beauty", "Justice",
            "Meaning", "Time", "Space", "Causality", "Self"
        ]

    def initialize_branches(self) -> None:
        """Initialize major philosophy branches."""
        branches = [
            (
                "Metaphysics",
                "Study of the nature of reality, existence, and being",
                ConceptType.THEORY
            ),
            (
                "Epistemology",
                "Study of knowledge, belief, and justification",
                ConceptType.THEORY
            ),
            (
                "Ethics",
                "Study of moral principles and conduct",
                ConceptType.THEORY
            ),
            (
                "Logic",
                "Study of valid reasoning and argumentation",
                ConceptType.THEORY
            ),
            (
                "Aesthetics",
                "Study of beauty, art, and taste",
                ConceptType.THEORY
            ),
            (
                "Political Philosophy",
                "Study of governance, justice, and rights",
                ConceptType.THEORY
            ),
            (
                "Philosophy of Mind",
                "Study of consciousness and mental phenomena",
                ConceptType.THEORY
            ),
            (
                "Philosophy of Science",
                "Study of foundations and methods of science",
                ConceptType.THEORY
            ),
            (
                "Philosophy of Language",
                "Study of meaning, reference, and communication",
                ConceptType.THEORY
            ),
            (
                "Existentialism",
                "Study of individual existence and meaning",
                ConceptType.THEORY
            ),
            (
                "Phenomenology",
                "Study of structures of experience and consciousness",
                ConceptType.THEORY
            ),
            (
                "Ontology",
                "Study of being and what exists",
                ConceptType.THEORY
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_schools_of_thought(self) -> None:
        """Initialize major philosophical schools."""
        schools = [
            # Ancient
            ("Platonism", "Reality consists of ideal Forms", "Ancient"),
            ("Aristotelianism", "Knowledge through observation and logic", "Ancient"),
            ("Stoicism", "Virtue through reason and acceptance", "Ancient"),
            ("Epicureanism", "Pleasure and absence of pain", "Ancient"),
            ("Skepticism", "Suspension of judgment", "Ancient"),

            # Modern
            ("Rationalism", "Knowledge through reason alone", "Modern"),
            ("Empiricism", "Knowledge through sensory experience", "Modern"),
            ("Idealism", "Reality is fundamentally mental", "Modern"),
            ("Materialism", "Reality is fundamentally physical", "Modern"),
            ("Dualism", "Mind and body are distinct substances", "Modern"),

            # Contemporary
            ("Pragmatism", "Truth is what works in practice", "Contemporary"),
            ("Existentialism", "Existence precedes essence", "Contemporary"),
            ("Phenomenology", "Study of conscious experience", "Contemporary"),
            ("Analytic Philosophy", "Logic and language analysis", "Contemporary"),
            ("Postmodernism", "Questioning grand narratives", "Contemporary"),
        ]

        for name, description, era in schools:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description
            )
            concept.metadata["era"] = era

    def initialize_philosophers(self) -> None:
        """Initialize major philosophers."""
        philosophers = [
            ("Socrates", "470-399 BCE", "Greek", ["Dialectic method", "Examined life"]),
            ("Plato", "428-348 BCE", "Greek", ["Forms", "Republic"]),
            ("Aristotle", "384-322 BCE", "Greek", ["Logic", "Virtue ethics"]),
            ("Descartes", "1596-1650", "French", ["Cogito", "Mind-body dualism"]),
            ("Spinoza", "1632-1677", "Dutch", ["Substance monism", "Ethics"]),
            ("Leibniz", "1646-1716", "German", ["Monads", "Pre-established harmony"]),
            ("Locke", "1632-1704", "English", ["Empiricism", "Tabula rasa"]),
            ("Hume", "1711-1776", "Scottish", ["Skepticism", "Is-ought problem"]),
            ("Kant", "1724-1804", "German", ["Transcendental idealism", "Categorical imperative"]),
            ("Hegel", "1770-1831", "German", ["Dialectics", "Absolute idealism"]),
            ("Nietzsche", "1844-1900", "German", ["Will to power", "Eternal recurrence"]),
            ("Wittgenstein", "1889-1951", "Austrian", ["Language games", "Logical positivism"]),
            ("Heidegger", "1889-1976", "German", ["Being", "Dasein"]),
            ("Sartre", "1905-1980", "French", ["Existentialism", "Bad faith"]),
        ]

        for name, years, nationality, contributions in philosophers:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=f"{nationality} philosopher ({years})"
            )
            concept.metadata.update({
                "years": years,
                "nationality": nationality,
                "key_contributions": contributions
            })

    def initialize_thought_experiments(self) -> None:
        """Initialize famous philosophical thought experiments."""
        experiments = [
            (
                "Trolley Problem",
                "Should you divert a trolley to kill one instead of five?",
                "Ethics"
            ),
            (
                "Ship of Theseus",
                "Is a ship with all parts replaced still the same ship?",
                "Identity"
            ),
            (
                "Brain in a Vat",
                "How do we know we're not brains in vats?",
                "Epistemology"
            ),
            (
                "Chinese Room",
                "Can a computer truly understand language?",
                "Philosophy of Mind"
            ),
            (
                "Mary's Room",
                "Can knowledge be non-physical?",
                "Consciousness"
            ),
            (
                "Plato's Cave",
                "Are we seeing reality or shadows?",
                "Metaphysics"
            ),
            (
                "Zeno's Paradoxes",
                "Can motion exist if space is infinitely divisible?",
                "Metaphysics"
            ),
            (
                "The Veil of Ignorance",
                "What principles would you choose not knowing your place?",
                "Political Philosophy"
            ),
        ]

        for name, question, domain in experiments:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.HYPOTHESIS,
                description=question
            )
            concept.metadata["philosophical_domain"] = domain

    def initialize_dialectical_pairs(self) -> None:
        """Initialize fundamental dialectical pairs."""
        pairs = [
            ("Being", "Non-Being", "The fundamental ontological duality"),
            ("One", "Many", "Unity versus plurality"),
            ("Same", "Other", "Identity versus difference"),
            ("Mind", "Body", "The psychophysical problem"),
            ("Subject", "Object", "The epistemological divide"),
            ("Freedom", "Determinism", "The question of free will"),
            ("Appearance", "Reality", "The phenomenal versus noumenal"),
            ("Finite", "Infinite", "The bounded versus unbounded"),
            ("Thesis", "Antithesis", "Dialectical opposition leading to synthesis"),
            ("Good", "Evil", "The moral duality"),
        ]

        for positive, negative, description in pairs:
            # Create both concepts
            pos_concept = self.create_concept(
                name=positive,
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole in the {positive}/{negative} duality"
            )
            neg_concept = self.create_concept(
                name=negative,
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole in the {positive}/{negative} duality"
            )

            # Create dialectical relation
            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50  # Balanced opposition
            )

    def demonstrate_philosophical_balance(self) -> dict[str, Any]:
        """
        Demonstrate philosophical balance principles.
        Shows META 50/50 in philosophical thought.
        """
        return {
            "concept": "Philosophical Equilibrium",
            "dialectics": {
                "thesis_antithesis": {
                    "thesis": 50.0,
                    "antithesis": 50.0,
                    "synthesis": "Emerges from balanced opposition",
                    "meaning": "Progress through reconciliation of opposites"
                },
                "being_non_being": {
                    "being": 50.0,
                    "non_being": 50.0,
                    "meaning": "Existence defined against its negation"
                },
                "absolute_relative": {
                    "absolute": 50.0,
                    "relative": 50.0,
                    "meaning": "Truth requires both perspectives"
                }
            },
            "balance_in_ethics": {
                "justice": "Balance of competing interests",
                "virtue": "Mean between extremes (Aristotle)",
                "rights": "Balance of individual and collective"
            },
            "meta_meaning": "Philosophy seeks equilibrium between opposing truths"
        }

    def get_logical_forms(self) -> dict[str, str]:
        """Get basic logical forms."""
        return {
            "modus_ponens": "If P then Q; P; therefore Q",
            "modus_tollens": "If P then Q; not Q; therefore not P",
            "disjunctive_syllogism": "P or Q; not P; therefore Q",
            "hypothetical_syllogism": "If P then Q; if Q then R; therefore if P then R",
            "constructive_dilemma": "(P→Q) ∧ (R→S); P ∨ R; therefore Q ∨ S",
            "reductio_ad_absurdum": "Assume P; derive contradiction; therefore not P",
        }


def create_philosophy_domain(
    meta_equilibrium: MetaEquilibrium | None = None,
    initialize_all: bool = True
) -> PhilosophyDomain:
    """
    Factory function to create a fully initialized philosophy domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized PhilosophyDomain
    """
    domain = PhilosophyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_schools_of_thought()
        domain.initialize_philosophers()
        domain.initialize_thought_experiments()
        domain.initialize_dialectical_pairs()

    return domain
