"""
Calculus Domain
===============
Calculus knowledge domain with META 50/50 equilibrium.
Fundamental duality: Derivative/Integral (rate vs accumulation).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class CalculusDomain(KnowledgeDomain):
    """
    Calculus knowledge domain.

    Fundamental Duality: Derivative / Integral
    - Derivative: Rate of change, slope, differentiation
    - Integral: Accumulation, area, antidifferentiation

    Secondary Dualities:
    - Limit / Infinity
    - Continuous / Discontinuous
    - Maximum / Minimum
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Calculus",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of continuous change through derivatives and integrals",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Derivative/Integral duality."""
        self._domain.set_duality(
            positive_name="derivative",
            positive_value=50,
            negative_name="integral",
            negative_value=50,
            duality_name="calculus_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental calculus theorems as axioms."""
        theorems = [
            (
                "Fundamental Theorem of Calculus",
                "Differentiation and integration are inverse operations",
            ),
            (
                "Mean Value Theorem",
                "Continuous function attains its average rate at some point",
            ),
            (
                "Intermediate Value Theorem",
                "Continuous function takes all values between endpoints",
            ),
            (
                "Extreme Value Theorem",
                "Continuous function on closed interval has max and min",
            ),
            (
                "Chain Rule",
                "Derivative of composition is product of derivatives",
            ),
            (
                "L'Hôpital's Rule",
                "Indeterminate forms can be evaluated using derivatives",
            ),
            (
                "Taylor's Theorem",
                "Functions can be approximated by polynomial series",
            ),
            (
                "Squeeze Theorem",
                "Function bounded by converging functions also converges",
            ),
        ]

        for name, description in theorems:
            self.create_concept(
                name=name,
                concept_type=ConceptType.THEOREM,
                description=description,
                certainty=100,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental calculus concepts."""
        return [
            "Limit",
            "Derivative",
            "Integral",
            "Continuity",
            "Convergence",
            "Series",
            "Function",
            "Slope",
            "Area",
            "Rate",
            "Differential",
            "Antiderivative",
            "Maximum",
            "Minimum",
            "Infinity",
        ]

    def initialize_branches(self) -> None:
        """Initialize major calculus branches."""
        branches = [
            (
                "Differential Calculus",
                "Study of rates of change and slopes",
                ConceptType.THEORY,
            ),
            (
                "Integral Calculus",
                "Study of accumulation and areas",
                ConceptType.THEORY,
            ),
            (
                "Multivariable Calculus",
                "Calculus of functions of multiple variables",
                ConceptType.THEORY,
            ),
            (
                "Vector Calculus",
                "Calculus of vector fields",
                ConceptType.THEORY,
            ),
            (
                "Differential Equations",
                "Equations involving derivatives",
                ConceptType.THEORY,
            ),
            (
                "Real Analysis",
                "Rigorous foundation of calculus",
                ConceptType.THEORY,
            ),
            (
                "Complex Analysis",
                "Calculus of complex-valued functions",
                ConceptType.THEORY,
            ),
            (
                "Numerical Analysis",
                "Computational methods for calculus",
                ConceptType.THEORY,
            ),
            (
                "Calculus of Variations",
                "Optimization of functionals",
                ConceptType.THEORY,
            ),
            (
                "Stochastic Calculus",
                "Calculus for random processes",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_derivative_rules(self) -> None:
        """Initialize differentiation rules."""
        rules = [
            ("Power Rule", "d/dx[xⁿ] = nxⁿ⁻¹", "Polynomial differentiation"),
            ("Product Rule", "d/dx[fg] = f'g + fg'", "Product of functions"),
            ("Quotient Rule", "d/dx[f/g] = (f'g - fg')/g²", "Quotient of functions"),
            ("Chain Rule", "d/dx[f(g(x))] = f'(g(x))g'(x)", "Composition"),
            ("Sum Rule", "d/dx[f + g] = f' + g'", "Sum of functions"),
            ("Constant Rule", "d/dx[c] = 0", "Constant function"),
            ("Exponential Rule", "d/dx[eˣ] = eˣ", "Natural exponential"),
            ("Logarithm Rule", "d/dx[ln(x)] = 1/x", "Natural logarithm"),
        ]

        for name, formula, description in rules:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["formula"] = formula

    def initialize_integral_types(self) -> None:
        """Initialize integration types."""
        integrals = [
            ("Indefinite Integral", "∫f(x)dx = F(x) + C", "Antiderivative"),
            ("Definite Integral", "∫[a,b]f(x)dx = F(b) - F(a)", "Signed area"),
            ("Improper Integral", "Integral with infinite limits", "Limit of definite"),
            ("Line Integral", "∫C f ds", "Integral along curve"),
            ("Surface Integral", "∫∫S f dS", "Integral over surface"),
            ("Volume Integral", "∫∫∫V f dV", "Integral over volume"),
            ("Contour Integral", "∮ f(z) dz", "Complex line integral"),
        ]

        for name, notation, description in integrals:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["notation"] = notation

    def initialize_limits(self) -> None:
        """Initialize limit concepts."""
        limits = [
            ("Limit at a Point", "lim(x→a) f(x) = L", "Approach value at point"),
            ("One-Sided Limit", "lim(x→a⁺) or lim(x→a⁻)", "Approach from one side"),
            ("Limit at Infinity", "lim(x→∞) f(x)", "Behavior as x grows"),
            ("Infinite Limit", "lim(x→a) f(x) = ∞", "Unbounded growth"),
            ("Epsilon-Delta", "|f(x) - L| < ε when |x - a| < δ", "Rigorous definition"),
        ]

        for name, notation, description in limits:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["notation"] = notation

    def initialize_series(self) -> None:
        """Initialize series types."""
        series = [
            ("Geometric Series", "Σarⁿ", "|r| < 1 for convergence"),
            ("Harmonic Series", "Σ1/n", "Diverges"),
            ("Power Series", "Σaₙxⁿ", "Within radius of convergence"),
            ("Taylor Series", "Σf⁽ⁿ⁾(a)(x-a)ⁿ/n!", "Polynomial approximation"),
            ("Maclaurin Series", "Taylor series at a=0", "Around origin"),
            ("Fourier Series", "Σ(aₙcos(nx) + bₙsin(nx))", "Periodic functions"),
        ]

        for name, form, property_desc in series:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=property_desc,
            )
            concept.metadata["general_form"] = form

    def initialize_calculus_pairs(self) -> None:
        """Initialize fundamental calculus pairs with META 50/50 balance."""
        pairs = [
            ("Derivative", "Integral", "Rate vs accumulation"),
            ("Differential", "Summation", "Infinitesimal vs total"),
            ("Limit", "Infinity", "Approaching vs unbounded"),
            ("Continuous", "Discontinuous", "Smooth vs broken"),
            ("Convergent", "Divergent", "Approaching vs escaping"),
            ("Maximum", "Minimum", "Peak vs valley"),
            ("Increasing", "Decreasing", "Rising vs falling"),
            ("Concave Up", "Concave Down", "Curving up vs down"),
            ("Partial", "Total", "One vs all variables"),
            ("Definite", "Indefinite", "Bounded vs unbounded integral"),
            ("Instantaneous", "Average", "Moment vs interval"),
            ("Local", "Global", "Nearby vs everywhere"),
            ("Ordinary", "Partial", "One vs many variables"),
            ("First Order", "Higher Order", "Simple vs complex"),
            ("Linear", "Nonlinear", "Proportional vs not"),
            ("Analytic", "Numerical", "Exact vs approximate"),
            ("Bounded", "Unbounded", "Limited vs unlimited"),
            ("Smooth", "Rough", "Differentiable vs not"),
            ("Scalar", "Vector", "Magnitude vs direction"),
            ("Real", "Complex", "One vs two dimensional"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Calculus)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Calculus)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_common_derivatives(self) -> dict[str, str]:
        """Get common derivative formulas."""
        return {
            "x^n": "n*x^(n-1)",
            "e^x": "e^x",
            "ln(x)": "1/x",
            "sin(x)": "cos(x)",
            "cos(x)": "-sin(x)",
            "tan(x)": "sec²(x)",
            "a^x": "a^x * ln(a)",
        }

    def get_common_integrals(self) -> dict[str, str]:
        """Get common integral formulas."""
        return {
            "x^n": "x^(n+1)/(n+1) + C",
            "e^x": "e^x + C",
            "1/x": "ln|x| + C",
            "sin(x)": "-cos(x) + C",
            "cos(x)": "sin(x) + C",
            "sec²(x)": "tan(x) + C",
        }

    def demonstrate_calculus_balance(self) -> dict[str, Any]:
        """Demonstrate calculus balance principles."""
        return {
            "concept": "Calculus Equilibrium",
            "dualities": {
                "derivative_integral": {
                    "differentiation": 50.0,
                    "integration": 50.0,
                    "meaning": "Inverse operations, fundamental theorem",
                },
                "rate_accumulation": {
                    "instantaneous_rate": 50.0,
                    "total_accumulation": 50.0,
                    "meaning": "Two views of the same function",
                },
                "local_global": {
                    "local_behavior": 50.0,
                    "global_behavior": 50.0,
                    "meaning": "Point properties vs overall properties",
                },
            },
            "fundamental_theorem": {
                "d_dx_integral": "Returns original function",
                "integral_derivative": "Returns original function",
                "description": "Perfect inverse relationship",
            },
            "meta_meaning": "Calculus demonstrates META 50/50 in derivative-integral duality",
        }


def create_calculus_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> CalculusDomain:
    """
    Factory function to create a fully initialized calculus domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized CalculusDomain
    """
    domain = CalculusDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_derivative_rules()
        domain.initialize_integral_types()
        domain.initialize_limits()
        domain.initialize_series()
        domain.initialize_calculus_pairs()

    return domain
