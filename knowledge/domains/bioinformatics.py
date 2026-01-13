"""
Bioinformatics Domain
=====================
Bioinformatics knowledge domain with META 50/50 equilibrium.
Fundamental duality: Biology/Computation (life sciences vs informatics).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class BioinformaticsDomain(KnowledgeDomain):
    """
    Bioinformatics knowledge domain.

    Fundamental Duality: Biology / Computation
    - Biology: Biological data, living systems, experiments
    - Computation: Algorithms, databases, analysis tools

    Secondary Dualities:
    - Sequence / Structure
    - Wet Lab / Dry Lab
    - Discovery / Validation
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Bioinformatics",
            domain_type=DomainType.FUNDAMENTAL,
            description="The computational analysis of biological data",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Biology/Computation duality."""
        self._domain.set_duality(
            positive_name="biology",
            positive_value=50,
            negative_name="computation",
            negative_value=50,
            duality_name="bioinformatics_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental bioinformatics principles."""
        principles = [
            (
                "Sequence Determines Function",
                "Biological sequence encodes function",
            ),
            (
                "Homology Implies Similarity",
                "Related sequences have similar functions",
            ),
            (
                "Data Integration",
                "Combine multiple data types",
            ),
            (
                "Reproducibility",
                "Analyses must be reproducible",
            ),
            (
                "Scalability",
                "Methods must handle big data",
            ),
            (
                "Statistical Rigor",
                "Proper statistical validation",
            ),
            (
                "Open Science",
                "Share data and methods",
            ),
            (
                "Biological Context",
                "Interpret computationally in biological terms",
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
        """Get fundamental bioinformatics concepts."""
        return [
            "Sequence",
            "Alignment",
            "Database",
            "Algorithm",
            "Annotation",
            "Genome",
            "Proteome",
            "Transcriptome",
            "Homology",
            "Phylogeny",
            "Structure",
            "Pathway",
            "Network",
            "Expression",
            "Variant",
        ]

    def initialize_branches(self) -> None:
        """Initialize major bioinformatics branches."""
        branches = [
            (
                "Genomics",
                "Genome analysis",
                ConceptType.THEORY,
            ),
            (
                "Proteomics",
                "Protein analysis",
                ConceptType.THEORY,
            ),
            (
                "Transcriptomics",
                "Gene expression analysis",
                ConceptType.THEORY,
            ),
            (
                "Structural Bioinformatics",
                "Protein structure prediction",
                ConceptType.THEORY,
            ),
            (
                "Phylogenetics",
                "Evolutionary relationships",
                ConceptType.THEORY,
            ),
            (
                "Systems Biology",
                "Biological networks",
                ConceptType.THEORY,
            ),
            (
                "Metagenomics",
                "Community genomics",
                ConceptType.THEORY,
            ),
            (
                "Cheminformatics",
                "Chemical data analysis",
                ConceptType.THEORY,
            ),
            (
                "Clinical Bioinformatics",
                "Medical applications",
                ConceptType.THEORY,
            ),
            (
                "Text Mining",
                "Literature analysis",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_methods(self) -> None:
        """Initialize bioinformatics methods."""
        methods = [
            ("Sequence Alignment", "Comparing sequences", "Analysis"),
            ("BLAST", "Sequence similarity search", "Search"),
            ("Hidden Markov Models", "Probabilistic sequence models", "Modeling"),
            ("Clustering", "Grouping similar items", "Classification"),
            ("Machine Learning", "Pattern recognition", "Prediction"),
            ("Network Analysis", "Biological networks", "Systems"),
        ]

        for name, description, category in methods:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_databases(self) -> None:
        """Initialize major bioinformatics databases."""
        databases = [
            ("GenBank", "Nucleotide sequences", "NCBI"),
            ("UniProt", "Protein sequences", "SIB"),
            ("PDB", "Protein structures", "RCSB"),
            ("KEGG", "Pathways and metabolism", "Kanehisa"),
            ("GO", "Gene ontology", "Consortium"),
            ("ENSEMBL", "Genome browser", "EBI"),
        ]

        for name, description, source in databases:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["source"] = source

    def initialize_bioinformatics_pairs(self) -> None:
        """Initialize fundamental bioinformatics pairs with META 50/50 balance."""
        pairs = [
            ("Biology", "Computation", "Life vs informatics"),
            ("Sequence", "Structure", "Linear vs 3D"),
            ("Wet Lab", "Dry Lab", "Experimental vs computational"),
            ("Discovery", "Validation", "Finding vs confirming"),
            ("Global", "Local", "Whole vs part alignment"),
            ("Pairwise", "Multiple", "Two vs many sequences"),
            ("Sensitive", "Specific", "Finding all vs finding true"),
            ("Homology", "Analogy", "Common ancestry vs convergence"),
            ("Annotation", "Prediction", "Known vs inferred"),
            ("Raw", "Processed", "Original vs cleaned data"),
            ("Supervised", "Unsupervised", "Labeled vs unlabeled"),
            ("Model", "Data", "Algorithm vs information"),
            ("Reference", "Query", "Known vs unknown"),
            ("Conserved", "Variable", "Unchanged vs changing"),
            ("Coding", "Non-coding", "Genes vs regulatory"),
            ("Assembly", "Mapping", "Build vs align"),
            ("De Novo", "Reference-Based", "From scratch vs guided"),
            ("Bulk", "Single-Cell", "Population vs individual"),
            ("Static", "Dynamic", "Snapshot vs temporal"),
            ("Open", "Proprietary", "Public vs private"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Bioinfo)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Bioinfo)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_central_dogma(self) -> dict[str, str]:
        """Get central dogma of molecular biology."""
        return {
            "replication": "DNA -> DNA",
            "transcription": "DNA -> RNA",
            "translation": "RNA -> Protein",
            "reverse_transcription": "RNA -> DNA (retroviruses)",
        }

    def demonstrate_bioinformatics_balance(self) -> dict[str, Any]:
        """Demonstrate bioinformatics balance principles."""
        return {
            "concept": "Bioinformatics Equilibrium",
            "dualities": {
                "biology_computation": {
                    "biology": 50.0,
                    "computation": 50.0,
                    "meaning": "Life sciences and informatics unified",
                },
                "sequence_structure": {
                    "sequence": 50.0,
                    "structure": 50.0,
                    "meaning": "Linear and 3D equally important",
                },
                "discovery_validation": {
                    "discovery": 50.0,
                    "validation": 50.0,
                    "meaning": "Finding and confirming both essential",
                },
            },
            "research_balance": {
                "wet_lab": 50.0,
                "dry_lab": 50.0,
                "description": "Experimental and computational complement",
            },
            "meta_meaning": "Bioinformatics demonstrates META 50/50 in biology-computation synthesis",
        }


def create_bioinformatics_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> BioinformaticsDomain:
    """
    Factory function to create a fully initialized bioinformatics domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized BioinformaticsDomain
    """
    domain = BioinformaticsDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_methods()
        domain.initialize_databases()
        domain.initialize_bioinformatics_pairs()

    return domain
