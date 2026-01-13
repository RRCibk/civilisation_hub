"""
Sociology Domain
================
Sociology knowledge domain with META 50/50 equilibrium.
Fundamental duality: Individual/Collective (person vs society).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class SociologyDomain(KnowledgeDomain):
    """
    Sociology knowledge domain.

    Fundamental Duality: Individual / Collective
    - Individual: Person, agency, micro-level phenomena
    - Collective: Society, structure, macro-level phenomena

    Secondary Dualities:
    - Structure / Agency
    - Consensus / Conflict
    - Order / Change
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Sociology",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of society, social relationships, and social institutions",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Individual/Collective duality."""
        self._domain.set_duality(
            positive_name="individual",
            positive_value=50,
            negative_name="collective",
            negative_value=50,
            duality_name="sociology_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental sociological principles."""
        principles = [
            (
                "Social Construction",
                "Reality is constructed through social interaction",
            ),
            (
                "Structural Influence",
                "Social structures shape individual behavior",
            ),
            (
                "Agency Principle",
                "Individuals can act independently of structures",
            ),
            (
                "Social Stratification",
                "Societies are organized into hierarchical layers",
            ),
            (
                "Cultural Relativity",
                "Cultural norms vary across societies",
            ),
            (
                "Institutional Persistence",
                "Social institutions tend to reproduce themselves",
            ),
            (
                "Social Change",
                "Societies undergo continuous transformation",
            ),
            (
                "Functional Interdependence",
                "Social parts are interconnected and interdependent",
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
        """Get fundamental sociology concepts."""
        return [
            "Society",
            "Culture",
            "Socialization",
            "Social Structure",
            "Social Institution",
            "Social Stratification",
            "Social Change",
            "Social Interaction",
            "Norm",
            "Value",
            "Role",
            "Status",
            "Group",
            "Community",
            "Power",
        ]

    def initialize_branches(self) -> None:
        """Initialize major sociology branches."""
        branches = [
            (
                "Microsociology",
                "Study of small-scale social interactions",
                ConceptType.THEORY,
            ),
            (
                "Macrosociology",
                "Study of large-scale social phenomena",
                ConceptType.THEORY,
            ),
            (
                "Urban Sociology",
                "Study of life in urban areas",
                ConceptType.THEORY,
            ),
            (
                "Rural Sociology",
                "Study of life in rural areas",
                ConceptType.THEORY,
            ),
            (
                "Political Sociology",
                "Study of politics and society",
                ConceptType.THEORY,
            ),
            (
                "Economic Sociology",
                "Study of economic phenomena in social context",
                ConceptType.THEORY,
            ),
            (
                "Medical Sociology",
                "Study of health and illness in society",
                ConceptType.THEORY,
            ),
            (
                "Environmental Sociology",
                "Study of society-environment relationships",
                ConceptType.THEORY,
            ),
            (
                "Sociology of Religion",
                "Study of religion in society",
                ConceptType.THEORY,
            ),
            (
                "Sociology of Education",
                "Study of education systems",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_theories(self) -> None:
        """Initialize major sociological theories."""
        theories = [
            ("Functionalism", "Durkheim/Parsons", "Society as integrated system"),
            ("Conflict Theory", "Marx/Weber", "Society shaped by power struggles"),
            ("Symbolic Interactionism", "Mead/Blumer", "Meaning through interaction"),
            ("Structural Functionalism", "Parsons", "Social structures serve functions"),
            ("Critical Theory", "Frankfurt School", "Critique of domination"),
            ("Feminist Theory", "Multiple", "Gender as social structure"),
            ("Rational Choice", "Coleman", "Individuals maximize utility"),
            ("Network Theory", "Granovetter", "Social ties structure opportunity"),
        ]

        for name, founder, description in theories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_social_institutions(self) -> None:
        """Initialize social institution types."""
        institutions = [
            ("Family", "Primary socialization unit", "Kinship, reproduction"),
            ("Education", "Knowledge transmission", "Schools, universities"),
            ("Religion", "Shared beliefs and practices", "Churches, rituals"),
            ("Economy", "Production and distribution", "Markets, firms"),
            ("Government", "Political organization", "State, laws"),
            ("Media", "Information dissemination", "News, entertainment"),
        ]

        for name, description, examples in institutions:
            concept = self.create_concept(
                name=f"{name} Institution",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_stratification(self) -> None:
        """Initialize stratification concepts."""
        concepts = [
            ("Social Class", "Economic position in society", "Upper/Middle/Lower"),
            ("Status", "Social prestige or honor", "Ascribed/Achieved"),
            ("Power", "Ability to impose will", "Authority/Influence"),
            ("Social Mobility", "Movement between strata", "Vertical/Horizontal"),
            ("Inequality", "Unequal distribution of resources", "Economic/Social"),
        ]

        for name, description, types in concepts:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["types"] = types

    def initialize_sociological_pairs(self) -> None:
        """Initialize fundamental sociological pairs with META 50/50 balance."""
        pairs = [
            ("Individual", "Collective", "Person vs society"),
            ("Structure", "Agency", "Constraint vs freedom"),
            ("Consensus", "Conflict", "Agreement vs struggle"),
            ("Order", "Change", "Stability vs transformation"),
            ("Macro", "Micro", "Large vs small scale"),
            ("Public", "Private", "Open vs closed sphere"),
            ("Formal", "Informal", "Official vs unofficial"),
            ("Sacred", "Profane", "Holy vs ordinary"),
            ("Integration", "Differentiation", "Unity vs diversity"),
            ("Ascribed", "Achieved", "Given vs earned status"),
            ("In-group", "Out-group", "Us vs them"),
            ("Primary", "Secondary", "Close vs distant groups"),
            ("Mechanical", "Organic", "Simple vs complex solidarity"),
            ("Gemeinschaft", "Gesellschaft", "Community vs society"),
            ("Traditional", "Modern", "Past vs present norms"),
            ("Rural", "Urban", "Country vs city"),
            ("Conformity", "Deviance", "Following vs breaking norms"),
            ("Manifest", "Latent", "Intended vs unintended"),
            ("Exploitation", "Cooperation", "Using vs helping"),
            ("Stratification", "Equality", "Hierarchy vs sameness"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Sociology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Sociology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_social_facts(self) -> dict[str, str]:
        """Get Durkheim's types of social facts."""
        return {
            "material": "Physical aspects like architecture and law",
            "non_material": "Norms, values, and collective representations",
            "morphological": "Structure and distribution of population",
            "institutional": "Established beliefs and practices",
        }

    def demonstrate_sociology_balance(self) -> dict[str, Any]:
        """Demonstrate sociology balance principles."""
        return {
            "concept": "Sociology Equilibrium",
            "dualities": {
                "individual_collective": {
                    "individual": 50.0,
                    "collective": 50.0,
                    "meaning": "Person and society mutually constitute each other",
                },
                "structure_agency": {
                    "structure": 50.0,
                    "agency": 50.0,
                    "meaning": "Constraints and freedom coexist",
                },
                "consensus_conflict": {
                    "consensus": 50.0,
                    "conflict": 50.0,
                    "meaning": "Both cooperation and struggle shape society",
                },
            },
            "social_balance": {
                "stability": 50.0,
                "change": 50.0,
                "description": "Societies maintain order while transforming",
            },
            "meta_meaning": "Sociology demonstrates META 50/50 in individual-collective duality",
        }


def create_sociology_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> SociologyDomain:
    """
    Factory function to create a fully initialized sociology domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized SociologyDomain
    """
    domain = SociologyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_theories()
        domain.initialize_social_institutions()
        domain.initialize_stratification()
        domain.initialize_sociological_pairs()

    return domain
