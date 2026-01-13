"""
Genetics Domain
===============
Genetic knowledge domain with META 50/50 equilibrium.
Fundamental duality: Expression/Suppression (gene activity regulation).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class GeneticsDomain(KnowledgeDomain):
    """
    Genetics knowledge domain.

    Fundamental Duality: Expression / Suppression
    - Expression: Active genes, transcription, protein production
    - Suppression: Silenced genes, repression, epigenetic control

    Secondary Dualities:
    - Dominant / Recessive
    - Genotype / Phenotype
    - Hereditary / Acquired
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Genetics",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of heredity, genes, and genetic variation",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Expression/Suppression duality."""
        self._domain.set_duality(
            positive_name="expression",
            positive_value=50,
            negative_name="suppression",
            negative_value=50,
            duality_name="genetics_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental genetic principles."""
        principles = [
            (
                "Mendel's First Law",
                "Alleles segregate during gamete formation",
            ),
            (
                "Mendel's Second Law",
                "Genes for different traits assort independently",
            ),
            (
                "Central Dogma",
                "Information flows from DNA to RNA to protein",
            ),
            (
                "Watson-Crick Base Pairing",
                "A pairs with T, G pairs with C in DNA",
            ),
            (
                "Semi-Conservative Replication",
                "Each DNA strand serves as template for new strand",
            ),
            (
                "One Gene-One Polypeptide",
                "Each gene encodes one polypeptide chain",
            ),
            (
                "Genetic Code Universality",
                "Same codons specify same amino acids in all organisms",
            ),
            (
                "Mutation is Random",
                "Mutations occur randomly, not in response to need",
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=95,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental genetics concepts."""
        return [
            "Gene",
            "DNA",
            "RNA",
            "Chromosome",
            "Allele",
            "Genotype",
            "Phenotype",
            "Mutation",
            "Heredity",
            "Transcription",
            "Translation",
            "Replication",
            "Recombination",
            "Genome",
            "Epigenetics",
        ]

    def initialize_branches(self) -> None:
        """Initialize major genetics branches."""
        branches = [
            (
                "Classical Genetics",
                "Mendelian inheritance patterns",
                ConceptType.THEORY,
            ),
            (
                "Molecular Genetics",
                "Molecular basis of heredity",
                ConceptType.THEORY,
            ),
            (
                "Population Genetics",
                "Genetic variation in populations",
                ConceptType.THEORY,
            ),
            (
                "Quantitative Genetics",
                "Inheritance of complex traits",
                ConceptType.THEORY,
            ),
            (
                "Genomics",
                "Study of entire genomes",
                ConceptType.THEORY,
            ),
            (
                "Epigenetics",
                "Heritable changes without DNA sequence changes",
                ConceptType.THEORY,
            ),
            (
                "Genetic Engineering",
                "Manipulation of genetic material",
                ConceptType.THEORY,
            ),
            (
                "Human Genetics",
                "Genetics of human traits and diseases",
                ConceptType.THEORY,
            ),
            (
                "Cytogenetics",
                "Study of chromosomes",
                ConceptType.THEORY,
            ),
            (
                "Developmental Genetics",
                "Genetic control of development",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_nucleic_acid_components(self) -> None:
        """Initialize nucleic acid components."""
        components = [
            ("Adenine", "A", "Purine base", ["T in DNA", "U in RNA"]),
            ("Guanine", "G", "Purine base", ["C"]),
            ("Cytosine", "C", "Pyrimidine base", ["G"]),
            ("Thymine", "T", "Pyrimidine base (DNA only)", ["A"]),
            ("Uracil", "U", "Pyrimidine base (RNA only)", ["A"]),
            ("Deoxyribose", "dR", "Sugar in DNA", []),
            ("Ribose", "R", "Sugar in RNA", []),
            ("Phosphate", "P", "Backbone component", []),
        ]

        for name, symbol, description, pairs_with in components:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "symbol": symbol,
                "pairs_with": pairs_with,
            })

    def initialize_genetic_processes(self) -> None:
        """Initialize genetic processes."""
        processes = [
            ("Replication", "DNA copying before cell division", "DNA polymerase"),
            ("Transcription", "DNA to mRNA conversion", "RNA polymerase"),
            ("Translation", "mRNA to protein conversion", "Ribosome"),
            ("Splicing", "Intron removal from pre-mRNA", "Spliceosome"),
            ("Recombination", "Exchange of genetic material", "Recombinase"),
            ("Repair", "Correction of DNA damage", "DNA repair enzymes"),
            ("Methylation", "Addition of methyl groups", "Methyltransferase"),
            ("Acetylation", "Addition of acetyl groups", "Acetyltransferase"),
        ]

        for name, description, key_enzyme in processes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["key_enzyme"] = key_enzyme

    def initialize_mutation_types(self) -> None:
        """Initialize mutation classifications."""
        mutations = [
            ("Point Mutation", "Single nucleotide change", ["Silent", "Missense", "Nonsense"]),
            ("Insertion", "Addition of nucleotides", ["Frameshift if not multiple of 3"]),
            ("Deletion", "Removal of nucleotides", ["Frameshift if not multiple of 3"]),
            ("Duplication", "Copying of DNA segment", ["Gene amplification"]),
            ("Inversion", "Reversal of DNA segment", ["Chromosome rearrangement"]),
            ("Translocation", "Movement of DNA to different chromosome", ["Chromosome abnormality"]),
        ]

        for name, description, effects in mutations:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["effects"] = effects

    def initialize_inheritance_patterns(self) -> None:
        """Initialize inheritance pattern types."""
        patterns = [
            ("Autosomal Dominant", "One copy of mutant allele causes trait", "Huntington's disease"),
            ("Autosomal Recessive", "Two copies needed for trait", "Cystic fibrosis"),
            ("X-linked Dominant", "Dominant on X chromosome", "Rett syndrome"),
            ("X-linked Recessive", "Recessive on X chromosome", "Hemophilia"),
            ("Y-linked", "On Y chromosome, father to son", "Male infertility genes"),
            ("Mitochondrial", "Inherited from mother only", "LHON"),
            ("Polygenic", "Multiple genes contribute", "Height, skin color"),
            ("Codominant", "Both alleles expressed equally", "Blood type AB"),
        ]

        for name, description, example in patterns:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["example"] = example

    def initialize_genetic_pairs(self) -> None:
        """Initialize fundamental genetic pairs with META 50/50 balance."""
        pairs = [
            ("Expression", "Suppression", "Active vs silenced"),
            ("Dominant", "Recessive", "Expressed vs hidden"),
            ("Genotype", "Phenotype", "Code vs appearance"),
            ("Mutation", "Wild Type", "Changed vs original"),
            ("Hereditary", "Acquired", "Inherited vs gained"),
            ("Coding", "Noncoding", "Protein making vs not"),
            ("Transcription", "Translation", "DNA to RNA vs RNA to protein"),
            ("Replication", "Repair", "Copying vs fixing"),
            ("Homozygous", "Heterozygous", "Same vs different alleles"),
            ("Activation", "Repression", "Turning on vs off"),
            ("Intron", "Exon", "Removed vs kept sequence"),
            ("Promoter", "Terminator", "Start vs stop signal"),
            ("Sense", "Antisense", "Coding vs complementary"),
            ("Maternal", "Paternal", "Mother vs father origin"),
            ("Epigenetic", "Genetic", "Above vs in the code"),
            ("Somatic", "Germline", "Body vs reproductive"),
            ("Monogenic", "Polygenic", "One vs many genes"),
            ("Natural", "Engineered", "Evolved vs designed"),
            ("Trait", "Allele", "Feature vs variant"),
            ("Linkage", "Independence", "Together vs separate inheritance"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Genetics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Genetics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_genetic_code(self) -> dict[str, str]:
        """Get the standard genetic code (codons to amino acids)."""
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

    def demonstrate_genetic_balance(self) -> dict[str, Any]:
        """Demonstrate genetic balance principles."""
        return {
            "concept": "Genetic Equilibrium",
            "dualities": {
                "expression_suppression": {
                    "active_genes": 50.0,
                    "silenced_genes": 50.0,
                    "meaning": "Only fraction of genome expressed in any cell",
                },
                "base_pairing": {
                    "purines": 50.0,
                    "pyrimidines": 50.0,
                    "meaning": "Chargaff's rule: A=T, G=C",
                },
                "allelic_balance": {
                    "maternal_allele": 50.0,
                    "paternal_allele": 50.0,
                    "meaning": "Equal contribution from parents",
                },
            },
            "hardy_weinberg": {
                "allele_frequency_stable": True,
                "conditions": ["Large population", "Random mating", "No selection"],
                "description": "Genetic equilibrium in ideal population",
            },
            "meta_meaning": "Genetics demonstrates META 50/50 in hereditary balance",
        }


def create_genetics_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> GeneticsDomain:
    """
    Factory function to create a fully initialized genetics domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized GeneticsDomain
    """
    domain = GeneticsDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_nucleic_acid_components()
        domain.initialize_genetic_processes()
        domain.initialize_mutation_types()
        domain.initialize_inheritance_patterns()
        domain.initialize_genetic_pairs()

    return domain
