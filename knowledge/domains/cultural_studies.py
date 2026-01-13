"""
Cultural Studies Domain
=======================
Cultural studies knowledge domain with META 50/50 equilibrium.
Fundamental duality: Dominant/Subordinate (hegemony vs resistance).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class CulturalStudiesDomain(KnowledgeDomain):
    """
    Cultural Studies knowledge domain.

    Fundamental Duality: Dominant / Subordinate
    - Dominant: Hegemonic, mainstream, power
    - Subordinate: Counter-hegemonic, marginal, resistance

    Secondary Dualities:
    - High / Popular
    - Producer / Consumer
    - Structure / Agency
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="CulturalStudies",
            domain_type=DomainType.FUNDAMENTAL,
            description="The interdisciplinary study of culture, power, and identity",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Dominant/Subordinate duality."""
        self._domain.set_duality(
            positive_name="dominant",
            positive_value=50,
            negative_name="subordinate",
            negative_value=50,
            duality_name="cultural_studies_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental cultural studies principles."""
        principles = [
            (
                "Culture as Contested",
                "Culture is site of struggle over meaning",
            ),
            (
                "Hegemony",
                "Dominant ideas maintain power through consent",
            ),
            (
                "Articulation",
                "Meanings are linked in specific contexts",
            ),
            (
                "Encoding/Decoding",
                "Messages are produced and interpreted differently",
            ),
            (
                "Representation",
                "Culture represents and constructs reality",
            ),
            (
                "Identity Politics",
                "Identity is politically constructed",
            ),
            (
                "Popular Culture Matters",
                "Everyday culture is significant",
            ),
            (
                "Interdisciplinarity",
                "Multiple methods needed for cultural analysis",
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
        """Get fundamental cultural studies concepts."""
        return [
            "Culture",
            "Power",
            "Hegemony",
            "Identity",
            "Representation",
            "Ideology",
            "Discourse",
            "Subculture",
            "Popular Culture",
            "Media",
            "Gender",
            "Race",
            "Class",
            "Globalization",
            "Resistance",
        ]

    def initialize_branches(self) -> None:
        """Initialize major cultural studies branches."""
        branches = [
            (
                "Media Studies",
                "Analysis of media texts and institutions",
                ConceptType.THEORY,
            ),
            (
                "Gender Studies",
                "Gender as cultural construction",
                ConceptType.THEORY,
            ),
            (
                "Postcolonial Studies",
                "Culture and colonialism",
                ConceptType.THEORY,
            ),
            (
                "Race and Ethnicity Studies",
                "Race as cultural category",
                ConceptType.THEORY,
            ),
            (
                "Queer Studies",
                "Sexuality and identity",
                ConceptType.THEORY,
            ),
            (
                "Fan Studies",
                "Fan cultures and practices",
                ConceptType.THEORY,
            ),
            (
                "Subcultural Studies",
                "Youth and subcultural groups",
                ConceptType.THEORY,
            ),
            (
                "Digital Culture",
                "Internet and digital life",
                ConceptType.THEORY,
            ),
            (
                "Visual Culture",
                "Images and visual practices",
                ConceptType.THEORY,
            ),
            (
                "Material Culture",
                "Objects and things",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_theories(self) -> None:
        """Initialize cultural studies theories."""
        theories = [
            ("Birmingham School", "Hall", "Culture as lived experience"),
            ("Frankfurt School", "Adorno", "Culture industry critique"),
            ("Structuralism", "Barthes", "Sign systems"),
            ("Post-structuralism", "Foucault", "Discourse and power"),
            ("Feminist Theory", "hooks", "Intersectionality"),
            ("Postcolonialism", "Said", "Orientalism"),
            ("Queer Theory", "Butler", "Performativity"),
            ("New Materialism", "Barad", "Matter matters"),
        ]

        for name, founder, description in theories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_key_concepts(self) -> None:
        """Initialize key cultural studies concepts."""
        concepts = [
            ("Hegemony", "Gramsci", "Consent to domination"),
            ("Ideology", "Althusser", "System of representations"),
            ("Discourse", "Foucault", "Knowledge-power systems"),
            ("Performativity", "Butler", "Identity through repetition"),
            ("Hybridity", "Bhabha", "Cultural mixing"),
            ("Intersectionality", "Crenshaw", "Overlapping identities"),
        ]

        for name, theorist, description in concepts:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["theorist"] = theorist

    def initialize_cultural_forms(self) -> None:
        """Initialize cultural forms studied."""
        forms = [
            ("Television", "Broadcast medium", "Mass culture"),
            ("Film", "Cinema", "Visual narrative"),
            ("Music", "Popular music", "Youth culture"),
            ("Fashion", "Clothing and style", "Identity expression"),
            ("Advertising", "Commercial messages", "Consumerism"),
            ("Social Media", "Digital platforms", "Network culture"),
        ]

        for name, medium, aspect in forms:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=medium,
            )
            concept.metadata["aspect"] = aspect

    def initialize_cultural_studies_pairs(self) -> None:
        """Initialize fundamental cultural studies pairs with META 50/50 balance."""
        pairs = [
            ("Dominant", "Subordinate", "Hegemony vs resistance"),
            ("High", "Popular", "Elite vs mass culture"),
            ("Producer", "Consumer", "Maker vs user"),
            ("Structure", "Agency", "Constraint vs freedom"),
            ("Global", "Local", "World vs place"),
            ("Center", "Margin", "Mainstream vs peripheral"),
            ("Encoding", "Decoding", "Production vs reception"),
            ("Representation", "Reality", "Image vs world"),
            ("Text", "Context", "Content vs situation"),
            ("Ideology", "Resistance", "Dominant vs oppositional"),
            ("Homogenization", "Hybridization", "Same vs mixed"),
            ("Authentic", "Commodified", "Real vs commercial"),
            ("Active", "Passive", "Engaged vs receptive audience"),
            ("Public", "Private", "Visible vs hidden"),
            ("Mainstream", "Alternative", "Dominant vs counter"),
            ("Universal", "Particular", "General vs specific"),
            ("Modern", "Postmodern", "Grand narrative vs fragmentation"),
            ("Material", "Symbolic", "Thing vs meaning"),
            ("Local", "Transnational", "Place vs flow"),
            ("Identity", "Difference", "Same vs other"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Cultural Studies)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Cultural Studies)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_hall_encoding_decoding(self) -> dict[str, str]:
        """Get Stuart Hall's encoding/decoding positions."""
        return {
            "dominant_hegemonic": "Accepts preferred meaning",
            "negotiated": "Accepts some, rejects other meanings",
            "oppositional": "Decodes in contrary way",
        }

    def demonstrate_cultural_studies_balance(self) -> dict[str, Any]:
        """Demonstrate cultural studies balance principles."""
        return {
            "concept": "Cultural Studies Equilibrium",
            "dualities": {
                "dominant_subordinate": {
                    "dominant": 50.0,
                    "subordinate": 50.0,
                    "meaning": "Culture is always contested terrain",
                },
                "structure_agency": {
                    "structure": 50.0,
                    "agency": 50.0,
                    "meaning": "Both constraint and freedom shape culture",
                },
                "production_consumption": {
                    "production": 50.0,
                    "consumption": 50.0,
                    "meaning": "Making and using culture both matter",
                },
            },
            "power_balance": {
                "hegemony": 50.0,
                "resistance": 50.0,
                "description": "Power always meets counter-power",
            },
            "meta_meaning": "Cultural Studies demonstrates META 50/50 in power-resistance dialectic",
        }


def create_cultural_studies_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> CulturalStudiesDomain:
    """
    Factory function to create a fully initialized cultural studies domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized CulturalStudiesDomain
    """
    domain = CulturalStudiesDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_theories()
        domain.initialize_key_concepts()
        domain.initialize_cultural_forms()
        domain.initialize_cultural_studies_pairs()

    return domain
