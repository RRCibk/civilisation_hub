"""
Art Domain
==========
Art knowledge domain with META 50/50 equilibrium.
Fundamental duality: Form/Content (structure vs meaning).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class ArtDomain(KnowledgeDomain):
    """
    Art knowledge domain.

    Fundamental Duality: Form / Content
    - Form: Visual structure, technique, composition
    - Content: Meaning, subject matter, expression

    Secondary Dualities:
    - Representation / Abstraction
    - Traditional / Modern
    - Artist / Viewer
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Art",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of visual arts and their creation, meaning, and history",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Form/Content duality."""
        self._domain.set_duality(
            positive_name="form",
            positive_value=50,
            negative_name="content",
            negative_value=50,
            duality_name="art_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental art principles."""
        principles = [
            (
                "Unity in Variety",
                "Art balances diversity with coherence",
            ),
            (
                "Significant Form",
                "Form itself can carry meaning",
            ),
            (
                "Expression Theory",
                "Art expresses emotion",
            ),
            (
                "Institutional Definition",
                "Art is what the art world accepts",
            ),
            (
                "Autonomy of Art",
                "Art has intrinsic value",
            ),
            (
                "Context Dependency",
                "Meaning depends on context",
            ),
            (
                "Open Concept",
                "Art cannot be definitively defined",
            ),
            (
                "Medium Specificity",
                "Each medium has unique properties",
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
        """Get fundamental art concepts."""
        return [
            "Art",
            "Beauty",
            "Form",
            "Content",
            "Style",
            "Medium",
            "Composition",
            "Color",
            "Line",
            "Space",
            "Representation",
            "Abstraction",
            "Expression",
            "Aesthetic",
            "Meaning",
        ]

    def initialize_branches(self) -> None:
        """Initialize major art branches."""
        branches = [
            (
                "Art History",
                "Historical development of art",
                ConceptType.THEORY,
            ),
            (
                "Art Criticism",
                "Analysis and evaluation of art",
                ConceptType.THEORY,
            ),
            (
                "Aesthetics",
                "Philosophy of art and beauty",
                ConceptType.THEORY,
            ),
            (
                "Iconography",
                "Study of visual imagery",
                ConceptType.THEORY,
            ),
            (
                "Formalism",
                "Focus on visual elements",
                ConceptType.THEORY,
            ),
            (
                "Social Art History",
                "Art in social context",
                ConceptType.THEORY,
            ),
            (
                "Visual Culture",
                "Broader visual practices",
                ConceptType.THEORY,
            ),
            (
                "Conservation",
                "Preservation of artworks",
                ConceptType.THEORY,
            ),
            (
                "Curatorial Studies",
                "Exhibition and display",
                ConceptType.THEORY,
            ),
            (
                "Art Theory",
                "Theoretical frameworks",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_movements(self) -> None:
        """Initialize art movements."""
        movements = [
            ("Renaissance", "1400-1600", "Rebirth of classical ideals"),
            ("Baroque", "1600-1750", "Drama, movement, emotion"),
            ("Impressionism", "1860-1890", "Light, color, perception"),
            ("Expressionism", "1905-1920", "Emotional distortion"),
            ("Cubism", "1907-1920", "Multiple perspectives"),
            ("Abstract Expressionism", "1940-1960", "Gesture and field"),
            ("Pop Art", "1950-1970", "Mass culture imagery"),
            ("Conceptual Art", "1960s-", "Ideas over objects"),
        ]

        for name, period, description in movements:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["period"] = period

    def initialize_media(self) -> None:
        """Initialize art media."""
        media = [
            ("Painting", "Pigment on surface", "Oil, acrylic, watercolor"),
            ("Sculpture", "Three-dimensional form", "Stone, bronze, wood"),
            ("Drawing", "Marks on paper", "Pencil, ink, charcoal"),
            ("Printmaking", "Multiple impressions", "Etching, lithography"),
            ("Photography", "Light-based image", "Analog, digital"),
            ("Installation", "Site-specific work", "Environmental"),
        ]

        for name, description, examples in media:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_elements(self) -> None:
        """Initialize elements of art."""
        elements = [
            ("Line", "Path between points", "Contour, gesture"),
            ("Shape", "Enclosed area", "Geometric, organic"),
            ("Color", "Light wavelength", "Hue, value, saturation"),
            ("Texture", "Surface quality", "Actual, implied"),
            ("Space", "Area within/around", "Positive, negative"),
            ("Value", "Light and dark", "Tonal range"),
        ]

        for name, description, aspects in elements:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["aspects"] = aspects

    def initialize_art_pairs(self) -> None:
        """Initialize fundamental art pairs with META 50/50 balance."""
        pairs = [
            ("Form", "Content", "Structure vs meaning"),
            ("Representation", "Abstraction", "Likeness vs non-objective"),
            ("Traditional", "Modern", "Classic vs contemporary"),
            ("Artist", "Viewer", "Creator vs perceiver"),
            ("Objective", "Subjective", "External vs internal"),
            ("Technique", "Expression", "Skill vs emotion"),
            ("Line", "Color", "Drawing vs painting"),
            ("Positive", "Negative", "Figure vs ground"),
            ("Harmony", "Contrast", "Unity vs difference"),
            ("Balance", "Asymmetry", "Equal vs unequal"),
            ("Realism", "Idealism", "As is vs as should be"),
            ("Sacred", "Secular", "Religious vs worldly"),
            ("High Art", "Low Art", "Elite vs popular"),
            ("Original", "Copy", "Unique vs reproduced"),
            ("Figurative", "Abstract", "Representational vs non"),
            ("Static", "Dynamic", "Still vs moving"),
            ("Surface", "Depth", "Flat vs illusionistic"),
            ("Creation", "Reception", "Making vs viewing"),
            ("Concept", "Execution", "Idea vs realization"),
            ("Aesthetic", "Functional", "Beautiful vs useful"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Art)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Art)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_principles_of_design(self) -> dict[str, str]:
        """Get principles of design."""
        return {
            "balance": "Visual equilibrium",
            "contrast": "Difference creates interest",
            "emphasis": "Focal point",
            "movement": "Path of viewer's eye",
            "pattern": "Repetition of elements",
            "rhythm": "Visual tempo",
            "unity": "Coherence of whole",
        }

    def demonstrate_art_balance(self) -> dict[str, Any]:
        """Demonstrate art balance principles."""
        return {
            "concept": "Art Equilibrium",
            "dualities": {
                "form_content": {
                    "form": 50.0,
                    "content": 50.0,
                    "meaning": "How and what are equally important",
                },
                "representation_abstraction": {
                    "representation": 50.0,
                    "abstraction": 50.0,
                    "meaning": "Art spans representational spectrum",
                },
                "artist_viewer": {
                    "artist": 50.0,
                    "viewer": 50.0,
                    "meaning": "Creation and reception complete the work",
                },
            },
            "aesthetic_balance": {
                "beauty": 50.0,
                "meaning": 50.0,
                "description": "Visual pleasure and significance together",
            },
            "meta_meaning": "Art demonstrates META 50/50 in form-content unity",
        }


def create_art_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> ArtDomain:
    """
    Factory function to create a fully initialized art domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized ArtDomain
    """
    domain = ArtDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_movements()
        domain.initialize_media()
        domain.initialize_elements()
        domain.initialize_art_pairs()

    return domain
