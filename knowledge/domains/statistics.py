"""
Statistics Domain
=================
Statistical knowledge domain with META 50/50 equilibrium.
Fundamental duality: Signal/Noise (pattern vs randomness).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class StatisticsDomain(KnowledgeDomain):
    """
    Statistics knowledge domain.

    Fundamental Duality: Signal / Noise
    - Signal: True pattern, systematic variation, meaningful data
    - Noise: Random variation, error, meaningless fluctuation

    Secondary Dualities:
    - Mean / Variance
    - Population / Sample
    - Null / Alternative
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Statistics",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of data collection, analysis, interpretation, and presentation",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Signal/Noise duality."""
        self._domain.set_duality(
            positive_name="signal",
            positive_value=50,
            negative_name="noise",
            negative_value=50,
            duality_name="statistics_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental statistical principles."""
        principles = [
            (
                "Law of Large Numbers",
                "Sample average converges to expected value as sample size increases",
            ),
            (
                "Central Limit Theorem",
                "Sum of random variables approaches normal distribution",
            ),
            (
                "Bayes' Theorem",
                "Posterior probability from prior and likelihood",
            ),
            (
                "Maximum Likelihood Principle",
                "Best estimate maximizes likelihood of observed data",
            ),
            (
                "Regression to the Mean",
                "Extreme observations tend to be followed by less extreme ones",
            ),
            (
                "Independence Assumption",
                "Events are independent if one doesn't affect the other",
            ),
            (
                "Sufficiency Principle",
                "A statistic is sufficient if it captures all relevant information",
            ),
            (
                "Parsimony",
                "Simpler models are preferred when equally effective",
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
        """Get fundamental statistics concepts."""
        return [
            "Mean",
            "Median",
            "Mode",
            "Variance",
            "Standard Deviation",
            "Probability",
            "Distribution",
            "Sample",
            "Population",
            "Hypothesis",
            "Confidence",
            "Correlation",
            "Regression",
            "Significance",
            "Error",
        ]

    def initialize_branches(self) -> None:
        """Initialize major statistics branches."""
        branches = [
            (
                "Descriptive Statistics",
                "Summarizing and describing data",
                ConceptType.THEORY,
            ),
            (
                "Inferential Statistics",
                "Drawing conclusions from data",
                ConceptType.THEORY,
            ),
            (
                "Bayesian Statistics",
                "Probability as degree of belief",
                ConceptType.THEORY,
            ),
            (
                "Frequentist Statistics",
                "Probability as long-run frequency",
                ConceptType.THEORY,
            ),
            (
                "Probability Theory",
                "Mathematical study of random phenomena",
                ConceptType.THEORY,
            ),
            (
                "Regression Analysis",
                "Modeling relationships between variables",
                ConceptType.THEORY,
            ),
            (
                "Time Series Analysis",
                "Analyzing sequential data points",
                ConceptType.THEORY,
            ),
            (
                "Multivariate Statistics",
                "Analyzing multiple variables simultaneously",
                ConceptType.THEORY,
            ),
            (
                "Nonparametric Statistics",
                "Methods without distributional assumptions",
                ConceptType.THEORY,
            ),
            (
                "Sampling Theory",
                "Study of sample selection methods",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_distributions(self) -> None:
        """Initialize probability distributions."""
        distributions = [
            ("Normal Distribution", "Gaussian bell curve", "Continuous", "μ, σ"),
            ("Binomial Distribution", "Number of successes in n trials", "Discrete", "n, p"),
            ("Poisson Distribution", "Events in fixed interval", "Discrete", "λ"),
            ("Exponential Distribution", "Time between events", "Continuous", "λ"),
            ("Uniform Distribution", "Equal probability over range", "Both", "a, b"),
            ("Chi-Square Distribution", "Sum of squared normal variables", "Continuous", "df"),
            ("t-Distribution", "Normal with estimated variance", "Continuous", "df"),
            ("F-Distribution", "Ratio of chi-square variables", "Continuous", "df1, df2"),
        ]

        for name, description, dist_type, parameters in distributions:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "type": dist_type,
                "parameters": parameters,
            })

    def initialize_measures(self) -> None:
        """Initialize statistical measures."""
        measures = [
            ("Mean", "Average value", "Central tendency", "Σx/n"),
            ("Median", "Middle value", "Central tendency", "Middle when sorted"),
            ("Mode", "Most frequent value", "Central tendency", "Highest frequency"),
            ("Variance", "Spread around mean", "Dispersion", "Σ(x-μ)²/n"),
            ("Standard Deviation", "Square root of variance", "Dispersion", "√variance"),
            ("Range", "Maximum minus minimum", "Dispersion", "max - min"),
            ("Interquartile Range", "Q3 minus Q1", "Dispersion", "Q3 - Q1"),
            ("Skewness", "Asymmetry of distribution", "Shape", "Third moment"),
            ("Kurtosis", "Tailedness of distribution", "Shape", "Fourth moment"),
        ]

        for name, description, measure_type, formula in measures:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "type": measure_type,
                "formula": formula,
            })

    def initialize_hypothesis_testing(self) -> None:
        """Initialize hypothesis testing concepts."""
        concepts = [
            ("Null Hypothesis", "H0", "No effect or difference", "Default position"),
            ("Alternative Hypothesis", "H1", "Effect or difference exists", "Research claim"),
            ("P-value", "p", "Probability of data given H0", "Evidence against H0"),
            ("Significance Level", "α", "Threshold for rejecting H0", "Typically 0.05"),
            ("Type I Error", "α", "Rejecting true H0", "False positive"),
            ("Type II Error", "β", "Failing to reject false H0", "False negative"),
            ("Power", "1-β", "Correctly rejecting false H0", "True positive rate"),
            ("Effect Size", "d, r", "Magnitude of difference", "Practical significance"),
        ]

        for name, symbol, description, interpretation in concepts:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "symbol": symbol,
                "interpretation": interpretation,
            })

    def initialize_statistical_tests(self) -> None:
        """Initialize common statistical tests."""
        tests = [
            ("t-test", "Compare means of two groups", "Parametric"),
            ("ANOVA", "Compare means of multiple groups", "Parametric"),
            ("Chi-Square Test", "Test independence of categorical variables", "Non-parametric"),
            ("Mann-Whitney U", "Non-parametric alternative to t-test", "Non-parametric"),
            ("Pearson Correlation", "Linear relationship between variables", "Parametric"),
            ("Spearman Correlation", "Monotonic relationship", "Non-parametric"),
            ("Linear Regression", "Predict continuous outcome", "Parametric"),
            ("Logistic Regression", "Predict categorical outcome", "Parametric"),
        ]

        for name, description, test_type in tests:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["test_type"] = test_type

    def initialize_statistical_pairs(self) -> None:
        """Initialize fundamental statistical pairs with META 50/50 balance."""
        pairs = [
            ("Signal", "Noise", "Pattern vs randomness"),
            ("Mean", "Variance", "Center vs spread"),
            ("Population", "Sample", "All vs subset"),
            ("Parameter", "Statistic", "True vs estimated"),
            ("Null", "Alternative", "No effect vs effect"),
            ("Significant", "Insignificant", "Real vs chance"),
            ("Correlation", "Causation", "Associated vs causing"),
            ("Positive", "Negative", "Same vs opposite direction"),
            ("Discrete", "Continuous", "Countable vs measurable"),
            ("Descriptive", "Inferential", "Summarizing vs concluding"),
            ("Probability", "Frequency", "Theoretical vs observed"),
            ("Normal", "Skewed", "Symmetric vs asymmetric"),
            ("Type I Error", "Type II Error", "False positive vs negative"),
            ("Precision", "Accuracy", "Consistent vs correct"),
            ("Bias", "Variance", "Systematic vs random error"),
            ("Independent", "Dependent", "Unrelated vs related"),
            ("Parametric", "Nonparametric", "Assumed vs free distribution"),
            ("Univariate", "Multivariate", "One vs many variables"),
            ("Outlier", "Typical", "Extreme vs normal"),
            ("Confidence", "Uncertainty", "Sure vs unsure"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Statistics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Statistics)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_critical_values(self) -> dict[str, dict[str, float]]:
        """Get common critical values."""
        return {
            "z_scores": {
                "90%": 1.645,
                "95%": 1.96,
                "99%": 2.576,
            },
            "t_scores_df_30": {
                "90%": 1.697,
                "95%": 2.042,
                "99%": 2.750,
            },
        }

    def demonstrate_statistical_balance(self) -> dict[str, Any]:
        """Demonstrate statistical balance principles."""
        return {
            "concept": "Statistical Equilibrium",
            "dualities": {
                "signal_noise": {
                    "signal": 50.0,
                    "noise": 50.0,
                    "meaning": "Data contains both pattern and randomness",
                },
                "type_errors": {
                    "type_i_error": 50.0,
                    "type_ii_error": 50.0,
                    "meaning": "Trade-off between false positives and negatives",
                },
                "bias_variance": {
                    "bias": 50.0,
                    "variance": 50.0,
                    "meaning": "Trade-off in model complexity",
                },
            },
            "normal_distribution": {
                "below_mean": 50.0,
                "above_mean": 50.0,
                "description": "Symmetric distribution around the mean",
            },
            "meta_meaning": "Statistics demonstrates META 50/50 in error trade-offs",
        }


def create_statistics_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> StatisticsDomain:
    """
    Factory function to create a fully initialized statistics domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized StatisticsDomain
    """
    domain = StatisticsDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_distributions()
        domain.initialize_measures()
        domain.initialize_hypothesis_testing()
        domain.initialize_statistical_tests()
        domain.initialize_statistical_pairs()

    return domain
