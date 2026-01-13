"""
Artificial Intelligence Domain
==============================
Artificial intelligence knowledge domain with META 50/50 equilibrium.
Fundamental duality: Symbolic/Connectionist (logic vs learning).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class ArtificialIntelligenceDomain(KnowledgeDomain):
    """
    Artificial Intelligence knowledge domain.

    Fundamental Duality: Symbolic / Connectionist
    - Symbolic: Logic, rules, explicit knowledge
    - Connectionist: Neural networks, learning, implicit knowledge

    Secondary Dualities:
    - Narrow / General
    - Supervised / Unsupervised
    - Model / Data
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="ArtificialIntelligence",
            domain_type=DomainType.FUNDAMENTAL,
            description="The creation of intelligent machines and systems",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Symbolic/Connectionist duality."""
        self._domain.set_duality(
            positive_name="symbolic",
            positive_value=50,
            negative_name="connectionist",
            negative_value=50,
            duality_name="ai_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental AI principles."""
        principles = [
            (
                "Intelligence is Computable",
                "Intelligence can be implemented in machines",
            ),
            (
                "No Free Lunch",
                "No algorithm is best for all problems",
            ),
            (
                "Occam's Razor",
                "Prefer simpler explanations",
            ),
            (
                "Bias-Variance Tradeoff",
                "Balance model complexity",
            ),
            (
                "Representation Matters",
                "How data is represented affects learning",
            ),
            (
                "Data is Essential",
                "Quality data drives performance",
            ),
            (
                "Generalization",
                "Goal is to perform on unseen data",
            ),
            (
                "Interpretability",
                "Understanding decisions is important",
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
        """Get fundamental AI concepts."""
        return [
            "Intelligence",
            "Learning",
            "Knowledge",
            "Reasoning",
            "Perception",
            "Model",
            "Training",
            "Inference",
            "Neural Network",
            "Algorithm",
            "Data",
            "Feature",
            "Optimization",
            "Generalization",
            "Agent",
        ]

    def initialize_branches(self) -> None:
        """Initialize major AI branches."""
        branches = [
            (
                "Machine Learning",
                "Learning from data",
                ConceptType.THEORY,
            ),
            (
                "Deep Learning",
                "Neural network architectures",
                ConceptType.THEORY,
            ),
            (
                "Natural Language Processing",
                "Language understanding",
                ConceptType.THEORY,
            ),
            (
                "Computer Vision",
                "Visual understanding",
                ConceptType.THEORY,
            ),
            (
                "Reinforcement Learning",
                "Learning from interaction",
                ConceptType.THEORY,
            ),
            (
                "Knowledge Representation",
                "Encoding knowledge",
                ConceptType.THEORY,
            ),
            (
                "Planning",
                "Action sequencing",
                ConceptType.THEORY,
            ),
            (
                "Expert Systems",
                "Domain-specific reasoning",
                ConceptType.THEORY,
            ),
            (
                "Robotics AI",
                "Intelligent robots",
                ConceptType.THEORY,
            ),
            (
                "Multi-Agent Systems",
                "Multiple AI agents",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_paradigms(self) -> None:
        """Initialize AI learning paradigms."""
        paradigms = [
            ("Supervised Learning", "Labeled training data", "Classification"),
            ("Unsupervised Learning", "No labels", "Clustering"),
            ("Reinforcement Learning", "Reward signals", "Control"),
            ("Semi-Supervised", "Partial labels", "Hybrid"),
            ("Self-Supervised", "Self-generated labels", "Pretraining"),
            ("Transfer Learning", "Knowledge transfer", "Adaptation"),
        ]

        for name, description, application in paradigms:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["application"] = application

    def initialize_architectures(self) -> None:
        """Initialize neural network architectures."""
        architectures = [
            ("MLP", "Multi-layer perceptron", "Basic"),
            ("CNN", "Convolutional neural network", "Vision"),
            ("RNN", "Recurrent neural network", "Sequences"),
            ("Transformer", "Attention-based", "Language"),
            ("GAN", "Generative adversarial network", "Generation"),
            ("Autoencoder", "Encoding-decoding", "Representation"),
        ]

        for name, description, application in architectures:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["application"] = application

    def initialize_ai_pairs(self) -> None:
        """Initialize fundamental AI pairs with META 50/50 balance."""
        pairs = [
            ("Symbolic", "Connectionist", "Logic vs learning"),
            ("Narrow", "General", "Specific vs broad"),
            ("Supervised", "Unsupervised", "Labeled vs unlabeled"),
            ("Model", "Data", "Algorithm vs information"),
            ("Training", "Inference", "Learning vs applying"),
            ("Bias", "Variance", "Underfitting vs overfitting"),
            ("Exploration", "Exploitation", "Try new vs use known"),
            ("Accuracy", "Interpretability", "Performance vs understanding"),
            ("Local", "Global", "Nearby vs overall"),
            ("Online", "Batch", "Incremental vs all-at-once"),
            ("Discriminative", "Generative", "Classify vs generate"),
            ("Parametric", "Non-parametric", "Fixed vs flexible"),
            ("Shallow", "Deep", "Few vs many layers"),
            ("Dense", "Sparse", "Full vs selective"),
            ("Deterministic", "Stochastic", "Certain vs random"),
            ("Sequential", "Parallel", "Serial vs concurrent"),
            ("Reactive", "Deliberative", "Quick vs planned"),
            ("Black Box", "White Box", "Opaque vs transparent"),
            ("Human", "Machine", "Natural vs artificial"),
            ("Narrow", "Broad", "Task-specific vs general purpose"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (AI)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (AI)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_turing_test(self) -> dict[str, str]:
        """Get Turing test components."""
        return {
            "imitation_game": "Can machine imitate human?",
            "interrogator": "Human judge asks questions",
            "machine": "AI attempts to respond like human",
            "criterion": "Indistinguishable from human",
        }

    def demonstrate_ai_balance(self) -> dict[str, Any]:
        """Demonstrate AI balance principles."""
        return {
            "concept": "AI Equilibrium",
            "dualities": {
                "symbolic_connectionist": {
                    "symbolic": 50.0,
                    "connectionist": 50.0,
                    "meaning": "Both logic and learning are valuable",
                },
                "model_data": {
                    "model": 50.0,
                    "data": 50.0,
                    "meaning": "Algorithms and data equally important",
                },
                "bias_variance": {
                    "bias": 50.0,
                    "variance": 50.0,
                    "meaning": "Balance simplicity and complexity",
                },
            },
            "learning_balance": {
                "training": 50.0,
                "inference": 50.0,
                "description": "Learning and applying knowledge",
            },
            "meta_meaning": "AI demonstrates META 50/50 in symbolic-connectionist synthesis",
        }


def create_artificial_intelligence_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> ArtificialIntelligenceDomain:
    """
    Factory function to create a fully initialized AI domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized ArtificialIntelligenceDomain
    """
    domain = ArtificialIntelligenceDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_paradigms()
        domain.initialize_architectures()
        domain.initialize_ai_pairs()

    return domain
