"""
History Domain
==============
History knowledge domain with META 50/50 equilibrium.
Fundamental duality: Past/Present (then vs now).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class HistoryDomain(KnowledgeDomain):
    """
    History knowledge domain.

    Fundamental Duality: Past / Present
    - Past: Historical events, previous times, what was
    - Present: Current time, contemporary, what is

    Secondary Dualities:
    - Continuity / Change
    - Structure / Event
    - Cause / Effect
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="History",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of past events and their significance",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Past/Present duality."""
        self._domain.set_duality(
            positive_name="past",
            positive_value=50,
            negative_name="present",
            negative_value=50,
            duality_name="history_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental historical principles."""
        principles = [
            (
                "Historical Contingency",
                "Events could have turned out differently",
            ),
            (
                "Causation",
                "Events have causes and effects",
            ),
            (
                "Context Principle",
                "Events must be understood in their context",
            ),
            (
                "Source Criticism",
                "Sources must be evaluated critically",
            ),
            (
                "Multiple Perspectives",
                "Different viewpoints illuminate different aspects",
            ),
            (
                "Change and Continuity",
                "History shows both transformation and persistence",
            ),
            (
                "Periodization",
                "History can be divided into meaningful periods",
            ),
            (
                "Historical Significance",
                "Some events matter more than others",
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
        """Get fundamental history concepts."""
        return [
            "Event",
            "Cause",
            "Effect",
            "Period",
            "Era",
            "Source",
            "Evidence",
            "Interpretation",
            "Change",
            "Continuity",
            "Revolution",
            "Evolution",
            "Progress",
            "Decline",
            "Civilization",
        ]

    def initialize_branches(self) -> None:
        """Initialize major history branches."""
        branches = [
            (
                "Political History",
                "History of governments and politics",
                ConceptType.THEORY,
            ),
            (
                "Social History",
                "History of ordinary people and society",
                ConceptType.THEORY,
            ),
            (
                "Economic History",
                "History of economic systems",
                ConceptType.THEORY,
            ),
            (
                "Cultural History",
                "History of ideas, arts, beliefs",
                ConceptType.THEORY,
            ),
            (
                "Military History",
                "History of warfare and armed forces",
                ConceptType.THEORY,
            ),
            (
                "Intellectual History",
                "History of ideas and thought",
                ConceptType.THEORY,
            ),
            (
                "Environmental History",
                "History of human-environment relations",
                ConceptType.THEORY,
            ),
            (
                "World History",
                "Global and comparative history",
                ConceptType.THEORY,
            ),
            (
                "Microhistory",
                "History of small-scale subjects",
                ConceptType.THEORY,
            ),
            (
                "Public History",
                "History for public audiences",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_historiographical_schools(self) -> None:
        """Initialize historiographical schools."""
        schools = [
            ("Rankean History", "Ranke", "History as it actually was"),
            ("Marxist History", "Marx", "Material conditions drive history"),
            ("Annales School", "Braudel", "Long-term structures, mentalités"),
            ("Social History", "Thompson", "History from below"),
            ("Postmodern History", "White", "History as narrative construction"),
            ("Cliometrics", "Fogel", "Quantitative methods in history"),
            ("Microhistory", "Ginzburg", "Small-scale, intensive study"),
            ("World-Systems", "Wallerstein", "Global economic systems"),
        ]

        for name, founder, description in schools:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_periods(self) -> None:
        """Initialize historical periods."""
        periods = [
            ("Prehistory", "Before writing", "Stone Age, Bronze Age"),
            ("Ancient History", "3000 BCE - 500 CE", "Mesopotamia, Egypt, Rome"),
            ("Medieval History", "500 - 1500 CE", "Middle Ages, feudalism"),
            ("Early Modern", "1500 - 1800 CE", "Renaissance, Reformation"),
            ("Modern History", "1800 - present", "Industrial to information age"),
            ("Contemporary", "Living memory", "Recent past"),
        ]

        for name, timeframe, examples in periods:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=f"Period: {timeframe}",
            )
            concept.metadata["examples"] = examples

    def initialize_source_types(self) -> None:
        """Initialize historical source types."""
        sources = [
            ("Primary Sources", "Created during the period", "Documents, artifacts"),
            ("Secondary Sources", "Later analysis", "Scholarly works"),
            ("Written Sources", "Textual evidence", "Letters, records"),
            ("Material Sources", "Physical objects", "Archaeology, art"),
            ("Oral Sources", "Spoken testimony", "Interviews, traditions"),
        ]

        for name, description, examples in sources:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_historical_pairs(self) -> None:
        """Initialize fundamental historical pairs with META 50/50 balance."""
        pairs = [
            ("Past", "Present", "Then vs now"),
            ("Continuity", "Change", "Persistence vs transformation"),
            ("Structure", "Event", "Long-term vs immediate"),
            ("Cause", "Effect", "Origin vs result"),
            ("Primary", "Secondary", "Original vs derived source"),
            ("Fact", "Interpretation", "Data vs meaning"),
            ("Elite", "Popular", "Rulers vs ruled"),
            ("Local", "Global", "Place vs world"),
            ("Individual", "Collective", "Person vs group"),
            ("Political", "Social", "State vs society"),
            ("Progress", "Decline", "Improvement vs deterioration"),
            ("Revolution", "Evolution", "Sudden vs gradual"),
            ("Traditional", "Modern", "Old vs new"),
            ("Center", "Periphery", "Core vs margin"),
            ("Written", "Oral", "Text vs speech"),
            ("Agency", "Structure", "Choice vs constraint"),
            ("Memory", "History", "Remembered vs studied"),
            ("Narrative", "Analysis", "Story vs explanation"),
            ("Objectivity", "Subjectivity", "Neutral vs biased"),
            ("Synchronic", "Diachronic", "Moment vs process"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (History)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (History)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_braudel_times(self) -> dict[str, str]:
        """Get Braudel's three levels of historical time."""
        return {
            "longue_duree": "Long-term structures, geography, climate",
            "conjoncture": "Medium-term cycles, economic trends",
            "evenement": "Short-term events, political history",
        }

    def demonstrate_history_balance(self) -> dict[str, Any]:
        """Demonstrate history balance principles."""
        return {
            "concept": "History Equilibrium",
            "dualities": {
                "past_present": {
                    "past": 50.0,
                    "present": 50.0,
                    "meaning": "Past and present illuminate each other",
                },
                "continuity_change": {
                    "continuity": 50.0,
                    "change": 50.0,
                    "meaning": "History shows both persistence and transformation",
                },
                "structure_event": {
                    "structure": 50.0,
                    "event": 50.0,
                    "meaning": "Both long-term patterns and specific events matter",
                },
            },
            "temporal_balance": {
                "longue_duree": 33.3,
                "conjoncture": 33.3,
                "evenement": 33.3,
                "description": "Three levels of historical time",
            },
            "meta_meaning": "History demonstrates META 50/50 in past-present dialectic",
        }


def create_history_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> HistoryDomain:
    """
    Factory function to create a fully initialized history domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized HistoryDomain
    """
    domain = HistoryDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_historiographical_schools()
        domain.initialize_periods()
        domain.initialize_source_types()
        domain.initialize_historical_pairs()

    return domain
