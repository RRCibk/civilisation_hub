"""
Demography Domain
=================
Demography knowledge domain with META 50/50 equilibrium.
Fundamental duality: Birth/Death (fertility vs mortality).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class DemographyDomain(KnowledgeDomain):
    """
    Demography knowledge domain.

    Fundamental Duality: Birth / Death
    - Birth: Fertility, natality, population growth
    - Death: Mortality, population decline

    Secondary Dualities:
    - Immigration / Emigration
    - Growth / Decline
    - Young / Old
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Demography",
            domain_type=DomainType.FUNDAMENTAL,
            description="The statistical study of human populations",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Birth/Death duality."""
        self._domain.set_duality(
            positive_name="birth",
            positive_value=50,
            negative_name="death",
            negative_value=50,
            duality_name="demography_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental demographic principles."""
        principles = [
            (
                "Balancing Equation",
                "P1 = P0 + Births - Deaths + Immigration - Emigration",
            ),
            (
                "Demographic Transition",
                "Populations move from high to low birth/death rates",
            ),
            (
                "Malthusian Principle",
                "Population tends to outstrip resources",
            ),
            (
                "Population Momentum",
                "Population continues growing after fertility decline",
            ),
            (
                "Age Structure Effect",
                "Age distribution affects demographic outcomes",
            ),
            (
                "Fertility Replacement",
                "2.1 children per woman maintains population",
            ),
            (
                "Mortality Compression",
                "Deaths increasingly occur at older ages",
            ),
            (
                "Migration Selectivity",
                "Migrants differ from non-migrants",
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=90,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental demography concepts."""
        return [
            "Population",
            "Fertility",
            "Mortality",
            "Migration",
            "Age Structure",
            "Sex Ratio",
            "Life Expectancy",
            "Birth Rate",
            "Death Rate",
            "Growth Rate",
            "Dependency Ratio",
            "Census",
            "Cohort",
            "Generation",
            "Pyramid",
        ]

    def initialize_branches(self) -> None:
        """Initialize major demography branches."""
        branches = [
            (
                "Formal Demography",
                "Mathematical population analysis",
                ConceptType.THEORY,
            ),
            (
                "Social Demography",
                "Social factors in population change",
                ConceptType.THEORY,
            ),
            (
                "Historical Demography",
                "Population history",
                ConceptType.THEORY,
            ),
            (
                "Economic Demography",
                "Population and economy",
                ConceptType.THEORY,
            ),
            (
                "Political Demography",
                "Population and politics",
                ConceptType.THEORY,
            ),
            (
                "Biodemography",
                "Biological aspects of population",
                ConceptType.THEORY,
            ),
            (
                "Family Demography",
                "Household and family dynamics",
                ConceptType.THEORY,
            ),
            (
                "Migration Studies",
                "Population movement",
                ConceptType.THEORY,
            ),
            (
                "Population Geography",
                "Spatial distribution of population",
                ConceptType.THEORY,
            ),
            (
                "Applied Demography",
                "Practical population analysis",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_measures(self) -> None:
        """Initialize demographic measures."""
        measures = [
            ("Crude Birth Rate", "Births per 1000 population", "CBR"),
            ("Crude Death Rate", "Deaths per 1000 population", "CDR"),
            ("Total Fertility Rate", "Births per woman", "TFR"),
            ("Infant Mortality Rate", "Deaths under 1 per 1000 births", "IMR"),
            ("Life Expectancy", "Average years of life remaining", "e0"),
            ("Net Migration Rate", "Net migrants per 1000 population", "NMR"),
            ("Dependency Ratio", "Non-working to working age", "DR"),
            ("Sex Ratio", "Males per 100 females", "SR"),
        ]

        for name, description, abbreviation in measures:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["abbreviation"] = abbreviation

    def initialize_transition_stages(self) -> None:
        """Initialize demographic transition stages."""
        stages = [
            ("Stage 1", "High birth/death rates", "Pre-transition"),
            ("Stage 2", "Declining death rates", "Early transition"),
            ("Stage 3", "Declining birth rates", "Late transition"),
            ("Stage 4", "Low birth/death rates", "Post-transition"),
            ("Stage 5", "Below replacement fertility", "Second transition"),
        ]

        for name, description, phase in stages:
            concept = self.create_concept(
                name=f"Demographic Transition {name}",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["phase"] = phase

    def initialize_population_theories(self) -> None:
        """Initialize population theories."""
        theories = [
            ("Malthusian Theory", "Malthus", "Population outstrips resources"),
            ("Demographic Transition", "Notestein", "Modernization reduces rates"),
            ("Second Demographic Transition", "Van de Kaa", "Below replacement fertility"),
            ("Easterlin Hypothesis", "Easterlin", "Relative cohort size affects fertility"),
            ("Becker Model", "Becker", "Children as economic goods"),
            ("Caldwell Theory", "Caldwell", "Wealth flows and fertility"),
        ]

        for name, founder, description in theories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_demographic_pairs(self) -> None:
        """Initialize fundamental demographic pairs with META 50/50 balance."""
        pairs = [
            ("Birth", "Death", "Fertility vs mortality"),
            ("Immigration", "Emigration", "In vs out migration"),
            ("Growth", "Decline", "Increase vs decrease"),
            ("Young", "Old", "Youth vs aged"),
            ("Male", "Female", "Men vs women"),
            ("Fertility", "Mortality", "Natality vs death"),
            ("Urban", "Rural", "City vs country"),
            ("Developed", "Developing", "Rich vs poor nations"),
            ("High Fertility", "Low Fertility", "Many vs few births"),
            ("Internal", "International", "Domestic vs cross-border"),
            ("Push", "Pull", "Leave vs attract factors"),
            ("Voluntary", "Forced", "Chosen vs compelled migration"),
            ("Temporary", "Permanent", "Short vs long-term"),
            ("Natural", "Net", "Births-deaths vs total change"),
            ("Cohort", "Period", "Generation vs year effect"),
            ("Stock", "Flow", "Population vs change"),
            ("Crude", "Refined", "Simple vs adjusted rate"),
            ("Numerator", "Denominator", "Events vs population"),
            ("De Jure", "De Facto", "Legal vs actual residence"),
            ("Stationary", "Stable", "Zero vs constant growth"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Demography)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Demography)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_population_equation(self) -> dict[str, str]:
        """Get population balancing equation components."""
        return {
            "initial_population": "P0",
            "final_population": "P1",
            "births": "B",
            "deaths": "D",
            "immigration": "I",
            "emigration": "E",
            "equation": "P1 = P0 + B - D + I - E",
        }

    def demonstrate_demography_balance(self) -> dict[str, Any]:
        """Demonstrate demography balance principles."""
        return {
            "concept": "Demography Equilibrium",
            "dualities": {
                "birth_death": {
                    "birth": 50.0,
                    "death": 50.0,
                    "meaning": "Population balance requires fertility equals mortality",
                },
                "immigration_emigration": {
                    "immigration": 50.0,
                    "emigration": 50.0,
                    "meaning": "Net migration can be zero",
                },
                "growth_decline": {
                    "growth": 50.0,
                    "decline": 50.0,
                    "meaning": "Population change can be positive or negative",
                },
            },
            "replacement_balance": {
                "fertility_rate": 2.1,
                "meaning": "Replacement level fertility",
                "description": "Population neither grows nor declines",
            },
            "meta_meaning": "Demography demonstrates META 50/50 in birth-death balance",
        }


def create_demography_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> DemographyDomain:
    """
    Factory function to create a fully initialized demography domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized DemographyDomain
    """
    domain = DemographyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_measures()
        domain.initialize_transition_stages()
        domain.initialize_population_theories()
        domain.initialize_demographic_pairs()

    return domain
