"""
Public Health Domain
====================
Public health knowledge domain with META 50/50 equilibrium.
Fundamental duality: Individual/Population (personal vs collective).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class PublicHealthDomain(KnowledgeDomain):
    """
    Public Health knowledge domain.

    Fundamental Duality: Individual / Population
    - Individual: Personal health, clinical focus
    - Population: Community health, epidemiological focus

    Secondary Dualities:
    - Prevention / Treatment
    - Upstream / Downstream
    - Equity / Efficiency
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="PublicHealth",
            domain_type=DomainType.FUNDAMENTAL,
            description="The science of protecting and improving community health",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Individual/Population duality."""
        self._domain.set_duality(
            positive_name="individual",
            positive_value=50,
            negative_name="population",
            negative_value=50,
            duality_name="public_health_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental public health principles."""
        principles = [
            (
                "Prevention Focus",
                "Preventing disease is more effective than treating it",
            ),
            (
                "Social Determinants",
                "Health shaped by social and economic factors",
            ),
            (
                "Health Equity",
                "Everyone deserves opportunity for health",
            ),
            (
                "Evidence-Based Policy",
                "Decisions based on scientific evidence",
            ),
            (
                "Community Participation",
                "Communities involved in health decisions",
            ),
            (
                "Intersectoral Action",
                "Health requires collaboration across sectors",
            ),
            (
                "Surveillance",
                "Monitoring disease patterns essential",
            ),
            (
                "Health Promotion",
                "Enable people to increase control over health",
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
        """Get fundamental public health concepts."""
        return [
            "Population",
            "Prevention",
            "Epidemiology",
            "Health Promotion",
            "Disease Surveillance",
            "Outbreak",
            "Risk Factor",
            "Determinants",
            "Equity",
            "Policy",
            "Intervention",
            "Screening",
            "Vaccination",
            "Sanitation",
            "Environment",
        ]

    def initialize_branches(self) -> None:
        """Initialize major public health branches."""
        branches = [
            (
                "Epidemiology",
                "Study of disease distribution",
                ConceptType.THEORY,
            ),
            (
                "Biostatistics",
                "Statistical methods in health",
                ConceptType.THEORY,
            ),
            (
                "Health Policy",
                "Policy development and analysis",
                ConceptType.THEORY,
            ),
            (
                "Environmental Health",
                "Environmental factors in health",
                ConceptType.THEORY,
            ),
            (
                "Health Education",
                "Health information and behavior",
                ConceptType.THEORY,
            ),
            (
                "Occupational Health",
                "Workplace health and safety",
                ConceptType.THEORY,
            ),
            (
                "Maternal and Child Health",
                "Women's and children's health",
                ConceptType.THEORY,
            ),
            (
                "Global Health",
                "International health issues",
                ConceptType.THEORY,
            ),
            (
                "Health Economics",
                "Economic aspects of health",
                ConceptType.THEORY,
            ),
            (
                "Infectious Disease",
                "Communicable disease control",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_prevention_levels(self) -> None:
        """Initialize levels of prevention."""
        levels = [
            ("Primary Prevention", "Prevent disease occurrence", "Before"),
            ("Secondary Prevention", "Early detection", "Early"),
            ("Tertiary Prevention", "Reduce complications", "After"),
            ("Primordial Prevention", "Address root causes", "Upstream"),
        ]

        for name, description, timing in levels:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["timing"] = timing

    def initialize_interventions(self) -> None:
        """Initialize public health interventions."""
        interventions = [
            ("Immunization Programs", "Vaccination campaigns", "Prevention"),
            ("Screening Programs", "Early disease detection", "Secondary"),
            ("Health Education", "Behavior change communication", "Promotion"),
            ("Policy Interventions", "Laws and regulations", "Structural"),
            ("Environmental Interventions", "Clean water, sanitation", "Environment"),
            ("Emergency Response", "Outbreak management", "Crisis"),
        ]

        for name, description, category in interventions:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_public_health_pairs(self) -> None:
        """Initialize fundamental public health pairs with META 50/50 balance."""
        pairs = [
            ("Individual", "Population", "Person vs community"),
            ("Prevention", "Treatment", "Avoiding vs curing"),
            ("Upstream", "Downstream", "Root causes vs immediate"),
            ("Equity", "Efficiency", "Fair vs optimal"),
            ("Universal", "Targeted", "All vs specific groups"),
            ("Voluntary", "Mandatory", "Choice vs requirement"),
            ("Local", "Global", "Community vs world"),
            ("Acute", "Chronic", "Sudden vs long-term"),
            ("Infectious", "Non-communicable", "Contagious vs lifestyle"),
            ("Curative", "Preventive", "Treatment vs protection"),
            ("Clinical", "Population", "Patient vs public"),
            ("Biomedical", "Social", "Biological vs societal"),
            ("Risk", "Protective", "Harm vs benefit factors"),
            ("Surveillance", "Intervention", "Monitoring vs acting"),
            ("Evidence", "Policy", "Science vs politics"),
            ("Access", "Quality", "Availability vs excellence"),
            ("Cost", "Benefit", "Resources vs outcomes"),
            ("Vertical", "Horizontal", "Disease-specific vs system-wide"),
            ("Emergency", "Routine", "Crisis vs ongoing"),
            ("Government", "Community", "Top-down vs bottom-up"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Public Health)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Public Health)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_social_determinants(self) -> dict[str, str]:
        """Get social determinants of health."""
        return {
            "education": "Level of schooling and literacy",
            "income": "Economic resources and poverty",
            "employment": "Work conditions and security",
            "housing": "Living conditions and homelessness",
            "social_support": "Community and relationships",
            "healthcare_access": "Availability of services",
        }

    def demonstrate_public_health_balance(self) -> dict[str, Any]:
        """Demonstrate public health balance principles."""
        return {
            "concept": "Public Health Equilibrium",
            "dualities": {
                "individual_population": {
                    "individual": 50.0,
                    "population": 50.0,
                    "meaning": "Personal and community health are interdependent",
                },
                "prevention_treatment": {
                    "prevention": 50.0,
                    "treatment": 50.0,
                    "meaning": "Both preventing and treating disease essential",
                },
                "equity_efficiency": {
                    "equity": 50.0,
                    "efficiency": 50.0,
                    "meaning": "Fair distribution and optimal outcomes both matter",
                },
            },
            "intervention_balance": {
                "upstream": 50.0,
                "downstream": 50.0,
                "description": "Address root causes and immediate needs",
            },
            "meta_meaning": "Public Health demonstrates META 50/50 in individual-population synthesis",
        }


def create_public_health_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> PublicHealthDomain:
    """
    Factory function to create a fully initialized public health domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized PublicHealthDomain
    """
    domain = PublicHealthDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_prevention_levels()
        domain.initialize_interventions()
        domain.initialize_public_health_pairs()

    return domain
