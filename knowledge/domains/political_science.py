"""
Political Science Domain
========================
Political science knowledge domain with META 50/50 equilibrium.
Fundamental duality: Power/Liberty (authority vs freedom).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class PoliticalScienceDomain(KnowledgeDomain):
    """
    Political Science knowledge domain.

    Fundamental Duality: Power / Liberty
    - Power: Authority, control, governance
    - Liberty: Freedom, rights, autonomy

    Secondary Dualities:
    - State / Individual
    - Order / Freedom
    - Public / Private
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="PoliticalScience",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of government, politics, and political behavior",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Power/Liberty duality."""
        self._domain.set_duality(
            positive_name="power",
            positive_value=50,
            negative_name="liberty",
            negative_value=50,
            duality_name="political_science_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental political principles."""
        principles = [
            (
                "Social Contract",
                "Legitimate authority derives from consent of governed",
            ),
            (
                "Separation of Powers",
                "Power divided prevents tyranny",
            ),
            (
                "Popular Sovereignty",
                "Ultimate authority resides in the people",
            ),
            (
                "Rule of Law",
                "Laws apply equally to all",
            ),
            (
                "Pluralism",
                "Multiple groups compete for influence",
            ),
            (
                "Checks and Balances",
                "Branches constrain each other",
            ),
            (
                "Legitimacy Principle",
                "Effective rule requires perceived legitimacy",
            ),
            (
                "Power Distribution",
                "Power tends toward concentration or distribution",
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
        """Get fundamental political science concepts."""
        return [
            "State",
            "Government",
            "Power",
            "Authority",
            "Legitimacy",
            "Sovereignty",
            "Democracy",
            "Rights",
            "Liberty",
            "Justice",
            "Law",
            "Policy",
            "Citizenship",
            "Representation",
            "Election",
        ]

    def initialize_branches(self) -> None:
        """Initialize major political science branches."""
        branches = [
            (
                "Political Theory",
                "Normative questions about politics",
                ConceptType.THEORY,
            ),
            (
                "Comparative Politics",
                "Comparing political systems",
                ConceptType.THEORY,
            ),
            (
                "International Relations",
                "Relations between states",
                ConceptType.THEORY,
            ),
            (
                "Public Administration",
                "Implementation of policy",
                ConceptType.THEORY,
            ),
            (
                "Public Policy",
                "Government decisions and actions",
                ConceptType.THEORY,
            ),
            (
                "Political Economy",
                "Intersection of politics and economics",
                ConceptType.THEORY,
            ),
            (
                "Political Behavior",
                "Individual political actions",
                ConceptType.THEORY,
            ),
            (
                "Constitutional Law",
                "Fundamental legal framework",
                ConceptType.THEORY,
            ),
            (
                "Electoral Studies",
                "Elections and voting",
                ConceptType.THEORY,
            ),
            (
                "Political Communication",
                "Information flow in politics",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_political_systems(self) -> None:
        """Initialize political system types."""
        systems = [
            ("Democracy", "Rule by the people", "Elections, representation"),
            ("Authoritarianism", "Concentrated power", "Limited participation"),
            ("Totalitarianism", "Total state control", "Ideology, terror"),
            ("Monarchy", "Rule by hereditary sovereign", "Traditional authority"),
            ("Oligarchy", "Rule by few", "Elite control"),
            ("Theocracy", "Religious rule", "Divine authority"),
        ]

        for name, description, characteristic in systems:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["characteristic"] = characteristic

    def initialize_ideologies(self) -> None:
        """Initialize political ideologies."""
        ideologies = [
            ("Liberalism", "Individual rights, limited government", "Locke, Mill"),
            ("Conservatism", "Tradition, gradual change", "Burke"),
            ("Socialism", "Social ownership, equality", "Marx, Engels"),
            ("Fascism", "Nationalist authoritarianism", "Mussolini"),
            ("Libertarianism", "Maximum individual freedom", "Nozick"),
            ("Feminism", "Gender equality", "Wollstonecraft"),
            ("Environmentalism", "Ecological sustainability", "Carson"),
        ]

        for name, description, thinkers in ideologies:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["key_thinkers"] = thinkers

    def initialize_government_types(self) -> None:
        """Initialize government structure types."""
        types = [
            ("Unitary", "Central government holds power", "France"),
            ("Federal", "Power divided between levels", "USA, Germany"),
            ("Confederal", "Weak central authority", "EU elements"),
            ("Presidential", "Separate executive branch", "USA, Brazil"),
            ("Parliamentary", "Executive from legislature", "UK, Canada"),
            ("Semi-presidential", "Dual executive", "France"),
        ]

        for name, description, example in types:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["example"] = example

    def initialize_political_pairs(self) -> None:
        """Initialize fundamental political pairs with META 50/50 balance."""
        pairs = [
            ("Power", "Liberty", "Authority vs freedom"),
            ("State", "Individual", "Collective vs person"),
            ("Order", "Freedom", "Stability vs autonomy"),
            ("Public", "Private", "Common vs personal"),
            ("Left", "Right", "Progressive vs conservative"),
            ("Central", "Local", "National vs regional"),
            ("Elite", "Mass", "Few vs many"),
            ("Majority", "Minority", "Most vs some"),
            ("Rights", "Duties", "Entitlements vs obligations"),
            ("Representation", "Participation", "Indirect vs direct"),
            ("Legitimacy", "Coercion", "Consent vs force"),
            ("Stability", "Change", "Continuity vs reform"),
            ("Security", "Privacy", "Safety vs secrecy"),
            ("Equality", "Hierarchy", "Same vs ranked"),
            ("Domestic", "Foreign", "Internal vs external"),
            ("War", "Peace", "Conflict vs harmony"),
            ("Executive", "Legislative", "Action vs lawmaking"),
            ("Elected", "Appointed", "Chosen vs selected"),
            ("Formal", "Informal", "Official vs unofficial"),
            ("Sovereign", "Subject", "Ruler vs ruled"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Political Science)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Political Science)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_forms_of_power(self) -> dict[str, str]:
        """Get Weber's forms of legitimate authority."""
        return {
            "traditional": "Authority based on custom and tradition",
            "charismatic": "Authority based on personal qualities",
            "rational_legal": "Authority based on rules and laws",
        }

    def demonstrate_political_balance(self) -> dict[str, Any]:
        """Demonstrate political balance principles."""
        return {
            "concept": "Political Equilibrium",
            "dualities": {
                "power_liberty": {
                    "power": 50.0,
                    "liberty": 50.0,
                    "meaning": "Government must balance authority with freedom",
                },
                "state_individual": {
                    "state": 50.0,
                    "individual": 50.0,
                    "meaning": "Collective needs balanced with personal rights",
                },
                "order_freedom": {
                    "order": 50.0,
                    "freedom": 50.0,
                    "meaning": "Security requires some constraint on liberty",
                },
            },
            "separation_balance": {
                "executive": 33.3,
                "legislative": 33.3,
                "judicial": 33.3,
                "description": "Three branches check each other",
            },
            "meta_meaning": "Political Science demonstrates META 50/50 in power-liberty balance",
        }


def create_political_science_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> PoliticalScienceDomain:
    """
    Factory function to create a fully initialized political science domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized PoliticalScienceDomain
    """
    domain = PoliticalScienceDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_political_systems()
        domain.initialize_ideologies()
        domain.initialize_government_types()
        domain.initialize_political_pairs()

    return domain
