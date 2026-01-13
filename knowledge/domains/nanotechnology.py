"""
Nanotechnology Domain
=====================
Nanotechnology knowledge domain with META 50/50 equilibrium.
Fundamental duality: Top-Down/Bottom-Up (miniaturization vs assembly).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class NanotechnologyDomain(KnowledgeDomain):
    """
    Nanotechnology knowledge domain.

    Fundamental Duality: Top-Down / Bottom-Up
    - Top-Down: Miniaturization, lithography, carving
    - Bottom-Up: Self-assembly, molecular construction

    Secondary Dualities:
    - Quantum / Classical
    - Surface / Bulk
    - Synthesis / Characterization
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Nanotechnology",
            domain_type=DomainType.FUNDAMENTAL,
            description="The manipulation of matter at atomic and molecular scales",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Top-Down/Bottom-Up duality."""
        self._domain.set_duality(
            positive_name="top_down",
            positive_value=50,
            negative_name="bottom_up",
            negative_value=50,
            duality_name="nanotechnology_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental nanotechnology principles."""
        principles = [
            (
                "Size-Dependent Properties",
                "Properties change at nanoscale",
            ),
            (
                "Surface Area Effects",
                "High surface-to-volume ratio dominates",
            ),
            (
                "Quantum Effects",
                "Quantum mechanics governs behavior",
            ),
            (
                "Self-Assembly",
                "Molecules can organize spontaneously",
            ),
            (
                "Precision Control",
                "Atomic-level control is achievable",
            ),
            (
                "Interdisciplinary Nature",
                "Requires multiple scientific disciplines",
            ),
            (
                "Scale Bridging",
                "Connects molecular to macroscopic",
            ),
            (
                "Novel Properties",
                "Nanomaterials exhibit unique behaviors",
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
        """Get fundamental nanotechnology concepts."""
        return [
            "Nanoscale",
            "Nanoparticle",
            "Nanostructure",
            "Self-Assembly",
            "Quantum Dot",
            "Nanotube",
            "Graphene",
            "Surface Area",
            "Lithography",
            "Molecular Machine",
            "AFM",
            "STM",
            "Thin Film",
            "Nanofabrication",
            "Nanomedicine",
        ]

    def initialize_branches(self) -> None:
        """Initialize major nanotechnology branches."""
        branches = [
            (
                "Nanomaterials",
                "Nanoscale materials synthesis",
                ConceptType.THEORY,
            ),
            (
                "Nanoelectronics",
                "Nanoscale electronic devices",
                ConceptType.THEORY,
            ),
            (
                "Nanomedicine",
                "Medical nanotechnology",
                ConceptType.THEORY,
            ),
            (
                "Nanophotonics",
                "Light-matter interactions at nanoscale",
                ConceptType.THEORY,
            ),
            (
                "Nanobiotechnology",
                "Biological nanotechnology",
                ConceptType.THEORY,
            ),
            (
                "Nanofabrication",
                "Manufacturing at nanoscale",
                ConceptType.THEORY,
            ),
            (
                "Nanofluidics",
                "Fluid behavior at nanoscale",
                ConceptType.THEORY,
            ),
            (
                "Molecular Nanotechnology",
                "Molecular machines",
                ConceptType.THEORY,
            ),
            (
                "Nanocharacterization",
                "Nanoscale analysis",
                ConceptType.THEORY,
            ),
            (
                "Computational Nanotechnology",
                "Modeling nanoscale systems",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_nanomaterials(self) -> None:
        """Initialize types of nanomaterials."""
        materials = [
            ("Carbon Nanotubes", "Cylindrical carbon", "Exceptional strength"),
            ("Graphene", "2D carbon sheet", "Electronic properties"),
            ("Quantum Dots", "Semiconductor nanocrystals", "Optical properties"),
            ("Nanowires", "1D nanostructures", "Electronics"),
            ("Nanoparticles", "0D nanostructures", "Catalysis"),
            ("Dendrimers", "Branched polymers", "Drug delivery"),
        ]

        for name, description, application in materials:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["application"] = application

    def initialize_techniques(self) -> None:
        """Initialize nanotechnology techniques."""
        techniques = [
            ("AFM", "Atomic force microscopy", "Imaging"),
            ("STM", "Scanning tunneling microscopy", "Imaging"),
            ("TEM", "Transmission electron microscopy", "Characterization"),
            ("Lithography", "Pattern transfer", "Fabrication"),
            ("CVD", "Chemical vapor deposition", "Synthesis"),
            ("Self-Assembly", "Spontaneous organization", "Bottom-up"),
        ]

        for name, description, category in techniques:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_nano_pairs(self) -> None:
        """Initialize fundamental nanotechnology pairs with META 50/50 balance."""
        pairs = [
            ("Top-Down", "Bottom-Up", "Miniaturization vs assembly"),
            ("Quantum", "Classical", "Wave-particle vs Newtonian"),
            ("Surface", "Bulk", "Interface vs interior"),
            ("Synthesis", "Characterization", "Making vs measuring"),
            ("0D", "3D", "Nanoparticle vs bulk"),
            ("Organic", "Inorganic", "Carbon-based vs metallic"),
            ("Single", "Ensemble", "Individual vs collective"),
            ("Wet", "Dry", "Solution vs vacuum"),
            ("Hard", "Soft", "Inorganic vs biological"),
            ("Active", "Passive", "Functional vs structural"),
            ("Local", "Global", "Site vs system"),
            ("Static", "Dynamic", "Fixed vs changing"),
            ("Ordered", "Random", "Structured vs disordered"),
            ("Natural", "Artificial", "Found vs made"),
            ("Experimental", "Theoretical", "Lab vs model"),
            ("Fundamental", "Applied", "Science vs technology"),
            ("Risk", "Benefit", "Danger vs advantage"),
            ("Small", "Large", "Nano vs macro effects"),
            ("Homogeneous", "Heterogeneous", "Uniform vs varied"),
            ("Intrinsic", "Extrinsic", "Inherent vs induced"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Nano)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Nano)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_length_scales(self) -> dict[str, str]:
        """Get relevant length scales in nanotechnology."""
        return {
            "angstrom": "0.1 nm - atomic bonds",
            "nanometer": "1-100 nm - nanostructures",
            "micrometer": "1000 nm - cells, microdevices",
            "quantum_confinement": "< 10 nm - quantum effects",
            "surface_effects": "< 100 nm - surface dominates",
            "molecular": "0.1-10 nm - molecules",
        }

    def demonstrate_nano_balance(self) -> dict[str, Any]:
        """Demonstrate nanotechnology balance principles."""
        return {
            "concept": "Nanotechnology Equilibrium",
            "dualities": {
                "top_down_bottom_up": {
                    "top_down": 50.0,
                    "bottom_up": 50.0,
                    "meaning": "Both approaches equally valuable",
                },
                "quantum_classical": {
                    "quantum": 50.0,
                    "classical": 50.0,
                    "meaning": "Nanoscale bridges quantum and classical",
                },
                "surface_bulk": {
                    "surface": 50.0,
                    "bulk": 50.0,
                    "meaning": "Interface and interior both matter",
                },
            },
            "research_balance": {
                "synthesis": 50.0,
                "characterization": 50.0,
                "description": "Making and measuring equally important",
            },
            "meta_meaning": "Nanotechnology demonstrates META 50/50 in top-down-bottom-up synthesis",
        }


def create_nanotechnology_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> NanotechnologyDomain:
    """
    Factory function to create a fully initialized nanotechnology domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized NanotechnologyDomain
    """
    domain = NanotechnologyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_nanomaterials()
        domain.initialize_techniques()
        domain.initialize_nano_pairs()

    return domain
