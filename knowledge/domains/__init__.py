"""
Knowledge Domains Package
=========================
Central package for all knowledge domains with META 50/50 equilibrium.
"""

from knowledge.domains.registry import (
    DomainRegistry,
    get_registry,
    reset_registry,
)

# Original Domains
from knowledge.domains.mathematics import create_mathematics_domain
from knowledge.domains.physics import create_physics_domain
from knowledge.domains.code import create_code_domain
from knowledge.domains.biology import create_biology_domain
from knowledge.domains.philosophy import create_philosophy_domain

# Natural Sciences
from knowledge.domains.chemistry import create_chemistry_domain
from knowledge.domains.astronomy import create_astronomy_domain
from knowledge.domains.geology import create_geology_domain
from knowledge.domains.ecology import create_ecology_domain
from knowledge.domains.meteorology import create_meteorology_domain
from knowledge.domains.oceanography import create_oceanography_domain
from knowledge.domains.botany import create_botany_domain
from knowledge.domains.zoology import create_zoology_domain
from knowledge.domains.microbiology import create_microbiology_domain
from knowledge.domains.genetics import create_genetics_domain
from knowledge.domains.neuroscience import create_neuroscience_domain
from knowledge.domains.pharmacology import create_pharmacology_domain
from knowledge.domains.anatomy import create_anatomy_domain
from knowledge.domains.physiology import create_physiology_domain
from knowledge.domains.paleontology import create_paleontology_domain

# Formal Sciences
from knowledge.domains.logic import create_logic_domain
from knowledge.domains.statistics import create_statistics_domain
from knowledge.domains.geometry import create_geometry_domain
from knowledge.domains.algebra import create_algebra_domain
from knowledge.domains.calculus import create_calculus_domain
from knowledge.domains.set_theory import create_set_theory_domain
from knowledge.domains.information_theory import create_information_theory_domain
from knowledge.domains.computation import create_computation_domain

# Social Sciences
from knowledge.domains.psychology import create_psychology_domain
from knowledge.domains.sociology import create_sociology_domain
from knowledge.domains.economics import create_economics_domain
from knowledge.domains.political_science import create_political_science_domain
from knowledge.domains.anthropology import create_anthropology_domain
from knowledge.domains.history import create_history_domain
from knowledge.domains.geography import create_geography_domain
from knowledge.domains.linguistics import create_linguistics_domain
from knowledge.domains.law import create_law_domain
from knowledge.domains.criminology import create_criminology_domain
from knowledge.domains.education import create_education_domain
from knowledge.domains.communication import create_communication_domain
from knowledge.domains.demography import create_demography_domain
from knowledge.domains.urban_studies import create_urban_studies_domain
from knowledge.domains.international_relations import create_international_relations_domain

# Humanities
from knowledge.domains.literature import create_literature_domain
from knowledge.domains.art import create_art_domain
from knowledge.domains.music import create_music_domain
from knowledge.domains.theater import create_theater_domain
from knowledge.domains.film import create_film_domain
from knowledge.domains.architecture import create_architecture_domain
from knowledge.domains.religious_studies import create_religious_studies_domain
from knowledge.domains.ethics import create_ethics_domain
from knowledge.domains.aesthetics import create_aesthetics_domain
from knowledge.domains.rhetoric import create_rhetoric_domain
from knowledge.domains.classics import create_classics_domain
from knowledge.domains.cultural_studies import create_cultural_studies_domain

# Applied Sciences
from knowledge.domains.engineering import create_engineering_domain
from knowledge.domains.medicine import create_medicine_domain
from knowledge.domains.agriculture import create_agriculture_domain
from knowledge.domains.computer_science import create_computer_science_domain
from knowledge.domains.nursing import create_nursing_domain
from knowledge.domains.dentistry import create_dentistry_domain
from knowledge.domains.veterinary_medicine import create_veterinary_medicine_domain
from knowledge.domains.public_health import create_public_health_domain
from knowledge.domains.environmental_science import create_environmental_science_domain
from knowledge.domains.materials_science import create_materials_science_domain
from knowledge.domains.biotechnology import create_biotechnology_domain
from knowledge.domains.nanotechnology import create_nanotechnology_domain
from knowledge.domains.robotics import create_robotics_domain
from knowledge.domains.artificial_intelligence import create_artificial_intelligence_domain
from knowledge.domains.data_science import create_data_science_domain
from knowledge.domains.cybersecurity import create_cybersecurity_domain
from knowledge.domains.aerospace import create_aerospace_domain
from knowledge.domains.nutrition_science import create_nutrition_science_domain
from knowledge.domains.forensic_science import create_forensic_science_domain
from knowledge.domains.management_science import create_management_science_domain

