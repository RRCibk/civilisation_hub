"""
Veterinary Medicine Domain
==========================
Veterinary medicine knowledge domain with META 50/50 equilibrium.
Fundamental duality: Animal/Human (veterinary vs comparative).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class VeterinaryMedicineDomain(KnowledgeDomain):
    """
    Veterinary Medicine knowledge domain.

    Fundamental Duality: Animal / Human
    - Animal: Species-specific care, veterinary focus
    - Human: Comparative medicine, zoonotic connections

    Secondary Dualities:
    - Companion / Production
    - Individual / Herd
    - Treatment / Prevention
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="VeterinaryMedicine",
            domain_type=DomainType.FUNDAMENTAL,
            description="The science and practice of animal health care",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Animal/Human duality."""
        self._domain.set_duality(
            positive_name="animal",
            positive_value=50,
            negative_name="human",
            negative_value=50,
            duality_name="veterinary_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental veterinary principles."""
        principles = [
            (
                "Animal Welfare",
                "Promote animal health and prevent suffering",
            ),
            (
                "One Health",
                "Animal, human, and environmental health interconnected",
            ),
            (
                "Species Specificity",
                "Each species has unique health needs",
            ),
            (
                "Preventive Medicine",
                "Prevention is cornerstone of animal health",
            ),
            (
                "Evidence-Based Practice",
                "Treatment based on scientific evidence",
            ),
            (
                "Client Communication",
                "Educate animal owners effectively",
            ),
            (
                "Ethical Euthanasia",
                "Humane end-of-life decisions",
            ),
            (
                "Zoonotic Awareness",
                "Recognize diseases transmissible to humans",
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
        """Get fundamental veterinary concepts."""
        return [
            "Animal",
            "Health",
            "Disease",
            "Diagnosis",
            "Treatment",
            "Prevention",
            "Vaccination",
            "Surgery",
            "Nutrition",
            "Behavior",
            "Zoonosis",
            "Welfare",
            "Anatomy",
            "Pathology",
            "Pharmacology",
        ]

    def initialize_branches(self) -> None:
        """Initialize major veterinary specialties."""
        branches = [
            (
                "Small Animal Medicine",
                "Companion animal care",
                ConceptType.THEORY,
            ),
            (
                "Large Animal Medicine",
                "Farm animal health",
                ConceptType.THEORY,
            ),
            (
                "Equine Medicine",
                "Horse health",
                ConceptType.THEORY,
            ),
            (
                "Avian Medicine",
                "Bird health",
                ConceptType.THEORY,
            ),
            (
                "Exotic Animal Medicine",
                "Non-traditional pets",
                ConceptType.THEORY,
            ),
            (
                "Veterinary Surgery",
                "Surgical procedures",
                ConceptType.THEORY,
            ),
            (
                "Veterinary Pathology",
                "Disease diagnosis",
                ConceptType.THEORY,
            ),
            (
                "Veterinary Public Health",
                "Animal-human health interface",
                ConceptType.THEORY,
            ),
            (
                "Theriogenology",
                "Animal reproduction",
                ConceptType.THEORY,
            ),
            (
                "Veterinary Oncology",
                "Animal cancer treatment",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_species_groups(self) -> None:
        """Initialize major animal species groups."""
        species = [
            ("Canine", "Dogs", "Companion"),
            ("Feline", "Cats", "Companion"),
            ("Equine", "Horses", "Performance"),
            ("Bovine", "Cattle", "Production"),
            ("Ovine", "Sheep", "Production"),
            ("Porcine", "Pigs", "Production"),
        ]

        for name, description, category in species:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_preventive_measures(self) -> None:
        """Initialize preventive veterinary measures."""
        measures = [
            ("Vaccination", "Immunization programs", "Infectious"),
            ("Parasite Control", "Deworming and flea prevention", "Parasitic"),
            ("Nutrition Management", "Proper feeding", "Metabolic"),
            ("Dental Care", "Oral health maintenance", "Preventive"),
            ("Spay/Neuter", "Population control", "Surgical"),
            ("Wellness Exams", "Regular health checks", "Screening"),
        ]

        for name, description, category in measures:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_veterinary_pairs(self) -> None:
        """Initialize fundamental veterinary pairs with META 50/50 balance."""
        pairs = [
            ("Animal", "Human", "Veterinary vs comparative"),
            ("Companion", "Production", "Pet vs farm"),
            ("Individual", "Herd", "Single vs population"),
            ("Treatment", "Prevention", "Cure vs protect"),
            ("Medical", "Surgical", "Non-invasive vs operative"),
            ("Acute", "Chronic", "Sudden vs long-term"),
            ("Physical", "Behavioral", "Body vs mind"),
            ("Diagnostic", "Therapeutic", "Finding vs treating"),
            ("Wild", "Domestic", "Free-ranging vs captive"),
            ("Emergency", "Routine", "Urgent vs scheduled"),
            ("Specialist", "Generalist", "Focused vs broad"),
            ("Clinical", "Research", "Practice vs science"),
            ("Welfare", "Production", "Quality vs quantity"),
            ("Owner", "Animal", "Client vs patient"),
            ("Euthanasia", "Treatment", "End vs continue"),
            ("Zoonotic", "Non-zoonotic", "Transmissible vs species-specific"),
            ("Infectious", "Non-infectious", "Contagious vs non-contagious"),
            ("Young", "Old", "Pediatric vs geriatric"),
            ("Male", "Female", "Male vs female patients"),
            ("Rural", "Urban", "Farm vs city practice"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Veterinary)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Veterinary)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_zoonotic_diseases(self) -> dict[str, str]:
        """Get major zoonotic diseases."""
        return {
            "rabies": "Viral disease from animal bites",
            "leptospirosis": "Bacterial disease from water",
            "salmonella": "Bacterial foodborne illness",
            "ringworm": "Fungal skin infection",
            "toxoplasmosis": "Parasitic infection from cats",
            "brucellosis": "Bacterial reproductive disease",
        }

    def demonstrate_veterinary_balance(self) -> dict[str, Any]:
        """Demonstrate veterinary medicine balance principles."""
        return {
            "concept": "Veterinary Medicine Equilibrium",
            "dualities": {
                "animal_human": {
                    "animal": 50.0,
                    "human": 50.0,
                    "meaning": "One Health connects animal and human medicine",
                },
                "treatment_prevention": {
                    "treatment": 50.0,
                    "prevention": 50.0,
                    "meaning": "Both curing and preventing disease essential",
                },
                "individual_herd": {
                    "individual": 50.0,
                    "herd": 50.0,
                    "meaning": "Single animal and population health both matter",
                },
            },
            "practice_balance": {
                "companion": 50.0,
                "production": 50.0,
                "description": "Pet and farm animal medicine equally valued",
            },
            "meta_meaning": "Veterinary Medicine demonstrates META 50/50 in animal-human health unity",
        }


def create_veterinary_medicine_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> VeterinaryMedicineDomain:
    """
    Factory function to create a fully initialized veterinary medicine domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized VeterinaryMedicineDomain
    """
    domain = VeterinaryMedicineDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_species_groups()
        domain.initialize_preventive_measures()
        domain.initialize_veterinary_pairs()

    return domain
