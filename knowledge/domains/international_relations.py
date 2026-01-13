"""
International Relations Domain
==============================
International relations knowledge domain with META 50/50 equilibrium.
Fundamental duality: Cooperation/Conflict (peace vs war).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class InternationalRelationsDomain(KnowledgeDomain):
    """
    International Relations knowledge domain.

    Fundamental Duality: Cooperation / Conflict
    - Cooperation: Peace, alliance, diplomacy, trade
    - Conflict: War, competition, tension, rivalry

    Secondary Dualities:
    - State / Non-state
    - National / International
    - Power / Interdependence
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="InternationalRelations",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of relations between states and other international actors",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Cooperation/Conflict duality."""
        self._domain.set_duality(
            positive_name="cooperation",
            positive_value=50,
            negative_name="conflict",
            negative_value=50,
            duality_name="international_relations_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental IR principles."""
        principles = [
            (
                "Anarchy",
                "International system lacks overarching authority",
            ),
            (
                "Sovereignty",
                "States are supreme within their territory",
            ),
            (
                "Balance of Power",
                "States seek equilibrium to prevent hegemony",
            ),
            (
                "Security Dilemma",
                "Defensive measures can appear threatening",
            ),
            (
                "Interdependence",
                "States are mutually dependent",
            ),
            (
                "National Interest",
                "States pursue their own interests",
            ),
            (
                "Collective Security",
                "Attack on one is attack on all",
            ),
            (
                "Democratic Peace",
                "Democracies rarely fight each other",
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
        """Get fundamental IR concepts."""
        return [
            "State",
            "Sovereignty",
            "Power",
            "Security",
            "War",
            "Peace",
            "Diplomacy",
            "Alliance",
            "Treaty",
            "International Law",
            "International Organization",
            "Globalization",
            "Hegemony",
            "Balance of Power",
            "National Interest",
        ]

    def initialize_branches(self) -> None:
        """Initialize major IR branches."""
        branches = [
            (
                "International Security",
                "Military and strategic issues",
                ConceptType.THEORY,
            ),
            (
                "International Political Economy",
                "Economic aspects of IR",
                ConceptType.THEORY,
            ),
            (
                "Foreign Policy Analysis",
                "State decision-making",
                ConceptType.THEORY,
            ),
            (
                "International Organization",
                "IGOs and global governance",
                ConceptType.THEORY,
            ),
            (
                "International Law",
                "Legal aspects of IR",
                ConceptType.THEORY,
            ),
            (
                "Diplomatic Studies",
                "Practice of diplomacy",
                ConceptType.THEORY,
            ),
            (
                "Conflict Studies",
                "Causes and resolution of conflict",
                ConceptType.THEORY,
            ),
            (
                "Peace Studies",
                "Conditions for peace",
                ConceptType.THEORY,
            ),
            (
                "Global Governance",
                "Managing global issues",
                ConceptType.THEORY,
            ),
            (
                "Area Studies",
                "Regional international relations",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_theories(self) -> None:
        """Initialize IR theories."""
        theories = [
            ("Realism", "Morgenthau", "Power and national interest"),
            ("Liberalism", "Keohane", "Institutions and cooperation"),
            ("Constructivism", "Wendt", "Ideas and identity"),
            ("Neorealism", "Waltz", "Structural constraints"),
            ("Neoliberalism", "Nye", "Complex interdependence"),
            ("English School", "Bull", "International society"),
            ("Marxism", "Wallerstein", "Economic structures"),
            ("Feminism", "Tickner", "Gender in IR"),
        ]

        for name, founder, description in theories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_actors(self) -> None:
        """Initialize international actors."""
        actors = [
            ("State", "Sovereign political entity", "Primary actor"),
            ("IGO", "Intergovernmental organization", "UN, WTO, NATO"),
            ("NGO", "Non-governmental organization", "Amnesty, Greenpeace"),
            ("MNC", "Multinational corporation", "Economic actors"),
            ("Terrorist Group", "Non-state violent actor", "Security threat"),
            ("Individual", "Leaders, diplomats", "Agency"),
        ]

        for name, description, examples in actors:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_system_types(self) -> None:
        """Initialize international system types."""
        systems = [
            ("Unipolar", "One dominant power", "Post-Cold War US"),
            ("Bipolar", "Two dominant powers", "Cold War"),
            ("Multipolar", "Several great powers", "19th century Europe"),
            ("Hegemonic", "Single hegemon", "Pax Britannica"),
        ]

        for name, description, example in systems:
            concept = self.create_concept(
                name=f"{name} System",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["example"] = example

    def initialize_ir_pairs(self) -> None:
        """Initialize fundamental IR pairs with META 50/50 balance."""
        pairs = [
            ("Cooperation", "Conflict", "Peace vs war"),
            ("State", "Non-state", "Government vs other actors"),
            ("National", "International", "Domestic vs global"),
            ("Power", "Interdependence", "Autonomy vs connection"),
            ("Unilateral", "Multilateral", "Alone vs together"),
            ("Hard Power", "Soft Power", "Coercion vs attraction"),
            ("Security", "Economy", "Military vs trade"),
            ("Bilateral", "Multilateral", "Two vs many parties"),
            ("Idealism", "Realism", "Should vs is"),
            ("Sovereignty", "Intervention", "Non-interference vs action"),
            ("North", "South", "Developed vs developing"),
            ("East", "West", "Eastern vs Western bloc"),
            ("Domestic", "Foreign", "Internal vs external"),
            ("Alliance", "Neutrality", "Aligned vs non-aligned"),
            ("War", "Peace", "Armed vs unarmed"),
            ("Deterrence", "Compellence", "Prevent vs force"),
            ("Integration", "Fragmentation", "Unity vs division"),
            ("Globalization", "Nationalism", "World vs nation"),
            ("Absolute", "Relative", "Total vs comparative gains"),
            ("Status Quo", "Revisionist", "Maintain vs change"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (IR)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (IR)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_levels_of_analysis(self) -> dict[str, str]:
        """Get levels of analysis in IR."""
        return {
            "individual": "Leaders, decision-makers",
            "state": "Domestic politics, regime type",
            "system": "International structure, polarity",
        }

    def demonstrate_ir_balance(self) -> dict[str, Any]:
        """Demonstrate IR balance principles."""
        return {
            "concept": "International Relations Equilibrium",
            "dualities": {
                "cooperation_conflict": {
                    "cooperation": 50.0,
                    "conflict": 50.0,
                    "meaning": "International system combines both",
                },
                "power_interdependence": {
                    "power": 50.0,
                    "interdependence": 50.0,
                    "meaning": "States seek power but are connected",
                },
                "state_non_state": {
                    "state": 50.0,
                    "non_state": 50.0,
                    "meaning": "Multiple actors shape world politics",
                },
            },
            "balance_of_power": {
                "major_powers": "distributed",
                "description": "System tends toward equilibrium",
            },
            "meta_meaning": "IR demonstrates META 50/50 in cooperation-conflict balance",
        }


def create_international_relations_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> InternationalRelationsDomain:
    """
    Factory function to create a fully initialized international relations domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized InternationalRelationsDomain
    """
    domain = InternationalRelationsDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_theories()
        domain.initialize_actors()
        domain.initialize_system_types()
        domain.initialize_ir_pairs()

    return domain
