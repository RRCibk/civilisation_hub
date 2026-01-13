"""
Chemistry Domain
================
Chemical knowledge domain with META 50/50 equilibrium.
Fundamental duality: Stable/Reactive (molecular stability vs chemical reactivity).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class ChemistryDomain(KnowledgeDomain):
    """
    Chemistry knowledge domain.

    Fundamental Duality: Stable / Reactive
    - Stable: Inert, balanced electron configurations, low energy states
    - Reactive: Active, seeking electron balance, high energy states

    Secondary Dualities:
    - Acid / Base (proton dynamics)
    - Oxidation / Reduction (electron transfer)
    - Endothermic / Exothermic (energy flow)
    - Organic / Inorganic (carbon basis)
    - Ionic / Covalent (bonding types)
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Chemistry",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of matter, its properties, composition, and transformations",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Stable/Reactive duality."""
        self._domain.set_duality(
            positive_name="stable",
            positive_value=50,
            negative_name="reactive",
            negative_value=50,
            duality_name="chemistry_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental chemical laws as axioms."""
        laws = [
            (
                "Conservation of Mass",
                "Matter cannot be created or destroyed in chemical reactions",
            ),
            (
                "Law of Definite Proportions",
                "A compound always contains the same elements in the same proportions by mass",
            ),
            (
                "Law of Multiple Proportions",
                "Elements combine in ratios of small whole numbers",
            ),
            (
                "Avogadro's Law",
                "Equal volumes of gases at the same temperature and pressure contain equal numbers of molecules",
            ),
            (
                "Periodic Law",
                "Properties of elements are periodic functions of their atomic numbers",
            ),
            (
                "Octet Rule",
                "Atoms tend to gain, lose, or share electrons to achieve eight valence electrons",
            ),
            (
                "Le Chatelier's Principle",
                "Systems at equilibrium shift to counteract applied stress",
            ),
            (
                "Hess's Law",
                "Total enthalpy change is independent of the reaction pathway",
            ),
        ]

        for name, description in laws:
            self.create_concept(
                name=name,
                concept_type=ConceptType.LAW,
                description=description,
                certainty=90,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental chemistry concepts."""
        return [
            "Atom",
            "Molecule",
            "Element",
            "Compound",
            "Bond",
            "Electron",
            "Proton",
            "Neutron",
            "Ion",
            "Reaction",
            "Catalyst",
            "Solution",
            "Equilibrium",
            "pH",
            "Entropy",
        ]

    def initialize_branches(self) -> None:
        """Initialize major chemistry branches."""
        branches = [
            (
                "Organic Chemistry",
                "Study of carbon-containing compounds and their reactions",
                ConceptType.THEORY,
            ),
            (
                "Inorganic Chemistry",
                "Study of non-carbon compounds and metals",
                ConceptType.THEORY,
            ),
            (
                "Physical Chemistry",
                "Study of physical principles underlying chemical systems",
                ConceptType.THEORY,
            ),
            (
                "Analytical Chemistry",
                "Study of composition and structure of matter",
                ConceptType.THEORY,
            ),
            (
                "Biochemistry",
                "Study of chemical processes in living organisms",
                ConceptType.THEORY,
            ),
            (
                "Nuclear Chemistry",
                "Study of radioactive substances and nuclear processes",
                ConceptType.THEORY,
            ),
            (
                "Electrochemistry",
                "Study of chemical reactions that produce or are caused by electricity",
                ConceptType.THEORY,
            ),
            (
                "Thermochemistry",
                "Study of heat energy in chemical reactions",
                ConceptType.THEORY,
            ),
            (
                "Polymer Chemistry",
                "Study of large molecules made of repeating units",
                ConceptType.THEORY,
            ),
            (
                "Environmental Chemistry",
                "Study of chemical processes in the environment",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_elements(self) -> None:
        """Initialize key chemical elements."""
        elements = [
            ("Hydrogen", "H", 1, "Lightest element, most abundant in universe"),
            ("Carbon", "C", 6, "Basis of organic chemistry and life"),
            ("Nitrogen", "N", 7, "Essential for proteins and DNA"),
            ("Oxygen", "O", 8, "Essential for respiration and combustion"),
            ("Sodium", "Na", 11, "Reactive alkali metal"),
            ("Chlorine", "Cl", 17, "Reactive halogen"),
            ("Iron", "Fe", 26, "Essential transition metal"),
            ("Gold", "Au", 79, "Noble metal, highly stable"),
            ("Uranium", "U", 92, "Radioactive actinide"),
            ("Helium", "He", 2, "Noble gas, completely inert"),
        ]

        for name, symbol, atomic_number, description in elements:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "symbol": symbol,
                "atomic_number": atomic_number,
            })

    def initialize_bond_types(self) -> None:
        """Initialize chemical bond types."""
        bonds = [
            ("Ionic Bond", "Electrostatic attraction between oppositely charged ions", "NaCl"),
            ("Covalent Bond", "Sharing of electron pairs between atoms", "H2O"),
            ("Metallic Bond", "Sea of delocalized electrons among metal atoms", "Fe"),
            ("Hydrogen Bond", "Weak attraction between H and electronegative atoms", "H2O-H2O"),
            ("Van der Waals", "Weak intermolecular forces from temporary dipoles", "Noble gases"),
            ("Polar Covalent", "Unequal sharing of electrons", "HCl"),
            ("Nonpolar Covalent", "Equal sharing of electrons", "O2"),
            ("Coordinate Bond", "Both electrons from one atom", "NH4+"),
        ]

        for name, description, example in bonds:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["example"] = example

    def initialize_reaction_types(self) -> None:
        """Initialize chemical reaction types."""
        reactions = [
            ("Synthesis", "A + B -> AB", "Combination of reactants"),
            ("Decomposition", "AB -> A + B", "Breaking down of compound"),
            ("Single Replacement", "A + BC -> AC + B", "One element replaces another"),
            ("Double Replacement", "AB + CD -> AD + CB", "Exchange of ions"),
            ("Combustion", "Fuel + O2 -> CO2 + H2O", "Rapid oxidation with heat"),
            ("Redox", "Electron transfer between species", "Oxidation-reduction"),
            ("Neutralization", "Acid + Base -> Salt + Water", "Acid-base reaction"),
            ("Precipitation", "Formation of insoluble solid", "Ionic reaction"),
        ]

        for name, equation, description in reactions:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["equation_form"] = equation

    def initialize_states_of_matter(self) -> None:
        """Initialize states of matter."""
        states = [
            ("Solid", "Fixed shape and volume, particles vibrate in place"),
            ("Liquid", "Fixed volume, takes container shape, particles flow"),
            ("Gas", "Fills container, particles move freely"),
            ("Plasma", "Ionized gas, fourth state of matter"),
            ("Bose-Einstein Condensate", "Quantum state at near absolute zero"),
        ]

        for name, description in states:
            self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )

    def initialize_chemical_pairs(self) -> None:
        """Initialize fundamental chemical pairs with META 50/50 balance."""
        pairs = [
            ("Stable", "Reactive", "Molecular stability vs reactivity"),
            ("Element", "Compound", "Pure substance vs combination"),
            ("Acid", "Base", "Proton donor vs acceptor"),
            ("Oxidation", "Reduction", "Electron loss vs gain"),
            ("Endothermic", "Exothermic", "Heat absorbing vs releasing"),
            ("Organic", "Inorganic", "Carbon-based vs mineral"),
            ("Solid", "Gas", "Fixed vs dispersed state"),
            ("Solute", "Solvent", "Dissolved vs dissolving"),
            ("Cation", "Anion", "Positive vs negative ion"),
            ("Synthesis", "Decomposition", "Building vs breaking"),
            ("Ionic", "Covalent", "Electron transfer vs sharing"),
            ("Polar", "Nonpolar", "Charge asymmetry vs symmetry"),
            ("Saturated", "Unsaturated", "Full vs available bonds"),
            ("Catalyst", "Inhibitor", "Accelerating vs slowing"),
            ("Concentrated", "Dilute", "High vs low density"),
            ("Pure", "Mixture", "Single vs multiple substances"),
            ("Crystalline", "Amorphous", "Ordered vs disordered"),
            ("Hydrophilic", "Hydrophobic", "Water-loving vs fearing"),
            ("Metallic", "Nonmetallic", "Conductor vs insulator"),
            ("Reactant", "Product", "Starting vs ending material"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=positive,
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=negative,
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_periodic_table_groups(self) -> dict[str, list[str]]:
        """Get periodic table group classifications."""
        return {
            "alkali_metals": ["Li", "Na", "K", "Rb", "Cs", "Fr"],
            "alkaline_earth": ["Be", "Mg", "Ca", "Sr", "Ba", "Ra"],
            "transition_metals": ["Fe", "Cu", "Zn", "Ag", "Au", "Pt"],
            "halogens": ["F", "Cl", "Br", "I", "At"],
            "noble_gases": ["He", "Ne", "Ar", "Kr", "Xe", "Rn"],
            "metalloids": ["B", "Si", "Ge", "As", "Sb", "Te"],
            "lanthanides": ["La", "Ce", "Pr", "Nd", "Pm", "Sm"],
            "actinides": ["Ac", "Th", "Pa", "U", "Np", "Pu"],
        }

    def get_chemical_constants(self) -> dict[str, dict[str, Any]]:
        """Get important chemical constants."""
        return {
            "avogadro": {
                "value": 6.022e23,
                "unit": "mol^-1",
                "symbol": "NA",
                "description": "Number of particles in one mole",
            },
            "gas_constant": {
                "value": 8.314,
                "unit": "J/(mol·K)",
                "symbol": "R",
                "description": "Ideal gas constant",
            },
            "faraday": {
                "value": 96485,
                "unit": "C/mol",
                "symbol": "F",
                "description": "Charge per mole of electrons",
            },
            "boltzmann": {
                "value": 1.381e-23,
                "unit": "J/K",
                "symbol": "kB",
                "description": "Relates temperature to energy",
            },
            "planck": {
                "value": 6.626e-34,
                "unit": "J·s",
                "symbol": "h",
                "description": "Quantum of action",
            },
        }

    def demonstrate_chemical_balance(self) -> dict[str, Any]:
        """Demonstrate chemical balance principles."""
        return {
            "concept": "Chemical Equilibrium",
            "dualities": {
                "stable_reactive": {
                    "stable": 50.0,
                    "reactive": 50.0,
                    "meaning": "All matter exists between stability and reactivity",
                },
                "acid_base": {
                    "acid": 50.0,
                    "base": 50.0,
                    "meaning": "pH 7 represents perfect acid-base balance",
                },
                "oxidation_reduction": {
                    "oxidation": 50.0,
                    "reduction": 50.0,
                    "meaning": "Electrons lost equal electrons gained",
                },
            },
            "equilibrium_principle": {
                "forward_rate": 50.0,
                "reverse_rate": 50.0,
                "description": "At equilibrium, forward and reverse rates are equal",
            },
            "energy_balance": {
                "endothermic": 50.0,
                "exothermic": 50.0,
                "meaning": "Energy absorbed equals energy released in closed system",
            },
            "meta_meaning": "Chemistry demonstrates META 50/50 in all balanced reactions",
        }


def create_chemistry_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> ChemistryDomain:
    """
    Factory function to create a fully initialized chemistry domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized ChemistryDomain
    """
    domain = ChemistryDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_elements()
        domain.initialize_bond_types()
        domain.initialize_reaction_types()
        domain.initialize_states_of_matter()
        domain.initialize_chemical_pairs()

    return domain
