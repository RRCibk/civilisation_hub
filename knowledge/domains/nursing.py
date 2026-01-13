"""
Nursing Domain
==============
Nursing knowledge domain with META 50/50 equilibrium.
Fundamental duality: Care/Cure (nurturing vs treating).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class NursingDomain(KnowledgeDomain):
    """
    Nursing knowledge domain.

    Fundamental Duality: Care / Cure
    - Care: Nurturing, comfort, support
    - Cure: Treatment, healing, intervention

    Secondary Dualities:
    - Art / Science
    - Holistic / Focused
    - Dependent / Independent
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Nursing",
            domain_type=DomainType.FUNDAMENTAL,
            description="The profession of caring for patients and promoting health",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Care/Cure duality."""
        self._domain.set_duality(
            positive_name="care",
            positive_value=50,
            negative_name="cure",
            negative_value=50,
            duality_name="nursing_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental nursing principles."""
        principles = [
            (
                "Patient-Centered Care",
                "Patient needs are primary focus",
            ),
            (
                "Advocacy",
                "Speak for patients who cannot speak for themselves",
            ),
            (
                "Compassion",
                "Empathetic presence with suffering",
            ),
            (
                "Safety First",
                "Prevent harm to patients",
            ),
            (
                "Evidence-Based Practice",
                "Care based on best available evidence",
            ),
            (
                "Holistic Assessment",
                "Consider whole person, not just symptoms",
            ),
            (
                "Communication",
                "Clear, therapeutic communication essential",
            ),
            (
                "Professional Boundaries",
                "Maintain appropriate nurse-patient relationship",
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
        """Get fundamental nursing concepts."""
        return [
            "Care",
            "Patient",
            "Assessment",
            "Intervention",
            "Evaluation",
            "Health",
            "Wellness",
            "Comfort",
            "Safety",
            "Advocacy",
            "Education",
            "Documentation",
            "Ethics",
            "Communication",
            "Teamwork",
        ]

    def initialize_branches(self) -> None:
        """Initialize major nursing specialties."""
        branches = [
            (
                "Medical-Surgical Nursing",
                "Adult acute care",
                ConceptType.THEORY,
            ),
            (
                "Pediatric Nursing",
                "Child healthcare",
                ConceptType.THEORY,
            ),
            (
                "Obstetric Nursing",
                "Maternal and newborn care",
                ConceptType.THEORY,
            ),
            (
                "Psychiatric Nursing",
                "Mental health nursing",
                ConceptType.THEORY,
            ),
            (
                "Critical Care Nursing",
                "Intensive care",
                ConceptType.THEORY,
            ),
            (
                "Emergency Nursing",
                "Urgent and emergency care",
                ConceptType.THEORY,
            ),
            (
                "Community Health Nursing",
                "Public health focus",
                ConceptType.THEORY,
            ),
            (
                "Geriatric Nursing",
                "Elderly care",
                ConceptType.THEORY,
            ),
            (
                "Oncology Nursing",
                "Cancer care",
                ConceptType.THEORY,
            ),
            (
                "Palliative Nursing",
                "End-of-life care",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_nursing_process(self) -> None:
        """Initialize the nursing process steps."""
        steps = [
            ("Assessment", "Data collection", "Foundation"),
            ("Diagnosis", "Problem identification", "Analysis"),
            ("Planning", "Goal setting", "Preparation"),
            ("Implementation", "Carrying out interventions", "Action"),
            ("Evaluation", "Outcome assessment", "Review"),
        ]

        for name, description, phase in steps:
            concept = self.create_concept(
                name=f"Nursing {name}",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["phase"] = phase

    def initialize_care_theories(self) -> None:
        """Initialize nursing care theories."""
        theories = [
            ("Watson's Caring", "Jean Watson", "Caring is essence of nursing"),
            ("Orem's Self-Care", "Dorothea Orem", "Self-care deficit theory"),
            ("Roy's Adaptation", "Callista Roy", "Adaptation model"),
            ("Nightingale's Environment", "Florence Nightingale", "Environmental theory"),
            ("Henderson's Needs", "Virginia Henderson", "14 basic needs"),
            ("Benner's Novice to Expert", "Patricia Benner", "Skill acquisition"),
        ]

        for name, theorist, description in theories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["theorist"] = theorist

    def initialize_nursing_pairs(self) -> None:
        """Initialize fundamental nursing pairs with META 50/50 balance."""
        pairs = [
            ("Care", "Cure", "Nurturing vs treating"),
            ("Art", "Science", "Intuition vs evidence"),
            ("Holistic", "Focused", "Whole vs part"),
            ("Dependent", "Independent", "Delegated vs autonomous"),
            ("Preventive", "Restorative", "Avoiding vs fixing"),
            ("Physical", "Psychological", "Body vs mind care"),
            ("Individual", "Community", "Person vs population"),
            ("Acute", "Chronic", "Short-term vs long-term"),
            ("Direct", "Indirect", "Hands-on vs coordinating"),
            ("Technical", "Relational", "Skills vs relationship"),
            ("Assessment", "Intervention", "Finding vs doing"),
            ("Teaching", "Practicing", "Education vs action"),
            ("Autonomy", "Collaboration", "Independent vs team"),
            ("Comfort", "Function", "Ease vs ability"),
            ("Safety", "Dignity", "Protection vs respect"),
            ("Evidence", "Experience", "Research vs practice wisdom"),
            ("Generalist", "Specialist", "Broad vs focused"),
            ("Hospital", "Community", "Institutional vs home"),
            ("Quantity", "Quality", "Amount vs excellence"),
            ("Task", "Relationship", "Doing vs being"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Nursing)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Nursing)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_nursing_ethics(self) -> dict[str, str]:
        """Get nursing ethical principles."""
        return {
            "autonomy": "Respect patient's right to decide",
            "beneficence": "Do good for the patient",
            "non_maleficence": "Do no harm",
            "justice": "Fair treatment for all",
            "fidelity": "Keep promises to patients",
            "veracity": "Tell the truth",
        }

    def demonstrate_nursing_balance(self) -> dict[str, Any]:
        """Demonstrate nursing balance principles."""
        return {
            "concept": "Nursing Equilibrium",
            "dualities": {
                "care_cure": {
                    "care": 50.0,
                    "cure": 50.0,
                    "meaning": "Caring and curing are equally essential",
                },
                "art_science": {
                    "art": 50.0,
                    "science": 50.0,
                    "meaning": "Nursing combines intuition and evidence",
                },
                "holistic_focused": {
                    "holistic": 50.0,
                    "focused": 50.0,
                    "meaning": "See whole person while addressing specific needs",
                },
            },
            "practice_balance": {
                "technical": 50.0,
                "relational": 50.0,
                "description": "Skills and relationships both matter",
            },
            "meta_meaning": "Nursing demonstrates META 50/50 in care-cure synthesis",
        }


def create_nursing_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> NursingDomain:
    """
    Factory function to create a fully initialized nursing domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized NursingDomain
    """
    domain = NursingDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_nursing_process()
        domain.initialize_care_theories()
        domain.initialize_nursing_pairs()

    return domain