# Interdisciplinary Sciences
from knowledge.domains.cognitive_science import create_cognitive_science_domain
from knowledge.domains.biophysics import create_biophysics_domain
from knowledge.domains.geochemistry import create_geochemistry_domain
from knowledge.domains.astrophysics import create_astrophysics_domain
from knowledge.domains.bioethics import create_bioethics_domain
from knowledge.domains.sociobiology import create_sociobiology_domain
from knowledge.domains.psycholinguistics import create_psycholinguistics_domain
from knowledge.domains.econometrics import create_econometrics_domain
from knowledge.domains.bioinformatics import create_bioinformatics_domain
from knowledge.domains.systems_science import create_systems_science_domain

# Professional Sciences
from knowledge.domains.accounting import create_accounting_domain
from knowledge.domains.marketing import create_marketing_domain
from knowledge.domains.human_resources import create_human_resources_domain
from knowledge.domains.logistics import create_logistics_domain
from knowledge.domains.journalism import create_journalism_domain
from knowledge.domains.library_science import create_library_science_domain
from knowledge.domains.social_work import create_social_work_domain
from knowledge.domains.sports_science import create_sports_science_domain
from knowledge.domains.actuarial_science import create_actuarial_science_domain
from knowledge.domains.urban_planning import create_urban_planning_domain
from knowledge.domains.archival_science import create_archival_science_domain
from knowledge.domains.museum_studies import create_museum_studies_domain
from knowledge.domains.translation_studies import create_translation_studies_domain
from knowledge.domains.game_design import create_game_design_domain
from knowledge.domains.hospitality import create_hospitality_domain

__all__ = [
    # Registry
    "DomainRegistry",
    "get_registry",
    "reset_registry",
    # Original Domains
    "create_mathematics_domain",
    "create_physics_domain",
    "create_code_domain",
    "create_biology_domain",
    "create_philosophy_domain",
    # Natural Sciences
    "create_chemistry_domain",
    "create_astronomy_domain",
    "create_geology_domain",
    "create_ecology_domain",
    "create_meteorology_domain",
    "create_oceanography_domain",
    "create_botany_domain",
    "create_zoology_domain",
    "create_microbiology_domain",
    "create_genetics_domain",
    "create_neuroscience_domain",
    "create_pharmacology_domain",
    "create_anatomy_domain",
    "create_physiology_domain",
    "create_paleontology_domain",
    # Formal Sciences
    "create_logic_domain",
    "create_statistics_domain",
    "create_geometry_domain",
    "create_algebra_domain",
    "create_calculus_domain",
    "create_set_theory_domain",
    "create_information_theory_domain",
    "create_computation_domain",
    # Social Sciences
    "create_psychology_domain",
    "create_sociology_domain",
    "create_economics_domain",
    "create_political_science_domain",
    "create_anthropology_domain",
    "create_history_domain",
    "create_geography_domain",
    "create_linguistics_domain",
    "create_law_domain",
    "create_criminology_domain",
    "create_education_domain",
    "create_communication_domain",
    "create_demography_domain",
    "create_urban_studies_domain",
    "create_international_relations_domain",
    # Humanities
    "create_literature_domain",
    "create_art_domain",
    "create_music_domain",
    "create_theater_domain",
    "create_film_domain",
    "create_architecture_domain",
    "create_religious_studies_domain",
    "create_ethics_domain",
    "create_aesthetics_domain",
    "create_rhetoric_domain",
    "create_classics_domain",
    "create_cultural_studies_domain",
    # Applied Sciences
    "create_engineering_domain",
    "create_medicine_domain",
    "create_agriculture_domain",
    "create_computer_science_domain",
    "create_nursing_domain",
    "create_dentistry_domain",
    "create_veterinary_medicine_domain",
    "create_public_health_domain",
    "create_environmental_science_domain",
    "create_materials_science_domain",
    "create_biotechnology_domain",
    "create_nanotechnology_domain",
    "create_robotics_domain",
    "create_artificial_intelligence_domain",
    "create_data_science_domain",
    "create_cybersecurity_domain",
    "create_aerospace_domain",
    "create_nutrition_science_domain",
    "create_forensic_science_domain",
    "create_management_science_domain",
    # Interdisciplinary Sciences
    "create_cognitive_science_domain",
    "create_biophysics_domain",
    "create_geochemistry_domain",
    "create_astrophysics_domain",
    "create_bioethics_domain",
    "create_sociobiology_domain",
    "create_psycholinguistics_domain",
    "create_econometrics_domain",
    "create_bioinformatics_domain",
    "create_systems_science_domain",
    # Professional Sciences
    "create_accounting_domain",
    "create_marketing_domain",
    "create_human_resources_domain",
    "create_logistics_domain",
    "create_journalism_domain",
    "create_library_science_domain",
    "create_social_work_domain",
    "create_sports_science_domain",
    "create_actuarial_science_domain",
    "create_urban_planning_domain",
    "create_archival_science_domain",
    "create_museum_studies_domain",
    "create_translation_studies_domain",
    "create_game_design_domain",
    "create_hospitality_domain",
]


