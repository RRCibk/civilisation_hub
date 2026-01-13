"""
Accounting Domain
=================
Accounting knowledge domain with META 50/50 equilibrium.
Fundamental duality: Assets/Liabilities (what you own vs what you owe).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class AccountingDomain(KnowledgeDomain):
    """
    Accounting knowledge domain.

    Fundamental Duality: Assets / Liabilities
    - Assets: What the entity owns, resources
    - Liabilities: What the entity owes, obligations

    Secondary Dualities:
    - Debit / Credit
    - Revenue / Expense
    - Financial / Managerial
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Accounting",
            domain_type=DomainType.FUNDAMENTAL,
            description="The measurement and communication of financial information",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Assets/Liabilities duality."""
        self._domain.set_duality(
            positive_name="assets",
            positive_value=50,
            negative_name="liabilities",
            negative_value=50,
            duality_name="accounting_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental accounting principles."""
        principles = [
            ("Accounting Equation", "Assets = Liabilities + Equity"),
            ("Double Entry", "Every transaction has two effects"),
            ("Accrual Basis", "Record when earned, not when received"),
            ("Going Concern", "Assume business continues"),
            ("Materiality", "Report significant information"),
            ("Consistency", "Use same methods over time"),
            ("Conservatism", "When uncertain, choose lower values"),
            ("Full Disclosure", "Report all relevant information"),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=95,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental accounting concepts."""
        return ["Assets", "Liabilities", "Equity", "Revenue", "Expense", "Debit",
                "Credit", "Journal", "Ledger", "Trial Balance", "Income Statement",
                "Balance Sheet", "Cash Flow", "Audit", "GAAP"]

    def initialize_branches(self) -> None:
        """Initialize major accounting branches."""
        branches = [
            ("Financial Accounting", "External reporting", ConceptType.THEORY),
            ("Managerial Accounting", "Internal decision-making", ConceptType.THEORY),
            ("Cost Accounting", "Product costing", ConceptType.THEORY),
            ("Tax Accounting", "Tax compliance", ConceptType.THEORY),
            ("Auditing", "Financial verification", ConceptType.THEORY),
            ("Forensic Accounting", "Fraud investigation", ConceptType.THEORY),
            ("Government Accounting", "Public sector", ConceptType.THEORY),
            ("International Accounting", "Cross-border standards", ConceptType.THEORY),
            ("Environmental Accounting", "Sustainability reporting", ConceptType.THEORY),
            ("Non-profit Accounting", "Charitable organizations", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_statements(self) -> None:
        """Initialize financial statements."""
        statements = [
            ("Balance Sheet", "Financial position", "Point in time"),
            ("Income Statement", "Profitability", "Period"),
            ("Cash Flow Statement", "Cash movements", "Period"),
            ("Statement of Equity", "Ownership changes", "Period"),
        ]

        for name, description, timing in statements:
            concept = self.create_concept(name, ConceptType.DEFINITION, description)
            concept.metadata["timing"] = timing

    def initialize_accounting_pairs(self) -> None:
        """Initialize fundamental accounting pairs with META 50/50 balance."""
        pairs = [
            ("Assets", "Liabilities", "Own vs owe"),
            ("Debit", "Credit", "Left vs right entry"),
            ("Revenue", "Expense", "Income vs cost"),
            ("Financial", "Managerial", "External vs internal"),
            ("Accrual", "Cash", "Earned vs received"),
            ("Current", "Non-current", "Short vs long term"),
            ("Operating", "Financing", "Core vs capital activities"),
            ("Direct", "Indirect", "Traceable vs allocated"),
            ("Fixed", "Variable", "Constant vs changing costs"),
            ("Actual", "Budget", "Real vs planned"),
            ("Historical", "Fair Value", "Past vs current worth"),
            ("Gross", "Net", "Before vs after deductions"),
            ("Internal", "External", "Inside vs outside users"),
            ("Quantitative", "Qualitative", "Numbers vs narrative"),
            ("Objective", "Subjective", "Verifiable vs estimated"),
            ("Relevant", "Reliable", "Decision-useful vs accurate"),
            ("Periodic", "Perpetual", "Batch vs continuous"),
            ("Manual", "Automated", "Human vs system"),
            ("Compliance", "Advisory", "Rules vs strategy"),
            ("Materiality", "Precision", "Significant vs exact"),
        ]

        for positive, negative, description in pairs:
            pos = self.create_concept(f"{positive} (Accounting)", ConceptType.DEFINITION,
                                       f"Positive pole: {description.split(' vs ')[0]}")
            neg = self.create_concept(f"{negative} (Accounting)", ConceptType.DEFINITION,
                                       f"Negative pole: {description.split(' vs ')[1]}")
            self.create_relation(pos, neg, RelationType.CONTRADICTS, strength=50)

    def demonstrate_accounting_balance(self) -> dict[str, Any]:
        """Demonstrate accounting balance principles."""
        return {
            "concept": "Accounting Equilibrium",
            "dualities": {
                "assets_liabilities": {"assets": 50.0, "liabilities": 50.0,
                    "meaning": "Balance sheet must balance"},
                "debit_credit": {"debit": 50.0, "credit": 50.0,
                    "meaning": "Every entry has equal opposite"},
            },
            "meta_meaning": "Accounting demonstrates META 50/50 in assets-liabilities balance",
        }


def create_accounting_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> AccountingDomain:
    domain = AccountingDomain(meta_equilibrium)
    if initialize_all:
        domain.initialize_branches()
        domain.initialize_statements()
        domain.initialize_accounting_pairs()
    return domain
