"""
Medicine Domain
===============
Medicine knowledge domain with META 50/50 equilibrium.
Fundamental duality: Health/Disease (wellness vs illness).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class MedicineDomain(KnowledgeDomain):
    """
    Medicine knowledge domain.

    Fundamental Duality: Health / Disease
    - Health: Wellness, function, homeostasis
    - Disease: Illness, dysfunction, pathology

    Secondary Dualities:
    - Prevention / Treatment
    - Body / Mind
    - Acute / Chronic
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Medicine",
            domain_type=DomainType.FUNDAMENTAL,
            description="The science and practice of diagnosing and treating illness",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Health/Disease duality."""
        self._domain.set_duality(
            positive_name="health",
            positive_value=50,
            negative_name="disease",
            negative_value=50,
            duality_name="medicine_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental medical principles."""
        principles = [
            (
                "Primum Non Nocere",
                "First, do no harm",
            ),
            (
                "Beneficence",
                "Act in patient's best interest",
            ),
            (
                "Patient Autonomy",
                "Respect patient's right to decide",
            ),
            (
                "Justice",
                "Fair distribution of healthcare resources",
            ),
            (
                "Evidence-Based Practice",
                "Treatment based on best available evidence",
            ),
            (
                "Holistic Care",
                "Treat the whole person, not just symptoms",
            ),
            (
                "Confidentiality",
                "Protect patient information",
            ),
            (
                "Continuous Learning",
                "Medicine evolves with new knowledge",
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=95,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental medicine concepts."""
        return [
            "Health",
            "Disease",
            "Diagnosis",
            "Treatment",
            "Prevention",
            "Patient",
            "Symptom",
            "Etiology",
            "Pathology",
            "Therapy",
            "Prognosis",
            "Anatomy",
            "Physiology",
            "Pharmacology",
            "Surgery",
        ]

    def initialize_branches(self) -> None:
        """Initialize major medical specialties."""
        branches = [
            (
                "Internal Medicine",
                "Adult internal diseases",
                ConceptType.THEORY,
            ),
            (
                "Surgery",
                "Operative treatment",
                ConceptType.THEORY,
            ),
            (
                "Pediatrics",
                "Child health",
                ConceptType.THEORY,
            ),
            (
                "Psychiatry",
                "Mental health",
                ConceptType.THEORY,
            ),
            (
                "Obstetrics and Gynecology",
                "Women's reproductive health",
                ConceptType.THEORY,
            ),
            (
                "Cardiology",
                "Heart diseases",
                ConceptType.THEORY,
            ),
            (
                "Oncology",
                "Cancer treatment",
                ConceptType.THEORY,
            ),
            (
                "Neurology",
                "Nervous system disorders",
                ConceptType.THEORY,
            ),
            (
                "Emergency Medicine",
                "Acute care",
                ConceptType.THEORY,
            ),
            (
                "Family Medicine",
                "Primary care across lifespan",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_diagnostic_methods(self) -> None:
        """Initialize diagnostic methods."""
        methods = [
            ("Physical Examination", "Clinical assessment", "Bedside"),
            ("Laboratory Tests", "Blood and fluid analysis", "Pathology"),
            ("Imaging", "X-ray, CT, MRI, ultrasound", "Radiology"),
            ("Biopsy", "Tissue sampling", "Histology"),
            ("Endoscopy", "Internal visualization", "Procedure"),
            ("Genetic Testing", "DNA analysis", "Genomics"),
        ]

        for name, description, category in methods:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_treatment_modalities(self) -> None:
        """Initialize treatment approaches."""
        treatments = [
            ("Pharmacotherapy", "Drug treatment", "Medication"),
            ("Surgery", "Operative intervention", "Invasive"),
            ("Radiation Therapy", "Ionizing radiation treatment", "Oncology"),
            ("Physical Therapy", "Movement rehabilitation", "Rehabilitation"),
            ("Psychotherapy", "Talk therapy", "Mental health"),
            ("Immunotherapy", "Immune system modulation", "Biological"),
        ]

        for name, description, category in treatments:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_medicine_pairs(self) -> None:
        """Initialize fundamental medicine pairs with META 50/50 balance."""
        pairs = [
            ("Health", "Disease", "Wellness vs illness"),
            ("Prevention", "Treatment", "Avoid vs cure"),
            ("Body", "Mind", "Physical vs psychological"),
            ("Acute", "Chronic", "Sudden vs long-term"),
            ("Diagnosis", "Therapy", "Finding vs fixing"),
            ("Science", "Art", "Evidence vs judgment"),
            ("Generalist", "Specialist", "Broad vs focused"),
            ("Conservative", "Aggressive", "Minimal vs maximal intervention"),
            ("Curative", "Palliative", "Cure-seeking vs comfort-focused"),
            ("Individual", "Population", "Patient vs public health"),
            ("Biological", "Psychosocial", "Body vs context"),
            ("Symptom", "Cause", "Manifestation vs etiology"),
            ("Local", "Systemic", "Site vs whole body"),
            ("Invasive", "Non-invasive", "Penetrating vs external"),
            ("Empirical", "Rational", "Experience vs theory"),
            ("Standard", "Personalized", "Protocol vs tailored"),
            ("Conventional", "Alternative", "Mainstream vs complementary"),
            ("Risk", "Benefit", "Harm potential vs help potential"),
            ("Quality", "Quantity", "Life quality vs life length"),
            ("Autonomy", "Paternalism", "Patient choice vs doctor direction"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Medicine)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Medicine)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_hippocratic_principles(self) -> dict[str, str]:
        """Get Hippocratic medical principles."""
        return {
            "do_no_harm": "Primum non nocere - first do no harm",
            "beneficence": "Act for patient's good",
            "confidentiality": "Keep patient secrets",
            "teaching": "Pass knowledge to next generation",
        }

    def demonstrate_medicine_balance(self) -> dict[str, Any]:
        """Demonstrate medicine balance principles."""
        return {
            "concept": "Medicine Equilibrium",
            "dualities": {
                "health_disease": {
                    "health": 50.0,
                    "disease": 50.0,
                    "meaning": "Understanding both health and disease equally",
                },
                "prevention_treatment": {
                    "prevention": 50.0,
                    "treatment": 50.0,
                    "meaning": "Both preventing and treating illness matter",
                },
                "body_mind": {
                    "body": 50.0,
                    "mind": 50.0,
                    "meaning": "Physical and mental health are unified",
                },
            },
            "care_balance": {
                "science": 50.0,
                "art": 50.0,
                "description": "Medicine combines evidence and clinical judgment",
            },
            "meta_meaning": "Medicine demonstrates META 50/50 in health-disease equilibrium",
        }


def create_medicine_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> MedicineDomain:
    """
    Factory function to create a fully initialized medicine domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized MedicineDomain
    """
    domain = MedicineDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_diagnostic_methods()
        domain.initialize_treatment_modalities()
        domain.initialize_medicine_pairs()

    return domain
