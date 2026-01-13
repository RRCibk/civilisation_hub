"""
Anthropology Domain
===================
Anthropology knowledge domain with META 50/50 equilibrium.
Fundamental duality: Nature/Culture (biological vs social).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class AnthropologyDomain(KnowledgeDomain):
    """
    Anthropology knowledge domain.

    Fundamental Duality: Nature / Culture
    - Nature: Biological, innate, universal human traits
    - Culture: Learned, variable, socially constructed

    Secondary Dualities:
    - Universal / Particular
    - Etic / Emic
    - Self / Other
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Anthropology",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of humans, past and present, in their cultural and biological aspects",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Nature/Culture duality."""
        self._domain.set_duality(
            positive_name="nature",
            positive_value=50,
            negative_name="culture",
            negative_value=50,
            duality_name="anthropology_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental anthropological principles."""
        principles = [
            (
                "Cultural Relativism",
                "Cultures must be understood on their own terms",
            ),
            (
                "Holism",
                "Human experience must be studied as interconnected whole",
            ),
            (
                "Participant Observation",
                "Understanding requires immersion in culture",
            ),
            (
                "Human Universality",
                "All humans share fundamental characteristics",
            ),
            (
                "Cultural Diversity",
                "Human cultures vary enormously",
            ),
            (
                "Biocultural Evolution",
                "Biology and culture co-evolve",
            ),
            (
                "Ethnocentrism Awareness",
                "Own culture shapes perception of others",
            ),
            (
                "Four-Field Approach",
                "Study human from biological, cultural, linguistic, archaeological views",
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
        """Get fundamental anthropology concepts."""
        return [
            "Culture",
            "Society",
            "Kinship",
            "Religion",
            "Language",
            "Symbol",
            "Ritual",
            "Myth",
            "Identity",
            "Ethnicity",
            "Race",
            "Gender",
            "Power",
            "Exchange",
            "Evolution",
        ]

    def initialize_branches(self) -> None:
        """Initialize major anthropology branches."""
        branches = [
            (
                "Cultural Anthropology",
                "Study of human cultures",
                ConceptType.THEORY,
            ),
            (
                "Biological Anthropology",
                "Human biological evolution and variation",
                ConceptType.THEORY,
            ),
            (
                "Linguistic Anthropology",
                "Language in cultural context",
                ConceptType.THEORY,
            ),
            (
                "Archaeology",
                "Study of past through material remains",
                ConceptType.THEORY,
            ),
            (
                "Medical Anthropology",
                "Health and healing across cultures",
                ConceptType.THEORY,
            ),
            (
                "Economic Anthropology",
                "Economic systems in cultural context",
                ConceptType.THEORY,
            ),
            (
                "Political Anthropology",
                "Power and politics across cultures",
                ConceptType.THEORY,
            ),
            (
                "Visual Anthropology",
                "Visual representation of culture",
                ConceptType.THEORY,
            ),
            (
                "Urban Anthropology",
                "Anthropology of cities",
                ConceptType.THEORY,
            ),
            (
                "Applied Anthropology",
                "Practical applications of anthropology",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_theories(self) -> None:
        """Initialize major anthropological theories."""
        theories = [
            ("Evolutionism", "Tylor/Morgan", "Cultures evolve through stages"),
            ("Functionalism", "Malinowski", "Culture serves human needs"),
            ("Structural-Functionalism", "Radcliffe-Brown", "Social structures maintain order"),
            ("Structuralism", "Lévi-Strauss", "Universal mental structures"),
            ("Interpretive", "Geertz", "Culture as text to interpret"),
            ("Marxist Anthropology", "Wolf", "Political economy of culture"),
            ("Feminist Anthropology", "Mead", "Gender in cultural context"),
            ("Postmodern Anthropology", "Clifford", "Critique of representation"),
        ]

        for name, founder, description in theories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_kinship_systems(self) -> None:
        """Initialize kinship system types."""
        systems = [
            ("Patrilineal", "Descent through father", "Father's line"),
            ("Matrilineal", "Descent through mother", "Mother's line"),
            ("Bilateral", "Both parents equally", "Ego-centered"),
            ("Ambilineal", "Choice of either line", "Flexible"),
            ("Cognatic", "All relatives recognized", "Non-unilineal"),
        ]

        for name, description, characteristic in systems:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["characteristic"] = characteristic

    def initialize_exchange_types(self) -> None:
        """Initialize exchange system types."""
        exchanges = [
            ("Reciprocity", "Gift exchange", "Generalized, balanced, negative"),
            ("Redistribution", "Central collection and distribution", "Chiefdoms"),
            ("Market Exchange", "Price-based exchange", "Money, supply/demand"),
            ("Potlatch", "Competitive gift giving", "Northwest Coast"),
            ("Kula Ring", "Ceremonial exchange circuit", "Trobriand Islands"),
        ]

        for name, description, examples in exchanges:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_anthropological_pairs(self) -> None:
        """Initialize fundamental anthropological pairs with META 50/50 balance."""
        pairs = [
            ("Nature", "Culture", "Biological vs social"),
            ("Universal", "Particular", "Common vs unique"),
            ("Etic", "Emic", "Outsider vs insider view"),
            ("Self", "Other", "Us vs them"),
            ("Sacred", "Profane", "Holy vs ordinary"),
            ("Tradition", "Modernity", "Old vs new"),
            ("Local", "Global", "Place vs world"),
            ("Indigenous", "Colonial", "Native vs imposed"),
            ("Oral", "Literate", "Spoken vs written"),
            ("Kinship", "Affinity", "Blood vs marriage"),
            ("Patrilineal", "Matrilineal", "Father vs mother line"),
            ("Endogamy", "Exogamy", "Marry within vs without"),
            ("Domestic", "Public", "Home vs outside"),
            ("Gift", "Commodity", "Social vs market exchange"),
            ("Myth", "History", "Sacred vs secular time"),
            ("Ritual", "Everyday", "Special vs ordinary"),
            ("Symbol", "Sign", "Meaning vs indicator"),
            ("Structure", "Agency", "Pattern vs action"),
            ("Synchronic", "Diachronic", "Snapshot vs change"),
            ("Fieldwork", "Theory", "Observation vs explanation"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Anthropology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Anthropology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_culture_elements(self) -> dict[str, str]:
        """Get elements of culture."""
        return {
            "symbols": "Anything that carries meaning within culture",
            "language": "System of symbols for communication",
            "values": "Culturally defined standards of desirability",
            "norms": "Rules and expectations guiding behavior",
            "material_culture": "Physical objects created by culture",
        }

    def demonstrate_anthropology_balance(self) -> dict[str, Any]:
        """Demonstrate anthropology balance principles."""
        return {
            "concept": "Anthropology Equilibrium",
            "dualities": {
                "nature_culture": {
                    "nature": 50.0,
                    "culture": 50.0,
                    "meaning": "Humans are equally biological and cultural beings",
                },
                "universal_particular": {
                    "universal": 50.0,
                    "particular": 50.0,
                    "meaning": "Human unity expressed through cultural diversity",
                },
                "etic_emic": {
                    "etic": 50.0,
                    "emic": 50.0,
                    "meaning": "Both outsider and insider perspectives needed",
                },
            },
            "four_fields": {
                "cultural": 25.0,
                "biological": 25.0,
                "linguistic": 25.0,
                "archaeological": 25.0,
                "description": "Holistic approach to human study",
            },
            "meta_meaning": "Anthropology demonstrates META 50/50 in nature-culture duality",
        }


def create_anthropology_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> AnthropologyDomain:
    """
    Factory function to create a fully initialized anthropology domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized AnthropologyDomain
    """
    domain = AnthropologyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_theories()
        domain.initialize_kinship_systems()
        domain.initialize_exchange_types()
        domain.initialize_anthropological_pairs()

    return domain
