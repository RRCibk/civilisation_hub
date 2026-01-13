"""
Religious Studies Domain
========================
Religious studies knowledge domain with META 50/50 equilibrium.
Fundamental duality: Sacred/Profane (holy vs ordinary).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class ReligiousStudiesDomain(KnowledgeDomain):
    """
    Religious Studies knowledge domain.

    Fundamental Duality: Sacred / Profane
    - Sacred: Holy, divine, transcendent, set apart
    - Profane: Ordinary, mundane, worldly, everyday

    Secondary Dualities:
    - Faith / Reason
    - Immanent / Transcendent
    - Orthodoxy / Heterodoxy
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="ReligiousStudies",
            domain_type=DomainType.FUNDAMENTAL,
            description="The academic study of religious beliefs, practices, and institutions",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Sacred/Profane duality."""
        self._domain.set_duality(
            positive_name="sacred",
            positive_value=50,
            negative_name="profane",
            negative_value=50,
            duality_name="religious_studies_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental religious studies principles."""
        principles = [
            (
                "Sacred-Profane Distinction",
                "Religion divides reality into sacred and ordinary",
            ),
            (
                "Methodological Agnosticism",
                "Academic study brackets truth claims",
            ),
            (
                "Comparative Method",
                "Religions can be compared systematically",
            ),
            (
                "Phenomenological Approach",
                "Religious experience studied on its own terms",
            ),
            (
                "Cultural Embeddedness",
                "Religion reflects and shapes culture",
            ),
            (
                "Ritual Efficacy",
                "Rituals produce real effects for participants",
            ),
            (
                "Symbol Systems",
                "Religions create meaning through symbols",
            ),
            (
                "Universality and Particularity",
                "Common patterns with unique expressions",
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
        """Get fundamental religious studies concepts."""
        return [
            "Sacred",
            "Religion",
            "God",
            "Faith",
            "Ritual",
            "Myth",
            "Symbol",
            "Belief",
            "Practice",
            "Community",
            "Scripture",
            "Tradition",
            "Revelation",
            "Salvation",
            "Transcendence",
        ]

    def initialize_branches(self) -> None:
        """Initialize major religious studies branches."""
        branches = [
            (
                "History of Religions",
                "Historical development of religions",
                ConceptType.THEORY,
            ),
            (
                "Comparative Religion",
                "Cross-cultural comparison",
                ConceptType.THEORY,
            ),
            (
                "Sociology of Religion",
                "Religion and society",
                ConceptType.THEORY,
            ),
            (
                "Psychology of Religion",
                "Religious experience and mind",
                ConceptType.THEORY,
            ),
            (
                "Anthropology of Religion",
                "Religion in cultural context",
                ConceptType.THEORY,
            ),
            (
                "Philosophy of Religion",
                "Philosophical analysis",
                ConceptType.THEORY,
            ),
            (
                "Theology",
                "Systematic religious thought",
                ConceptType.THEORY,
            ),
            (
                "Biblical Studies",
                "Study of biblical texts",
                ConceptType.THEORY,
            ),
            (
                "Ritual Studies",
                "Analysis of religious practices",
                ConceptType.THEORY,
            ),
            (
                "New Religious Movements",
                "Contemporary religions",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_world_religions(self) -> None:
        """Initialize major world religions."""
        religions = [
            ("Christianity", "2.4 billion", "Jesus Christ, salvation"),
            ("Islam", "1.9 billion", "Muhammad, submission to God"),
            ("Hinduism", "1.2 billion", "Dharma, karma, moksha"),
            ("Buddhism", "500 million", "Buddha, enlightenment"),
            ("Judaism", "15 million", "Torah, covenant, monotheism"),
            ("Sikhism", "30 million", "Guru Nanak, one God"),
        ]

        for name, adherents, core in religions:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=core,
            )
            concept.metadata["adherents"] = adherents

    def initialize_theoretical_approaches(self) -> None:
        """Initialize theoretical approaches."""
        approaches = [
            ("Functionalism", "Durkheim", "Religion creates social solidarity"),
            ("Phenomenology", "Otto/Eliade", "Sacred experience"),
            ("Structuralism", "Lévi-Strauss", "Underlying structures"),
            ("Rational Choice", "Stark", "Religious economy"),
            ("Cognitive", "Boyer", "Mental mechanisms"),
            ("Feminist", "Christ/Daly", "Gender critique"),
        ]

        for name, founder, description in approaches:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_religious_elements(self) -> None:
        """Initialize elements of religion."""
        elements = [
            ("Ritual", "Formalized actions", "Prayer, sacrifice"),
            ("Myth", "Sacred narrative", "Creation stories"),
            ("Doctrine", "Systematic beliefs", "Creeds, teachings"),
            ("Ethics", "Moral prescriptions", "Commandments"),
            ("Experience", "Personal encounter", "Mysticism"),
            ("Community", "Religious group", "Church, sangha"),
        ]

        for name, description, examples in elements:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_religious_pairs(self) -> None:
        """Initialize fundamental religious pairs with META 50/50 balance."""
        pairs = [
            ("Sacred", "Profane", "Holy vs ordinary"),
            ("Faith", "Reason", "Belief vs logic"),
            ("Immanent", "Transcendent", "Within vs beyond"),
            ("Orthodoxy", "Heterodoxy", "Right vs different belief"),
            ("Exoteric", "Esoteric", "Outer vs inner teaching"),
            ("Monotheism", "Polytheism", "One vs many gods"),
            ("Theism", "Atheism", "God exists vs not"),
            ("Religion", "Spirituality", "Organized vs personal"),
            ("Revelation", "Reason", "Divine vs human knowledge"),
            ("Scripture", "Tradition", "Text vs practice"),
            ("Priest", "Prophet", "Institution vs charisma"),
            ("Salvation", "Liberation", "Christian vs Eastern"),
            ("Sin", "Ignorance", "Moral vs cognitive"),
            ("Grace", "Works", "Gift vs effort"),
            ("Personal", "Impersonal", "God as person vs force"),
            ("Ritual", "Spontaneous", "Formal vs informal"),
            ("Exclusive", "Inclusive", "One way vs many"),
            ("Individual", "Communal", "Personal vs group"),
            ("Traditional", "Reform", "Conservative vs change"),
            ("Literal", "Symbolic", "Actual vs metaphorical"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Religious Studies)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Religious Studies)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_ninian_smart_dimensions(self) -> dict[str, str]:
        """Get Ninian Smart's seven dimensions of religion."""
        return {
            "doctrinal": "Beliefs and teachings",
            "mythical": "Sacred narratives",
            "ethical": "Moral guidelines",
            "ritual": "Ceremonial practices",
            "experiential": "Religious experiences",
            "social": "Community aspects",
            "material": "Physical manifestations",
        }

    def demonstrate_religious_balance(self) -> dict[str, Any]:
        """Demonstrate religious studies balance principles."""
        return {
            "concept": "Religious Studies Equilibrium",
            "dualities": {
                "sacred_profane": {
                    "sacred": 50.0,
                    "profane": 50.0,
                    "meaning": "Religion distinguishes but connects both realms",
                },
                "faith_reason": {
                    "faith": 50.0,
                    "reason": 50.0,
                    "meaning": "Both ways of knowing have place",
                },
                "immanent_transcendent": {
                    "immanent": 50.0,
                    "transcendent": 50.0,
                    "meaning": "Divine is both within and beyond",
                },
            },
            "religious_balance": {
                "belief": 50.0,
                "practice": 50.0,
                "description": "Faith expressed through action",
            },
            "meta_meaning": "Religious Studies demonstrates META 50/50 in sacred-profane dialectic",
        }


def create_religious_studies_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> ReligiousStudiesDomain:
    """
    Factory function to create a fully initialized religious studies domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized ReligiousStudiesDomain
    """
    domain = ReligiousStudiesDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_world_religions()
        domain.initialize_theoretical_approaches()
        domain.initialize_religious_elements()
        domain.initialize_religious_pairs()

    return domain
