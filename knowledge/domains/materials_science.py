"""
Materials Science Domain
========================
Materials science knowledge domain with META 50/50 equilibrium.
Fundamental duality: Structure/Property (arrangement vs behavior).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class MaterialsScienceDomain(KnowledgeDomain):
    """
    Materials Science knowledge domain.

    Fundamental Duality: Structure / Property
    - Structure: Atomic arrangement, microstructure
    - Property: Mechanical, electrical, thermal behavior

    Secondary Dualities:
    - Natural / Synthetic
    - Processing / Performance
    - Strength / Ductility
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="MaterialsScience",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of materials structure, properties, and applications",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Structure/Property duality."""
        self._domain.set_duality(
            positive_name="structure",
            positive_value=50,
            negative_name="property",
            negative_value=50,
            duality_name="materials_science_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental materials science principles."""
        principles = [
            (
                "Structure-Property Relationship",
                "Structure determines properties",
            ),
            (
                "Processing-Structure Link",
                "Processing determines structure",
            ),
            (
                "Scale Dependence",
                "Properties vary with length scale",
            ),
            (
                "Thermodynamic Stability",
                "Materials seek lowest energy state",
            ),
            (
                "Defect Influence",
                "Defects control many properties",
            ),
            (
                "Kinetics Matter",
                "Rate processes affect structure",
            ),
            (
                "Composition Effects",
                "Chemical composition affects properties",
            ),
            (
                "Processing History",
                "Past processing affects current state",
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
        """Get fundamental materials science concepts."""
        return [
            "Structure",
            "Property",
            "Microstructure",
            "Crystal",
            "Defect",
            "Phase",
            "Strength",
            "Hardness",
            "Ductility",
            "Conductivity",
            "Corrosion",
            "Alloy",
            "Polymer",
            "Ceramic",
            "Composite",
        ]

    def initialize_branches(self) -> None:
        """Initialize major materials science branches."""
        branches = [
            (
                "Metallurgy",
                "Metal processing and properties",
                ConceptType.THEORY,
            ),
            (
                "Polymer Science",
                "Polymer synthesis and behavior",
                ConceptType.THEORY,
            ),
            (
                "Ceramic Science",
                "Ceramic materials",
                ConceptType.THEORY,
            ),
            (
                "Semiconductor Materials",
                "Electronic materials",
                ConceptType.THEORY,
            ),
            (
                "Biomaterials",
                "Medical materials",
                ConceptType.THEORY,
            ),
            (
                "Nanomaterials",
                "Nanoscale materials",
                ConceptType.THEORY,
            ),
            (
                "Composite Materials",
                "Multi-phase materials",
                ConceptType.THEORY,
            ),
            (
                "Tribology",
                "Friction and wear",
                ConceptType.THEORY,
            ),
            (
                "Corrosion Science",
                "Material degradation",
                ConceptType.THEORY,
            ),
            (
                "Materials Characterization",
                "Analysis techniques",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_material_classes(self) -> None:
        """Initialize major material classes."""
        classes = [
            ("Metals", "Metallic bonding", "Conductive, ductile"),
            ("Ceramics", "Ionic/covalent bonding", "Hard, brittle"),
            ("Polymers", "Chain molecules", "Flexible, lightweight"),
            ("Composites", "Combined materials", "Engineered properties"),
            ("Semiconductors", "Band gap materials", "Electronic control"),
            ("Biomaterials", "Biocompatible", "Medical applications"),
        ]

        for name, bonding, properties in classes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=bonding,
            )
            concept.metadata["properties"] = properties

    def initialize_properties(self) -> None:
        """Initialize material properties."""
        properties = [
            ("Mechanical", "Stress-strain behavior", "Strength, hardness"),
            ("Electrical", "Electron transport", "Conductivity"),
            ("Thermal", "Heat behavior", "Conductivity, expansion"),
            ("Optical", "Light interaction", "Transparency, color"),
            ("Magnetic", "Magnetic behavior", "Permeability"),
            ("Chemical", "Chemical reactivity", "Corrosion resistance"),
        ]

        for name, description, examples in properties:
            concept = self.create_concept(
                name=f"{name} Properties",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_materials_pairs(self) -> None:
        """Initialize fundamental materials science pairs with META 50/50 balance."""
        pairs = [
            ("Structure", "Property", "Arrangement vs behavior"),
            ("Natural", "Synthetic", "Found vs made"),
            ("Processing", "Performance", "Making vs using"),
            ("Strength", "Ductility", "Strong vs formable"),
            ("Crystalline", "Amorphous", "Ordered vs disordered"),
            ("Elastic", "Plastic", "Reversible vs permanent"),
            ("Brittle", "Tough", "Breaking vs absorbing"),
            ("Conductor", "Insulator", "Conducting vs blocking"),
            ("Pure", "Alloy", "Single vs mixed"),
            ("Bulk", "Surface", "Interior vs exterior"),
            ("Equilibrium", "Non-equilibrium", "Stable vs metastable"),
            ("Intrinsic", "Extrinsic", "Inherent vs added"),
            ("Macro", "Micro", "Large scale vs small scale"),
            ("Single Crystal", "Polycrystalline", "One vs many grains"),
            ("Hard", "Soft", "Resistant vs yielding"),
            ("Dense", "Porous", "Solid vs holey"),
            ("Homogeneous", "Heterogeneous", "Uniform vs varied"),
            ("Static", "Dynamic", "Fixed vs changing"),
            ("Primary", "Secondary", "Direct vs derived"),
            ("Raw", "Processed", "As-found vs treated"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Materials)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Materials)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_crystal_structures(self) -> dict[str, str]:
        """Get common crystal structures."""
        return {
            "fcc": "Face-centered cubic - Cu, Al, Au",
            "bcc": "Body-centered cubic - Fe, W, Cr",
            "hcp": "Hexagonal close-packed - Ti, Zn, Mg",
            "diamond": "Diamond cubic - C, Si, Ge",
            "rocksalt": "NaCl structure - ionic compounds",
            "perovskite": "ABO3 structure - functional ceramics",
        }

    def demonstrate_materials_balance(self) -> dict[str, Any]:
        """Demonstrate materials science balance principles."""
        return {
            "concept": "Materials Science Equilibrium",
            "dualities": {
                "structure_property": {
                    "structure": 50.0,
                    "property": 50.0,
                    "meaning": "Structure and property are inseparable",
                },
                "processing_performance": {
                    "processing": 50.0,
                    "performance": 50.0,
                    "meaning": "How made determines how performs",
                },
                "strength_ductility": {
                    "strength": 50.0,
                    "ductility": 50.0,
                    "meaning": "Trade-off between strong and formable",
                },
            },
            "design_balance": {
                "composition": 50.0,
                "microstructure": 50.0,
                "description": "Chemistry and structure both determine properties",
            },
            "meta_meaning": "Materials Science demonstrates META 50/50 in structure-property unity",
        }


def create_materials_science_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> MaterialsScienceDomain:
    """
    Factory function to create a fully initialized materials science domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized MaterialsScienceDomain
    """
    domain = MaterialsScienceDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_material_classes()
        domain.initialize_properties()
        domain.initialize_materials_pairs()

    return domain
