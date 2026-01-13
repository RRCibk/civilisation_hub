"""
Biotechnology Domain
====================
Biotechnology knowledge domain with META 50/50 equilibrium.
Fundamental duality: Nature/Technology (biological vs engineered).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class BiotechnologyDomain(KnowledgeDomain):
    """
    Biotechnology knowledge domain.

    Fundamental Duality: Nature / Technology
    - Nature: Biological systems, natural processes
    - Technology: Engineering, modification, applications

    Secondary Dualities:
    - Research / Application
    - Risk / Benefit
    - Traditional / Modern
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Biotechnology",
            domain_type=DomainType.FUNDAMENTAL,
            description="The application of biology to develop technologies and products",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Nature/Technology duality."""
        self._domain.set_duality(
            positive_name="nature",
            positive_value=50,
            negative_name="technology",
            negative_value=50,
            duality_name="biotechnology_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental biotechnology principles."""
        principles = [
            (
                "Biological Basis",
                "All biotechnology built on biological understanding",
            ),
            (
                "Genetic Information",
                "DNA contains instructions for life",
            ),
            (
                "Protein Function",
                "Proteins are functional molecules",
            ),
            (
                "Cell as Factory",
                "Cells can be engineered production systems",
            ),
            (
                "Evolution as Tool",
                "Natural selection can be directed",
            ),
            (
                "Bioethics",
                "Ethical considerations guide applications",
            ),
            (
                "Safety First",
                "Biosafety essential in all work",
            ),
            (
                "Scale-Up Challenge",
                "Lab to production requires optimization",
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=85,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental biotechnology concepts."""
        return [
            "DNA",
            "Gene",
            "Protein",
            "Cell",
            "Enzyme",
            "Fermentation",
            "Cloning",
            "Recombinant",
            "Expression",
            "Vector",
            "Transgenic",
            "Bioreactor",
            "Downstream",
            "Biosafety",
            "Bioproduct",
        ]

    def initialize_branches(self) -> None:
        """Initialize major biotechnology branches."""
        branches = [
            (
                "Medical Biotechnology",
                "Healthcare applications",
                ConceptType.THEORY,
            ),
            (
                "Agricultural Biotechnology",
                "Crop and animal improvement",
                ConceptType.THEORY,
            ),
            (
                "Industrial Biotechnology",
                "Manufacturing applications",
                ConceptType.THEORY,
            ),
            (
                "Environmental Biotechnology",
                "Environmental applications",
                ConceptType.THEORY,
            ),
            (
                "Marine Biotechnology",
                "Ocean-based applications",
                ConceptType.THEORY,
            ),
            (
                "Genetic Engineering",
                "DNA modification",
                ConceptType.THEORY,
            ),
            (
                "Synthetic Biology",
                "Designed biological systems",
                ConceptType.THEORY,
            ),
            (
                "Bioinformatics",
                "Computational biology",
                ConceptType.THEORY,
            ),
            (
                "Bioprocessing",
                "Production processes",
                ConceptType.THEORY,
            ),
            (
                "Tissue Engineering",
                "Artificial tissues",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_techniques(self) -> None:
        """Initialize biotechnology techniques."""
        techniques = [
            ("PCR", "DNA amplification", "Molecular"),
            ("CRISPR", "Gene editing", "Genetic"),
            ("Fermentation", "Microbial production", "Bioprocess"),
            ("Chromatography", "Protein purification", "Downstream"),
            ("Sequencing", "DNA reading", "Analytical"),
            ("Cell Culture", "Cell growth", "Cell biology"),
        ]

        for name, description, category in techniques:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_products(self) -> None:
        """Initialize biotechnology products."""
        products = [
            ("Vaccines", "Disease prevention", "Medical"),
            ("Antibiotics", "Infection treatment", "Pharmaceutical"),
            ("Enzymes", "Industrial catalysts", "Industrial"),
            ("Biofuels", "Renewable energy", "Environmental"),
            ("GM Crops", "Modified plants", "Agricultural"),
            ("Biologics", "Protein drugs", "Therapeutic"),
        ]

        for name, description, sector in products:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["sector"] = sector

    def initialize_biotech_pairs(self) -> None:
        """Initialize fundamental biotechnology pairs with META 50/50 balance."""
        pairs = [
            ("Nature", "Technology", "Biological vs engineered"),
            ("Research", "Application", "Discovery vs use"),
            ("Risk", "Benefit", "Danger vs advantage"),
            ("Traditional", "Modern", "Classic vs new methods"),
            ("In Vivo", "In Vitro", "Living vs lab"),
            ("Upstream", "Downstream", "Production vs purification"),
            ("Prokaryotic", "Eukaryotic", "Bacteria vs complex cells"),
            ("Wild Type", "Mutant", "Natural vs modified"),
            ("Expression", "Regulation", "Making vs controlling"),
            ("Discovery", "Development", "Finding vs optimizing"),
            ("Academic", "Industrial", "Research vs commercial"),
            ("Small Scale", "Large Scale", "Lab vs production"),
            ("Qualitative", "Quantitative", "Type vs amount"),
            ("Targeted", "Random", "Precise vs undirected"),
            ("Containment", "Release", "Controlled vs open"),
            ("Patent", "Public", "Protected vs shared"),
            ("Basic", "Applied", "Fundamental vs practical"),
            ("Red", "Green", "Medical vs agricultural biotech"),
            ("Natural", "Synthetic", "Found vs designed"),
            ("Safety", "Efficacy", "Safe vs effective"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Biotech)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Biotech)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_color_classification(self) -> dict[str, str]:
        """Get biotechnology color classification."""
        return {
            "red": "Medical and pharmaceutical biotechnology",
            "green": "Agricultural biotechnology",
            "white": "Industrial biotechnology",
            "blue": "Marine and aquatic biotechnology",
            "grey": "Environmental biotechnology",
            "gold": "Bioinformatics and computational",
        }

    def demonstrate_biotech_balance(self) -> dict[str, Any]:
        """Demonstrate biotechnology balance principles."""
        return {
            "concept": "Biotechnology Equilibrium",
            "dualities": {
                "nature_technology": {
                    "nature": 50.0,
                    "technology": 50.0,
                    "meaning": "Understanding biology to engineer solutions",
                },
                "risk_benefit": {
                    "risk": 50.0,
                    "benefit": 50.0,
                    "meaning": "Assessing both dangers and advantages",
                },
                "research_application": {
                    "research": 50.0,
                    "application": 50.0,
                    "meaning": "Discovery and use are complementary",
                },
            },
            "development_balance": {
                "upstream": 50.0,
                "downstream": 50.0,
                "description": "Production and purification equally important",
            },
            "meta_meaning": "Biotechnology demonstrates META 50/50 in nature-technology synthesis",
        }


def create_biotechnology_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> BiotechnologyDomain:
    """
    Factory function to create a fully initialized biotechnology domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized BiotechnologyDomain
    """
    domain = BiotechnologyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_techniques()
        domain.initialize_products()
        domain.initialize_biotech_pairs()

    return domain
