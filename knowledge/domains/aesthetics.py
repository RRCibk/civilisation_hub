"""
Aesthetics Domain
=================
Aesthetics knowledge domain with META 50/50 equilibrium.
Fundamental duality: Beautiful/Ugly (pleasing vs displeasing).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class AestheticsDomain(KnowledgeDomain):
    """
    Aesthetics knowledge domain.

    Fundamental Duality: Beautiful / Ugly
    - Beautiful: Pleasing, harmonious, excellent
    - Ugly: Displeasing, discordant, deficient

    Secondary Dualities:
    - Sublime / Mundane
    - Art / Nature
    - Form / Content
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Aesthetics",
            domain_type=DomainType.FUNDAMENTAL,
            description="The philosophy of beauty, art, and aesthetic experience",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Beautiful/Ugly duality."""
        self._domain.set_duality(
            positive_name="beautiful",
            positive_value=50,
            negative_name="ugly",
            negative_value=50,
            duality_name="aesthetics_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental aesthetic principles."""
        principles = [
            (
                "Disinterestedness",
                "Aesthetic judgment free from practical interest",
            ),
            (
                "Universality",
                "Beauty claims universal validity",
            ),
            (
                "Purposiveness Without Purpose",
                "Art appears designed but serves no function",
            ),
            (
                "Free Play",
                "Aesthetic experience involves imagination and understanding",
            ),
            (
                "Significant Form",
                "Form itself carries aesthetic value",
            ),
            (
                "Expression",
                "Art expresses and communicates feeling",
            ),
            (
                "Mimesis",
                "Art imitates nature or reality",
            ),
            (
                "Aesthetic Autonomy",
                "Art has intrinsic value",
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
        """Get fundamental aesthetics concepts."""
        return [
            "Beauty",
            "Art",
            "Taste",
            "Sublime",
            "Form",
            "Expression",
            "Representation",
            "Imagination",
            "Emotion",
            "Pleasure",
            "Judgment",
            "Value",
            "Style",
            "Meaning",
            "Experience",
        ]

    def initialize_branches(self) -> None:
        """Initialize major aesthetics branches."""
        branches = [
            (
                "Philosophy of Art",
                "Nature and definition of art",
                ConceptType.THEORY,
            ),
            (
                "Theory of Beauty",
                "Nature of the beautiful",
                ConceptType.THEORY,
            ),
            (
                "Philosophy of Music",
                "Aesthetics of musical experience",
                ConceptType.THEORY,
            ),
            (
                "Philosophy of Literature",
                "Aesthetics of literary works",
                ConceptType.THEORY,
            ),
            (
                "Film Aesthetics",
                "Aesthetics of cinema",
                ConceptType.THEORY,
            ),
            (
                "Environmental Aesthetics",
                "Aesthetics of nature",
                ConceptType.THEORY,
            ),
            (
                "Everyday Aesthetics",
                "Beauty in ordinary life",
                ConceptType.THEORY,
            ),
            (
                "Neuroaesthetics",
                "Brain science of aesthetic experience",
                ConceptType.THEORY,
            ),
            (
                "Cross-Cultural Aesthetics",
                "Aesthetics across cultures",
                ConceptType.THEORY,
            ),
            (
                "Digital Aesthetics",
                "Aesthetics of digital media",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_theories(self) -> None:
        """Initialize aesthetic theories."""
        theories = [
            ("Formalism", "Bell", "Significant form is key"),
            ("Expressionism", "Collingwood", "Art expresses emotion"),
            ("Institutionalism", "Dickie", "Art world defines art"),
            ("Functionalism", "Beardsley", "Aesthetic experience is function"),
            ("Historical Definition", "Levinson", "Art relates to art history"),
            ("Cluster Theory", "Gaut", "Family resemblance"),
        ]

        for name, founder, description in theories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_aesthetic_categories(self) -> None:
        """Initialize aesthetic categories."""
        categories = [
            ("Beautiful", "Pleasing, harmonious", "Classic ideal"),
            ("Sublime", "Overwhelming, awe-inspiring", "Burke, Kant"),
            ("Picturesque", "Charmingly irregular", "Gilpin"),
            ("Grotesque", "Bizarre, distorted", "Hugo"),
            ("Kitsch", "Tasteless, sentimental", "Mass culture"),
            ("Camp", "Ironic appreciation", "Sontag"),
        ]

        for name, description, context in categories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["context"] = context

    def initialize_aesthetic_properties(self) -> None:
        """Initialize aesthetic properties."""
        properties = [
            ("Unity", "Coherence of parts", "Formal"),
            ("Complexity", "Richness of elements", "Formal"),
            ("Intensity", "Vividness of effect", "Expressive"),
            ("Balance", "Equilibrium of elements", "Formal"),
            ("Elegance", "Graceful simplicity", "Formal"),
        ]

        for name, description, category in properties:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_aesthetic_pairs(self) -> None:
        """Initialize fundamental aesthetic pairs with META 50/50 balance."""
        pairs = [
            ("Beautiful", "Ugly", "Pleasing vs displeasing"),
            ("Sublime", "Mundane", "Overwhelming vs ordinary"),
            ("Art", "Nature", "Made vs given"),
            ("Form", "Content", "Structure vs meaning"),
            ("Objective", "Subjective", "In object vs in perceiver"),
            ("Unity", "Diversity", "Oneness vs variety"),
            ("Simple", "Complex", "Pure vs elaborate"),
            ("High", "Low", "Elite vs popular"),
            ("Classic", "Romantic", "Order vs emotion"),
            ("Representational", "Abstract", "Mimetic vs non-objective"),
            ("Harmony", "Discord", "Consonance vs dissonance"),
            ("Organic", "Geometric", "Natural vs mathematical"),
            ("Implicit", "Explicit", "Suggested vs stated"),
            ("Surface", "Depth", "Apparent vs hidden"),
            ("Serious", "Playful", "Grave vs light"),
            ("Original", "Derivative", "New vs borrowed"),
            ("Authentic", "Fake", "Real vs imitation"),
            ("Expression", "Imitation", "Inner vs outer"),
            ("Pleasure", "Meaning", "Enjoyment vs significance"),
            ("Aesthetic", "Practical", "Contemplative vs useful"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Aesthetics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Aesthetics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_kant_aesthetic_judgment(self) -> dict[str, str]:
        """Get Kant's moments of aesthetic judgment."""
        return {
            "quality": "Disinterested satisfaction",
            "quantity": "Universal without concept",
            "relation": "Purposiveness without purpose",
            "modality": "Necessary satisfaction",
        }

    def demonstrate_aesthetics_balance(self) -> dict[str, Any]:
        """Demonstrate aesthetics balance principles."""
        return {
            "concept": "Aesthetics Equilibrium",
            "dualities": {
                "beautiful_ugly": {
                    "beautiful": 50.0,
                    "ugly": 50.0,
                    "meaning": "Aesthetic value spans the spectrum",
                },
                "form_content": {
                    "form": 50.0,
                    "content": 50.0,
                    "meaning": "How and what equally matter",
                },
                "subjective_objective": {
                    "subjective": 50.0,
                    "objective": 50.0,
                    "meaning": "Beauty is in dialogue between object and perceiver",
                },
            },
            "experience_balance": {
                "pleasure": 50.0,
                "meaning": 50.0,
                "description": "Aesthetic experience combines enjoyment and significance",
            },
            "meta_meaning": "Aesthetics demonstrates META 50/50 in beautiful-ugly polarity",
        }


def create_aesthetics_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> AestheticsDomain:
    """
    Factory function to create a fully initialized aesthetics domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized AestheticsDomain
    """
    domain = AestheticsDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_theories()
        domain.initialize_aesthetic_categories()
        domain.initialize_aesthetic_properties()
        domain.initialize_aesthetic_pairs()

    return domain
