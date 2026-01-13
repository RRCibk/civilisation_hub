"""
Bioethics Domain
================
Bioethics knowledge domain with META 50/50 equilibrium.
Fundamental duality: Life/Choice (sanctity vs autonomy).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class BioethicsDomain(KnowledgeDomain):
    """
    Bioethics knowledge domain.

    Fundamental Duality: Life / Choice
    - Life: Sanctity of life, preservation, protection
    - Choice: Autonomy, self-determination, freedom

    Secondary Dualities:
    - Benefit / Harm
    - Individual / Society
    - Natural / Artificial
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Bioethics",
            domain_type=DomainType.FUNDAMENTAL,
            description="The ethics of biological and medical sciences",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Life/Choice duality."""
        self._domain.set_duality(
            positive_name="life",
            positive_value=50,
            negative_name="choice",
            negative_value=50,
            duality_name="bioethics_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental bioethics principles."""
        principles = [
            (
                "Respect for Autonomy",
                "Honor individual self-determination",
            ),
            (
                "Beneficence",
                "Act for patient's benefit",
            ),
            (
                "Non-maleficence",
                "Do no harm",
            ),
            (
                "Justice",
                "Fair distribution of benefits and burdens",
            ),
            (
                "Informed Consent",
                "Voluntary agreement with understanding",
            ),
            (
                "Dignity",
                "Respect inherent human worth",
            ),
            (
                "Vulnerability",
                "Protect those who cannot protect themselves",
            ),
            (
                "Solidarity",
                "Support for collective well-being",
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
        """Get fundamental bioethics concepts."""
        return [
            "Autonomy",
            "Consent",
            "Dignity",
            "Justice",
            "Harm",
            "Benefit",
            "Rights",
            "Duty",
            "Life",
            "Death",
            "Privacy",
            "Confidentiality",
            "Research",
            "Treatment",
            "Enhancement",
        ]

    def initialize_branches(self) -> None:
        """Initialize major bioethics branches."""
        branches = [
            (
                "Medical Ethics",
                "Clinical practice ethics",
                ConceptType.THEORY,
            ),
            (
                "Research Ethics",
                "Human subjects research",
                ConceptType.THEORY,
            ),
            (
                "Clinical Ethics",
                "Bedside decisions",
                ConceptType.THEORY,
            ),
            (
                "Public Health Ethics",
                "Population-level ethics",
                ConceptType.THEORY,
            ),
            (
                "Neuroethics",
                "Brain and behavior ethics",
                ConceptType.THEORY,
            ),
            (
                "Environmental Ethics",
                "Nature and ecology ethics",
                ConceptType.THEORY,
            ),
            (
                "Animal Ethics",
                "Non-human animal welfare",
                ConceptType.THEORY,
            ),
            (
                "Reproductive Ethics",
                "Reproduction and genetics",
                ConceptType.THEORY,
            ),
            (
                "End-of-Life Ethics",
                "Death and dying",
                ConceptType.THEORY,
            ),
            (
                "Global Bioethics",
                "International perspectives",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_issues(self) -> None:
        """Initialize major bioethical issues."""
        issues = [
            ("Euthanasia", "Assisted dying", "End-of-life"),
            ("Abortion", "Pregnancy termination", "Reproductive"),
            ("Genetic Enhancement", "Genetic modification", "Biotechnology"),
            ("Cloning", "Reproductive cloning", "Biotechnology"),
            ("Organ Allocation", "Transplant distribution", "Resource"),
            ("Clinical Trials", "Research participation", "Research"),
        ]

        for name, description, category in issues:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_frameworks(self) -> None:
        """Initialize ethical frameworks."""
        frameworks = [
            ("Principlism", "Beauchamp & Childress", "Four principles approach"),
            ("Virtue Ethics", "Aristotle", "Character-based"),
            ("Deontology", "Kant", "Duty-based"),
            ("Consequentialism", "Mill", "Outcome-based"),
            ("Care Ethics", "Gilligan", "Relationship-based"),
            ("Casuistry", "Jonsen", "Case-based reasoning"),
        ]

        for name, source, description in frameworks:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["source"] = source

    def initialize_bioethics_pairs(self) -> None:
        """Initialize fundamental bioethics pairs with META 50/50 balance."""
        pairs = [
            ("Life", "Choice", "Sanctity vs autonomy"),
            ("Benefit", "Harm", "Good vs bad outcomes"),
            ("Individual", "Society", "Person vs collective"),
            ("Natural", "Artificial", "Given vs made"),
            ("Rights", "Duties", "Entitlements vs obligations"),
            ("Autonomy", "Paternalism", "Self-rule vs protection"),
            ("Privacy", "Transparency", "Hidden vs open"),
            ("Treatment", "Enhancement", "Cure vs improve"),
            ("Quality", "Sanctity", "Life quality vs life itself"),
            ("Present", "Future", "Current vs coming generations"),
            ("Human", "Non-human", "People vs animals"),
            ("Research", "Treatment", "Knowledge vs care"),
            ("Universal", "Cultural", "Global vs local values"),
            ("Consent", "Override", "Agreement vs exception"),
            ("Active", "Passive", "Doing vs allowing"),
            ("Ordinary", "Extraordinary", "Standard vs heroic"),
            ("Withholding", "Withdrawing", "Not starting vs stopping"),
            ("Competent", "Incompetent", "Capable vs incapable"),
            ("Voluntary", "Involuntary", "Willing vs forced"),
            ("Disclosure", "Concealment", "Telling vs hiding"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Bioethics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Bioethics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_belmont_principles(self) -> dict[str, str]:
        """Get Belmont Report principles."""
        return {
            "respect_for_persons": "Autonomy and protection of vulnerable",
            "beneficence": "Maximize benefits, minimize harms",
            "justice": "Fair selection and distribution",
        }

    def demonstrate_bioethics_balance(self) -> dict[str, Any]:
        """Demonstrate bioethics balance principles."""
        return {
            "concept": "Bioethics Equilibrium",
            "dualities": {
                "life_choice": {
                    "life": 50.0,
                    "choice": 50.0,
                    "meaning": "Sanctity and autonomy both valued",
                },
                "benefit_harm": {
                    "benefit": 50.0,
                    "harm": 50.0,
                    "meaning": "Weighing good against bad",
                },
                "individual_society": {
                    "individual": 50.0,
                    "society": 50.0,
                    "meaning": "Personal and collective interests",
                },
            },
            "ethical_balance": {
                "rights": 50.0,
                "responsibilities": 50.0,
                "description": "Claims and duties balance",
            },
            "meta_meaning": "Bioethics demonstrates META 50/50 in life-choice equilibrium",
        }


def create_bioethics_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> BioethicsDomain:
    """
    Factory function to create a fully initialized bioethics domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized BioethicsDomain
    """
    domain = BioethicsDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_issues()
        domain.initialize_frameworks()
        domain.initialize_bioethics_pairs()

    return domain
