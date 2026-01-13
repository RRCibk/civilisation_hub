"""
Social Work Domain
==================
Social Work knowledge domain with META 50/50 equilibrium.
Fundamental duality: Person/Environment (individual vs context).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class SocialWorkDomain(KnowledgeDomain):
    """
    Social Work knowledge domain.

    Fundamental Duality: Person / Environment
    - Person: Individual needs, strengths, agency
    - Environment: Social context, systems, structures

    Secondary Dualities:
    - Clinical / Macro
    - Support / Challenge
    - Empowerment / Protection
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="SocialWork",
            domain_type=DomainType.FUNDAMENTAL,
            description="The profession promoting social change and well-being",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Person/Environment duality."""
        self._domain.set_duality(
            positive_name="person",
            positive_value=50,
            negative_name="environment",
            negative_value=50,
            duality_name="social_work_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental social work principles."""
        principles = [
            ("Human Dignity", "Inherent worth of every person"),
            ("Social Justice", "Challenge injustice and inequality"),
            ("Self-Determination", "Respect client autonomy"),
            ("Integrity", "Behave in trustworthy manner"),
            ("Competence", "Practice within expertise"),
            ("Service", "Primary goal is to help"),
            ("Human Relationships", "Relationships are central to change"),
            ("Confidentiality", "Protect client information"),
        ]

        for name, description in principles:
            self.create_concept(name, ConceptType.PRINCIPLE, description, certainty=90)

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental social work concepts."""
        return ["Client", "Assessment", "Intervention", "Advocacy", "Case Management",
                "Empowerment", "Strengths", "Systems", "Crisis", "Support",
                "Resources", "Boundaries", "Ethics", "Supervision", "Community"]

    def initialize_branches(self) -> None:
        """Initialize major social work branches."""
        branches = [
            ("Clinical Social Work", "Mental health treatment", ConceptType.THEORY),
            ("Child Welfare", "Child protection services", ConceptType.THEORY),
            ("Medical Social Work", "Healthcare settings", ConceptType.THEORY),
            ("School Social Work", "Educational settings", ConceptType.THEORY),
            ("Gerontological Social Work", "Elderly services", ConceptType.THEORY),
            ("Community Organization", "Macro-level change", ConceptType.THEORY),
            ("Policy Practice", "Social policy work", ConceptType.THEORY),
            ("Forensic Social Work", "Criminal justice", ConceptType.THEORY),
            ("Military Social Work", "Armed forces support", ConceptType.THEORY),
            ("International Social Work", "Global practice", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_methods(self) -> None:
        """Initialize social work methods."""
        methods = [
            ("Casework", "Individual practice", "Micro"),
            ("Group Work", "Small group practice", "Mezzo"),
            ("Community Work", "Community practice", "Macro"),
            ("Administration", "Organizational management", "Macro"),
            ("Research", "Knowledge development", "All levels"),
            ("Policy", "Policy development", "Macro"),
        ]

        for name, description, level in methods:
            concept = self.create_concept(name, ConceptType.DEFINITION, description)
            concept.metadata["level"] = level

    def initialize_social_work_pairs(self) -> None:
        """Initialize fundamental social work pairs with META 50/50 balance."""
        pairs = [
            ("Person", "Environment", "Individual vs context"),
            ("Clinical", "Macro", "Direct vs systemic practice"),
            ("Support", "Challenge", "Nurture vs confront"),
            ("Empowerment", "Protection", "Enable vs safeguard"),
            ("Strengths", "Problems", "Assets vs deficits"),
            ("Process", "Outcome", "Journey vs result"),
            ("Client", "System", "Person vs institution"),
            ("Voluntary", "Involuntary", "Willing vs mandated"),
            ("Prevention", "Intervention", "Before vs after"),
            ("Direct", "Indirect", "Hands-on vs advocacy"),
            ("Short-term", "Long-term", "Brief vs extended"),
            ("Individual", "Family", "Person vs unit"),
            ("Engagement", "Termination", "Begin vs end"),
            ("Assessment", "Action", "Understand vs do"),
            ("Boundaries", "Flexibility", "Limits vs adaptation"),
            ("Evidence", "Intuition", "Research vs practice wisdom"),
            ("Specialist", "Generalist", "Focused vs broad"),
            ("Crisis", "Stabilization", "Acute vs chronic"),
            ("Rights", "Responsibilities", "Entitlements vs duties"),
            ("Self-Disclosure", "Privacy", "Share vs withhold"),
        ]

        for positive, negative, description in pairs:
            pos = self.create_concept(f"{positive} (Social Work)", ConceptType.DEFINITION,
                                       f"Positive pole: {description.split(' vs ')[0]}")
            neg = self.create_concept(f"{negative} (Social Work)", ConceptType.DEFINITION,
                                       f"Negative pole: {description.split(' vs ')[1]}")
            self.create_relation(pos, neg, RelationType.CONTRADICTS, strength=50)

    def demonstrate_social_work_balance(self) -> dict[str, Any]:
        """Demonstrate social work balance principles."""
        return {
            "concept": "Social Work Equilibrium",
            "dualities": {
                "person_environment": {"person": 50.0, "environment": 50.0,
                    "meaning": "Balance individual and systemic focus"},
                "support_challenge": {"support": 50.0, "challenge": 50.0,
                    "meaning": "Balance nurturing with growth"},
            },
            "meta_meaning": "Social Work demonstrates META 50/50 in person-environment balance",
        }


def create_social_work_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> SocialWorkDomain:
    domain = SocialWorkDomain(meta_equilibrium)
    if initialize_all:
        domain.initialize_branches()
        domain.initialize_methods()
        domain.initialize_social_work_pairs()
    return domain
