"""
Law Domain
==========
Law knowledge domain with META 50/50 equilibrium.
Fundamental duality: Rights/Duties (entitlements vs obligations).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class LawDomain(KnowledgeDomain):
    """
    Law knowledge domain.

    Fundamental Duality: Rights / Duties
    - Rights: Entitlements, freedoms, legal claims
    - Duties: Obligations, responsibilities, legal requirements

    Secondary Dualities:
    - Public / Private
    - Criminal / Civil
    - Positive / Natural
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Law",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of rules enforced through social institutions",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Rights/Duties duality."""
        self._domain.set_duality(
            positive_name="rights",
            positive_value=50,
            negative_name="duties",
            negative_value=50,
            duality_name="law_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental legal principles."""
        principles = [
            (
                "Rule of Law",
                "Law applies equally to all",
            ),
            (
                "Due Process",
                "Fair procedures must be followed",
            ),
            (
                "Presumption of Innocence",
                "Accused is innocent until proven guilty",
            ),
            (
                "Stare Decisis",
                "Courts follow precedent",
            ),
            (
                "Nullum Crimen Sine Lege",
                "No crime without law defining it",
            ),
            (
                "Pacta Sunt Servanda",
                "Agreements must be kept",
            ),
            (
                "Natural Justice",
                "Fair hearing and impartial judge",
            ),
            (
                "Equality Before Law",
                "Equal treatment regardless of status",
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=95,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental law concepts."""
        return [
            "Law",
            "Right",
            "Duty",
            "Justice",
            "Equity",
            "Contract",
            "Crime",
            "Punishment",
            "Court",
            "Judge",
            "Precedent",
            "Statute",
            "Constitution",
            "Liability",
            "Remedy",
        ]

    def initialize_branches(self) -> None:
        """Initialize major law branches."""
        branches = [
            (
                "Constitutional Law",
                "Fundamental government structure",
                ConceptType.THEORY,
            ),
            (
                "Criminal Law",
                "Offenses against society",
                ConceptType.THEORY,
            ),
            (
                "Civil Law",
                "Private disputes between parties",
                ConceptType.THEORY,
            ),
            (
                "Contract Law",
                "Enforceable agreements",
                ConceptType.THEORY,
            ),
            (
                "Tort Law",
                "Civil wrongs and remedies",
                ConceptType.THEORY,
            ),
            (
                "Property Law",
                "Ownership and possession",
                ConceptType.THEORY,
            ),
            (
                "Administrative Law",
                "Government agency actions",
                ConceptType.THEORY,
            ),
            (
                "International Law",
                "Relations between states",
                ConceptType.THEORY,
            ),
            (
                "Corporate Law",
                "Business organizations",
                ConceptType.THEORY,
            ),
            (
                "Family Law",
                "Marriage, divorce, children",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_legal_systems(self) -> None:
        """Initialize legal system types."""
        systems = [
            ("Common Law", "Case law and precedent", "UK, USA, Australia"),
            ("Civil Law", "Codified statutes", "France, Germany, Japan"),
            ("Religious Law", "Divine law", "Islamic Sharia, Canon Law"),
            ("Customary Law", "Traditional practices", "Indigenous systems"),
            ("Mixed Systems", "Multiple traditions", "South Africa, Scotland"),
        ]

        for name, description, examples in systems:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_legal_theories(self) -> None:
        """Initialize legal theories."""
        theories = [
            ("Natural Law", "Aquinas/Locke", "Law derives from morality"),
            ("Legal Positivism", "Austin/Hart", "Law is command of sovereign"),
            ("Legal Realism", "Holmes", "Law is what courts do"),
            ("Critical Legal Studies", "Unger", "Law reflects power"),
            ("Feminist Jurisprudence", "MacKinnon", "Law reflects patriarchy"),
            ("Law and Economics", "Posner", "Efficiency analysis of law"),
        ]

        for name, founder, description in theories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_court_hierarchy(self) -> None:
        """Initialize court hierarchy."""
        courts = [
            ("Supreme Court", "Highest appellate court", "Final interpretation"),
            ("Appellate Court", "Reviews lower court decisions", "Error correction"),
            ("Trial Court", "Original jurisdiction", "Fact finding"),
            ("Specialized Court", "Limited jurisdiction", "Tax, bankruptcy"),
        ]

        for name, description, function in courts:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["function"] = function

    def initialize_legal_pairs(self) -> None:
        """Initialize fundamental legal pairs with META 50/50 balance."""
        pairs = [
            ("Rights", "Duties", "Entitlements vs obligations"),
            ("Public", "Private", "State vs individual"),
            ("Criminal", "Civil", "Prosecution vs dispute"),
            ("Plaintiff", "Defendant", "Accuser vs accused"),
            ("Prosecution", "Defense", "State vs accused"),
            ("Statute", "Precedent", "Written vs case law"),
            ("Substantive", "Procedural", "What vs how"),
            ("Guilt", "Innocence", "Liable vs not liable"),
            ("Legal", "Illegal", "Permitted vs prohibited"),
            ("Legitimate", "Illegitimate", "Valid vs invalid"),
            ("Justice", "Injustice", "Fair vs unfair"),
            ("Equity", "Law", "Fairness vs strict rule"),
            ("Intent", "Negligence", "Purposeful vs careless"),
            ("Contract", "Tort", "Agreement vs wrong"),
            ("Liability", "Immunity", "Responsible vs protected"),
            ("Remedy", "Harm", "Cure vs injury"),
            ("Majority", "Dissent", "Main vs differing opinion"),
            ("Appeal", "Affirm", "Challenge vs uphold"),
            ("De Jure", "De Facto", "In law vs in fact"),
            ("Formal", "Informal", "Official vs unofficial"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Law)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Law)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_hohfeld_relations(self) -> dict[str, str]:
        """Get Hohfeld's fundamental legal relations."""
        return {
            "right_duty": "Claim right correlates with duty",
            "privilege_no_right": "Liberty correlates with no-right",
            "power_liability": "Power correlates with liability",
            "immunity_disability": "Immunity correlates with disability",
        }

    def demonstrate_law_balance(self) -> dict[str, Any]:
        """Demonstrate law balance principles."""
        return {
            "concept": "Law Equilibrium",
            "dualities": {
                "rights_duties": {
                    "rights": 50.0,
                    "duties": 50.0,
                    "meaning": "Every right implies a correlative duty",
                },
                "public_private": {
                    "public": 50.0,
                    "private": 50.0,
                    "meaning": "State and individual interests balanced",
                },
                "justice_mercy": {
                    "justice": 50.0,
                    "mercy": 50.0,
                    "meaning": "Strict law tempered by equity",
                },
            },
            "adversarial_balance": {
                "prosecution": 50.0,
                "defense": 50.0,
                "description": "Both sides equally heard",
            },
            "meta_meaning": "Law demonstrates META 50/50 in rights-duties correlation",
        }


def create_law_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> LawDomain:
    """
    Factory function to create a fully initialized law domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized LawDomain
    """
    domain = LawDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_legal_systems()
        domain.initialize_legal_theories()
        domain.initialize_court_hierarchy()
        domain.initialize_legal_pairs()

    return domain
