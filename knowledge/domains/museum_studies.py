"""
Museum Studies Domain
=====================
Museum Studies knowledge domain with META 50/50 equilibrium.
Fundamental duality: Collection/Exhibition (acquire vs display).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class MuseumStudiesDomain(KnowledgeDomain):
    """
    Museum Studies knowledge domain.

    Fundamental Duality: Collection / Exhibition
    - Collection: Acquisition, preservation, storage
    - Exhibition: Display, interpretation, engagement

    Secondary Dualities:
    - Object / Experience
    - Conservation / Access
    - Education / Entertainment
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="MuseumStudies",
            domain_type=DomainType.FUNDAMENTAL,
            description="The theory and practice of museum work",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Collection/Exhibition duality."""
        self._domain.set_duality(
            positive_name="collection",
            positive_value=50,
            negative_name="exhibition",
            negative_value=50,
            duality_name="museum_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental museum principles."""
        principles = [
            ("Public Service", "Museums serve the public"),
            ("Stewardship", "Care for collections in trust"),
            ("Education", "Museums teach and inform"),
            ("Preservation", "Protect cultural heritage"),
            ("Accessibility", "Open to all visitors"),
            ("Authenticity", "Present genuine objects"),
            ("Ethics", "Follow professional standards"),
            ("Research", "Advance knowledge"),
        ]

        for name, description in principles:
            self.create_concept(name, ConceptType.PRINCIPLE, description, certainty=90)

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental museum concepts."""
        return ["Collection", "Exhibition", "Curator", "Conservation", "Interpretation",
                "Visitor", "Object", "Display", "Catalog", "Acquisition",
                "Deaccession", "Storage", "Gallery", "Education", "Engagement"]

    def initialize_branches(self) -> None:
        """Initialize major museum branches."""
        branches = [
            ("Curatorial Studies", "Collection management", ConceptType.THEORY),
            ("Museum Education", "Learning programs", ConceptType.THEORY),
            ("Exhibition Design", "Display creation", ConceptType.THEORY),
            ("Conservation", "Object preservation", ConceptType.THEORY),
            ("Registration", "Collection documentation", ConceptType.THEORY),
            ("Visitor Studies", "Audience research", ConceptType.THEORY),
            ("Museum Management", "Administration", ConceptType.THEORY),
            ("Digital Museology", "Technology applications", ConceptType.THEORY),
            ("Community Engagement", "Public relations", ConceptType.THEORY),
            ("Museum Ethics", "Professional standards", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_types(self) -> None:
        """Initialize museum types."""
        types = [
            ("Art Museum", "Fine arts collections", "Aesthetic"),
            ("Natural History", "Natural specimens", "Scientific"),
            ("Science Museum", "Scientific concepts", "Educational"),
            ("History Museum", "Historical artifacts", "Cultural"),
            ("Children's Museum", "Youth engagement", "Interactive"),
            ("Living Museum", "Active demonstrations", "Experiential"),
        ]

        for name, description, focus in types:
            concept = self.create_concept(name, ConceptType.DEFINITION, description)
            concept.metadata["focus"] = focus

    def initialize_museum_pairs(self) -> None:
        """Initialize fundamental museum pairs with META 50/50 balance."""
        pairs = [
            ("Collection", "Exhibition", "Acquire vs display"),
            ("Object", "Experience", "Thing vs encounter"),
            ("Conservation", "Access", "Preserve vs show"),
            ("Education", "Entertainment", "Learn vs enjoy"),
            ("Permanent", "Temporary", "Fixed vs changing"),
            ("Original", "Reproduction", "Authentic vs copy"),
            ("Scholarship", "Accessibility", "Expert vs public"),
            ("Physical", "Digital", "Real vs virtual"),
            ("Local", "Global", "Community vs world"),
            ("Historic", "Contemporary", "Past vs present"),
            ("Acquisition", "Deaccession", "Add vs remove"),
            ("Storage", "Display", "Warehouse vs gallery"),
            ("Interpretation", "Experience", "Tell vs discover"),
            ("Expert", "Visitor", "Curator vs public"),
            ("Formal", "Informal", "Structured vs free"),
            ("Individual", "Social", "Solo vs group"),
            ("Passive", "Interactive", "View vs participate"),
            ("Free", "Paid", "No-cost vs admission"),
            ("Specialized", "General", "Focused vs broad"),
            ("Traditional", "Innovative", "Classic vs new"),
        ]

        for positive, negative, description in pairs:
            pos = self.create_concept(f"{positive} (Museum)", ConceptType.DEFINITION,
                                       f"Positive pole: {description.split(' vs ')[0]}")
            neg = self.create_concept(f"{negative} (Museum)", ConceptType.DEFINITION,
                                       f"Negative pole: {description.split(' vs ')[1]}")
            self.create_relation(pos, neg, RelationType.CONTRADICTS, strength=50)

    def demonstrate_museum_balance(self) -> dict[str, Any]:
        """Demonstrate museum balance principles."""
        return {
            "concept": "Museum Studies Equilibrium",
            "dualities": {
                "collection_exhibition": {"collection": 50.0, "exhibition": 50.0,
                    "meaning": "Balance acquiring with displaying"},
                "education_entertainment": {"education": 50.0, "entertainment": 50.0,
                    "meaning": "Balance learning with enjoyment"},
            },
            "meta_meaning": "Museum Studies demonstrates META 50/50 in collection-exhibition balance",
        }


def create_museum_studies_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> MuseumStudiesDomain:
    domain = MuseumStudiesDomain(meta_equilibrium)
    if initialize_all:
        domain.initialize_branches()
        domain.initialize_types()
        domain.initialize_museum_pairs()
    return domain
