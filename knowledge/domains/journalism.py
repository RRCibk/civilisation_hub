"""
Journalism Domain
=================
Journalism knowledge domain with META 50/50 equilibrium.
Fundamental duality: Truth/Story (facts vs narrative).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class JournalismDomain(KnowledgeDomain):
    """
    Journalism knowledge domain.

    Fundamental Duality: Truth / Story
    - Truth: Facts, accuracy, verification
    - Story: Narrative, engagement, human interest

    Secondary Dualities:
    - Objectivity / Perspective
    - Breaking / In-depth
    - Print / Digital
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Journalism",
            domain_type=DomainType.FUNDAMENTAL,
            description="The gathering, verification, and presentation of news",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Truth/Story duality."""
        self._domain.set_duality(
            positive_name="truth",
            positive_value=50,
            negative_name="story",
            negative_value=50,
            duality_name="journalism_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental journalism principles."""
        principles = [
            ("Truth-Seeking", "Primary obligation is to truth"),
            ("Independence", "Free from influence"),
            ("Verification", "Check facts before publishing"),
            ("Public Interest", "Serve the public"),
            ("Fairness", "Present multiple perspectives"),
            ("Accountability", "Take responsibility for work"),
            ("Transparency", "Be open about methods"),
            ("Harm Minimization", "Consider consequences"),
        ]

        for name, description in principles:
            self.create_concept(name, ConceptType.PRINCIPLE, description, certainty=90)

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental journalism concepts."""
        return ["News", "Source", "Story", "Lead", "Headline", "Byline",
                "Deadline", "Editor", "Reporter", "Beat", "Interview",
                "Investigation", "Verification", "Ethics", "Audience"]

    def initialize_branches(self) -> None:
        """Initialize major journalism branches."""
        branches = [
            ("News Reporting", "Breaking news", ConceptType.THEORY),
            ("Investigative Journalism", "In-depth investigation", ConceptType.THEORY),
            ("Feature Writing", "Human interest stories", ConceptType.THEORY),
            ("Opinion Journalism", "Commentary and analysis", ConceptType.THEORY),
            ("Broadcast Journalism", "TV and radio", ConceptType.THEORY),
            ("Digital Journalism", "Online platforms", ConceptType.THEORY),
            ("Data Journalism", "Data-driven stories", ConceptType.THEORY),
            ("Photojournalism", "Visual storytelling", ConceptType.THEORY),
            ("Sports Journalism", "Athletic coverage", ConceptType.THEORY),
            ("Science Journalism", "Scientific reporting", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_elements(self) -> None:
        """Initialize news elements (5 Ws and H)."""
        elements = [
            ("Who", "People involved", "Character"),
            ("What", "Events that happened", "Action"),
            ("When", "Time of events", "Temporal"),
            ("Where", "Location", "Spatial"),
            ("Why", "Causes and reasons", "Causation"),
            ("How", "Process and method", "Process"),
        ]

        for name, description, category in elements:
            concept = self.create_concept(name, ConceptType.DEFINITION, description)
            concept.metadata["category"] = category

    def initialize_journalism_pairs(self) -> None:
        """Initialize fundamental journalism pairs with META 50/50 balance."""
        pairs = [
            ("Truth", "Story", "Facts vs narrative"),
            ("Objectivity", "Perspective", "Neutral vs viewpoint"),
            ("Breaking", "In-depth", "Speed vs thoroughness"),
            ("Print", "Digital", "Paper vs online"),
            ("Local", "Global", "Community vs world"),
            ("News", "Opinion", "Reporting vs commentary"),
            ("Public", "Private", "Open vs confidential"),
            ("On-Record", "Off-Record", "Quotable vs background"),
            ("Hard News", "Soft News", "Events vs features"),
            ("Broadcast", "Print", "Audiovisual vs text"),
            ("Professional", "Citizen", "Trained vs amateur"),
            ("Mainstream", "Alternative", "Established vs indie"),
            ("Free", "Paid", "Open vs subscription"),
            ("Speed", "Accuracy", "Fast vs correct"),
            ("Access", "Independence", "Close vs distant"),
            ("Sensational", "Sober", "Dramatic vs restrained"),
            ("Named", "Anonymous", "Identified vs hidden source"),
            ("Exclusive", "Shared", "Unique vs common"),
            ("Live", "Recorded", "Real-time vs edited"),
            ("Disclosure", "Privacy", "Reveal vs protect"),
        ]

        for positive, negative, description in pairs:
            pos = self.create_concept(f"{positive} (Journalism)", ConceptType.DEFINITION,
                                       f"Positive pole: {description.split(' vs ')[0]}")
            neg = self.create_concept(f"{negative} (Journalism)", ConceptType.DEFINITION,
                                       f"Negative pole: {description.split(' vs ')[1]}")
            self.create_relation(pos, neg, RelationType.CONTRADICTS, strength=50)

    def demonstrate_journalism_balance(self) -> dict[str, Any]:
        """Demonstrate journalism balance principles."""
        return {
            "concept": "Journalism Equilibrium",
            "dualities": {
                "truth_story": {"truth": 50.0, "story": 50.0,
                    "meaning": "Facts and narrative both matter"},
                "speed_accuracy": {"speed": 50.0, "accuracy": 50.0,
                    "meaning": "Balance timeliness and correctness"},
            },
            "meta_meaning": "Journalism demonstrates META 50/50 in truth-story synthesis",
        }


def create_journalism_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> JournalismDomain:
    domain = JournalismDomain(meta_equilibrium)
    if initialize_all:
        domain.initialize_branches()
        domain.initialize_elements()
        domain.initialize_journalism_pairs()
    return domain
