"""
Human Resources Domain
======================
Human Resources knowledge domain with META 50/50 equilibrium.
Fundamental duality: Organization/Individual (company vs employee).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class HumanResourcesDomain(KnowledgeDomain):
    """
    Human Resources knowledge domain.

    Fundamental Duality: Organization / Individual
    - Organization: Company needs, business goals
    - Individual: Employee needs, personal development

    Secondary Dualities:
    - Strategic / Operational
    - Hire / Develop
    - Performance / Potential
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="HumanResources",
            domain_type=DomainType.FUNDAMENTAL,
            description="The management of people in organizations",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Organization/Individual duality."""
        self._domain.set_duality(
            positive_name="organization",
            positive_value=50,
            negative_name="individual",
            negative_value=50,
            duality_name="hr_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental HR principles."""
        principles = [
            ("People as Assets", "Employees are valuable resources"),
            ("Strategic Alignment", "HR supports business strategy"),
            ("Fair Treatment", "Treat employees equitably"),
            ("Development", "Invest in employee growth"),
            ("Performance Management", "Measure and improve performance"),
            ("Engagement", "Engaged employees perform better"),
            ("Compliance", "Follow employment laws"),
            ("Culture", "Culture drives behavior"),
        ]

        for name, description in principles:
            self.create_concept(name, ConceptType.PRINCIPLE, description, certainty=85)

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental HR concepts."""
        return ["Recruitment", "Selection", "Training", "Development", "Compensation",
                "Benefits", "Performance", "Engagement", "Culture", "Retention",
                "Succession", "Compliance", "Diversity", "Leadership", "Talent"]

    def initialize_branches(self) -> None:
        """Initialize major HR branches."""
        branches = [
            ("Talent Acquisition", "Recruiting and hiring", ConceptType.THEORY),
            ("Learning and Development", "Training programs", ConceptType.THEORY),
            ("Compensation and Benefits", "Total rewards", ConceptType.THEORY),
            ("Performance Management", "Goal setting and review", ConceptType.THEORY),
            ("Employee Relations", "Workplace issues", ConceptType.THEORY),
            ("HR Analytics", "People data", ConceptType.THEORY),
            ("Organizational Development", "Change management", ConceptType.THEORY),
            ("Diversity and Inclusion", "Workforce diversity", ConceptType.THEORY),
            ("HR Technology", "HR systems", ConceptType.THEORY),
            ("Strategic HR", "Business partnership", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_lifecycle(self) -> None:
        """Initialize employee lifecycle stages."""
        stages = [
            ("Attract", "Employer branding", "Pre-hire"),
            ("Recruit", "Candidate sourcing", "Acquisition"),
            ("Onboard", "New hire integration", "Entry"),
            ("Develop", "Growth and learning", "Tenure"),
            ("Retain", "Engagement and rewards", "Tenure"),
            ("Separate", "Exit management", "Departure"),
        ]

        for name, description, phase in stages:
            concept = self.create_concept(name, ConceptType.DEFINITION, description)
            concept.metadata["phase"] = phase

    def initialize_hr_pairs(self) -> None:
        """Initialize fundamental HR pairs with META 50/50 balance."""
        pairs = [
            ("Organization", "Individual", "Company vs employee"),
            ("Strategic", "Operational", "Big picture vs day-to-day"),
            ("Hire", "Develop", "Buy vs build talent"),
            ("Performance", "Potential", "Current vs future"),
            ("Intrinsic", "Extrinsic", "Internal vs external motivation"),
            ("Centralized", "Decentralized", "Corporate vs local"),
            ("Generalist", "Specialist", "Broad vs deep"),
            ("Internal", "External", "Promote vs hire"),
            ("Hard Skills", "Soft Skills", "Technical vs interpersonal"),
            ("Short-term", "Long-term", "Immediate vs future"),
            ("Quantitative", "Qualitative", "Metrics vs judgment"),
            ("Compliance", "Culture", "Rules vs values"),
            ("Cost", "Investment", "Expense vs return"),
            ("Uniformity", "Flexibility", "Standard vs customized"),
            ("Individual", "Team", "Person vs group"),
            ("Formal", "Informal", "Structured vs casual"),
            ("Merit", "Tenure", "Performance vs time"),
            ("Fixed", "Variable", "Base vs bonus pay"),
            ("Local", "Global", "Regional vs worldwide"),
            ("Reactive", "Proactive", "Respond vs anticipate"),
        ]

        for positive, negative, description in pairs:
            pos = self.create_concept(f"{positive} (HR)", ConceptType.DEFINITION,
                                       f"Positive pole: {description.split(' vs ')[0]}")
            neg = self.create_concept(f"{negative} (HR)", ConceptType.DEFINITION,
                                       f"Negative pole: {description.split(' vs ')[1]}")
            self.create_relation(pos, neg, RelationType.CONTRADICTS, strength=50)

    def demonstrate_hr_balance(self) -> dict[str, Any]:
        """Demonstrate HR balance principles."""
        return {
            "concept": "Human Resources Equilibrium",
            "dualities": {
                "organization_individual": {"organization": 50.0, "individual": 50.0,
                    "meaning": "Balance company and employee needs"},
                "performance_potential": {"performance": 50.0, "potential": 50.0,
                    "meaning": "Value current contribution and future growth"},
            },
            "meta_meaning": "Human Resources demonstrates META 50/50 in organization-individual balance",
        }


def create_human_resources_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> HumanResourcesDomain:
    domain = HumanResourcesDomain(meta_equilibrium)
    if initialize_all:
        domain.initialize_branches()
        domain.initialize_lifecycle()
        domain.initialize_hr_pairs()
    return domain
