"""
Architecture Domain
===================
Architecture knowledge domain with META 50/50 equilibrium.
Fundamental duality: Space/Structure (void vs solid).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class ArchitectureDomain(KnowledgeDomain):
    """
    Architecture knowledge domain.

    Fundamental Duality: Space / Structure
    - Space: Void, interior, enclosed area
    - Structure: Solid, material, building elements

    Secondary Dualities:
    - Form / Function
    - Beauty / Utility
    - Public / Private
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Architecture",
            domain_type=DomainType.FUNDAMENTAL,
            description="The art and science of designing buildings and spaces",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Space/Structure duality."""
        self._domain.set_duality(
            positive_name="space",
            positive_value=50,
            negative_name="structure",
            negative_value=50,
            duality_name="architecture_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental architectural principles."""
        principles = [
            (
                "Form Follows Function",
                "Design should derive from purpose",
            ),
            (
                "Firmitas, Utilitas, Venustas",
                "Strength, utility, beauty - Vitruvian triad",
            ),
            (
                "Human Scale",
                "Architecture relates to human body",
            ),
            (
                "Sense of Place",
                "Buildings respond to context",
            ),
            (
                "Materiality",
                "Materials express their nature",
            ),
            (
                "Light and Shadow",
                "Light shapes spatial experience",
            ),
            (
                "Circulation",
                "Movement through space is designed",
            ),
            (
                "Sustainability",
                "Buildings should minimize environmental impact",
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
        """Get fundamental architecture concepts."""
        return [
            "Space",
            "Structure",
            "Form",
            "Function",
            "Scale",
            "Proportion",
            "Light",
            "Material",
            "Site",
            "Context",
            "Plan",
            "Section",
            "Elevation",
            "Detail",
            "Program",
        ]

    def initialize_branches(self) -> None:
        """Initialize major architecture branches."""
        branches = [
            (
                "Architectural Design",
                "Creating buildings and spaces",
                ConceptType.THEORY,
            ),
            (
                "Architectural History",
                "Historical development",
                ConceptType.THEORY,
            ),
            (
                "Architectural Theory",
                "Ideas about architecture",
                ConceptType.THEORY,
            ),
            (
                "Urban Design",
                "Design at city scale",
                ConceptType.THEORY,
            ),
            (
                "Landscape Architecture",
                "Outdoor spaces",
                ConceptType.THEORY,
            ),
            (
                "Interior Architecture",
                "Interior spaces",
                ConceptType.THEORY,
            ),
            (
                "Building Technology",
                "Construction systems",
                ConceptType.THEORY,
            ),
            (
                "Sustainable Design",
                "Environmental architecture",
                ConceptType.THEORY,
            ),
            (
                "Historic Preservation",
                "Conservation of buildings",
                ConceptType.THEORY,
            ),
            (
                "Computational Design",
                "Digital design methods",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_styles(self) -> None:
        """Initialize architectural styles."""
        styles = [
            ("Classical", "Greek and Roman orders", "Proportion, symmetry"),
            ("Gothic", "Medieval pointed arch", "Height, light"),
            ("Renaissance", "Revival of classical", "Humanism"),
            ("Baroque", "Drama and movement", "Grandeur"),
            ("Modernism", "Form follows function", "Simplicity"),
            ("Postmodernism", "Reaction to modern", "Complexity"),
            ("Deconstructivism", "Fragmentation", "Disruption"),
            ("Sustainable", "Environmental design", "Green building"),
        ]

        for name, description, characteristic in styles:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["characteristic"] = characteristic

    def initialize_building_types(self) -> None:
        """Initialize building types."""
        types = [
            ("Residential", "Housing", "Homes, apartments"),
            ("Commercial", "Business", "Offices, retail"),
            ("Institutional", "Public purpose", "Schools, hospitals"),
            ("Religious", "Worship", "Churches, temples"),
            ("Industrial", "Production", "Factories, warehouses"),
            ("Cultural", "Arts and culture", "Museums, theaters"),
        ]

        for name, category, examples in types:
            concept = self.create_concept(
                name=f"{name} Architecture",
                concept_type=ConceptType.DEFINITION,
                description=category,
            )
            concept.metadata["examples"] = examples

    def initialize_structural_systems(self) -> None:
        """Initialize structural systems."""
        systems = [
            ("Post and Beam", "Vertical and horizontal", "Wood, steel"),
            ("Load-bearing Wall", "Walls carry loads", "Masonry"),
            ("Frame Structure", "Skeleton frame", "Steel, concrete"),
            ("Shell Structure", "Curved surfaces", "Thin shell"),
            ("Tensile Structure", "Tension cables", "Membrane"),
            ("Truss", "Triangulated frame", "Bridges, roofs"),
        ]

        for name, description, material in systems:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["material"] = material

    def initialize_architecture_pairs(self) -> None:
        """Initialize fundamental architectural pairs with META 50/50 balance."""
        pairs = [
            ("Space", "Structure", "Void vs solid"),
            ("Form", "Function", "Appearance vs use"),
            ("Beauty", "Utility", "Aesthetic vs practical"),
            ("Public", "Private", "Communal vs personal"),
            ("Interior", "Exterior", "Inside vs outside"),
            ("Vertical", "Horizontal", "Height vs spread"),
            ("Mass", "Void", "Solid vs opening"),
            ("Light", "Shadow", "Illuminated vs dark"),
            ("Natural", "Artificial", "Organic vs made"),
            ("Old", "New", "Historic vs contemporary"),
            ("Local", "Global", "Vernacular vs international"),
            ("Permanent", "Temporary", "Lasting vs ephemeral"),
            ("Monumental", "Human Scale", "Grand vs intimate"),
            ("Symmetry", "Asymmetry", "Balanced vs unbalanced"),
            ("Enclosed", "Open", "Bounded vs fluid"),
            ("Urban", "Rural", "City vs country"),
            ("Dense", "Sparse", "Compact vs spread"),
            ("Ornament", "Plain", "Decorated vs simple"),
            ("Traditional", "Innovative", "Conventional vs new"),
            ("Built", "Unbuilt", "Constructed vs design"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Architecture)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Architecture)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_vitruvian_principles(self) -> dict[str, str]:
        """Get Vitruvian principles."""
        return {
            "firmitas": "Structural soundness",
            "utilitas": "Functional suitability",
            "venustas": "Beauty and delight",
        }

    def demonstrate_architecture_balance(self) -> dict[str, Any]:
        """Demonstrate architecture balance principles."""
        return {
            "concept": "Architecture Equilibrium",
            "dualities": {
                "space_structure": {
                    "space": 50.0,
                    "structure": 50.0,
                    "meaning": "Architecture creates space through structure",
                },
                "form_function": {
                    "form": 50.0,
                    "function": 50.0,
                    "meaning": "How it looks and how it works",
                },
                "beauty_utility": {
                    "beauty": 50.0,
                    "utility": 50.0,
                    "meaning": "Aesthetic and practical together",
                },
            },
            "vitruvian_balance": {
                "firmitas": 33.3,
                "utilitas": 33.3,
                "venustas": 33.3,
                "description": "Three essential qualities of architecture",
            },
            "meta_meaning": "Architecture demonstrates META 50/50 in space-structure synthesis",
        }


def create_architecture_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> ArchitectureDomain:
    """
    Factory function to create a fully initialized architecture domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized ArchitectureDomain
    """
    domain = ArchitectureDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_styles()
        domain.initialize_building_types()
        domain.initialize_structural_systems()
        domain.initialize_architecture_pairs()

    return domain
