"""
Computation Domain
==================
Computation theory knowledge domain with META 50/50 equilibrium.
Fundamental duality: Input/Output (data transformation).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class ComputationDomain(KnowledgeDomain):
    """
    Computation knowledge domain.

    Fundamental Duality: Input / Output
    - Input: Data to be processed, initial state
    - Output: Result of computation, final state

    Secondary Dualities:
    - Deterministic / Probabilistic
    - Sequential / Parallel
    - Decidable / Undecidable
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Computation",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of algorithms, complexity, and computability",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Input/Output duality."""
        self._domain.set_duality(
            positive_name="input",
            positive_value=50,
            negative_name="output",
            negative_value=50,
            duality_name="computation_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental computation principles."""
        principles = [
            (
                "Church-Turing Thesis",
                "Anything computable is computable by a Turing machine",
            ),
            (
                "Halting Problem",
                "No algorithm can decide if arbitrary programs halt",
            ),
            (
                "Rice's Theorem",
                "All non-trivial semantic properties are undecidable",
            ),
            (
                "Time Hierarchy Theorem",
                "More time allows solving strictly harder problems",
            ),
            (
                "Space Hierarchy Theorem",
                "More space allows solving strictly harder problems",
            ),
            (
                "Cook-Levin Theorem",
                "SAT is NP-complete",
            ),
            (
                "P vs NP Conjecture",
                "Efficient verification may not imply efficient solution",
            ),
            (
                "Curry-Howard Correspondence",
                "Proofs correspond to programs, types to propositions",
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
        """Get fundamental computation concepts."""
        return [
            "Algorithm",
            "Turing Machine",
            "Complexity",
            "Decidability",
            "Computability",
            "Program",
            "Language",
            "Automaton",
            "Grammar",
            "Recursion",
            "Iteration",
            "State",
            "Transition",
            "Reduction",
            "Encoding",
        ]

    def initialize_branches(self) -> None:
        """Initialize major computation branches."""
        branches = [
            (
                "Computability Theory",
                "What can be computed",
                ConceptType.THEORY,
            ),
            (
                "Complexity Theory",
                "Resources needed for computation",
                ConceptType.THEORY,
            ),
            (
                "Automata Theory",
                "Abstract machines and languages",
                ConceptType.THEORY,
            ),
            (
                "Formal Languages",
                "Syntax and grammars",
                ConceptType.THEORY,
            ),
            (
                "Algorithm Analysis",
                "Efficiency of algorithms",
                ConceptType.THEORY,
            ),
            (
                "Quantum Computing",
                "Computation using quantum mechanics",
                ConceptType.THEORY,
            ),
            (
                "Parallel Computing",
                "Concurrent computation",
                ConceptType.THEORY,
            ),
            (
                "Distributed Computing",
                "Computation across multiple systems",
                ConceptType.THEORY,
            ),
            (
                "Randomized Algorithms",
                "Computation with randomness",
                ConceptType.THEORY,
            ),
            (
                "Cryptographic Computation",
                "Secure computation",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_complexity_classes(self) -> None:
        """Initialize complexity classes."""
        classes = [
            ("P", "Polynomial time decidable", "Efficiently solvable"),
            ("NP", "Nondeterministic polynomial", "Efficiently verifiable"),
            ("NP-Complete", "Hardest problems in NP", "SAT, Clique, etc."),
            ("NP-Hard", "At least as hard as NP-Complete", "May not be in NP"),
            ("PSPACE", "Polynomial space", "Space-bounded"),
            ("EXPTIME", "Exponential time", "Very hard problems"),
            ("BPP", "Bounded-error probabilistic polynomial", "Efficient with randomness"),
            ("BQP", "Bounded-error quantum polynomial", "Quantum efficiently solvable"),
        ]

        for name, description, characterization in classes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["characterization"] = characterization

    def initialize_automata(self) -> None:
        """Initialize automata types."""
        automata = [
            ("Finite Automaton", "Fixed memory states", "Regular languages"),
            ("Pushdown Automaton", "Stack memory", "Context-free languages"),
            ("Turing Machine", "Unbounded tape", "Recursively enumerable"),
            ("Linear Bounded Automaton", "Bounded tape", "Context-sensitive"),
            ("Nondeterministic FA", "Multiple transitions", "Same as DFA"),
            ("Quantum Automaton", "Quantum states", "Some advantage"),
        ]

        for name, description, language_class in automata:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["language_class"] = language_class

    def initialize_algorithm_paradigms(self) -> None:
        """Initialize algorithm design paradigms."""
        paradigms = [
            ("Divide and Conquer", "Split problem, solve parts, combine", "Merge sort"),
            ("Dynamic Programming", "Store subproblem solutions", "Fibonacci"),
            ("Greedy", "Make locally optimal choices", "Huffman coding"),
            ("Backtracking", "Explore and retreat", "N-Queens"),
            ("Branch and Bound", "Pruned tree search", "TSP"),
            ("Randomized", "Use random choices", "QuickSort"),
        ]

        for name, description, example in paradigms:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["example"] = example

    def initialize_time_complexity(self) -> None:
        """Initialize time complexity notations."""
        complexities = [
            ("O(1)", "Constant", "Array access"),
            ("O(log n)", "Logarithmic", "Binary search"),
            ("O(n)", "Linear", "Linear search"),
            ("O(n log n)", "Linearithmic", "Merge sort"),
            ("O(n²)", "Quadratic", "Bubble sort"),
            ("O(n³)", "Cubic", "Matrix multiplication"),
            ("O(2^n)", "Exponential", "Subset enumeration"),
            ("O(n!)", "Factorial", "Permutations"),
        ]

        for notation, name, example in complexities:
            concept = self.create_concept(
                name=f"{name} Time",
                concept_type=ConceptType.DEFINITION,
                description=f"Complexity: {notation}",
            )
            concept.metadata.update({
                "notation": notation,
                "example": example,
            })

    def initialize_computation_pairs(self) -> None:
        """Initialize fundamental computation pairs with META 50/50 balance."""
        pairs = [
            ("Input", "Output", "Data in vs result out"),
            ("Algorithm", "Heuristic", "Guaranteed vs approximate"),
            ("Deterministic", "Probabilistic", "Certain vs random"),
            ("Sequential", "Parallel", "One vs many at once"),
            ("Recursive", "Iterative", "Self-calling vs looping"),
            ("Decidable", "Undecidable", "Solvable vs not"),
            ("Tractable", "Intractable", "Feasible vs impractical"),
            ("Polynomial", "Exponential", "Manageable vs explosive"),
            ("Terminating", "Nonterminating", "Halting vs infinite"),
            ("Correct", "Incorrect", "Right vs wrong"),
            ("Complete", "Incomplete", "All vs some cases"),
            ("Optimal", "Suboptimal", "Best vs good enough"),
            ("Time", "Space", "Speed vs memory"),
            ("Complexity", "Simplicity", "Hard vs easy"),
            ("Computable", "Noncomputable", "Calculable vs not"),
            ("Syntax", "Semantics", "Form vs meaning"),
            ("Compile", "Interpret", "Translate vs execute"),
            ("Static", "Dynamic", "Fixed vs changing"),
            ("Formal", "Informal", "Rigorous vs flexible"),
            ("Theory", "Practice", "Abstract vs applied"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Computation)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Computation)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_complexity_relationships(self) -> dict[str, str]:
        """Get complexity class relationships."""
        return {
            "P_subset_NP": "P ⊆ NP",
            "NP_subset_PSPACE": "NP ⊆ PSPACE",
            "PSPACE_subset_EXPTIME": "PSPACE ⊆ EXPTIME",
            "P_vs_NP": "P = NP is unknown",
            "co_NP": "co-NP may equal NP",
        }

    def demonstrate_computation_balance(self) -> dict[str, Any]:
        """Demonstrate computation balance principles."""
        return {
            "concept": "Computation Equilibrium",
            "dualities": {
                "input_output": {
                    "input": 50.0,
                    "output": 50.0,
                    "meaning": "Every computation transforms input to output",
                },
                "time_space": {
                    "time": 50.0,
                    "space": 50.0,
                    "meaning": "Trade-off between speed and memory",
                },
                "decidable_undecidable": {
                    "decidable": 50.0,
                    "undecidable": 50.0,
                    "meaning": "Some problems cannot be solved algorithmically",
                },
            },
            "halting_balance": {
                "halting": 50.0,
                "non_halting": 50.0,
                "description": "Programs either halt or loop forever",
            },
            "meta_meaning": "Computation demonstrates META 50/50 in decidability limits",
        }


def create_computation_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> ComputationDomain:
    """
    Factory function to create a fully initialized computation domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized ComputationDomain
    """
    domain = ComputationDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_complexity_classes()
        domain.initialize_automata()
        domain.initialize_algorithm_paradigms()
        domain.initialize_time_complexity()
        domain.initialize_computation_pairs()

    return domain
