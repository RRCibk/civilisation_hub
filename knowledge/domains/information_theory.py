"""
Information Theory Domain
=========================
Information theory knowledge domain with META 50/50 equilibrium.
Fundamental duality: Order/Entropy (structure vs disorder).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class InformationTheoryDomain(KnowledgeDomain):
    """
    Information Theory knowledge domain.

    Fundamental Duality: Order / Entropy
    - Order: Structure, pattern, low entropy, information
    - Entropy: Disorder, randomness, high entropy, uncertainty

    Secondary Dualities:
    - Signal / Noise
    - Compression / Expansion
    - Encoding / Decoding
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="InformationTheory",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of quantification, storage, and communication of information",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Order/Entropy duality."""
        self._domain.set_duality(
            positive_name="order",
            positive_value=50,
            negative_name="entropy",
            negative_value=50,
            duality_name="information_theory_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental information theory principles."""
        principles = [
            (
                "Shannon's Source Coding Theorem",
                "Optimal compression approaches entropy rate",
            ),
            (
                "Shannon's Channel Coding Theorem",
                "Reliable communication possible below channel capacity",
            ),
            (
                "Data Processing Inequality",
                "Processing cannot increase information",
            ),
            (
                "Entropy is Non-Negative",
                "H(X) ≥ 0 for any random variable X",
            ),
            (
                "Conditional Entropy Reduction",
                "H(X|Y) ≤ H(X), knowledge reduces uncertainty",
            ),
            (
                "Chain Rule for Entropy",
                "H(X,Y) = H(X) + H(Y|X)",
            ),
            (
                "Mutual Information Symmetry",
                "I(X;Y) = I(Y;X)",
            ),
            (
                "Capacity-Cost Function",
                "Trade-off between rate and distortion",
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=100,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental information theory concepts."""
        return [
            "Information",
            "Entropy",
            "Bit",
            "Channel",
            "Capacity",
            "Encoding",
            "Decoding",
            "Compression",
            "Redundancy",
            "Noise",
            "Signal",
            "Bandwidth",
            "Mutual Information",
            "Error Correction",
            "Cryptography",
        ]

    def initialize_branches(self) -> None:
        """Initialize major information theory branches."""
        branches = [
            (
                "Classical Information Theory",
                "Shannon's original theory",
                ConceptType.THEORY,
            ),
            (
                "Quantum Information Theory",
                "Information in quantum systems",
                ConceptType.THEORY,
            ),
            (
                "Algorithmic Information Theory",
                "Kolmogorov complexity approach",
                ConceptType.THEORY,
            ),
            (
                "Network Information Theory",
                "Multi-user communication",
                ConceptType.THEORY,
            ),
            (
                "Rate-Distortion Theory",
                "Lossy compression limits",
                ConceptType.THEORY,
            ),
            (
                "Channel Coding",
                "Error correction and detection",
                ConceptType.THEORY,
            ),
            (
                "Source Coding",
                "Data compression methods",
                ConceptType.THEORY,
            ),
            (
                "Cryptographic Information Theory",
                "Information-theoretic security",
                ConceptType.THEORY,
            ),
            (
                "Statistical Inference",
                "Information in statistical models",
                ConceptType.THEORY,
            ),
            (
                "Information Geometry",
                "Geometric approach to information",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_entropy_measures(self) -> None:
        """Initialize entropy measures."""
        measures = [
            ("Shannon Entropy", "H(X) = -Σ p(x) log p(x)", "Uncertainty of random variable"),
            ("Joint Entropy", "H(X,Y)", "Uncertainty of pair"),
            ("Conditional Entropy", "H(X|Y)", "Remaining uncertainty given Y"),
            ("Mutual Information", "I(X;Y) = H(X) - H(X|Y)", "Shared information"),
            ("Relative Entropy", "D(P||Q) = Σ P log(P/Q)", "KL divergence"),
            ("Cross Entropy", "H(P,Q) = -Σ P log Q", "Encoding with wrong distribution"),
            ("Rényi Entropy", "Generalized entropy family", "Parameter α controls sensitivity"),
        ]

        for name, formula, description in measures:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["formula"] = formula

    def initialize_coding_methods(self) -> None:
        """Initialize coding methods."""
        methods = [
            ("Huffman Coding", "Optimal prefix-free code", "Lossless"),
            ("Arithmetic Coding", "Near-optimal entropy coding", "Lossless"),
            ("LZW Compression", "Dictionary-based compression", "Lossless"),
            ("Run-Length Encoding", "Consecutive symbol compression", "Lossless"),
            ("Hamming Code", "Single error correction", "Error correction"),
            ("Reed-Solomon Code", "Burst error correction", "Error correction"),
            ("Turbo Code", "Near-capacity codes", "Error correction"),
            ("LDPC Code", "Low-density parity check", "Error correction"),
        ]

        for name, description, category in methods:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_channel_types(self) -> None:
        """Initialize communication channel types."""
        channels = [
            ("Binary Symmetric Channel", "Bit flip with probability p", "1 - H(p)"),
            ("Binary Erasure Channel", "Bit erasure with probability p", "1 - p"),
            ("Gaussian Channel", "Additive white Gaussian noise", "½log(1 + SNR)"),
            ("Z Channel", "Asymmetric binary channel", "Calculated"),
            ("Discrete Memoryless Channel", "Independent symbol transmission", "max I(X;Y)"),
        ]

        for name, description, capacity in channels:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["capacity_formula"] = capacity

    def initialize_units(self) -> None:
        """Initialize information units."""
        units = [
            ("Bit", "Binary digit", "log₂", "Base-2"),
            ("Nat", "Natural unit", "ln", "Base-e"),
            ("Hartley", "Decimal digit", "log₁₀", "Base-10"),
            ("Byte", "8 bits", "Group", "Standard"),
            ("Shannon", "Unit of information", "Entropy", "Theoretical"),
        ]

        for name, description, formula_base, category in units:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "formula_base": formula_base,
                "category": category,
            })

    def initialize_information_pairs(self) -> None:
        """Initialize fundamental information theory pairs with META 50/50 balance."""
        pairs = [
            ("Order", "Entropy", "Structure vs disorder"),
            ("Signal", "Noise", "Message vs interference"),
            ("Compression", "Expansion", "Reducing vs increasing"),
            ("Encoding", "Decoding", "Creating vs reading"),
            ("Redundancy", "Efficiency", "Extra vs minimal"),
            ("Lossless", "Lossy", "Perfect vs approximate"),
            ("Bandwidth", "Latency", "Capacity vs delay"),
            ("Bit", "Byte", "Binary vs grouped"),
            ("Source", "Destination", "Sender vs receiver"),
            ("Channel", "Medium", "Path vs carrier"),
            ("Encryption", "Decryption", "Hiding vs revealing"),
            ("Syntax", "Semantics", "Form vs meaning"),
            ("Digital", "Analog", "Discrete vs continuous"),
            ("Synchronous", "Asynchronous", "Timed vs untimed"),
            ("Serial", "Parallel", "Sequential vs simultaneous"),
            ("Transmission", "Reception", "Sending vs receiving"),
            ("Error", "Correction", "Mistake vs fix"),
            ("Mutual Information", "Independence", "Shared vs separate"),
            ("Capacity", "Rate", "Maximum vs actual"),
            ("Certainty", "Uncertainty", "Known vs unknown"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Information Theory)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Information Theory)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_shannon_formula(self) -> dict[str, str]:
        """Get Shannon's key formulas."""
        return {
            "entropy": "H(X) = -Σ p(x) log₂ p(x)",
            "channel_capacity": "C = max I(X;Y)",
            "mutual_information": "I(X;Y) = H(X) + H(Y) - H(X,Y)",
            "data_processing": "I(X;Z) ≤ I(X;Y) if X→Y→Z",
        }

    def demonstrate_information_balance(self) -> dict[str, Any]:
        """Demonstrate information theory balance principles."""
        return {
            "concept": "Information Equilibrium",
            "dualities": {
                "order_entropy": {
                    "order": 50.0,
                    "entropy": 50.0,
                    "meaning": "Information exists at boundary of order and chaos",
                },
                "signal_noise": {
                    "signal": 50.0,
                    "noise": 50.0,
                    "meaning": "Communication separates signal from noise",
                },
                "compression_redundancy": {
                    "compression": 50.0,
                    "redundancy": 50.0,
                    "meaning": "Trade-off between efficiency and reliability",
                },
            },
            "channel_balance": {
                "transmission_rate": 50.0,
                "error_rate": 50.0,
                "description": "Rate-reliability trade-off",
            },
            "meta_meaning": "Information Theory demonstrates META 50/50 in entropy balance",
        }


def create_information_theory_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> InformationTheoryDomain:
    """
    Factory function to create a fully initialized information theory domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized InformationTheoryDomain
    """
    domain = InformationTheoryDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_entropy_measures()
        domain.initialize_coding_methods()
        domain.initialize_channel_types()
        domain.initialize_units()
        domain.initialize_information_pairs()

    return domain
