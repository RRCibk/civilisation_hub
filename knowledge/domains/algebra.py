"""
Algebra Domain
==============
Algebraic knowledge domain with META 50/50 equilibrium.
Fundamental duality: Known/Unknown (given vs sought values).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class AlgebraDomain(KnowledgeDomain):
    """
    Algebra knowledge domain.

    Fundamental Duality: Known / Unknown
    - Known: Given values, constants, determined quantities
    - Unknown: Sought values, variables, undetermined quantities

    Secondary Dualities:
    - Constant / Variable
    - Linear / Nonlinear
    - Real / Complex
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Algebra",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of mathematical symbols and rules for manipulating them",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Known/Unknown duality."""
        self._domain.set_duality(
            positive_name="known",
            positive_value=50,
            negative_name="unknown",
            negative_value=50,
            duality_name="algebra_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental algebraic axioms."""
        axioms = [
            (
                "Closure",
                "Operations on elements produce elements of the same set",
            ),
            (
                "Associativity",
                "(a + b) + c = a + (b + c) for addition and multiplication",
            ),
            (
                "Commutativity",
                "a + b = b + a for addition and multiplication",
            ),
            (
                "Identity Element",
                "0 for addition, 1 for multiplication",
            ),
            (
                "Inverse Element",
                "-a for addition, 1/a for multiplication",
            ),
            (
                "Distributivity",
                "a(b + c) = ab + ac",
            ),
            (
                "Trichotomy",
                "For any two reals: a < b, a = b, or a > b",
            ),
            (
                "Well-Ordering",
                "Every non-empty set of positive integers has a least element",
            ),
        ]

        for name, description in axioms:
            self.create_concept(
                name=name,
                concept_type=ConceptType.AXIOM,
                description=description,
                certainty=100,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental algebra concepts."""
        return [
            "Variable",
            "Constant",
            "Expression",
            "Equation",
            "Inequality",
            "Function",
            "Polynomial",
            "Root",
            "Factor",
            "Coefficient",
            "Exponent",
            "Matrix",
            "Vector",
            "Group",
            "Ring",
        ]

    def initialize_branches(self) -> None:
        """Initialize major algebra branches."""
        branches = [
            (
                "Elementary Algebra",
                "Basic operations and equations",
                ConceptType.THEORY,
            ),
            (
                "Linear Algebra",
                "Study of vectors, matrices, and linear transformations",
                ConceptType.THEORY,
            ),
            (
                "Abstract Algebra",
                "Study of algebraic structures like groups and rings",
                ConceptType.THEORY,
            ),
            (
                "Boolean Algebra",
                "Algebra of true/false values",
                ConceptType.THEORY,
            ),
            (
                "Polynomial Algebra",
                "Study of polynomials and their properties",
                ConceptType.THEORY,
            ),
            (
                "Matrix Algebra",
                "Operations on matrices",
                ConceptType.THEORY,
            ),
            (
                "Commutative Algebra",
                "Study of commutative rings",
                ConceptType.THEORY,
            ),
            (
                "Homological Algebra",
                "Algebraic structures using category theory",
                ConceptType.THEORY,
            ),
            (
                "Computer Algebra",
                "Algorithmic manipulation of expressions",
                ConceptType.THEORY,
            ),
            (
                "Lie Algebra",
                "Study of Lie groups and their structure",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_number_systems(self) -> None:
        """Initialize number systems."""
        systems = [
            ("Natural Numbers", "ℕ", "1, 2, 3, ...", "Counting numbers"),
            ("Integers", "ℤ", "..., -2, -1, 0, 1, 2, ...", "Whole numbers"),
            ("Rational Numbers", "ℚ", "p/q where q ≠ 0", "Fractions"),
            ("Real Numbers", "ℝ", "All points on number line", "Including irrationals"),
            ("Complex Numbers", "ℂ", "a + bi", "Including imaginary"),
            ("Quaternions", "ℍ", "a + bi + cj + dk", "4D extension"),
        ]

        for name, symbol, form, description in systems:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "symbol": symbol,
                "form": form,
            })

    def initialize_operations(self) -> None:
        """Initialize algebraic operations."""
        operations = [
            ("Addition", "+", "Combining quantities", "Commutative"),
            ("Subtraction", "-", "Finding difference", "Non-commutative"),
            ("Multiplication", "×", "Repeated addition", "Commutative"),
            ("Division", "÷", "Inverse of multiplication", "Non-commutative"),
            ("Exponentiation", "^", "Repeated multiplication", "Non-commutative"),
            ("Root", "√", "Inverse of exponentiation", "Non-commutative"),
            ("Logarithm", "log", "Inverse of exponentiation", "Non-commutative"),
            ("Modulo", "mod", "Remainder after division", "Non-commutative"),
        ]

        for name, symbol, description, property_type in operations:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "symbol": symbol,
                "commutativity": property_type,
            })

    def initialize_equation_types(self) -> None:
        """Initialize equation types."""
        equations = [
            ("Linear Equation", "ax + b = 0", 1, "One solution"),
            ("Quadratic Equation", "ax² + bx + c = 0", 2, "Up to two solutions"),
            ("Cubic Equation", "ax³ + bx² + cx + d = 0", 3, "Up to three solutions"),
            ("Polynomial Equation", "aₙxⁿ + ... + a₁x + a₀ = 0", "n", "Up to n solutions"),
            ("Exponential Equation", "aˣ = b", "varies", "Logarithmic solution"),
            ("Logarithmic Equation", "log(x) = a", "varies", "Exponential solution"),
            ("Rational Equation", "P(x)/Q(x) = 0", "varies", "Exclude Q(x)=0"),
        ]

        for name, form, degree, solutions in equations:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=f"Equation of form: {form}",
            )
            concept.metadata.update({
                "general_form": form,
                "degree": degree,
                "solution_behavior": solutions,
            })

    def initialize_algebraic_structures(self) -> None:
        """Initialize abstract algebraic structures."""
        structures = [
            ("Group", "Set with associative operation, identity, inverses", ["Integers under addition"]),
            ("Ring", "Group with second operation (multiplication)", ["Integers"]),
            ("Field", "Ring with multiplicative inverses", ["Rational numbers"]),
            ("Vector Space", "Set with vector addition and scalar multiplication", ["ℝⁿ"]),
            ("Module", "Generalization of vector space over ring", ["Abelian groups"]),
            ("Algebra", "Vector space with bilinear multiplication", ["Matrix algebras"]),
        ]

        for name, description, examples in structures:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_algebraic_pairs(self) -> None:
        """Initialize fundamental algebraic pairs with META 50/50 balance."""
        pairs = [
            ("Known", "Unknown", "Given vs sought"),
            ("Constant", "Variable", "Fixed vs changing"),
            ("Coefficient", "Exponent", "Multiplier vs power"),
            ("Equation", "Inequality", "Equal vs unequal"),
            ("Linear", "Nonlinear", "Straight vs curved"),
            ("Polynomial", "Rational", "Whole vs fractional"),
            ("Real", "Complex", "Line vs plane numbers"),
            ("Positive", "Negative", "Above vs below zero"),
            ("Integer", "Fraction", "Whole vs partial"),
            ("Finite", "Infinite", "Bounded vs unbounded"),
            ("Discrete", "Continuous", "Separate vs connected"),
            ("Domain", "Range", "Input vs output"),
            ("Function", "Relation", "Unique vs multiple outputs"),
            ("Inverse", "Direct", "Opposite vs same"),
            ("Factor", "Multiple", "Divides vs divisible"),
            ("Sum", "Product", "Addition vs multiplication"),
            ("Root", "Power", "Inverse vs direct operation"),
            ("Simple", "Compound", "One vs many operations"),
            ("Closed", "Open", "Complete vs incomplete"),
            ("Commutative", "Noncommutative", "Order free vs order matters"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Algebra)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Algebra)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_quadratic_formula(self) -> dict[str, str]:
        """Get the quadratic formula."""
        return {
            "formula": "x = (-b ± √(b²-4ac)) / 2a",
            "discriminant": "b² - 4ac",
            "two_real_roots": "discriminant > 0",
            "one_real_root": "discriminant = 0",
            "complex_roots": "discriminant < 0",
        }

    def demonstrate_algebraic_balance(self) -> dict[str, Any]:
        """Demonstrate algebraic balance principles."""
        return {
            "concept": "Algebraic Equilibrium",
            "dualities": {
                "equation_balance": {
                    "left_side": 50.0,
                    "right_side": 50.0,
                    "meaning": "Equations maintain equality across =",
                },
                "inverse_operations": {
                    "operation": 50.0,
                    "inverse": 50.0,
                    "meaning": "Every operation has an inverse",
                },
                "positive_negative": {
                    "positive": 50.0,
                    "negative": 50.0,
                    "meaning": "Number line extends equally both ways",
                },
            },
            "identity_balance": {
                "element": 50.0,
                "inverse": 50.0,
                "description": "a + (-a) = 0, a × (1/a) = 1",
            },
            "meta_meaning": "Algebra demonstrates META 50/50 in equation balance",
        }


def create_algebra_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> AlgebraDomain:
    """
    Factory function to create a fully initialized algebra domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized AlgebraDomain
    """
    domain = AlgebraDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_number_systems()
        domain.initialize_operations()
        domain.initialize_equation_types()
        domain.initialize_algebraic_structures()
        domain.initialize_algebraic_pairs()

    return domain
