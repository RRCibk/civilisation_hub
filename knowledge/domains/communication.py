"""
Communication Domain
====================
Communication knowledge domain with META 50/50 equilibrium.
Fundamental duality: Sender/Receiver (encoder vs decoder).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class CommunicationDomain(KnowledgeDomain):
    """
    Communication knowledge domain.

    Fundamental Duality: Sender / Receiver
    - Sender: Encoder, source, transmitter
    - Receiver: Decoder, destination, audience

    Secondary Dualities:
    - Verbal / Nonverbal
    - Mass / Interpersonal
    - Content / Relationship
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Communication",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of information exchange between entities",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Sender/Receiver duality."""
        self._domain.set_duality(
            positive_name="sender",
            positive_value=50,
            negative_name="receiver",
            negative_value=50,
            duality_name="communication_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental communication principles."""
        principles = [
            (
                "One Cannot Not Communicate",
                "All behavior is communication",
            ),
            (
                "Content and Relationship",
                "Communication has content and relational aspects",
            ),
            (
                "Punctuation",
                "Sequence of communication is negotiated",
            ),
            (
                "Digital and Analogic",
                "Communication uses verbal and nonverbal codes",
            ),
            (
                "Symmetric and Complementary",
                "Interactions can be equal or differentiated",
            ),
            (
                "Feedback Loop",
                "Communication is circular, not linear",
            ),
            (
                "Noise",
                "All communication involves potential distortion",
            ),
            (
                "Context Dependency",
                "Meaning depends on context",
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
        """Get fundamental communication concepts."""
        return [
            "Message",
            "Channel",
            "Sender",
            "Receiver",
            "Encoding",
            "Decoding",
            "Feedback",
            "Noise",
            "Context",
            "Medium",
            "Symbol",
            "Meaning",
            "Audience",
            "Rhetoric",
            "Persuasion",
        ]

    def initialize_branches(self) -> None:
        """Initialize major communication branches."""
        branches = [
            (
                "Mass Communication",
                "Communication to large audiences",
                ConceptType.THEORY,
            ),
            (
                "Interpersonal Communication",
                "Communication between individuals",
                ConceptType.THEORY,
            ),
            (
                "Organizational Communication",
                "Communication in organizations",
                ConceptType.THEORY,
            ),
            (
                "Intercultural Communication",
                "Communication across cultures",
                ConceptType.THEORY,
            ),
            (
                "Political Communication",
                "Communication in political contexts",
                ConceptType.THEORY,
            ),
            (
                "Health Communication",
                "Communication about health",
                ConceptType.THEORY,
            ),
            (
                "Media Studies",
                "Analysis of media content and effects",
                ConceptType.THEORY,
            ),
            (
                "Rhetoric",
                "Art of persuasive communication",
                ConceptType.THEORY,
            ),
            (
                "Journalism",
                "News gathering and reporting",
                ConceptType.THEORY,
            ),
            (
                "Public Relations",
                "Managing public perception",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_theories(self) -> None:
        """Initialize communication theories."""
        theories = [
            ("Shannon-Weaver Model", "Shannon", "Mathematical communication model"),
            ("Uses and Gratifications", "Katz", "Audience uses media for needs"),
            ("Agenda Setting", "McCombs", "Media tells us what to think about"),
            ("Cultivation Theory", "Gerbner", "TV shapes worldview"),
            ("Social Penetration", "Altman", "Self-disclosure deepens relations"),
            ("Uncertainty Reduction", "Berger", "Communication reduces uncertainty"),
            ("Symbolic Interactionism", "Mead", "Meaning through symbols"),
            ("Framing Theory", "Goffman", "How issues are presented"),
        ]

        for name, founder, description in theories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_media_types(self) -> None:
        """Initialize media types."""
        media = [
            ("Print Media", "Written, published material", "Newspapers, books"),
            ("Broadcast Media", "Radio and television", "Audio/visual transmission"),
            ("Digital Media", "Internet-based communication", "Websites, social media"),
            ("Social Media", "User-generated platforms", "Facebook, Twitter"),
            ("Traditional Media", "Legacy media forms", "Newspapers, TV, radio"),
            ("New Media", "Interactive digital media", "Internet, mobile"),
        ]

        for name, description, examples in media:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_communication_models(self) -> None:
        """Initialize communication models."""
        models = [
            ("Linear Model", "One-way transmission", "Shannon-Weaver"),
            ("Interactive Model", "Two-way with feedback", "Schramm"),
            ("Transactional Model", "Simultaneous exchange", "Barnlund"),
            ("Ritual Model", "Shared meaning creation", "Carey"),
        ]

        for name, description, example in models:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.MODEL,
                description=description,
            )
            concept.metadata["example"] = example

    def initialize_communication_pairs(self) -> None:
        """Initialize fundamental communication pairs with META 50/50 balance."""
        pairs = [
            ("Sender", "Receiver", "Encoder vs decoder"),
            ("Verbal", "Nonverbal", "Words vs gestures"),
            ("Mass", "Interpersonal", "Many vs few"),
            ("Content", "Relationship", "What vs how"),
            ("Encoding", "Decoding", "Creating vs interpreting"),
            ("Signal", "Noise", "Message vs interference"),
            ("Synchronous", "Asynchronous", "Same vs different time"),
            ("Mediated", "Face-to-face", "Indirect vs direct"),
            ("Public", "Private", "Open vs closed"),
            ("Formal", "Informal", "Official vs casual"),
            ("One-way", "Two-way", "Monologue vs dialogue"),
            ("Intrapersonal", "Interpersonal", "Self vs other"),
            ("Persuasion", "Information", "Influence vs inform"),
            ("Speaker", "Listener", "Talker vs hearer"),
            ("Production", "Reception", "Making vs consuming"),
            ("Explicit", "Implicit", "Stated vs implied"),
            ("Intended", "Unintended", "Planned vs accidental"),
            ("Active", "Passive", "Engaged vs receptive"),
            ("Linear", "Circular", "Sequential vs feedback"),
            ("Digital", "Analog", "Discrete vs continuous"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Communication)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Communication)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_lasswell_model(self) -> dict[str, str]:
        """Get Lasswell's communication model."""
        return {
            "who": "Sender analysis",
            "says_what": "Content analysis",
            "in_which_channel": "Media analysis",
            "to_whom": "Audience analysis",
            "with_what_effect": "Effect analysis",
        }

    def demonstrate_communication_balance(self) -> dict[str, Any]:
        """Demonstrate communication balance principles."""
        return {
            "concept": "Communication Equilibrium",
            "dualities": {
                "sender_receiver": {
                    "sender": 50.0,
                    "receiver": 50.0,
                    "meaning": "Communication requires both equally",
                },
                "content_relationship": {
                    "content": 50.0,
                    "relationship": 50.0,
                    "meaning": "What is said and how are equally important",
                },
                "encoding_decoding": {
                    "encoding": 50.0,
                    "decoding": 50.0,
                    "meaning": "Creation and interpretation are complementary",
                },
            },
            "transactional_balance": {
                "transmission": 50.0,
                "reception": 50.0,
                "description": "Communication is simultaneous exchange",
            },
            "meta_meaning": "Communication demonstrates META 50/50 in sender-receiver symmetry",
        }


def create_communication_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> CommunicationDomain:
    """
    Factory function to create a fully initialized communication domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized CommunicationDomain
    """
    domain = CommunicationDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_theories()
        domain.initialize_media_types()
        domain.initialize_communication_models()
        domain.initialize_communication_pairs()

    return domain
