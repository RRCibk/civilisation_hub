"""
Dentistry Domain
================
Dentistry knowledge domain with META 50/50 equilibrium.
Fundamental duality: Restoration/Prevention (repair vs protect).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class DentistryDomain(KnowledgeDomain):
    """
    Dentistry knowledge domain.

    Fundamental Duality: Restoration / Prevention
    - Restoration: Repair, reconstruct, replace
    - Prevention: Protect, maintain, prevent

    Secondary Dualities:
    - Function / Aesthetics
    - Conservative / Aggressive
    - Surgical / Non-surgical
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Dentistry",
            domain_type=DomainType.FUNDAMENTAL,
            description="The science and practice of oral health care",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Restoration/Prevention duality."""
        self._domain.set_duality(
            positive_name="restoration",
            positive_value=50,
            negative_name="prevention",
            negative_value=50,
            duality_name="dentistry_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental dentistry principles."""
        principles = [
            (
                "Prevention First",
                "Prevention is better than treatment",
            ),
            (
                "Minimally Invasive",
                "Preserve natural tooth structure",
            ),
            (
                "Patient Education",
                "Empower patients for self-care",
            ),
            (
                "Evidence-Based Practice",
                "Treatment based on best evidence",
            ),
            (
                "Function and Aesthetics",
                "Restore both function and appearance",
            ),
            (
                "Pain Management",
                "Minimize patient discomfort",
            ),
            (
                "Informed Consent",
                "Patient understands treatment options",
            ),
            (
                "Continuum of Care",
                "Ongoing maintenance essential",
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=90,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental dentistry concepts."""
        return [
            "Tooth",
            "Enamel",
            "Dentin",
            "Pulp",
            "Gum",
            "Periodontal",
            "Cavity",
            "Filling",
            "Crown",
            "Root Canal",
            "Extraction",
            "Implant",
            "Orthodontics",
            "Occlusion",
            "Hygiene",
        ]

    def initialize_branches(self) -> None:
        """Initialize major dentistry specialties."""
        branches = [
            (
                "General Dentistry",
                "Comprehensive oral care",
                ConceptType.THEORY,
            ),
            (
                "Orthodontics",
                "Teeth alignment",
                ConceptType.THEORY,
            ),
            (
                "Periodontics",
                "Gum disease treatment",
                ConceptType.THEORY,
            ),
            (
                "Endodontics",
                "Root canal therapy",
                ConceptType.THEORY,
            ),
            (
                "Prosthodontics",
                "Dental prosthetics",
                ConceptType.THEORY,
            ),
            (
                "Oral Surgery",
                "Surgical procedures",
                ConceptType.THEORY,
            ),
            (
                "Pediatric Dentistry",
                "Children's dental care",
                ConceptType.THEORY,
            ),
            (
                "Oral Pathology",
                "Oral diseases",
                ConceptType.THEORY,
            ),
            (
                "Cosmetic Dentistry",
                "Aesthetic improvement",
                ConceptType.THEORY,
            ),
            (
                "Dental Public Health",
                "Population oral health",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_procedures(self) -> None:
        """Initialize common dental procedures."""
        procedures = [
            ("Examination", "Diagnostic assessment", "Prevention"),
            ("Cleaning", "Professional hygiene", "Prevention"),
            ("Filling", "Cavity restoration", "Restoration"),
            ("Crown", "Tooth coverage", "Restoration"),
            ("Root Canal", "Pulp treatment", "Endodontic"),
            ("Extraction", "Tooth removal", "Surgical"),
        ]

        for name, description, category in procedures:
            concept = self.create_concept(
                name=f"Dental {name}",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_materials(self) -> None:
        """Initialize dental materials."""
        materials = [
            ("Amalgam", "Silver filling material", "Traditional"),
            ("Composite", "Tooth-colored filling", "Aesthetic"),
            ("Ceramic", "Porcelain restoration", "Aesthetic"),
            ("Gold", "Metal restoration", "Durable"),
            ("Titanium", "Implant material", "Biocompatible"),
            ("Fluoride", "Preventive agent", "Protective"),
        ]

        for name, description, property_type in materials:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["property"] = property_type

    def initialize_dentistry_pairs(self) -> None:
        """Initialize fundamental dentistry pairs with META 50/50 balance."""
        pairs = [
            ("Restoration", "Prevention", "Repair vs protect"),
            ("Function", "Aesthetics", "Working vs looking"),
            ("Conservative", "Aggressive", "Minimal vs extensive"),
            ("Surgical", "Non-surgical", "Invasive vs non-invasive"),
            ("Permanent", "Temporary", "Lasting vs interim"),
            ("Fixed", "Removable", "Attached vs detachable"),
            ("Hard Tissue", "Soft Tissue", "Tooth vs gum"),
            ("Direct", "Indirect", "Chair-side vs lab-made"),
            ("Natural", "Artificial", "Original vs prosthetic"),
            ("Adult", "Pediatric", "Grown vs child"),
            ("Emergency", "Routine", "Urgent vs scheduled"),
            ("Local", "General", "Area vs systemic"),
            ("Diagnostic", "Therapeutic", "Finding vs treating"),
            ("Simple", "Complex", "Basic vs complicated"),
            ("Single", "Multiple", "One tooth vs many"),
            ("Anterior", "Posterior", "Front vs back"),
            ("Upper", "Lower", "Maxillary vs mandibular"),
            ("Pain", "Comfort", "Discomfort vs ease"),
            ("Disease", "Health", "Pathology vs wellness"),
            ("Treatment", "Maintenance", "Active vs ongoing care"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Dentistry)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Dentistry)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_tooth_anatomy(self) -> dict[str, str]:
        """Get tooth anatomical structures."""
        return {
            "enamel": "Hard outer layer",
            "dentin": "Main tooth body",
            "pulp": "Nerve and blood supply",
            "cementum": "Root covering",
            "periodontal_ligament": "Attachment to bone",
            "alveolar_bone": "Jaw bone socket",
        }

    def demonstrate_dentistry_balance(self) -> dict[str, Any]:
        """Demonstrate dentistry balance principles."""
        return {
            "concept": "Dentistry Equilibrium",
            "dualities": {
                "restoration_prevention": {
                    "restoration": 50.0,
                    "prevention": 50.0,
                    "meaning": "Repair and protection equally important",
                },
                "function_aesthetics": {
                    "function": 50.0,
                    "aesthetics": 50.0,
                    "meaning": "Working and looking good both matter",
                },
                "conservative_aggressive": {
                    "conservative": 50.0,
                    "aggressive": 50.0,
                    "meaning": "Treatment intensity matched to need",
                },
            },
            "care_balance": {
                "treatment": 50.0,
                "maintenance": 50.0,
                "description": "Active care and ongoing maintenance equally valued",
            },
            "meta_meaning": "Dentistry demonstrates META 50/50 in restoration-prevention equilibrium",
        }


def create_dentistry_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> DentistryDomain:
    """
    Factory function to create a fully initialized dentistry domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized DentistryDomain
    """
    domain = DentistryDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_procedures()
        domain.initialize_materials()
        domain.initialize_dentistry_pairs()

    return domain
