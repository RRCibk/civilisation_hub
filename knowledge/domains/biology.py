"""
Biology Domain
==============
Life science knowledge domain with META 50/50 equilibrium.
Fundamental duality: Life/Death (anabolism/catabolism, creation/destruction).
"""

from typing import Any
from uuid import UUID

from models.domain import DomainType
from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    KnowledgeDomain,
    Concept,
    ConceptType,
    ConceptRelation,
    RelationType,
)


class BiologyDomain(KnowledgeDomain):
    """
    Biology knowledge domain.

    Fundamental Duality: Life / Death (Creation / Destruction)
    - Life: Growth, reproduction, metabolism, organization
    - Death: Decay, apoptosis, entropy, decomposition

    Secondary Dualities:
    - Anabolism / Catabolism (build up / break down)
    - Genotype / Phenotype (genetic / expressed)
    - Nature / Nurture (genetic / environmental)
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Biology",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of living organisms and life processes",
            meta_equilibrium=meta_equilibrium
        )

    def _initialize_duality(self) -> None:
        """Initialize Life/Death duality."""
        self._domain.set_duality(
            positive_name="life",
            positive_value=50,
            negative_name="death",
            negative_value=50,
            duality_name="biology_duality"
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental biological principles as axioms."""
        principles = [
            (
                "Cell Theory",
                "All living organisms are composed of cells; cells are the basic unit of life"
            ),
            (
                "Gene Theory",
                "Traits are inherited through genes; DNA is the hereditary material"
            ),
            (
                "Evolution by Natural Selection",
                "Species evolve through variation, inheritance, selection, and time"
            ),
            (
                "Homeostasis",
                "Living systems maintain internal equilibrium despite external changes"
            ),
            (
                "Energy Flow",
                "Energy flows through ecosystems from producers to consumers"
            ),
            (
                "Central Dogma",
                "Genetic information flows: DNA → RNA → Protein"
            ),
            (
                "Biogenesis",
                "Life arises only from existing life"
            ),
            (
                "Unity and Diversity",
                "All life shares common ancestry yet exhibits vast diversity"
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=95  # High certainty biological principles
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental biology concepts."""
        return [
            "Cell", "Gene", "Protein", "DNA", "RNA",
            "Organism", "Species", "Evolution", "Metabolism", "Reproduction",
            "Ecosystem", "Population", "Adaptation", "Mutation", "Selection"
        ]

    def initialize_branches(self) -> None:
        """Initialize major biology branches."""
        branches = [
            ("Molecular Biology", "Study of biological molecules", ConceptType.THEORY),
            ("Cell Biology", "Study of cell structure and function", ConceptType.THEORY),
            ("Genetics", "Study of heredity and variation", ConceptType.THEORY),
            ("Evolutionary Biology", "Study of evolutionary processes", ConceptType.THEORY),
            ("Ecology", "Study of organisms and environments", ConceptType.THEORY),
            ("Physiology", "Study of organism functions", ConceptType.THEORY),
            ("Anatomy", "Study of organism structure", ConceptType.THEORY),
            ("Biochemistry", "Chemistry of living systems", ConceptType.THEORY),
            ("Microbiology", "Study of microorganisms", ConceptType.THEORY),
            ("Botany", "Study of plants", ConceptType.THEORY),
            ("Zoology", "Study of animals", ConceptType.THEORY),
            ("Neuroscience", "Study of the nervous system", ConceptType.THEORY),
            ("Immunology", "Study of immune systems", ConceptType.THEORY),
            ("Bioinformatics", "Computational analysis of biological data", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_taxonomic_ranks(self) -> None:
        """Initialize biological classification hierarchy."""
        ranks = [
            ("Domain", "Highest taxonomic rank", "Bacteria, Archaea, Eukarya"),
            ("Kingdom", "Major group of organisms", "Animalia, Plantae, Fungi"),
            ("Phylum", "Body plan grouping", "Chordata, Arthropoda"),
            ("Class", "Subdivision of phylum", "Mammalia, Aves, Reptilia"),
            ("Order", "Subdivision of class", "Primates, Carnivora"),
            ("Family", "Subdivision of order", "Hominidae, Felidae"),
            ("Genus", "Group of related species", "Homo, Felis"),
            ("Species", "Basic unit of classification", "Homo sapiens"),
        ]

        concepts = []
        for name, description, examples in ranks:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description
            )
            concept.metadata["examples"] = examples
            concepts.append(concept)

        # Create hierarchy relations
        for i in range(len(concepts) - 1):
            self.create_relation(
                concepts[i],
                concepts[i + 1],
                RelationType.SPECIALIZES,
                strength=100
            )

    def initialize_cell_components(self) -> None:
        """Initialize cell structures and organelles."""
        organelles = [
            ("Nucleus", "Contains genetic material (DNA)", "Eukaryotes"),
            ("Mitochondria", "Produces ATP through cellular respiration", "Eukaryotes"),
            ("Chloroplast", "Performs photosynthesis", "Plants, algae"),
            ("Endoplasmic Reticulum", "Protein and lipid synthesis", "Eukaryotes"),
            ("Golgi Apparatus", "Modifies and packages proteins", "Eukaryotes"),
            ("Ribosome", "Protein synthesis", "All cells"),
            ("Cell Membrane", "Controls what enters and exits", "All cells"),
            ("Cell Wall", "Structural support", "Plants, fungi, bacteria"),
            ("Lysosome", "Digests cellular waste", "Animal cells"),
            ("Vacuole", "Storage of materials", "Plant cells"),
            ("Cytoplasm", "Gel-like fluid filling the cell", "All cells"),
            ("Cytoskeleton", "Structural support network", "Eukaryotes"),
        ]

        for name, function, found_in in organelles:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=function
            )
            concept.metadata["found_in"] = found_in

    def initialize_macromolecules(self) -> None:
        """Initialize biological macromolecules."""
        molecules = [
            (
                "Carbohydrates",
                "Energy storage and structural molecules",
                "Cn(H2O)n",
                ["Glucose", "Starch", "Cellulose"]
            ),
            (
                "Proteins",
                "Enzymes, structural components, signaling",
                "Amino acid polymers",
                ["Enzymes", "Antibodies", "Collagen"]
            ),
            (
                "Lipids",
                "Energy storage, membranes, signaling",
                "Fatty acids + glycerol",
                ["Fats", "Phospholipids", "Steroids"]
            ),
            (
                "Nucleic Acids",
                "Genetic information storage and transfer",
                "Nucleotide polymers",
                ["DNA", "RNA"]
            ),
        ]

        for name, function, structure, examples in molecules:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=function
            )
            concept.metadata.update({
                "basic_structure": structure,
                "examples": examples
            })

    def initialize_biological_processes(self) -> None:
        """Initialize key biological processes."""
        processes = [
            (
                "Photosynthesis",
                "Convert light energy to chemical energy",
                "6CO2 + 6H2O → C6H12O6 + 6O2"
            ),
            (
                "Cellular Respiration",
                "Extract energy from glucose",
                "C6H12O6 + 6O2 → 6CO2 + 6H2O + ATP"
            ),
            (
                "DNA Replication",
                "Copy genetic information",
                "DNA → 2 identical DNA molecules"
            ),
            (
                "Transcription",
                "Copy DNA to RNA",
                "DNA → mRNA"
            ),
            (
                "Translation",
                "Build proteins from mRNA",
                "mRNA → Protein"
            ),
            (
                "Mitosis",
                "Cell division for growth",
                "1 cell → 2 identical cells"
            ),
            (
                "Meiosis",
                "Cell division for reproduction",
                "1 cell → 4 haploid cells"
            ),
            (
                "Apoptosis",
                "Programmed cell death",
                "Controlled cellular destruction"
            ),
        ]

        for name, description, formula in processes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.MODEL,
                description=description
            )
            concept.metadata["formula"] = formula

    def demonstrate_biological_balance(self) -> dict[str, Any]:
        """
        Demonstrate biological balance principles.
        Shows META 50/50 in living systems.
        """
        return {
            "concept": "Biological Equilibrium",
            "dualities": {
                "anabolism_catabolism": {
                    "anabolism": 50.0,
                    "catabolism": 50.0,
                    "meaning": "Building up and breaking down must balance"
                },
                "birth_death": {
                    "birth": 50.0,
                    "death": 50.0,
                    "meaning": "Population equilibrium requires balanced rates"
                },
                "predator_prey": {
                    "predator": 50.0,
                    "prey": 50.0,
                    "meaning": "Ecosystem balance through population dynamics"
                },
                "production_consumption": {
                    "production": 50.0,
                    "consumption": 50.0,
                    "meaning": "Energy flow maintains ecosystem balance"
                }
            },
            "homeostasis": {
                "description": "Living systems maintain internal balance",
                "examples": [
                    "Body temperature regulation",
                    "Blood pH balance",
                    "Blood glucose levels",
                    "Water balance"
                ]
            },
            "meta_meaning": "Life maintains dynamic equilibrium through balanced processes"
        }

    def get_genetic_code(self) -> dict[str, str]:
        """Get the standard genetic code (codon to amino acid)."""
        return {
            "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
            "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
            "UAU": "Tyr", "UAC": "Tyr", "UAA": "Stop", "UAG": "Stop",
            "UGU": "Cys", "UGC": "Cys", "UGA": "Stop", "UGG": "Trp",
            "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
            "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
            "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
            "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
            "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
            "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
            "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
            "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
            "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
            "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
            "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
            "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
        }


def create_biology_domain(
    meta_equilibrium: MetaEquilibrium | None = None,
    initialize_all: bool = True
) -> BiologyDomain:
    """
    Factory function to create a fully initialized biology domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized BiologyDomain
    """
    domain = BiologyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_taxonomic_ranks()
        domain.initialize_cell_components()
        domain.initialize_macromolecules()
        domain.initialize_biological_processes()

    return domain
