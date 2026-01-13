"""
Code/Programming Domain
=======================
Software development knowledge domain with META 50/50 equilibrium.
Fundamental duality: Abstraction/Implementation (design/code).
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


class CodeDomain(KnowledgeDomain):
    """
    Code/Programming knowledge domain.

    Fundamental Duality: Abstraction / Implementation
    - Abstraction: Design, architecture, interfaces, concepts
    - Implementation: Code, execution, concrete solutions

    Secondary Dualities:
    - Static / Dynamic (compile-time / runtime)
    - Functional / Imperative (paradigms)
    - Simplicity / Complexity (design balance)
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Code",
            domain_type=DomainType.FUNDAMENTAL,
            description="The art and science of software development",
            meta_equilibrium=meta_equilibrium
        )

    def _initialize_duality(self) -> None:
        """Initialize Abstraction/Implementation duality."""
        self._domain.set_duality(
            positive_name="abstraction",
            positive_value=50,
            negative_name="implementation",
            negative_value=50,
            duality_name="code_duality"
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental programming principles as axioms."""
        principles = [
            (
                "DRY",
                "Don't Repeat Yourself - every piece of knowledge has a single representation"
            ),
            (
                "KISS",
                "Keep It Simple, Stupid - simplicity is a key goal in design"
            ),
            (
                "YAGNI",
                "You Aren't Gonna Need It - don't add functionality until necessary"
            ),
            (
                "Separation of Concerns",
                "Divide a program into distinct sections with minimal overlap"
            ),
            (
                "Single Responsibility",
                "A class should have only one reason to change"
            ),
            (
                "Open/Closed Principle",
                "Open for extension, closed for modification"
            ),
            (
                "Liskov Substitution",
                "Objects should be replaceable by subtypes"
            ),
            (
                "Interface Segregation",
                "Many specific interfaces are better than one general interface"
            ),
            (
                "Dependency Inversion",
                "Depend on abstractions, not concretions"
            ),
            (
                "Composition Over Inheritance",
                "Favor object composition over class inheritance"
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=90  # Principles are highly certain but context-dependent
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental programming concepts."""
        return [
            "Variable", "Function", "Class", "Object", "Interface",
            "Module", "Package", "Algorithm", "Data Structure", "Type",
            "Loop", "Condition", "Exception", "Thread", "Memory"
        ]

    def initialize_paradigms(self) -> None:
        """Initialize programming paradigms."""
        paradigms = [
            (
                "Imperative",
                "Programs as sequences of commands that change state",
                ["C", "Pascal", "BASIC"]
            ),
            (
                "Object-Oriented",
                "Programs as collections of interacting objects",
                ["Java", "C++", "Python"]
            ),
            (
                "Functional",
                "Programs as evaluation of mathematical functions",
                ["Haskell", "Lisp", "Erlang"]
            ),
            (
                "Declarative",
                "Programs express logic without describing control flow",
                ["SQL", "Prolog", "HTML"]
            ),
            (
                "Event-Driven",
                "Programs respond to events and user actions",
                ["JavaScript", "Visual Basic"]
            ),
            (
                "Concurrent",
                "Programs with multiple simultaneous execution paths",
                ["Go", "Erlang", "Rust"]
            ),
            (
                "Reactive",
                "Programs built around data streams and propagation",
                ["RxJS", "ReactiveX"]
            ),
            (
                "Logic",
                "Programs based on formal logic",
                ["Prolog", "Datalog"]
            ),
        ]

        for name, description, examples in paradigms:
            concept = self.create_concept(
                name=f"{name} Programming",
                concept_type=ConceptType.THEORY,
                description=description
            )
            concept.metadata["example_languages"] = examples

    def initialize_data_structures(self) -> None:
        """Initialize fundamental data structures."""
        structures = [
            ("Array", "Contiguous collection of elements", "O(1)", "O(n)"),
            ("Linked List", "Sequential collection via pointers", "O(n)", "O(1)"),
            ("Stack", "Last-In-First-Out collection", "O(1)", "O(1)"),
            ("Queue", "First-In-First-Out collection", "O(1)", "O(1)"),
            ("Hash Table", "Key-value pairs with hash function", "O(1)", "O(n)"),
            ("Binary Tree", "Hierarchical structure with two children", "O(log n)", "O(log n)"),
            ("Heap", "Complete binary tree with heap property", "O(log n)", "O(log n)"),
            ("Graph", "Nodes connected by edges", "O(V+E)", "O(V+E)"),
            ("Trie", "Tree for string retrieval", "O(m)", "O(m)"),
            ("B-Tree", "Self-balancing tree for databases", "O(log n)", "O(log n)"),
        ]

        for name, description, access_time, insert_time in structures:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description
            )
            concept.metadata.update({
                "access_complexity": access_time,
                "insert_complexity": insert_time
            })

    def initialize_algorithms(self) -> None:
        """Initialize fundamental algorithms."""
        algorithms = [
            ("Binary Search", "Search sorted array by halving", "O(log n)", "Searching"),
            ("Quick Sort", "Divide-and-conquer sorting", "O(n log n)", "Sorting"),
            ("Merge Sort", "Stable divide-and-conquer sort", "O(n log n)", "Sorting"),
            ("Heap Sort", "Selection sort using heap", "O(n log n)", "Sorting"),
            ("Depth-First Search", "Graph traversal going deep first", "O(V+E)", "Graph"),
            ("Breadth-First Search", "Graph traversal level by level", "O(V+E)", "Graph"),
            ("Dijkstra's Algorithm", "Shortest path in weighted graph", "O(V²)", "Graph"),
            ("Dynamic Programming", "Solve by combining subproblem solutions", "Varies", "Optimization"),
            ("Greedy Algorithm", "Local optimal choices for global solution", "Varies", "Optimization"),
            ("Backtracking", "Incremental solution with backtracking", "Varies", "Search"),
        ]

        for name, description, complexity, category in algorithms:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.MODEL,
                description=description
            )
            concept.metadata.update({
                "time_complexity": complexity,
                "category": category
            })

    def initialize_design_patterns(self) -> None:
        """Initialize common design patterns."""
        patterns = [
            # Creational
            ("Singleton", "Ensure single instance of a class", "Creational"),
            ("Factory", "Create objects without specifying exact class", "Creational"),
            ("Builder", "Construct complex objects step by step", "Creational"),
            ("Prototype", "Create objects by cloning", "Creational"),

            # Structural
            ("Adapter", "Convert interface to another interface", "Structural"),
            ("Decorator", "Add behavior dynamically", "Structural"),
            ("Facade", "Simplified interface to complex subsystem", "Structural"),
            ("Proxy", "Placeholder for another object", "Structural"),
            ("Composite", "Treat objects and compositions uniformly", "Structural"),

            # Behavioral
            ("Observer", "Notify dependents of state changes", "Behavioral"),
            ("Strategy", "Encapsulate interchangeable algorithms", "Behavioral"),
            ("Command", "Encapsulate request as object", "Behavioral"),
            ("Iterator", "Sequential access to collection elements", "Behavioral"),
            ("State", "Alter behavior when internal state changes", "Behavioral"),
        ]

        for name, description, category in patterns:
            concept = self.create_concept(
                name=f"{name} Pattern",
                concept_type=ConceptType.MODEL,
                description=description
            )
            concept.metadata["pattern_category"] = category

    def initialize_languages(self) -> None:
        """Initialize major programming languages."""
        languages = [
            ("Python", "High-level, interpreted, general-purpose", 1991, ["OOP", "Functional"]),
            ("JavaScript", "Web scripting language", 1995, ["OOP", "Functional", "Event-driven"]),
            ("Java", "Platform-independent OOP language", 1995, ["OOP"]),
            ("C", "Low-level systems programming", 1972, ["Imperative"]),
            ("C++", "C with classes and OOP features", 1985, ["OOP", "Imperative"]),
            ("Rust", "Memory-safe systems programming", 2010, ["Imperative", "Functional"]),
            ("Go", "Simple, efficient concurrent language", 2009, ["Imperative", "Concurrent"]),
            ("TypeScript", "Typed superset of JavaScript", 2012, ["OOP", "Functional"]),
            ("Swift", "Modern language for Apple platforms", 2014, ["OOP", "Functional"]),
            ("Kotlin", "Modern JVM language", 2011, ["OOP", "Functional"]),
            ("Haskell", "Pure functional programming", 1990, ["Functional"]),
            ("SQL", "Database query language", 1974, ["Declarative"]),
        ]

        for name, description, year, paradigms in languages:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description
            )
            concept.metadata.update({
                "year_created": year,
                "paradigms": paradigms
            })

    def demonstrate_code_balance(self) -> dict[str, Any]:
        """
        Demonstrate balanced code principles.
        Shows META 50/50 in software design.
        """
        return {
            "concept": "Balanced Software Design",
            "dualities": {
                "abstraction_implementation": {
                    "abstraction": 50.0,
                    "implementation": 50.0,
                    "meaning": "Design should balance high-level concepts with practical code"
                },
                "flexibility_simplicity": {
                    "flexibility": 50.0,
                    "simplicity": 50.0,
                    "meaning": "Code should be adaptable but not over-engineered"
                },
                "performance_readability": {
                    "performance": 50.0,
                    "readability": 50.0,
                    "meaning": "Optimize where needed, prioritize clarity elsewhere"
                },
                "testing_development": {
                    "testing": 50.0,
                    "development": 50.0,
                    "meaning": "Tests and code should grow together"
                }
            },
            "operational_ratio": {
                "structure": 52.0,
                "flexibility": 48.0,
                "meaning": "Slight structural bias enables maintainability"
            },
            "meta_meaning": "Good code maintains equilibrium between competing concerns"
        }

    def get_complexity_classes(self) -> dict[str, str]:
        """Get common algorithmic complexity classes."""
        return {
            "O(1)": "Constant - independent of input size",
            "O(log n)": "Logarithmic - halving with each step",
            "O(n)": "Linear - proportional to input",
            "O(n log n)": "Linearithmic - efficient sorting",
            "O(n²)": "Quadratic - nested iterations",
            "O(n³)": "Cubic - triple nested iterations",
            "O(2ⁿ)": "Exponential - doubles with each element",
            "O(n!)": "Factorial - permutations",
        }


def create_code_domain(
    meta_equilibrium: MetaEquilibrium | None = None,
    initialize_all: bool = True
) -> CodeDomain:
    """
    Factory function to create a fully initialized code domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized CodeDomain
    """
    domain = CodeDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_paradigms()
        domain.initialize_data_structures()
        domain.initialize_algorithms()
        domain.initialize_design_patterns()
        domain.initialize_languages()

    return domain
