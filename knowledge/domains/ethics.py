"""
Ethics Domain
=============
Ethics knowledge domain with META 50/50 equilibrium.
Fundamental duality: Right/Wrong (good vs bad action).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class EthicsDomain(KnowledgeDomain):
    """
    Ethics knowledge domain.

    Fundamental Duality: Right / Wrong
    - Right: Good, moral, virtuous, permissible
    - Wrong: Bad, immoral, vicious, impermissible

    Secondary Dualities:
    - Duty / Consequence
    - Individual / Society
    - Absolute / Relative
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Ethics",
            domain_type=DomainType.FUNDAMENTAL,
            description="The philosophical study of morality and right conduct",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Right/Wrong duality."""
        self._domain.set_duality(
            positive_name="right",
            positive_value=50,
            negative_name="wrong",
            negative_value=50,
            duality_name="ethics_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental ethical principles."""
        principles = [
            (
                "Universalizability",
                "Moral principles apply to all similar cases",
            ),
            (
                "Ought Implies Can",
                "Obligation requires ability",
            ),
            (
                "Moral Responsibility",
                "Agents are accountable for choices",
            ),
            (
                "Harm Principle",
                "Prevent harm to others",
            ),
            (
                "Golden Rule",
                "Treat others as you wish to be treated",
            ),
            (
                "Autonomy",
                "Respect for persons as self-governing",
            ),
            (
                "Justice",
                "Give each their due",
            ),
            (
                "Beneficence",
                "Act for the good of others",
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
        """Get fundamental ethics concepts."""
        return [
            "Good",
            "Right",
            "Duty",
            "Virtue",
            "Justice",
            "Autonomy",
            "Responsibility",
            "Consequence",
            "Intention",
            "Harm",
            "Benefit",
            "Rights",
            "Obligation",
            "Value",
            "Character",
        ]

    def initialize_branches(self) -> None:
        """Initialize major ethics branches."""
        branches = [
            (
                "Metaethics",
                "Nature of moral concepts",
                ConceptType.THEORY,
            ),
            (
                "Normative Ethics",
                "Standards of right action",
                ConceptType.THEORY,
            ),
            (
                "Applied Ethics",
                "Specific moral problems",
                ConceptType.THEORY,
            ),
            (
                "Virtue Ethics",
                "Character-based ethics",
                ConceptType.THEORY,
            ),
            (
                "Deontology",
                "Duty-based ethics",
                ConceptType.THEORY,
            ),
            (
                "Consequentialism",
                "Outcome-based ethics",
                ConceptType.THEORY,
            ),
            (
                "Care Ethics",
                "Relationship-based ethics",
                ConceptType.THEORY,
            ),
            (
                "Environmental Ethics",
                "Ethics of nature",
                ConceptType.THEORY,
            ),
            (
                "Bioethics",
                "Ethics of medicine and life",
                ConceptType.THEORY,
            ),
            (
                "Business Ethics",
                "Ethics in commerce",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_ethical_theories(self) -> None:
        """Initialize major ethical theories."""
        theories = [
            ("Utilitarianism", "Mill", "Greatest good for greatest number"),
            ("Kantian Ethics", "Kant", "Categorical imperative"),
            ("Virtue Ethics", "Aristotle", "Character and flourishing"),
            ("Social Contract", "Rawls", "Justice as fairness"),
            ("Natural Law", "Aquinas", "Reason discerns moral law"),
            ("Emotivism", "Ayer", "Moral statements express attitudes"),
            ("Care Ethics", "Gilligan", "Ethics of relationships"),
            ("Divine Command", "Various", "God determines morality"),
        ]

        for name, founder, description in theories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_virtues(self) -> None:
        """Initialize classical virtues."""
        virtues = [
            ("Courage", "Facing fear appropriately", "Cardinal"),
            ("Temperance", "Moderation in desire", "Cardinal"),
            ("Justice", "Giving each their due", "Cardinal"),
            ("Prudence", "Practical wisdom", "Cardinal"),
            ("Faith", "Trust in God", "Theological"),
            ("Hope", "Expectation of good", "Theological"),
            ("Charity", "Love of neighbor", "Theological"),
        ]

        for name, description, category in virtues:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_ethical_concepts(self) -> None:
        """Initialize key ethical concepts."""
        concepts = [
            ("Moral Agent", "Being capable of moral action", "Responsibility"),
            ("Moral Patient", "Being affected by moral action", "Consideration"),
            ("Intrinsic Value", "Good in itself", "Ends"),
            ("Instrumental Value", "Good as means", "Tools"),
            ("Supererogation", "Beyond duty", "Saintly acts"),
        ]

        for name, description, category in concepts:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_ethical_pairs(self) -> None:
        """Initialize fundamental ethical pairs with META 50/50 balance."""
        pairs = [
            ("Right", "Wrong", "Good vs bad action"),
            ("Duty", "Consequence", "Obligation vs outcome"),
            ("Individual", "Society", "Self vs others"),
            ("Absolute", "Relative", "Universal vs contextual"),
            ("Virtue", "Vice", "Excellence vs defect"),
            ("Act", "Omission", "Doing vs not doing"),
            ("Intention", "Outcome", "Motive vs result"),
            ("Justice", "Mercy", "Desert vs compassion"),
            ("Rights", "Responsibilities", "Claims vs duties"),
            ("Autonomy", "Beneficence", "Self-rule vs care"),
            ("Egoism", "Altruism", "Self vs other interest"),
            ("Moral", "Legal", "Ethics vs law"),
            ("Objective", "Subjective", "Universal vs personal"),
            ("Deontology", "Teleology", "Rules vs goals"),
            ("Agent", "Patient", "Actor vs affected"),
            ("Means", "Ends", "Method vs purpose"),
            ("Theory", "Practice", "Abstract vs applied"),
            ("Permitted", "Forbidden", "Allowed vs prohibited"),
            ("Obligatory", "Supererogatory", "Required vs beyond"),
            ("Natural", "Conventional", "Inherent vs agreed"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Ethics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Ethics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_categorical_imperative(self) -> dict[str, str]:
        """Get Kant's formulations of categorical imperative."""
        return {
            "universality": "Act only on maxims you could will as universal law",
            "humanity": "Treat humanity never merely as means but always as end",
            "autonomy": "Act as if a legislating member of kingdom of ends",
        }

    def demonstrate_ethics_balance(self) -> dict[str, Any]:
        """Demonstrate ethics balance principles."""
        return {
            "concept": "Ethics Equilibrium",
            "dualities": {
                "right_wrong": {
                    "right": 50.0,
                    "wrong": 50.0,
                    "meaning": "Moral judgment distinguishes good and bad",
                },
                "duty_consequence": {
                    "duty": 50.0,
                    "consequence": 50.0,
                    "meaning": "Both rules and outcomes matter",
                },
                "individual_society": {
                    "individual": 50.0,
                    "society": 50.0,
                    "meaning": "Personal and social ethics interrelated",
                },
            },
            "virtue_balance": {
                "excess": 0.0,
                "mean": 100.0,
                "deficiency": 0.0,
                "description": "Virtue is the mean between extremes",
            },
            "meta_meaning": "Ethics demonstrates META 50/50 in right-wrong discernment",
        }


def create_ethics_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> EthicsDomain:
    """
    Factory function to create a fully initialized ethics domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized EthicsDomain
    """
    domain = EthicsDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_ethical_theories()
        domain.initialize_virtues()
        domain.initialize_ethical_concepts()
        domain.initialize_ethical_pairs()

    return domain