def get_all_domain_factories() -> dict:
    """
    Get all domain factory functions organized by category.

    Returns:
        Dictionary mapping category names to lists of factory functions
    """
    return {
        "original": [
            create_mathematics_domain,
            create_physics_domain,
            create_code_domain,
            create_biology_domain,
            create_philosophy_domain,
        ],
        "natural_sciences": [
            create_chemistry_domain,
            create_astronomy_domain,
            create_geology_domain,
            create_ecology_domain,
            create_meteorology_domain,
            create_oceanography_domain,
            create_botany_domain,
            create_zoology_domain,
            create_microbiology_domain,
            create_genetics_domain,
            create_neuroscience_domain,
            create_pharmacology_domain,
            create_anatomy_domain,
            create_physiology_domain,
            create_paleontology_domain,
        ],
        "formal_sciences": [
            create_logic_domain,
            create_statistics_domain,
            create_geometry_domain,
            create_algebra_domain,
            create_calculus_domain,
            create_set_theory_domain,
            create_information_theory_domain,
            create_computation_domain,
        ],
        "social_sciences": [
            create_psychology_domain,
            create_sociology_domain,
            create_economics_domain,
            create_political_science_domain,
            create_anthropology_domain,
            create_history_domain,
            create_geography_domain,
            create_linguistics_domain,
            create_law_domain,
            create_criminology_domain,
            create_education_domain,
            create_communication_domain,
            create_demography_domain,
            create_urban_studies_domain,
            create_international_relations_domain,
        ],
        "humanities": [
            create_literature_domain,
            create_art_domain,
            create_music_domain,
            create_theater_domain,
            create_film_domain,
            create_architecture_domain,
            create_religious_studies_domain,
            create_ethics_domain,
            create_aesthetics_domain,
            create_rhetoric_domain,
            create_classics_domain,
            create_cultural_studies_domain,
        ],
        "applied_sciences": [
            create_engineering_domain,
            create_medicine_domain,
            create_agriculture_domain,
            create_computer_science_domain,
            create_nursing_domain,
            create_dentistry_domain,
            create_veterinary_medicine_domain,
            create_public_health_domain,
            create_environmental_science_domain,
            create_materials_science_domain,
            create_biotechnology_domain,
            create_nanotechnology_domain,
            create_robotics_domain,
            create_artificial_intelligence_domain,
            create_data_science_domain,
            create_cybersecurity_domain,
            create_aerospace_domain,
            create_nutrition_science_domain,
            create_forensic_science_domain,
            create_management_science_domain,
        ],
        "interdisciplinary_sciences": [
            create_cognitive_science_domain,
            create_biophysics_domain,
            create_geochemistry_domain,
            create_astrophysics_domain,
            create_bioethics_domain,
            create_sociobiology_domain,
            create_psycholinguistics_domain,
            create_econometrics_domain,
            create_bioinformatics_domain,
            create_systems_science_domain,
        ],
        "professional_sciences": [
            create_accounting_domain,
            create_marketing_domain,
            create_human_resources_domain,
            create_logistics_domain,
            create_journalism_domain,
            create_library_science_domain,
            create_social_work_domain,
            create_sports_science_domain,
            create_actuarial_science_domain,
            create_urban_planning_domain,
            create_archival_science_domain,
            create_museum_studies_domain,
            create_translation_studies_domain,
            create_game_design_domain,
            create_hospitality_domain,
        ],
    }


def create_all_domains(meta_equilibrium=None):
    """
    Create all available domains.

    Args:
        meta_equilibrium: Optional shared MetaEquilibrium instance

    Returns:
        List of all created domains
    """
    factories = get_all_domain_factories()
    domains = []
    for category_factories in factories.values():
        for factory in category_factories:
            domains.append(factory(meta_equilibrium=meta_equilibrium))
    return domains
