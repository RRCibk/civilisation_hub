"""
Rhetoric Domain
===============
Rhetoric knowledge domain with META 50/50 equilibrium.
Fundamental duality: Logos/Pathos (reason vs emotion).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class RhetoricDomain(KnowledgeDomain):
    """
    Rhetoric knowledge domain.

    Fundamental Duality: Logos / Pathos
    - Logos: Reason, logic, argument
    - Pathos: Emotion, feeling, passion

    Secondary Dualities:
    - Ethos / Logos
    - Persuasion / Information
    - Speaker / Audience
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Rhetoric",
            domain_type=DomainType.FUNDAMENTAL,
            description="The art of persuasion through effective communication",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Logos/Pathos duality."""
        self._domain.set_duality(
            positive_name="logos",
            positive_value=50,
            negative_name="pathos",
            negative_value=50,
            duality_name="rhetoric_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental rhetorical principles."""
        principles = [
            (
                "Kairos",
                "The right moment for persuasion",
            ),
            (
                "Decorum",
                "Appropriateness to context",
            ),
            (
                "Audience Adaptation",
                "Message shaped for receivers",
            ),
            (
                "Artistic Proofs",
                "Ethos, pathos, logos work together",
            ),
            (
                "Arrangement",
                "Order affects persuasiveness",
            ),
            (
                "Style",
                "How something is said matters",
            ),
            (
                "Memory",
                "Internalization enables delivery",
            ),
            (
                "Delivery",
                "Presentation affects reception",
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
        """Get fundamental rhetoric concepts."""
        return [
            "Persuasion",
            "Argument",
            "Audience",
            "Speaker",
            "Ethos",
            "Pathos",
            "Logos",
            "Style",
            "Arrangement",
            "Invention",
            "Delivery",
            "Figure",
            "Trope",
            "Discourse",
            "Context",
        ]

    def initialize_branches(self) -> None:
        """Initialize major rhetoric branches."""
        branches = [
            (
                "Classical Rhetoric",
                "Greek and Roman tradition",
                ConceptType.THEORY,
            ),
            (
                "New Rhetoric",
                "20th century revival",
                ConceptType.THEORY,
            ),
            (
                "Visual Rhetoric",
                "Persuasion through images",
                ConceptType.THEORY,
            ),
            (
                "Digital Rhetoric",
                "Online persuasion",
                ConceptType.THEORY,
            ),
            (
                "Political Rhetoric",
                "Rhetoric in politics",
                ConceptType.THEORY,
            ),
            (
                "Legal Rhetoric",
                "Courtroom persuasion",
                ConceptType.THEORY,
            ),
            (
                "Composition Studies",
                "Teaching writing",
                ConceptType.THEORY,
            ),
            (
                "Rhetorical Criticism",
                "Analysis of rhetoric",
                ConceptType.THEORY,
            ),
            (
                "Public Address",
                "Speech-making",
                ConceptType.THEORY,
            ),
            (
                "Argumentation Theory",
                "Structure of arguments",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_canons(self) -> None:
        """Initialize the five canons of rhetoric."""
        canons = [
            ("Invention", "Finding arguments", "Discovery of content"),
            ("Arrangement", "Organizing arguments", "Structure"),
            ("Style", "Language choices", "Diction, figures"),
            ("Memory", "Internalization", "Recall"),
            ("Delivery", "Presentation", "Voice, gesture"),
        ]

        for name, description, aspect in canons:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["aspect"] = aspect

    def initialize_appeals(self) -> None:
        """Initialize rhetorical appeals."""
        appeals = [
            ("Ethos", "Credibility of speaker", "Character, authority"),
            ("Pathos", "Emotional appeal", "Feelings, values"),
            ("Logos", "Logical appeal", "Reason, evidence"),
            ("Kairos", "Timeliness", "Right moment"),
        ]

        for name, description, basis in appeals:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["basis"] = basis

    def initialize_figures(self) -> None:
        """Initialize rhetorical figures."""
        figures = [
            ("Metaphor", "Implicit comparison", "Life is a journey"),
            ("Anaphora", "Repetition at start", "I have a dream..."),
            ("Antithesis", "Contrasting ideas", "Ask not what..."),
            ("Chiasmus", "Reversed structure", "JFK reversal"),
            ("Hyperbole", "Exaggeration", "Emphasis"),
            ("Irony", "Opposite meaning", "Verbal irony"),
        ]

        for name, description, example in figures:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["example"] = example

    def initialize_rhetoric_pairs(self) -> None:
        """Initialize fundamental rhetorical pairs with META 50/50 balance."""
        pairs = [
            ("Logos", "Pathos", "Reason vs emotion"),
            ("Ethos", "Logos", "Character vs argument"),
            ("Persuasion", "Information", "Convince vs inform"),
            ("Speaker", "Audience", "Sender vs receiver"),
            ("Invention", "Arrangement", "Finding vs organizing"),
            ("Style", "Substance", "How vs what"),
            ("Written", "Oral", "Text vs speech"),
            ("Deliberative", "Forensic", "Future vs past"),
            ("Epideictic", "Deliberative", "Praise vs policy"),
            ("Formal", "Informal", "Official vs casual"),
            ("Explicit", "Implicit", "Stated vs implied"),
            ("Literal", "Figurative", "Plain vs decorated"),
            ("High Style", "Low Style", "Grand vs plain"),
            ("Deductive", "Inductive", "General to specific vs reverse"),
            ("Thesis", "Antithesis", "Claim vs counter"),
            ("Analysis", "Synthesis", "Breaking down vs building up"),
            ("Concise", "Elaborate", "Brief vs detailed"),
            ("Direct", "Indirect", "Straightforward vs circuitous"),
            ("Assertion", "Question", "Statement vs inquiry"),
            ("Attack", "Defense", "Offense vs response"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Rhetoric)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Rhetoric)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_aristotle_appeals(self) -> dict[str, str]:
        """Get Aristotle's three appeals."""
        return {
            "ethos": "Appeal to speaker's credibility and character",
            "pathos": "Appeal to audience's emotions",
            "logos": "Appeal to logic and reason",
        }

    def demonstrate_rhetoric_balance(self) -> dict[str, Any]:
        """Demonstrate rhetoric balance principles."""
        return {
            "concept": "Rhetoric Equilibrium",
            "dualities": {
                "logos_pathos": {
                    "logos": 50.0,
                    "pathos": 50.0,
                    "meaning": "Effective persuasion uses both reason and emotion",
                },
                "speaker_audience": {
                    "speaker": 50.0,
                    "audience": 50.0,
                    "meaning": "Communication requires both parties",
                },
                "form_content": {
                    "form": 50.0,
                    "content": 50.0,
                    "meaning": "How and what both persuade",
                },
            },
            "appeals_balance": {
                "ethos": 33.3,
                "pathos": 33.3,
                "logos": 33.3,
                "description": "Three appeals work together",
            },
            "meta_meaning": "Rhetoric demonstrates META 50/50 in logos-pathos synthesis",
        }


def create_rhetoric_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> RhetoricDomain:
    """
    Factory function to create a fully initialized rhetoric domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized RhetoricDomain
    """
    domain = RhetoricDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_canons()
        domain.initialize_appeals()
        domain.initialize_figures()
        domain.initialize_rhetoric_pairs()

    return domain
