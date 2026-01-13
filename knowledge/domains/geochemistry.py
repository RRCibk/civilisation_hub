"""
Geochemistry Domain
===================
Geochemistry knowledge domain with META 50/50 equilibrium.
Fundamental duality: Earth/Chemistry (geological vs chemical processes).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class GeochemistryDomain(KnowledgeDomain):
    """
    Geochemistry knowledge domain.

    Fundamental Duality: Earth / Chemistry
    - Earth: Geological systems, planetary processes
    - Chemistry: Chemical reactions, element behavior

    Secondary Dualities:
    - Organic / Inorganic
    - Surface / Deep
    - Past / Present
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Geochemistry",
            domain_type=DomainType.FUNDAMENTAL,
            description="The chemistry of Earth and planetary systems",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Earth/Chemistry duality."""
        self._domain.set_duality(
            positive_name="earth",
            positive_value=50,
            negative_name="chemistry",
            negative_value=50,
            duality_name="geochemistry_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental geochemistry principles."""
        principles = [
            (
                "Element Distribution",
                "Elements partition between phases",
            ),
            (
                "Thermodynamic Control",
                "Reactions seek equilibrium",
            ),
            (
                "Kinetic Constraints",
                "Rates limit what forms",
            ),
            (
                "Isotope Fractionation",
                "Isotopes record processes",
            ),
            (
                "Mass Balance",
                "Matter is conserved in cycles",
            ),
            (
                "Redox Reactions",
                "Electron transfer drives chemistry",
            ),
            (
                "Fluid Transport",
                "Fluids move elements",
            ),
            (
                "Geological Time",
                "Processes operate over vast time",
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
        """Get fundamental geochemistry concepts."""
        return [
            "Element",
            "Isotope",
            "Mineral",
            "Fluid",
            "Magma",
            "Weathering",
            "Cycle",
            "Reservoir",
            "Flux",
            "Partitioning",
            "Fractionation",
            "Redox",
            "pH",
            "Solubility",
            "Equilibrium",
        ]

    def initialize_branches(self) -> None:
        """Initialize major geochemistry branches."""
        branches = [
            (
                "Isotope Geochemistry",
                "Isotope ratios and dating",
                ConceptType.THEORY,
            ),
            (
                "Aqueous Geochemistry",
                "Water chemistry",
                ConceptType.THEORY,
            ),
            (
                "Organic Geochemistry",
                "Carbon compounds in Earth",
                ConceptType.THEORY,
            ),
            (
                "Igneous Geochemistry",
                "Magmatic processes",
                ConceptType.THEORY,
            ),
            (
                "Sedimentary Geochemistry",
                "Sediment chemistry",
                ConceptType.THEORY,
            ),
            (
                "Biogeochemistry",
                "Life-Earth chemistry",
                ConceptType.THEORY,
            ),
            (
                "Cosmochemistry",
                "Solar system chemistry",
                ConceptType.THEORY,
            ),
            (
                "Environmental Geochemistry",
                "Pollution and remediation",
                ConceptType.THEORY,
            ),
            (
                "Low-Temperature Geochemistry",
                "Surface processes",
                ConceptType.THEORY,
            ),
            (
                "High-Temperature Geochemistry",
                "Deep Earth processes",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_cycles(self) -> None:
        """Initialize geochemical cycles."""
        cycles = [
            ("Carbon Cycle", "CO2 and organic carbon", "Climate"),
            ("Nitrogen Cycle", "N fixation and release", "Life"),
            ("Sulfur Cycle", "S oxidation states", "Redox"),
            ("Phosphorus Cycle", "P weathering and burial", "Nutrients"),
            ("Water Cycle", "H2O movement", "Transport"),
            ("Rock Cycle", "Rock transformation", "Geological"),
        ]

        for name, description, significance in cycles:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["significance"] = significance

    def initialize_techniques(self) -> None:
        """Initialize geochemical techniques."""
        techniques = [
            ("Mass Spectrometry", "Isotope measurement", "Analytical"),
            ("XRF", "Element analysis", "Bulk"),
            ("Electron Microprobe", "Mineral chemistry", "In situ"),
            ("ICP-MS", "Trace elements", "Solution"),
            ("SIMS", "Ion imaging", "In situ"),
            ("Thermodynamic Modeling", "Equilibrium calculation", "Computational"),
        ]

        for name, description, category in techniques:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_geochemistry_pairs(self) -> None:
        """Initialize fundamental geochemistry pairs with META 50/50 balance."""
        pairs = [
            ("Earth", "Chemistry", "Geological vs chemical"),
            ("Organic", "Inorganic", "Carbon-based vs mineral"),
            ("Surface", "Deep", "Shallow vs interior"),
            ("Past", "Present", "Ancient vs modern"),
            ("Oxidized", "Reduced", "Electron-poor vs electron-rich"),
            ("Solid", "Fluid", "Rock vs water"),
            ("Source", "Sink", "Origin vs destination"),
            ("Open", "Closed", "Exchanging vs isolated"),
            ("Equilibrium", "Kinetic", "Stable vs rate-limited"),
            ("Major", "Trace", "Abundant vs rare elements"),
            ("Lithophile", "Siderophile", "Rock-loving vs iron-loving"),
            ("Compatible", "Incompatible", "Stays vs leaves"),
            ("Radiogenic", "Stable", "Decaying vs permanent"),
            ("Light", "Heavy", "Low vs high mass isotopes"),
            ("Continental", "Oceanic", "Land vs sea"),
            ("Juvenile", "Recycled", "New vs old material"),
            ("Magmatic", "Hydrothermal", "Melt vs fluid"),
            ("Primary", "Secondary", "Original vs altered"),
            ("Bulk", "In Situ", "Average vs point analysis"),
            ("Natural", "Anthropogenic", "Geological vs human"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Geochem)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Geochem)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_goldschmidt_classification(self) -> dict[str, str]:
        """Get Goldschmidt's element classification."""
        return {
            "lithophile": "Silicate-loving (O, Si, Al, Ca)",
            "siderophile": "Iron-loving (Fe, Ni, Co)",
            "chalcophile": "Sulfur-loving (Cu, Zn, Pb)",
            "atmophile": "Atmosphere-loving (N, noble gases)",
        }

    def demonstrate_geochemistry_balance(self) -> dict[str, Any]:
        """Demonstrate geochemistry balance principles."""
        return {
            "concept": "Geochemistry Equilibrium",
            "dualities": {
                "earth_chemistry": {
                    "earth": 50.0,
                    "chemistry": 50.0,
                    "meaning": "Geological and chemical perspectives unified",
                },
                "source_sink": {
                    "source": 50.0,
                    "sink": 50.0,
                    "meaning": "Inputs and outputs balance in cycles",
                },
                "equilibrium_kinetic": {
                    "equilibrium": 50.0,
                    "kinetic": 50.0,
                    "meaning": "Thermodynamics and rates both matter",
                },
            },
            "cycle_balance": {
                "input": 50.0,
                "output": 50.0,
                "description": "Geochemical cycles maintain balance",
            },
            "meta_meaning": "Geochemistry demonstrates META 50/50 in earth-chemistry synthesis",
        }


def create_geochemistry_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> GeochemistryDomain:
    """
    Factory function to create a fully initialized geochemistry domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized GeochemistryDomain
    """
    domain = GeochemistryDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_cycles()
        domain.initialize_techniques()
        domain.initialize_geochemistry_pairs()

    return domain
