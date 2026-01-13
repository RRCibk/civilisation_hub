"""
Sociobiology Domain
===================
Sociobiology knowledge domain with META 50/50 equilibrium.
Fundamental duality: Nature/Nurture (genes vs environment).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class SociobiologyDomain(KnowledgeDomain):
    """
    Sociobiology knowledge domain.

    Fundamental Duality: Nature / Nurture
    - Nature: Genetic influences, evolutionary heritage
    - Nurture: Environmental influences, learning, culture

    Secondary Dualities:
    - Selfish / Altruistic
    - Individual / Group
    - Proximate / Ultimate
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Sociobiology",
            domain_type=DomainType.FUNDAMENTAL,
            description="The biological basis of social behavior",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Nature/Nurture duality."""
        self._domain.set_duality(
            positive_name="nature",
            positive_value=50,
            negative_name="nurture",
            negative_value=50,
            duality_name="sociobiology_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental sociobiology principles."""
        principles = [
            (
                "Natural Selection",
                "Behavior shaped by reproductive success",
            ),
            (
                "Inclusive Fitness",
                "Genes spread through relatives too",
            ),
            (
                "Reciprocal Altruism",
                "Cooperation benefits both parties",
            ),
            (
                "Kin Selection",
                "Help relatives who share genes",
            ),
            (
                "Sexual Selection",
                "Mate choice shapes traits",
            ),
            (
                "Gene-Culture Coevolution",
                "Genes and culture interact",
            ),
            (
                "Behavioral Ecology",
                "Behavior adapts to environment",
            ),
            (
                "Evolutionary Psychology",
                "Mind evolved for ancestral problems",
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
        """Get fundamental sociobiology concepts."""
        return [
            "Gene",
            "Behavior",
            "Fitness",
            "Selection",
            "Altruism",
            "Cooperation",
            "Competition",
            "Kin",
            "Mating",
            "Aggression",
            "Dominance",
            "Territory",
            "Parenting",
            "Communication",
            "Adaptation",
        ]

    def initialize_branches(self) -> None:
        """Initialize major sociobiology branches."""
        branches = [
            (
                "Evolutionary Psychology",
                "Human mind evolution",
                ConceptType.THEORY,
            ),
            (
                "Behavioral Ecology",
                "Ecological context of behavior",
                ConceptType.THEORY,
            ),
            (
                "Human Sociobiology",
                "Human social behavior",
                ConceptType.THEORY,
            ),
            (
                "Animal Behavior",
                "Non-human social behavior",
                ConceptType.THEORY,
            ),
            (
                "Evolutionary Genetics",
                "Genetic basis of behavior",
                ConceptType.THEORY,
            ),
            (
                "Sexual Selection Theory",
                "Mate choice evolution",
                ConceptType.THEORY,
            ),
            (
                "Kin Selection Theory",
                "Relatedness and altruism",
                ConceptType.THEORY,
            ),
            (
                "Game Theory Biology",
                "Strategic behavior",
                ConceptType.THEORY,
            ),
            (
                "Comparative Psychology",
                "Cross-species comparison",
                ConceptType.THEORY,
            ),
            (
                "Gene-Culture Theory",
                "Dual inheritance",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_behaviors(self) -> None:
        """Initialize social behaviors."""
        behaviors = [
            ("Altruism", "Helping others at cost", "Cooperation"),
            ("Aggression", "Harmful behavior", "Competition"),
            ("Parental Care", "Investment in offspring", "Reproduction"),
            ("Mate Choice", "Selecting partners", "Reproduction"),
            ("Territoriality", "Defending space", "Resource"),
            ("Dominance", "Social rank", "Hierarchy"),
        ]

        for name, description, category in behaviors:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_strategies(self) -> None:
        """Initialize evolutionary strategies."""
        strategies = [
            ("ESS", "Evolutionarily stable strategy", "Game theory"),
            ("Tit-for-Tat", "Reciprocate cooperation", "Reciprocity"),
            ("Hawk-Dove", "Aggression vs display", "Conflict"),
            ("Producer-Scrounger", "Find vs steal", "Foraging"),
            ("Sneaker Male", "Alternative mating", "Reproduction"),
            ("Bet-Hedging", "Spread risk", "Uncertainty"),
        ]

        for name, description, context in strategies:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["context"] = context

    def initialize_sociobiology_pairs(self) -> None:
        """Initialize fundamental sociobiology pairs with META 50/50 balance."""
        pairs = [
            ("Nature", "Nurture", "Genes vs environment"),
            ("Selfish", "Altruistic", "Self-interest vs helping"),
            ("Individual", "Group", "Personal vs collective"),
            ("Proximate", "Ultimate", "How vs why"),
            ("Cooperation", "Competition", "Together vs against"),
            ("Male", "Female", "Male vs female strategies"),
            ("Kin", "Non-kin", "Relatives vs strangers"),
            ("Innate", "Learned", "Hardwired vs acquired"),
            ("Adaptive", "Maladaptive", "Fit vs unfit"),
            ("Direct", "Indirect", "Personal vs kin fitness"),
            ("Monogamy", "Polygamy", "One vs multiple mates"),
            ("K-Selected", "r-Selected", "Quality vs quantity"),
            ("Honest", "Deceptive", "True vs false signals"),
            ("Parental", "Mating", "Care vs reproduction effort"),
            ("Genetic", "Cultural", "DNA vs learning"),
            ("Conservative", "Variable", "Fixed vs flexible"),
            ("Short-term", "Long-term", "Immediate vs delayed"),
            ("Overt", "Covert", "Open vs hidden"),
            ("Obligate", "Facultative", "Required vs optional"),
            ("Ancestral", "Derived", "Original vs new"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Sociobio)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Sociobio)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_hamilton_rule(self) -> dict[str, str]:
        """Get Hamilton's rule for altruism."""
        return {
            "formula": "rB > C",
            "r": "Relatedness coefficient",
            "B": "Benefit to recipient",
            "C": "Cost to actor",
            "meaning": "Help when benefit times relatedness exceeds cost",
        }

    def demonstrate_sociobiology_balance(self) -> dict[str, Any]:
        """Demonstrate sociobiology balance principles."""
        return {
            "concept": "Sociobiology Equilibrium",
            "dualities": {
                "nature_nurture": {
                    "nature": 50.0,
                    "nurture": 50.0,
                    "meaning": "Genes and environment both matter",
                },
                "selfish_altruistic": {
                    "selfish": 50.0,
                    "altruistic": 50.0,
                    "meaning": "Self-interest and helping coexist",
                },
                "cooperation_competition": {
                    "cooperation": 50.0,
                    "competition": 50.0,
                    "meaning": "Working together and against",
                },
            },
            "evolution_balance": {
                "individual": 50.0,
                "group": 50.0,
                "description": "Multiple levels of selection",
            },
            "meta_meaning": "Sociobiology demonstrates META 50/50 in nature-nurture synthesis",
        }


def create_sociobiology_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> SociobiologyDomain:
    """
    Factory function to create a fully initialized sociobiology domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized SociobiologyDomain
    """
    domain = SociobiologyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_behaviors()
        domain.initialize_strategies()
        domain.initialize_sociobiology_pairs()

    return domain
