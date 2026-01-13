"""
Mathematics Domain
==================
Mathematical knowledge domain with META 50/50 equilibrium.
Fundamental duality: Abstract/Concrete (pure/applied mathematics).
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


class MathematicsDomain(KnowledgeDomain):
    """
    Mathematics knowledge domain.

    Fundamental Duality: Abstract (pure) / Concrete (applied)
    - Abstract: Pure mathematical structures, proofs, theorems
    - Concrete: Applied mathematics, calculations, real-world models

    Both aspects maintain META 50/50 balance.
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Mathematics",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of numbers, quantities, structures, and patterns",
            meta_equilibrium=meta_equilibrium
        )

    def _initialize_duality(self) -> None:
        """Initialize Abstract/Concrete duality."""
        self._domain.set_duality(
            positive_name="abstract",
            positive_value=50,
            negative_name="concrete",
            negative_value=50,
            duality_name="mathematics_duality"
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental mathematical axioms."""
        axioms = [
            ("Identity", "For any value x, x = x (reflexivity)"),
            ("Non-Contradiction", "A statement cannot be both true and false"),
            ("Excluded Middle", "Every statement is either true or false"),
            ("Substitution", "Equal quantities can be substituted for each other"),
            ("Induction", "If P(0) and P(n)→P(n+1), then P(n) for all n"),
            ("Infinity", "There exists an infinite set"),
            ("Choice", "For any collection of non-empty sets, a choice function exists"),
            ("Extensionality", "Sets with the same elements are equal"),
        ]

        for name, description in axioms:
            self.create_concept(
                name=name,
                concept_type=ConceptType.AXIOM,
                description=description,
                certainty=100  # Axioms are certain by definition
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental mathematical concepts."""
        return [
            "Number", "Set", "Function", "Relation", "Operation",
            "Proof", "Theorem", "Definition", "Structure", "Space",
            "Infinity", "Limit", "Continuity", "Derivative", "Integral"
        ]

    def initialize_branches(self) -> None:
        """Initialize major mathematical branches as concepts."""
        branches = [
            ("Arithmetic", "Study of numbers and basic operations", ConceptType.THEORY),
            ("Algebra", "Study of mathematical symbols and rules", ConceptType.THEORY),
            ("Geometry", "Study of shapes, sizes, and spatial relationships", ConceptType.THEORY),
            ("Calculus", "Study of continuous change", ConceptType.THEORY),
            ("Analysis", "Study of limits and related theories", ConceptType.THEORY),
            ("Number Theory", "Study of integers and their properties", ConceptType.THEORY),
            ("Topology", "Study of properties preserved under deformation", ConceptType.THEORY),
            ("Probability", "Study of random phenomena", ConceptType.THEORY),
            ("Statistics", "Collection, analysis, and interpretation of data", ConceptType.THEORY),
            ("Logic", "Study of valid reasoning", ConceptType.THEORY),
            ("Set Theory", "Study of collections of objects", ConceptType.THEORY),
            ("Category Theory", "Study of abstract structures and relationships", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_number_systems(self) -> None:
        """Initialize number system concepts."""
        systems = [
            ("Natural Numbers", "Positive integers: 1, 2, 3, ...", "ℕ"),
            ("Integers", "Whole numbers: ..., -2, -1, 0, 1, 2, ...", "ℤ"),
            ("Rational Numbers", "Ratios of integers: p/q", "ℚ"),
            ("Real Numbers", "All points on the number line", "ℝ"),
            ("Complex Numbers", "Numbers with real and imaginary parts", "ℂ"),
            ("Quaternions", "Extension of complex numbers", "ℍ"),
            ("Octonions", "Eight-dimensional number system", "𝕆"),
        ]

        concepts = []
        for name, description, symbol in systems:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description
            )
            concept.metadata["symbol"] = symbol
            concepts.append(concept)

        # Create containment relations (ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ)
        for i in range(len(concepts) - 1):
            if i < 5:  # Standard containment chain
                self.create_relation(
                    concepts[i],
                    concepts[i + 1],
                    RelationType.SPECIALIZES,
                    strength=100
                )

    def add_theorem(
        self,
        name: str,
        statement: str,
        proof_sketch: str = "",
        certainty: float = 100.0
    ) -> Concept:
        """Add a mathematical theorem."""
        theorem = self.create_concept(
            name=name,
            concept_type=ConceptType.THEOREM,
            description=statement,
            certainty=certainty
        )
        theorem.metadata["proof_sketch"] = proof_sketch
        return theorem

    def add_definition(
        self,
        name: str,
        definition: str,
        notation: str = ""
    ) -> Concept:
        """Add a mathematical definition."""
        concept = self.create_concept(
            name=name,
            concept_type=ConceptType.DEFINITION,
            description=definition
        )
        if notation:
            concept.metadata["notation"] = notation
        return concept

    def initialize_fundamental_theorems(self) -> None:
        """Initialize fundamental mathematical theorems."""
        theorems = [
            (
                "Pythagorean Theorem",
                "In a right triangle, a² + b² = c²",
                "Proof by similar triangles or algebraic methods"
            ),
            (
                "Fundamental Theorem of Arithmetic",
                "Every integer > 1 is either prime or a unique product of primes",
                "Proof by strong induction"
            ),
            (
                "Fundamental Theorem of Calculus",
                "Differentiation and integration are inverse operations",
                "Links differential and integral calculus"
            ),
            (
                "Fundamental Theorem of Algebra",
                "Every non-constant polynomial has at least one complex root",
                "Multiple proofs: algebraic, analytic, topological"
            ),
            (
                "Gödel's Incompleteness Theorems",
                "Any consistent formal system has unprovable truths",
                "Self-referential construction"
            ),
            (
                "Cantor's Theorem",
                "The power set of any set has greater cardinality",
                "Diagonal argument"
            ),
        ]

        for name, statement, proof in theorems:
            self.add_theorem(name, statement, proof)

    def calculate_pi_approximation(self, iterations: int = 1000) -> float:
        """
        Calculate π using Leibniz formula (for demonstration).
        π/4 = 1 - 1/3 + 1/5 - 1/7 + ...
        """
        result = 0.0
        for i in range(iterations):
            result += ((-1) ** i) / (2 * i + 1)
        return result * 4

    def demonstrate_golden_ratio(self) -> dict[str, Any]:
        """
        Demonstrate the golden ratio φ = (1 + √5) / 2.
        Shows mathematical harmony and balance.
        """
        import math
        phi = (1 + math.sqrt(5)) / 2
        psi = (1 - math.sqrt(5)) / 2  # Conjugate

        return {
            "phi": phi,
            "psi": psi,
            "phi_squared": phi ** 2,
            "phi_plus_1": phi + 1,
            "phi_squared_equals_phi_plus_1": abs(phi ** 2 - (phi + 1)) < 1e-10,
            "phi_times_psi": phi * psi,  # Should be -1
            "phi_plus_psi": phi + psi,   # Should be 1
            "balance_demonstrated": True
        }

    def get_mathematical_constants(self) -> dict[str, float]:
        """Get fundamental mathematical constants."""
        import math
        return {
            "pi": math.pi,
            "e": math.e,
            "phi": (1 + math.sqrt(5)) / 2,
            "sqrt2": math.sqrt(2),
            "sqrt3": math.sqrt(3),
            "ln2": math.log(2),
            "euler_gamma": 0.5772156649015329,  # Euler-Mascheroni constant
        }


def create_mathematics_domain(
    meta_equilibrium: MetaEquilibrium | None = None,
    initialize_all: bool = True
) -> MathematicsDomain:
    """
    Factory function to create a fully initialized mathematics domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized MathematicsDomain
    """
    domain = MathematicsDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_number_systems()
        domain.initialize_fundamental_theorems()

    return domain
