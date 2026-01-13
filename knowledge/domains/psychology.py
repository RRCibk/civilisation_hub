"""
Psychology Domain
=================
Psychology knowledge domain with META 50/50 equilibrium.
Fundamental duality: Conscious/Unconscious (awareness vs hidden).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class PsychologyDomain(KnowledgeDomain):
    """
    Psychology knowledge domain.

    Fundamental Duality: Conscious / Unconscious
    - Conscious: Awareness, explicit processes, deliberate thought
    - Unconscious: Hidden processes, implicit memory, automatic behavior

    Secondary Dualities:
    - Nature / Nurture
    - Mind / Body
    - Internal / External
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Psychology",
            domain_type=DomainType.FUNDAMENTAL,
            description="The scientific study of mind, behavior, and mental processes",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Conscious/Unconscious duality."""
        self._domain.set_duality(
            positive_name="conscious",
            positive_value=50,
            negative_name="unconscious",
            negative_value=50,
            duality_name="psychology_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental psychological principles."""
        principles = [
            (
                "Psychic Determinism",
                "All mental events have causes",
            ),
            (
                "Behavioral Plasticity",
                "Behavior can be modified through experience",
            ),
            (
                "Individual Differences",
                "People vary systematically in psychological attributes",
            ),
            (
                "Mind-Body Interaction",
                "Mental and physical processes mutually influence each other",
            ),
            (
                "Developmental Continuity",
                "Current behavior reflects developmental history",
            ),
            (
                "Adaptive Function",
                "Psychological processes serve adaptive purposes",
            ),
            (
                "Multiple Determination",
                "Behavior results from multiple interacting factors",
            ),
            (
                "Cognitive Mediation",
                "Thoughts mediate between stimulus and response",
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
        """Get fundamental psychology concepts."""
        return [
            "Mind",
            "Behavior",
            "Cognition",
            "Emotion",
            "Motivation",
            "Perception",
            "Memory",
            "Learning",
            "Personality",
            "Development",
            "Consciousness",
            "Intelligence",
            "Attention",
            "Language",
            "Social Behavior",
        ]

    def initialize_branches(self) -> None:
        """Initialize major psychology branches."""
        branches = [
            (
                "Clinical Psychology",
                "Assessment and treatment of mental disorders",
                ConceptType.THEORY,
            ),
            (
                "Cognitive Psychology",
                "Study of mental processes",
                ConceptType.THEORY,
            ),
            (
                "Developmental Psychology",
                "Study of psychological changes across lifespan",
                ConceptType.THEORY,
            ),
            (
                "Social Psychology",
                "Study of social influences on behavior",
                ConceptType.THEORY,
            ),
            (
                "Neuroscience Psychology",
                "Biological bases of behavior",
                ConceptType.THEORY,
            ),
            (
                "Industrial-Organizational",
                "Psychology in workplace settings",
                ConceptType.THEORY,
            ),
            (
                "Educational Psychology",
                "Psychology of learning and teaching",
                ConceptType.THEORY,
            ),
            (
                "Health Psychology",
                "Psychological factors in health and illness",
                ConceptType.THEORY,
            ),
            (
                "Forensic Psychology",
                "Psychology in legal contexts",
                ConceptType.THEORY,
            ),
            (
                "Positive Psychology",
                "Study of human flourishing",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_theories(self) -> None:
        """Initialize major psychological theories."""
        theories = [
            ("Psychoanalytic Theory", "Freud", "Unconscious drives behavior"),
            ("Behaviorism", "Watson/Skinner", "Observable behavior focus"),
            ("Humanistic Psychology", "Maslow/Rogers", "Self-actualization emphasis"),
            ("Cognitive Theory", "Piaget/Beck", "Mental processes focus"),
            ("Evolutionary Psychology", "Cosmides/Tooby", "Adaptive mechanisms"),
            ("Social Learning Theory", "Bandura", "Observational learning"),
            ("Attachment Theory", "Bowlby/Ainsworth", "Early relationships"),
            ("Information Processing", "Atkinson/Shiffrin", "Mind as computer"),
        ]

        for name, founder, description in theories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_mental_processes(self) -> None:
        """Initialize mental process types."""
        processes = [
            ("Perception", "Organizing sensory information", "Bottom-up/Top-down"),
            ("Attention", "Selective focus of awareness", "Selective/Divided"),
            ("Memory", "Encoding, storage, retrieval", "Short-term/Long-term"),
            ("Thinking", "Manipulation of mental representations", "Convergent/Divergent"),
            ("Language", "Symbolic communication system", "Receptive/Expressive"),
            ("Problem Solving", "Moving toward goals", "Algorithmic/Heuristic"),
            ("Decision Making", "Choosing among alternatives", "Rational/Emotional"),
        ]

        for name, description, types in processes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["types"] = types

    def initialize_disorders(self) -> None:
        """Initialize psychological disorder categories."""
        disorders = [
            ("Anxiety Disorders", "Excessive fear and worry", "GAD, Phobias, Panic"),
            ("Mood Disorders", "Disturbances in emotion", "Depression, Bipolar"),
            ("Psychotic Disorders", "Loss of contact with reality", "Schizophrenia"),
            ("Personality Disorders", "Enduring maladaptive patterns", "BPD, NPD"),
            ("Neurodevelopmental", "Early developmental impairments", "ADHD, ASD"),
            ("Trauma Disorders", "Response to traumatic events", "PTSD, ASD"),
        ]

        for name, description, examples in disorders:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_psychological_pairs(self) -> None:
        """Initialize fundamental psychological pairs with META 50/50 balance."""
        pairs = [
            ("Conscious", "Unconscious", "Aware vs hidden"),
            ("Nature", "Nurture", "Innate vs learned"),
            ("Mind", "Body", "Mental vs physical"),
            ("Internal", "External", "Inside vs outside"),
            ("Cognition", "Emotion", "Thinking vs feeling"),
            ("Explicit", "Implicit", "Deliberate vs automatic"),
            ("Approach", "Avoidance", "Toward vs away"),
            ("Excitation", "Inhibition", "Activation vs suppression"),
            ("Assimilation", "Accommodation", "Fit in vs adjust"),
            ("Encoding", "Retrieval", "Store vs recall"),
            ("Short-term", "Long-term", "Temporary vs permanent"),
            ("Bottom-up", "Top-down", "Data vs concept driven"),
            ("Intrinsic", "Extrinsic", "Internal vs external motivation"),
            ("Fixed", "Growth", "Static vs changeable mindset"),
            ("Attachment", "Separation", "Bond vs detach"),
            ("Ego", "Id", "Reality vs pleasure principle"),
            ("Reinforcement", "Punishment", "Increase vs decrease behavior"),
            ("Classical", "Operant", "Association vs consequence"),
            ("State", "Trait", "Temporary vs enduring"),
            ("Normal", "Abnormal", "Typical vs atypical"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Psychology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Psychology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_defense_mechanisms(self) -> dict[str, str]:
        """Get Freudian defense mechanisms."""
        return {
            "repression": "Pushing threatening thoughts to unconscious",
            "denial": "Refusing to accept reality",
            "projection": "Attributing own feelings to others",
            "displacement": "Redirecting emotions to safer target",
            "rationalization": "Creating logical explanations for behavior",
            "sublimation": "Channeling impulses into acceptable activities",
            "regression": "Returning to earlier developmental stage",
        }

    def demonstrate_psychology_balance(self) -> dict[str, Any]:
        """Demonstrate psychology balance principles."""
        return {
            "concept": "Psychology Equilibrium",
            "dualities": {
                "conscious_unconscious": {
                    "conscious": 50.0,
                    "unconscious": 50.0,
                    "meaning": "Mind operates at both levels simultaneously",
                },
                "nature_nurture": {
                    "nature": 50.0,
                    "nurture": 50.0,
                    "meaning": "Genes and environment equally shape behavior",
                },
                "cognition_emotion": {
                    "cognition": 50.0,
                    "emotion": 50.0,
                    "meaning": "Thinking and feeling are intertwined",
                },
            },
            "therapeutic_balance": {
                "insight": 50.0,
                "behavior_change": 50.0,
                "description": "Understanding and action both required for healing",
            },
            "meta_meaning": "Psychology demonstrates META 50/50 in mind-body duality",
        }


def create_psychology_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> PsychologyDomain:
    """
    Factory function to create a fully initialized psychology domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized PsychologyDomain
    """
    domain = PsychologyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_theories()
        domain.initialize_mental_processes()
        domain.initialize_disorders()
        domain.initialize_psychological_pairs()

    return domain
