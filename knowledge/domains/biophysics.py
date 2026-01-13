"""
Biophysics Domain
=================
Biophysics knowledge domain with META 50/50 equilibrium.
Fundamental duality: Life/Physics (biological vs physical principles).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class BiophysicsDomain(KnowledgeDomain):
    """
    Biophysics knowledge domain.

    Fundamental Duality: Life / Physics
    - Life: Biological complexity, living systems
    - Physics: Physical laws, quantitative analysis

    Secondary Dualities:
    - Structure / Function
    - Molecular / Cellular
    - Theory / Experiment
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Biophysics",
            domain_type=DomainType.FUNDAMENTAL,
            description="The application of physics to biological systems",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Life/Physics duality."""
        self._domain.set_duality(
            positive_name="life",
            positive_value=50,
            negative_name="physics",
            negative_value=50,
            duality_name="biophysics_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental biophysics principles."""
        principles = [
            (
                "Physical Laws Apply",
                "Biology obeys physics",
            ),
            (
                "Structure Determines Function",
                "Molecular shape dictates activity",
            ),
            (
                "Energy Drives Life",
                "Thermodynamics governs biology",
            ),
            (
                "Quantitative Analysis",
                "Measure biological phenomena",
            ),
            (
                "Scale Matters",
                "Different physics at different scales",
            ),
            (
                "Dynamic Equilibrium",
                "Living systems maintain steady states",
            ),
            (
                "Information Flow",
                "Genetic and signaling information",
            ),
            (
                "Self-Organization",
                "Complex structures emerge",
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
        """Get fundamental biophysics concepts."""
        return [
            "Protein",
            "Membrane",
            "DNA",
            "Energy",
            "Force",
            "Diffusion",
            "Conformation",
            "Binding",
            "Folding",
            "Dynamics",
            "Structure",
            "Mechanics",
            "Thermodynamics",
            "Kinetics",
            "Spectroscopy",
        ]

    def initialize_branches(self) -> None:
        """Initialize major biophysics branches."""
        branches = [
            (
                "Molecular Biophysics",
                "Molecular structure and dynamics",
                ConceptType.THEORY,
            ),
            (
                "Membrane Biophysics",
                "Biological membranes",
                ConceptType.THEORY,
            ),
            (
                "Structural Biology",
                "Macromolecular structures",
                ConceptType.THEORY,
            ),
            (
                "Single Molecule Biophysics",
                "Individual molecule behavior",
                ConceptType.THEORY,
            ),
            (
                "Computational Biophysics",
                "Simulations and modeling",
                ConceptType.THEORY,
            ),
            (
                "Cellular Biophysics",
                "Physical cell properties",
                ConceptType.THEORY,
            ),
            (
                "Neurobiophysics",
                "Neural signal physics",
                ConceptType.THEORY,
            ),
            (
                "Biomechanics",
                "Mechanical properties of life",
                ConceptType.THEORY,
            ),
            (
                "Photobiophysics",
                "Light-biology interactions",
                ConceptType.THEORY,
            ),
            (
                "Medical Biophysics",
                "Clinical applications",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_techniques(self) -> None:
        """Initialize biophysical techniques."""
        techniques = [
            ("X-ray Crystallography", "Atomic structure", "Structural"),
            ("NMR Spectroscopy", "Solution structure", "Structural"),
            ("Cryo-EM", "Electron microscopy", "Imaging"),
            ("Fluorescence", "Molecular probing", "Spectroscopy"),
            ("AFM", "Surface imaging", "Microscopy"),
            ("Optical Tweezers", "Force measurement", "Manipulation"),
        ]

        for name, description, category in techniques:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_phenomena(self) -> None:
        """Initialize biophysical phenomena."""
        phenomena = [
            ("Protein Folding", "3D structure formation", "Molecular"),
            ("Ion Channel Gating", "Membrane transport", "Cellular"),
            ("Molecular Motors", "Force generation", "Mechanical"),
            ("DNA Replication", "Genetic copying", "Molecular"),
            ("Photosynthesis", "Light energy capture", "Energy"),
            ("Membrane Fusion", "Vesicle merging", "Cellular"),
        ]

        for name, description, category in phenomena:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_biophysics_pairs(self) -> None:
        """Initialize fundamental biophysics pairs with META 50/50 balance."""
        pairs = [
            ("Life", "Physics", "Biological vs physical"),
            ("Structure", "Function", "Form vs activity"),
            ("Molecular", "Cellular", "Molecule vs cell"),
            ("Theory", "Experiment", "Model vs measurement"),
            ("Static", "Dynamic", "Fixed vs moving"),
            ("Equilibrium", "Non-equilibrium", "Stable vs driven"),
            ("Deterministic", "Stochastic", "Predictable vs random"),
            ("In Vitro", "In Vivo", "Test tube vs living"),
            ("Single", "Ensemble", "One vs many"),
            ("Local", "Global", "Site vs whole"),
            ("Classical", "Quantum", "Newtonian vs quantum"),
            ("Reversible", "Irreversible", "Undoable vs permanent"),
            ("Active", "Passive", "Energy-using vs spontaneous"),
            ("Ordered", "Disordered", "Structured vs random"),
            ("Bound", "Free", "Attached vs loose"),
            ("Native", "Denatured", "Folded vs unfolded"),
            ("Hydrophobic", "Hydrophilic", "Water-fearing vs water-loving"),
            ("Specific", "Non-specific", "Selective vs general"),
            ("Fast", "Slow", "Quick vs gradual kinetics"),
            ("Strong", "Weak", "High vs low affinity"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Biophysics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Biophysics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_forces_in_biology(self) -> dict[str, str]:
        """Get forces important in biology."""
        return {
            "electrostatic": "Charge-charge interactions",
            "van_der_waals": "Weak attractive forces",
            "hydrogen_bond": "H-bond donor-acceptor",
            "hydrophobic": "Water exclusion effect",
            "covalent": "Electron sharing",
            "entropic": "Disorder-driven forces",
        }

    def demonstrate_biophysics_balance(self) -> dict[str, Any]:
        """Demonstrate biophysics balance principles."""
        return {
            "concept": "Biophysics Equilibrium",
            "dualities": {
                "life_physics": {
                    "life": 50.0,
                    "physics": 50.0,
                    "meaning": "Biology and physics unified",
                },
                "structure_function": {
                    "structure": 50.0,
                    "function": 50.0,
                    "meaning": "Form and activity inseparable",
                },
                "theory_experiment": {
                    "theory": 50.0,
                    "experiment": 50.0,
                    "meaning": "Models and measurements complement",
                },
            },
            "scale_balance": {
                "molecular": 50.0,
                "cellular": 50.0,
                "description": "Different scales equally important",
            },
            "meta_meaning": "Biophysics demonstrates META 50/50 in life-physics synthesis",
        }


def create_biophysics_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> BiophysicsDomain:
    """
    Factory function to create a fully initialized biophysics domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized BiophysicsDomain
    """
    domain = BiophysicsDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_techniques()
        domain.initialize_phenomena()
        domain.initialize_biophysics_pairs()

    return domain
