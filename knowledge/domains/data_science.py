"""
Data Science Domain
===================
Data science knowledge domain with META 50/50 equilibrium.
Fundamental duality: Data/Insight (raw information vs understanding).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class DataScienceDomain(KnowledgeDomain):
    """
    Data Science knowledge domain.

    Fundamental Duality: Data / Insight
    - Data: Raw information, observations, measurements
    - Insight: Understanding, patterns, actionable knowledge

    Secondary Dualities:
    - Exploration / Confirmation
    - Descriptive / Predictive
    - Quantitative / Qualitative
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="DataScience",
            domain_type=DomainType.FUNDAMENTAL,
            description="The extraction of knowledge from data",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Data/Insight duality."""
        self._domain.set_duality(
            positive_name="data",
            positive_value=50,
            negative_name="insight",
            negative_value=50,
            duality_name="data_science_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental data science principles."""
        principles = [
            (
                "Data Quality",
                "Garbage in, garbage out",
            ),
            (
                "Reproducibility",
                "Results must be reproducible",
            ),
            (
                "Domain Knowledge",
                "Context is essential for interpretation",
            ),
            (
                "Iteration",
                "Analysis is iterative process",
            ),
            (
                "Visualization",
                "Show data to reveal patterns",
            ),
            (
                "Communication",
                "Insights must be communicated effectively",
            ),
            (
                "Ethics",
                "Data use has ethical implications",
            ),
            (
                "Skepticism",
                "Question results and assumptions",
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
        """Get fundamental data science concepts."""
        return [
            "Data",
            "Analysis",
            "Model",
            "Pattern",
            "Prediction",
            "Feature",
            "Variable",
            "Correlation",
            "Regression",
            "Classification",
            "Clustering",
            "Visualization",
            "Pipeline",
            "Validation",
            "Metric",
        ]

    def initialize_branches(self) -> None:
        """Initialize major data science branches."""
        branches = [
            (
                "Descriptive Analytics",
                "What happened",
                ConceptType.THEORY,
            ),
            (
                "Diagnostic Analytics",
                "Why it happened",
                ConceptType.THEORY,
            ),
            (
                "Predictive Analytics",
                "What will happen",
                ConceptType.THEORY,
            ),
            (
                "Prescriptive Analytics",
                "What to do about it",
                ConceptType.THEORY,
            ),
            (
                "Data Engineering",
                "Data infrastructure",
                ConceptType.THEORY,
            ),
            (
                "Statistical Modeling",
                "Statistical approaches",
                ConceptType.THEORY,
            ),
            (
                "Machine Learning",
                "Algorithmic learning",
                ConceptType.THEORY,
            ),
            (
                "Data Visualization",
                "Visual communication",
                ConceptType.THEORY,
            ),
            (
                "Big Data",
                "Large-scale data processing",
                ConceptType.THEORY,
            ),
            (
                "Business Intelligence",
                "Business decision support",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_process(self) -> None:
        """Initialize data science process stages."""
        stages = [
            ("Data Collection", "Gather data", "Input"),
            ("Data Cleaning", "Prepare data", "Preprocessing"),
            ("Exploration", "Understand data", "Analysis"),
            ("Modeling", "Build models", "Core"),
            ("Evaluation", "Assess results", "Validation"),
            ("Deployment", "Implement solutions", "Output"),
        ]

        for name, description, phase in stages:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["phase"] = phase

    def initialize_techniques(self) -> None:
        """Initialize data science techniques."""
        techniques = [
            ("Regression", "Predict continuous values", "Prediction"),
            ("Classification", "Predict categories", "Prediction"),
            ("Clustering", "Group similar items", "Discovery"),
            ("Dimensionality Reduction", "Reduce features", "Preprocessing"),
            ("Time Series", "Temporal patterns", "Analysis"),
            ("A/B Testing", "Experimental comparison", "Validation"),
        ]

        for name, description, category in techniques:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_data_science_pairs(self) -> None:
        """Initialize fundamental data science pairs with META 50/50 balance."""
        pairs = [
            ("Data", "Insight", "Information vs understanding"),
            ("Exploration", "Confirmation", "Discovery vs validation"),
            ("Descriptive", "Predictive", "Past vs future"),
            ("Quantitative", "Qualitative", "Numbers vs qualities"),
            ("Structured", "Unstructured", "Organized vs free-form"),
            ("Batch", "Streaming", "Historical vs real-time"),
            ("Supervised", "Unsupervised", "Guided vs exploratory"),
            ("Feature", "Target", "Input vs output"),
            ("Training", "Testing", "Learning vs validating"),
            ("Bias", "Variance", "Systematic vs random error"),
            ("Precision", "Recall", "Accuracy vs completeness"),
            ("Signal", "Noise", "Pattern vs randomness"),
            ("Sample", "Population", "Subset vs whole"),
            ("Local", "Global", "Specific vs general"),
            ("Simple", "Complex", "Basic vs sophisticated"),
            ("Correlation", "Causation", "Association vs cause"),
            ("Interpolation", "Extrapolation", "Within vs beyond"),
            ("Breadth", "Depth", "Wide vs deep analysis"),
            ("Automated", "Manual", "Machine vs human"),
            ("Raw", "Processed", "Original vs transformed"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Data Science)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Data Science)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_data_types(self) -> dict[str, str]:
        """Get data type classifications."""
        return {
            "numerical": "Quantitative measurements",
            "categorical": "Discrete categories",
            "ordinal": "Ordered categories",
            "text": "Unstructured text",
            "temporal": "Time-based data",
            "spatial": "Geographic data",
        }

    def demonstrate_data_science_balance(self) -> dict[str, Any]:
        """Demonstrate data science balance principles."""
        return {
            "concept": "Data Science Equilibrium",
            "dualities": {
                "data_insight": {
                    "data": 50.0,
                    "insight": 50.0,
                    "meaning": "Raw data and understanding equally important",
                },
                "exploration_confirmation": {
                    "exploration": 50.0,
                    "confirmation": 50.0,
                    "meaning": "Discovery and validation both essential",
                },
                "descriptive_predictive": {
                    "descriptive": 50.0,
                    "predictive": 50.0,
                    "meaning": "Understanding past and predicting future",
                },
            },
            "analysis_balance": {
                "quantitative": 50.0,
                "qualitative": 50.0,
                "description": "Numbers and context both inform",
            },
            "meta_meaning": "Data Science demonstrates META 50/50 in data-insight synthesis",
        }


def create_data_science_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> DataScienceDomain:
    """
    Factory function to create a fully initialized data science domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized DataScienceDomain
    """
    domain = DataScienceDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_process()
        domain.initialize_techniques()
        domain.initialize_data_science_pairs()

    return domain
