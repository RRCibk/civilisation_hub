"""
Archival Science Domain
=======================
Archival Science knowledge domain with META 50/50 equilibrium.
Fundamental duality: Preservation/Access (protect vs provide).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class ArchivalScienceDomain(KnowledgeDomain):
    """
    Archival Science knowledge domain.

    Fundamental Duality: Preservation / Access
    - Preservation: Protection, conservation, longevity
    - Access: Availability, use, retrieval

    Secondary Dualities:
    - Original / Copy
    - Physical / Digital
    - Retention / Disposal
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="ArchivalScience",
            domain_type=DomainType.FUNDAMENTAL,
            description="The management and preservation of records and archives",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Preservation/Access duality."""
        self._domain.set_duality(
            positive_name="preservation",
            positive_value=50,
            negative_name="access",
            negative_value=50,
            duality_name="archival_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental archival principles."""
        principles = [
            ("Provenance", "Maintain original source and context"),
            ("Original Order", "Preserve creator's arrangement"),
            ("Authenticity", "Ensure records are genuine"),
            ("Integrity", "Maintain completeness"),
            ("Accessibility", "Make records available"),
            ("Accountability", "Support organizational memory"),
            ("Appraisal", "Select records of value"),
            ("Description", "Document archival holdings"),
        ]

        for name, description in principles:
            self.create_concept(name, ConceptType.PRINCIPLE, description, certainty=95)

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental archival concepts."""
        return ["Record", "Archive", "Fonds", "Series", "Item", "Provenance",
                "Arrangement", "Description", "Finding Aid", "Retention",
                "Disposition", "Appraisal", "Accession", "Preservation", "Access"]

    def initialize_branches(self) -> None:
        """Initialize major archival branches."""
        branches = [
            ("Records Management", "Active records control", ConceptType.THEORY),
            ("Digital Preservation", "Electronic records", ConceptType.THEORY),
            ("Archival Arrangement", "Organization methods", ConceptType.THEORY),
            ("Archival Description", "Finding aids creation", ConceptType.THEORY),
            ("Conservation", "Physical preservation", ConceptType.THEORY),
            ("Electronic Records", "Digital management", ConceptType.THEORY),
            ("Oral History", "Audio/video archives", ConceptType.THEORY),
            ("Manuscript Collections", "Personal papers", ConceptType.THEORY),
            ("Government Archives", "Public records", ConceptType.THEORY),
            ("Corporate Archives", "Business records", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_levels(self) -> None:
        """Initialize archival description levels."""
        levels = [
            ("Fonds", "Creator level", "Highest"),
            ("Sub-fonds", "Subdivision", "High"),
            ("Series", "Records system", "Medium"),
            ("File", "Document group", "Low"),
            ("Item", "Single document", "Lowest"),
            ("Collection", "Assembled materials", "Variable"),
        ]

        for name, description, hierarchy in levels:
            concept = self.create_concept(name, ConceptType.DEFINITION, description)
            concept.metadata["hierarchy"] = hierarchy

    def initialize_archival_pairs(self) -> None:
        """Initialize fundamental archival pairs with META 50/50 balance."""
        pairs = [
            ("Preservation", "Access", "Protect vs provide"),
            ("Original", "Copy", "Authentic vs reproduction"),
            ("Physical", "Digital", "Tangible vs electronic"),
            ("Retention", "Disposal", "Keep vs destroy"),
            ("Active", "Inactive", "Current vs historical"),
            ("Open", "Restricted", "Public vs limited"),
            ("Arrangement", "Description", "Organize vs document"),
            ("Centralized", "Distributed", "Single vs multiple"),
            ("Permanent", "Temporary", "Forever vs limited"),
            ("Organic", "Acquired", "Created vs collected"),
            ("Public", "Private", "Government vs personal"),
            ("Textual", "Non-textual", "Documents vs other"),
            ("Series", "Item", "Aggregate vs individual"),
            ("Appraisal", "Accession", "Evaluate vs acquire"),
            ("Context", "Content", "Surrounding vs substance"),
            ("Original Order", "Re-arrangement", "Creator vs archivist"),
            ("Macro", "Micro", "Collection vs item"),
            ("Analog", "Born-Digital", "Converted vs native"),
            ("Security", "Accessibility", "Protection vs use"),
            ("Theory", "Practice", "Principle vs application"),
        ]

        for positive, negative, description in pairs:
            pos = self.create_concept(f"{positive} (Archival)", ConceptType.DEFINITION,
                                       f"Positive pole: {description.split(' vs ')[0]}")
            neg = self.create_concept(f"{negative} (Archival)", ConceptType.DEFINITION,
                                       f"Negative pole: {description.split(' vs ')[1]}")
            self.create_relation(pos, neg, RelationType.CONTRADICTS, strength=50)

    def demonstrate_archival_balance(self) -> dict[str, Any]:
        """Demonstrate archival balance principles."""
        return {
            "concept": "Archival Science Equilibrium",
            "dualities": {
                "preservation_access": {"preservation": 50.0, "access": 50.0,
                    "meaning": "Balance protection with availability"},
                "retention_disposal": {"retention": 50.0, "disposal": 50.0,
                    "meaning": "Balance keeping with removing"},
            },
            "meta_meaning": "Archival Science demonstrates META 50/50 in preservation-access balance",
        }


def create_archival_science_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> ArchivalScienceDomain:
    domain = ArchivalScienceDomain(meta_equilibrium)
    if initialize_all:
        domain.initialize_branches()
        domain.initialize_levels()
        domain.initialize_archival_pairs()
    return domain
