"""
Econometrics Domain
===================
Econometrics knowledge domain with META 50/50 equilibrium.
Fundamental duality: Theory/Data (economic models vs empirical evidence).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class EconometricsDomain(KnowledgeDomain):
    """
    Econometrics knowledge domain.

    Fundamental Duality: Theory / Data
    - Theory: Economic models, hypotheses, assumptions
    - Data: Empirical evidence, measurements, observations

    Secondary Dualities:
    - Structural / Reduced Form
    - Cross-Section / Time Series
    - Parametric / Non-parametric
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Econometrics",
            domain_type=DomainType.FUNDAMENTAL,
            description="The statistical analysis of economic relationships",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Theory/Data duality."""
        self._domain.set_duality(
            positive_name="theory",
            positive_value=50,
            negative_name="data",
            negative_value=50,
            duality_name="econometrics_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental econometrics principles."""
        principles = [
            (
                "Identification",
                "Model parameters must be identifiable",
            ),
            (
                "Exogeneity",
                "Right-hand variables independent of error",
            ),
            (
                "Consistency",
                "Estimators converge to true values",
            ),
            (
                "Efficiency",
                "Minimum variance among estimators",
            ),
            (
                "Specification",
                "Model must be correctly specified",
            ),
            (
                "Robustness",
                "Results stable under assumptions",
            ),
            (
                "Causality",
                "Distinguish correlation from causation",
            ),
            (
                "Inference",
                "Proper statistical testing",
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
        """Get fundamental econometrics concepts."""
        return [
            "Regression",
            "Estimation",
            "Hypothesis",
            "Coefficient",
            "Error",
            "Variance",
            "Bias",
            "Endogeneity",
            "Instrument",
            "Panel",
            "Time Series",
            "Causality",
            "Identification",
            "Specification",
            "Inference",
        ]

    def initialize_branches(self) -> None:
        """Initialize major econometrics branches."""
        branches = [
            (
                "Cross-Sectional Analysis",
                "Multiple units, one time",
                ConceptType.THEORY,
            ),
            (
                "Time Series Analysis",
                "One unit, multiple times",
                ConceptType.THEORY,
            ),
            (
                "Panel Data Analysis",
                "Multiple units, multiple times",
                ConceptType.THEORY,
            ),
            (
                "Microeconometrics",
                "Individual and firm data",
                ConceptType.THEORY,
            ),
            (
                "Macroeconometrics",
                "Aggregate economic data",
                ConceptType.THEORY,
            ),
            (
                "Financial Econometrics",
                "Financial markets data",
                ConceptType.THEORY,
            ),
            (
                "Spatial Econometrics",
                "Geographic dependence",
                ConceptType.THEORY,
            ),
            (
                "Bayesian Econometrics",
                "Bayesian inference",
                ConceptType.THEORY,
            ),
            (
                "Nonparametric Econometrics",
                "Flexible functional forms",
                ConceptType.THEORY,
            ),
            (
                "Causal Inference",
                "Treatment effects",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_methods(self) -> None:
        """Initialize econometric methods."""
        methods = [
            ("OLS", "Ordinary least squares", "Linear"),
            ("IV", "Instrumental variables", "Endogeneity"),
            ("GMM", "Generalized method of moments", "General"),
            ("MLE", "Maximum likelihood", "Parametric"),
            ("Difference-in-Differences", "Treatment effects", "Causal"),
            ("Regression Discontinuity", "Threshold effects", "Causal"),
        ]

        for name, description, category in methods:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_problems(self) -> None:
        """Initialize econometric problems."""
        problems = [
            ("Endogeneity", "Correlation with error", "Bias"),
            ("Heteroskedasticity", "Non-constant variance", "Efficiency"),
            ("Autocorrelation", "Correlated errors", "Efficiency"),
            ("Multicollinearity", "Correlated regressors", "Precision"),
            ("Omitted Variable", "Missing regressor", "Bias"),
            ("Measurement Error", "Noisy variables", "Attenuation"),
        ]

        for name, description, consequence in problems:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["consequence"] = consequence

    def initialize_econometrics_pairs(self) -> None:
        """Initialize fundamental econometrics pairs with META 50/50 balance."""
        pairs = [
            ("Theory", "Data", "Model vs evidence"),
            ("Structural", "Reduced Form", "Causal vs predictive"),
            ("Cross-Section", "Time Series", "Across vs over time"),
            ("Parametric", "Non-parametric", "Assumed vs flexible"),
            ("Bias", "Variance", "Systematic vs random error"),
            ("Consistency", "Efficiency", "Converging vs precise"),
            ("Endogenous", "Exogenous", "Internal vs external"),
            ("Identified", "Unidentified", "Estimable vs not"),
            ("Linear", "Nonlinear", "Straight vs curved"),
            ("Static", "Dynamic", "Point vs temporal"),
            ("Frequentist", "Bayesian", "Classical vs probabilistic"),
            ("Experimental", "Observational", "Controlled vs natural"),
            ("Population", "Sample", "All vs subset"),
            ("Point", "Interval", "Single vs range estimate"),
            ("Null", "Alternative", "No effect vs effect"),
            ("Type I", "Type II", "False positive vs false negative"),
            ("Micro", "Macro", "Individual vs aggregate"),
            ("Short-Run", "Long-Run", "Immediate vs eventual"),
            ("Weak", "Strong", "Weak vs strong instruments"),
            ("Homogeneous", "Heterogeneous", "Same vs different effects"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Econometric)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Econometric)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_gauss_markov_assumptions(self) -> dict[str, str]:
        """Get Gauss-Markov assumptions."""
        return {
            "linearity": "Linear in parameters",
            "random_sample": "Random sampling",
            "no_perfect_collinearity": "No exact linear relationships",
            "zero_conditional_mean": "E(u|X) = 0",
            "homoskedasticity": "Var(u|X) = constant",
        }

    def demonstrate_econometrics_balance(self) -> dict[str, Any]:
        """Demonstrate econometrics balance principles."""
        return {
            "concept": "Econometrics Equilibrium",
            "dualities": {
                "theory_data": {
                    "theory": 50.0,
                    "data": 50.0,
                    "meaning": "Models and evidence equally important",
                },
                "bias_variance": {
                    "bias": 50.0,
                    "variance": 50.0,
                    "meaning": "Trade-off between accuracy and precision",
                },
                "structural_reduced": {
                    "structural": 50.0,
                    "reduced_form": 50.0,
                    "meaning": "Causal and predictive both valuable",
                },
            },
            "estimation_balance": {
                "consistency": 50.0,
                "efficiency": 50.0,
                "description": "Convergence and precision both matter",
            },
            "meta_meaning": "Econometrics demonstrates META 50/50 in theory-data synthesis",
        }


def create_econometrics_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> EconometricsDomain:
    """
    Factory function to create a fully initialized econometrics domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized EconometricsDomain
    """
    domain = EconometricsDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_methods()
        domain.initialize_problems()
        domain.initialize_econometrics_pairs()

    return domain
