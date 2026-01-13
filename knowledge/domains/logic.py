"""
Logic Domain
============
Logical knowledge domain with META 50/50 equilibrium.
Fundamental duality: True/False (validity of propositions).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class LogicDomain(KnowledgeDomain):
    """
    Logic knowledge domain.

    Fundamental Duality: True / False
    - True: Valid, correct, sound, affirmed
    - False: Invalid, incorrect, unsound, negated

    Secondary Dualities:
    - Valid / Invalid
    - Necessary / Contingent
    - Universal / Particular
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Logic",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of valid reasoning and argumentation",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize True/False duality."""
        self._domain.set_duality(
            positive_name="true",
            positive_value=50,
            negative_name="false",
            negative_value=50,
            duality_name="logic_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental logical laws."""
        laws = [
            (
                "Law of Identity",
                "A is A; everything is identical to itself",
            ),
            (
                "Law of Non-Contradiction",
                "A cannot be both A and not-A at the same time",
            ),
            (
                "Law of Excluded Middle",
                "Either A or not-A; no third option",
            ),
            (
                "Modus Ponens",
                "If P then Q; P; therefore Q",
            ),
            (
                "Modus Tollens",
                "If P then Q; not Q; therefore not P",
            ),
            (
                "Syllogism",
                "All A are B; all B are C; therefore all A are C",
            ),
            (
                "Double Negation",
                "Not-not-A is equivalent to A",
            ),
            (
                "De Morgan's Laws",
                "Negation distributes over conjunction and disjunction",
            ),
        ]

        for name, description in laws:
            self.create_concept(
                name=name,
                concept_type=ConceptType.LAW,
                description=description,
                certainty=100,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental logic concepts."""
        return [
            "Proposition",
            "Argument",
            "Premise",
            "Conclusion",
            "Validity",
            "Soundness",
            "Truth",
            "Fallacy",
            "Inference",
            "Deduction",
            "Induction",
            "Negation",
            "Conjunction",
            "Disjunction",
            "Implication",
        ]

    def initialize_branches(self) -> None:
        """Initialize major logic branches."""
        branches = [
            (
                "Propositional Logic",
                "Logic of propositions and connectives",
                ConceptType.THEORY,
            ),
            (
                "Predicate Logic",
                "Logic with quantifiers and predicates",
                ConceptType.THEORY,
            ),
            (
                "Modal Logic",
                "Logic of necessity and possibility",
                ConceptType.THEORY,
            ),
            (
                "Boolean Logic",
                "Algebraic logic with true/false values",
                ConceptType.THEORY,
            ),
            (
                "Fuzzy Logic",
                "Logic with degrees of truth",
                ConceptType.THEORY,
            ),
            (
                "Temporal Logic",
                "Logic of time and temporal relations",
                ConceptType.THEORY,
            ),
            (
                "Deontic Logic",
                "Logic of obligation and permission",
                ConceptType.THEORY,
            ),
            (
                "Intuitionistic Logic",
                "Constructive logic without excluded middle",
                ConceptType.THEORY,
            ),
            (
                "Informal Logic",
                "Study of everyday reasoning",
                ConceptType.THEORY,
            ),
            (
                "Mathematical Logic",
                "Formal logic in mathematics",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_logical_connectives(self) -> None:
        """Initialize logical connectives."""
        connectives = [
            ("Negation", "NOT", "~", "Reverses truth value"),
            ("Conjunction", "AND", "∧", "True when both true"),
            ("Disjunction", "OR", "∨", "True when at least one true"),
            ("Implication", "IF-THEN", "→", "False only when P true and Q false"),
            ("Biconditional", "IF AND ONLY IF", "↔", "True when both same"),
            ("Exclusive Or", "XOR", "⊕", "True when exactly one true"),
        ]

        for name, keyword, symbol, description in connectives:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "keyword": keyword,
                "symbol": symbol,
            })

    def initialize_quantifiers(self) -> None:
        """Initialize logical quantifiers."""
        quantifiers = [
            ("Universal Quantifier", "∀", "For all", "All members satisfy"),
            ("Existential Quantifier", "∃", "There exists", "At least one satisfies"),
            ("Uniqueness Quantifier", "∃!", "There exists unique", "Exactly one satisfies"),
        ]

        for name, symbol, reading, meaning in quantifiers:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=meaning,
            )
            concept.metadata.update({
                "symbol": symbol,
                "reading": reading,
            })

    def initialize_fallacies(self) -> None:
        """Initialize common logical fallacies."""
        fallacies = [
            ("Ad Hominem", "Attacking the person instead of the argument"),
            ("Straw Man", "Misrepresenting opponent's position"),
            ("Appeal to Authority", "Using authority as proof"),
            ("False Dichotomy", "Presenting only two options when more exist"),
            ("Slippery Slope", "Assuming chain of events without justification"),
            ("Circular Reasoning", "Using conclusion as premise"),
            ("Hasty Generalization", "Generalizing from insufficient examples"),
            ("Red Herring", "Introducing irrelevant topic"),
            ("Appeal to Emotion", "Using emotions instead of logic"),
            ("Post Hoc", "Assuming causation from correlation"),
        ]

        for name, description in fallacies:
            self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=f"Fallacy: {description}",
            )

    def initialize_argument_forms(self) -> None:
        """Initialize valid argument forms."""
        forms = [
            ("Modus Ponens", "P→Q, P ⊢ Q", "Affirming the antecedent"),
            ("Modus Tollens", "P→Q, ~Q ⊢ ~P", "Denying the consequent"),
            ("Hypothetical Syllogism", "P→Q, Q→R ⊢ P→R", "Chain argument"),
            ("Disjunctive Syllogism", "P∨Q, ~P ⊢ Q", "Elimination"),
            ("Constructive Dilemma", "(P→Q)∧(R→S), P∨R ⊢ Q∨S", "Double conditional"),
            ("Reductio Ad Absurdum", "Assume P, derive contradiction ⊢ ~P", "Proof by contradiction"),
        ]

        for name, form, description in forms:
            concept = self.create_concept(
                name=f"{name} (Argument Form)",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["formal_notation"] = form

    def initialize_logical_pairs(self) -> None:
        """Initialize fundamental logical pairs with META 50/50 balance."""
        pairs = [
            ("True", "False", "Valid vs invalid"),
            ("Premise", "Conclusion", "Starting vs ending point"),
            ("Valid", "Invalid", "Correct vs incorrect form"),
            ("Sound", "Unsound", "True premises vs false"),
            ("Deductive", "Inductive", "Certain vs probable"),
            ("Necessary", "Contingent", "Must be vs might be"),
            ("Consistent", "Contradictory", "Compatible vs conflicting"),
            ("Tautology", "Contradiction", "Always true vs never"),
            ("Implication", "Equivalence", "If-then vs if-and-only-if"),
            ("Conjunction", "Disjunction", "And vs or"),
            ("Affirmation", "Negation", "Asserting vs denying"),
            ("Universal", "Particular", "All vs some"),
            ("A Priori", "A Posteriori", "Before vs after experience"),
            ("Analytic", "Synthetic", "Definition vs discovery"),
            ("Formal", "Informal", "Structured vs natural"),
            ("Proof", "Refutation", "Establishing vs disproving"),
            ("Axiom", "Theorem", "Assumed vs derived"),
            ("Sufficient", "Necessary", "Enough vs required"),
            ("Strong", "Weak", "Compelling vs suggestive"),
            ("Fallacy", "Valid Argument", "Error vs correct"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Logic)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Logic)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_truth_table_and(self) -> dict[tuple[bool, bool], bool]:
        """Get AND truth table."""
        return {
            (True, True): True,
            (True, False): False,
            (False, True): False,
            (False, False): False,
        }

    def get_truth_table_or(self) -> dict[tuple[bool, bool], bool]:
        """Get OR truth table."""
        return {
            (True, True): True,
            (True, False): True,
            (False, True): True,
            (False, False): False,
        }

    def demonstrate_logical_balance(self) -> dict[str, Any]:
        """Demonstrate logical balance principles."""
        return {
            "concept": "Logical Equilibrium",
            "dualities": {
                "true_false": {
                    "true": 50.0,
                    "false": 50.0,
                    "meaning": "Every proposition is either true or false",
                },
                "affirmation_negation": {
                    "affirmation": 50.0,
                    "negation": 50.0,
                    "meaning": "For every P there exists not-P",
                },
                "universal_particular": {
                    "universal": 50.0,
                    "particular": 50.0,
                    "meaning": "All vs some quantification",
                },
            },
            "law_of_excluded_middle": {
                "P": 50.0,
                "not_P": 50.0,
                "description": "Either P or not-P, with no middle ground",
            },
            "meta_meaning": "Logic demonstrates META 50/50 in truth value balance",
        }


def create_logic_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> LogicDomain:
    """
    Factory function to create a fully initialized logic domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized LogicDomain
    """
    domain = LogicDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_logical_connectives()
        domain.initialize_quantifiers()
        domain.initialize_fallacies()
        domain.initialize_argument_forms()
        domain.initialize_logical_pairs()

    return domain
