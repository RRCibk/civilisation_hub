"""
Cognitive Science Domain
========================
Cognitive science knowledge domain with META 50/50 equilibrium.
Fundamental duality: Mind/Brain (mental vs physical).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class CognitiveScienceDomain(KnowledgeDomain):
    """
    Cognitive Science knowledge domain.

    Fundamental Duality: Mind / Brain
    - Mind: Mental processes, cognition, representations
    - Brain: Neural substrate, physical implementation

    Secondary Dualities:
    - Symbolic / Connectionist
    - Innate / Learned
    - Conscious / Unconscious
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="CognitiveScience",
            domain_type=DomainType.FUNDAMENTAL,
            description="The interdisciplinary study of mind and intelligence",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Mind/Brain duality."""
        self._domain.set_duality(
            positive_name="mind",
            positive_value=50,
            negative_name="brain",
            negative_value=50,
            duality_name="cognitive_science_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental cognitive science principles."""
        principles = [
            (
                "Computational Mind",
                "Mind as information processing system",
            ),
            (
                "Representation",
                "Cognition involves mental representations",
            ),
            (
                "Modularity",
                "Mind has specialized processing modules",
            ),
            (
                "Embodiment",
                "Cognition shaped by body and environment",
            ),
            (
                "Interdisciplinarity",
                "Multiple disciplines needed for understanding",
            ),
            (
                "Levels of Analysis",
                "Computational, algorithmic, implementation levels",
            ),
            (
                "Cognitive Architecture",
                "Mind has organized structure",
            ),
            (
                "Bounded Rationality",
                "Cognition operates within limits",
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
        """Get fundamental cognitive science concepts."""
        return [
            "Cognition",
            "Mind",
            "Brain",
            "Representation",
            "Computation",
            "Memory",
            "Attention",
            "Perception",
            "Language",
            "Reasoning",
            "Learning",
            "Consciousness",
            "Intelligence",
            "Emotion",
            "Decision",
        ]

    def initialize_branches(self) -> None:
        """Initialize major cognitive science branches."""
        branches = [
            (
                "Cognitive Psychology",
                "Experimental study of cognition",
                ConceptType.THEORY,
            ),
            (
                "Cognitive Neuroscience",
                "Neural basis of cognition",
                ConceptType.THEORY,
            ),
            (
                "Artificial Intelligence",
                "Machine cognition",
                ConceptType.THEORY,
            ),
            (
                "Linguistics",
                "Language and mind",
                ConceptType.THEORY,
            ),
            (
                "Philosophy of Mind",
                "Nature of mental states",
                ConceptType.THEORY,
            ),
            (
                "Cognitive Anthropology",
                "Culture and cognition",
                ConceptType.THEORY,
            ),
            (
                "Developmental Cognition",
                "Cognitive development",
                ConceptType.THEORY,
            ),
            (
                "Computational Modeling",
                "Formal models of cognition",
                ConceptType.THEORY,
            ),
            (
                "Cognitive Linguistics",
                "Language and thought",
                ConceptType.THEORY,
            ),
            (
                "Embodied Cognition",
                "Body-mind interaction",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_cognitive_processes(self) -> None:
        """Initialize cognitive processes."""
        processes = [
            ("Perception", "Sensory processing", "Input"),
            ("Attention", "Selective focus", "Filter"),
            ("Memory", "Information storage", "Storage"),
            ("Language", "Symbolic communication", "Communication"),
            ("Reasoning", "Logical inference", "Processing"),
            ("Decision Making", "Choice selection", "Output"),
        ]

        for name, description, function in processes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["function"] = function

    def initialize_theories(self) -> None:
        """Initialize cognitive theories."""
        theories = [
            ("Computational Theory", "Marr", "Mind as computation"),
            ("Connectionism", "Rumelhart", "Neural network models"),
            ("Embodied Cognition", "Varela", "Body shapes mind"),
            ("Dual Process", "Kahneman", "System 1 and System 2"),
            ("Global Workspace", "Baars", "Consciousness theory"),
            ("Predictive Processing", "Clark", "Brain as prediction machine"),
        ]

        for name, theorist, description in theories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["theorist"] = theorist

    def initialize_cogsci_pairs(self) -> None:
        """Initialize fundamental cognitive science pairs with META 50/50 balance."""
        pairs = [
            ("Mind", "Brain", "Mental vs physical"),
            ("Symbolic", "Connectionist", "Rules vs networks"),
            ("Innate", "Learned", "Nature vs nurture"),
            ("Conscious", "Unconscious", "Aware vs automatic"),
            ("Serial", "Parallel", "Sequential vs simultaneous"),
            ("Top-Down", "Bottom-Up", "Concept vs data driven"),
            ("Modular", "Distributed", "Localized vs spread"),
            ("Embodied", "Disembodied", "Body vs abstract"),
            ("Rational", "Emotional", "Logic vs feeling"),
            ("Implicit", "Explicit", "Automatic vs deliberate"),
            ("Domain-General", "Domain-Specific", "Universal vs specialized"),
            ("Representation", "Process", "Structure vs operation"),
            ("Competence", "Performance", "Ability vs behavior"),
            ("Central", "Peripheral", "Core vs edge processing"),
            ("Declarative", "Procedural", "Knowing that vs knowing how"),
            ("Automatic", "Controlled", "Effortless vs effortful"),
            ("Abstract", "Concrete", "General vs specific"),
            ("Individual", "Social", "Personal vs shared cognition"),
            ("Online", "Offline", "Real-time vs reflective"),
            ("Natural", "Artificial", "Human vs machine"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (CogSci)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (CogSci)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_marr_levels(self) -> dict[str, str]:
        """Get Marr's levels of analysis."""
        return {
            "computational": "What is computed and why",
            "algorithmic": "How is it computed",
            "implementational": "Physical realization",
        }

    def demonstrate_cogsci_balance(self) -> dict[str, Any]:
        """Demonstrate cognitive science balance principles."""
        return {
            "concept": "Cognitive Science Equilibrium",
            "dualities": {
                "mind_brain": {
                    "mind": 50.0,
                    "brain": 50.0,
                    "meaning": "Mental and neural equally important",
                },
                "symbolic_connectionist": {
                    "symbolic": 50.0,
                    "connectionist": 50.0,
                    "meaning": "Both paradigms offer insights",
                },
                "innate_learned": {
                    "innate": 50.0,
                    "learned": 50.0,
                    "meaning": "Nature and nurture both contribute",
                },
            },
            "processing_balance": {
                "top_down": 50.0,
                "bottom_up": 50.0,
                "description": "Concept and data driven processing",
            },
            "meta_meaning": "Cognitive Science demonstrates META 50/50 in mind-brain unity",
        }


def create_cognitive_science_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> CognitiveScienceDomain:
    """
    Factory function to create a fully initialized cognitive science domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized CognitiveScienceDomain
    """
    domain = CognitiveScienceDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_cognitive_processes()
        domain.initialize_theories()
        domain.initialize_cogsci_pairs()

    return domain
