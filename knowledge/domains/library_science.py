"""
Library Science Domain
======================
Library Science knowledge domain with META 50/50 equilibrium.
Fundamental duality: Access/Preservation (availability vs protection).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class LibraryScienceDomain(KnowledgeDomain):
    """
    Library Science knowledge domain.

    Fundamental Duality: Access / Preservation
    - Access: Availability, retrieval, dissemination
    - Preservation: Protection, conservation, archiving

    Secondary Dualities:
    - Physical / Digital
    - Collection / User
    - Organization / Discovery
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="LibraryScience",
            domain_type=DomainType.FUNDAMENTAL,
            description="The organization and management of information resources",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Access/Preservation duality."""
        self._domain.set_duality(
            positive_name="access",
            positive_value=50,
            negative_name="preservation",
            negative_value=50,
            duality_name="library_science_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental library science principles."""
        principles = [
            ("Information Access", "Knowledge should be accessible to all"),
            ("Organization", "Information must be systematically organized"),
            ("Preservation", "Cultural heritage must be protected"),
            ("Service", "Libraries serve their communities"),
            ("Intellectual Freedom", "Free inquiry without censorship"),
            ("Privacy", "Patron information is confidential"),
            ("Literacy", "Promote reading and information literacy"),
            ("Equity", "Equal access regardless of background"),
        ]

        for name, description in principles:
            self.create_concept(name, ConceptType.PRINCIPLE, description, certainty=90)

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental library science concepts."""
        return ["Catalog", "Classification", "Collection", "Circulation", "Reference",
                "Metadata", "Indexing", "Acquisition", "Weeding", "Stack",
                "Repository", "Archive", "Database", "OPAC", "ILS"]

    def initialize_branches(self) -> None:
        """Initialize major library science branches."""
        branches = [
            ("Academic Libraries", "University libraries", ConceptType.THEORY),
            ("Public Libraries", "Community libraries", ConceptType.THEORY),
            ("Special Libraries", "Specialized collections", ConceptType.THEORY),
            ("Digital Libraries", "Online collections", ConceptType.THEORY),
            ("Information Science", "Information theory", ConceptType.THEORY),
            ("Archival Science", "Records management", ConceptType.THEORY),
            ("Knowledge Management", "Organizational knowledge", ConceptType.THEORY),
            ("Bibliometrics", "Publication analysis", ConceptType.THEORY),
            ("Children's Services", "Youth librarianship", ConceptType.THEORY),
            ("Technical Services", "Cataloging and processing", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_systems(self) -> None:
        """Initialize classification systems."""
        systems = [
            ("Dewey Decimal", "DDC classification", "Public"),
            ("Library of Congress", "LC classification", "Academic"),
            ("Universal Decimal", "UDC classification", "International"),
            ("MARC", "Machine-readable cataloging", "Standard"),
            ("Dublin Core", "Metadata standard", "Digital"),
            ("RDA", "Resource description", "Modern"),
        ]

        for name, description, scope in systems:
            concept = self.create_concept(name, ConceptType.DEFINITION, description)
            concept.metadata["scope"] = scope

    def initialize_library_pairs(self) -> None:
        """Initialize fundamental library science pairs with META 50/50 balance."""
        pairs = [
            ("Access", "Preservation", "Availability vs protection"),
            ("Physical", "Digital", "Tangible vs virtual"),
            ("Collection", "User", "Holdings vs patrons"),
            ("Organization", "Discovery", "Arrange vs find"),
            ("Acquisition", "Weeding", "Add vs remove"),
            ("Centralized", "Distributed", "Single vs multiple locations"),
            ("Open", "Closed", "Public vs restricted"),
            ("Print", "Electronic", "Paper vs digital"),
            ("Catalog", "Index", "Describe vs point to"),
            ("Subject", "Author", "Topic vs creator access"),
            ("Known-Item", "Exploratory", "Specific vs browsing"),
            ("Local", "Networked", "Own vs shared resources"),
            ("Free", "Fee", "No-cost vs paid"),
            ("General", "Special", "Broad vs focused"),
            ("Circulating", "Reference", "Borrowable vs in-library"),
            ("Original", "Copy", "Unique vs reproduction"),
            ("Current", "Historical", "New vs old materials"),
            ("Owned", "Licensed", "Purchased vs subscribed"),
            ("Human", "Automated", "Librarian vs system"),
            ("Breadth", "Depth", "Wide vs deep coverage"),
        ]

        for positive, negative, description in pairs:
            pos = self.create_concept(f"{positive} (Library)", ConceptType.DEFINITION,
                                       f"Positive pole: {description.split(' vs ')[0]}")
            neg = self.create_concept(f"{negative} (Library)", ConceptType.DEFINITION,
                                       f"Negative pole: {description.split(' vs ')[1]}")
            self.create_relation(pos, neg, RelationType.CONTRADICTS, strength=50)

    def demonstrate_library_balance(self) -> dict[str, Any]:
        """Demonstrate library science balance principles."""
        return {
            "concept": "Library Science Equilibrium",
            "dualities": {
                "access_preservation": {"access": 50.0, "preservation": 50.0,
                    "meaning": "Balance availability with protection"},
                "physical_digital": {"physical": 50.0, "digital": 50.0,
                    "meaning": "Integrate tangible and virtual collections"},
            },
            "meta_meaning": "Library Science demonstrates META 50/50 in access-preservation balance",
        }


def create_library_science_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> LibraryScienceDomain:
    domain = LibraryScienceDomain(meta_equilibrium)
    if initialize_all:
        domain.initialize_branches()
        domain.initialize_systems()
        domain.initialize_library_pairs()
    return domain
