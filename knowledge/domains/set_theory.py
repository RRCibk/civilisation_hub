"""
Set Theory Domain
=================
Set theory knowledge domain with META 50/50 equilibrium.
Fundamental duality: Element/Set (member vs collection).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class SetTheoryDomain(KnowledgeDomain):
    """
    Set Theory knowledge domain.

    Fundamental Duality: Element / Set
    - Element: Individual member, contained object
    - Set: Collection, container, aggregate

    Secondary Dualities:
    - Union / Intersection
    - Subset / Superset
    - Finite / Infinite
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="SetTheory",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of sets, collections, and their properties",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Element/Set duality."""
        self._domain.set_duality(
            positive_name="element",
            positive_value=50,
            negative_name="set",
            negative_value=50,
            duality_name="set_theory_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize Zermelo-Fraenkel axioms."""
        axioms = [
            (
                "Axiom of Extensionality",
                "Sets with the same elements are equal",
            ),
            (
                "Axiom of Empty Set",
                "There exists a set with no elements",
            ),
            (
                "Axiom of Pairing",
                "For any two sets, there is a set containing just them",
            ),
            (
                "Axiom of Union",
                "For any set of sets, there is a set containing all their elements",
            ),
            (
                "Axiom of Power Set",
                "For any set, there is a set of all its subsets",
            ),
            (
                "Axiom of Infinity",
                "There exists an infinite set",
            ),
            (
                "Axiom of Replacement",
                "Image of a set under a function is a set",
            ),
            (
                "Axiom of Choice",
                "Every collection of non-empty sets has a choice function",
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
        """Get fundamental set theory concepts."""
        return [
            "Set",
            "Element",
            "Subset",
            "Union",
            "Intersection",
            "Complement",
            "Empty Set",
            "Universal Set",
            "Power Set",
            "Cardinality",
            "Finite",
            "Infinite",
            "Function",
            "Relation",
            "Bijection",
        ]

    def initialize_branches(self) -> None:
        """Initialize major set theory branches."""
        branches = [
            (
                "Naive Set Theory",
                "Intuitive approach to sets",
                ConceptType.THEORY,
            ),
            (
                "Axiomatic Set Theory",
                "Formal axiom-based approach",
                ConceptType.THEORY,
            ),
            (
                "Descriptive Set Theory",
                "Study of definable sets of reals",
                ConceptType.THEORY,
            ),
            (
                "Large Cardinal Theory",
                "Study of very large infinite sets",
                ConceptType.THEORY,
            ),
            (
                "Forcing",
                "Method for proving independence results",
                ConceptType.THEORY,
            ),
            (
                "Cardinal Arithmetic",
                "Arithmetic of infinite numbers",
                ConceptType.THEORY,
            ),
            (
                "Ordinal Theory",
                "Study of well-ordered sets",
                ConceptType.THEORY,
            ),
            (
                "Constructive Set Theory",
                "Sets without excluded middle",
                ConceptType.THEORY,
            ),
            (
                "Fuzzy Set Theory",
                "Sets with degrees of membership",
                ConceptType.THEORY,
            ),
            (
                "Rough Set Theory",
                "Approximation of sets",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_set_operations(self) -> None:
        """Initialize set operations."""
        operations = [
            ("Union", "A ∪ B", "All elements in A or B", "Combination"),
            ("Intersection", "A ∩ B", "Elements in both A and B", "Common elements"),
            ("Complement", "A'", "Elements not in A", "Everything else"),
            ("Difference", "A - B", "Elements in A but not B", "Subtraction"),
            ("Symmetric Difference", "A △ B", "Elements in A or B but not both", "XOR"),
            ("Cartesian Product", "A × B", "All ordered pairs", "Pairing"),
            ("Power Set", "P(A)", "Set of all subsets", "2^n elements"),
        ]

        for name, symbol, description, meaning in operations:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "symbol": symbol,
                "meaning": meaning,
            })

    def initialize_set_relations(self) -> None:
        """Initialize set relations."""
        relations = [
            ("Subset", "A ⊆ B", "All elements of A are in B"),
            ("Proper Subset", "A ⊂ B", "Subset but not equal"),
            ("Superset", "A ⊇ B", "Contains all elements of B"),
            ("Equality", "A = B", "Same elements"),
            ("Disjoint", "A ∩ B = ∅", "No common elements"),
            ("Element of", "a ∈ A", "a is in set A"),
        ]

        for name, symbol, description in relations:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["symbol"] = symbol

    def initialize_cardinalities(self) -> None:
        """Initialize cardinality concepts."""
        cardinalities = [
            ("Finite", "Natural number", "Countable elements"),
            ("Countably Infinite", "ℵ₀ (aleph-null)", "Same as natural numbers"),
            ("Uncountably Infinite", "c (continuum)", "Same as real numbers"),
            ("Power of Continuum", "2^c", "Power set of reals"),
        ]

        for name, symbol, description in cardinalities:
            concept = self.create_concept(
                name=f"{name} Cardinality",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["symbol"] = symbol

    def initialize_function_types(self) -> None:
        """Initialize function types in set theory."""
        functions = [
            ("Injection", "One-to-one", "Different inputs give different outputs"),
            ("Surjection", "Onto", "Every element in codomain is hit"),
            ("Bijection", "One-to-one correspondence", "Both injection and surjection"),
            ("Relation", "Subset of Cartesian product", "Pairs of related elements"),
            ("Partial Function", "May be undefined", "Not all inputs mapped"),
            ("Choice Function", "Selects from each set", "Axiom of choice"),
        ]

        for name, alternative, description in functions:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["alternative_name"] = alternative

    def initialize_set_theory_pairs(self) -> None:
        """Initialize fundamental set theory pairs with META 50/50 balance."""
        pairs = [
            ("Element", "Set", "Member vs collection"),
            ("Subset", "Superset", "Contained vs containing"),
            ("Union", "Intersection", "Combined vs common"),
            ("Empty", "Universal", "Nothing vs everything"),
            ("Finite", "Infinite", "Countable vs uncountable"),
            ("Member", "Nonmember", "In vs out"),
            ("Proper", "Improper", "Strict vs equal"),
            ("Disjoint", "Overlapping", "Separate vs shared"),
            ("Complement", "Original", "Outside vs inside"),
            ("Singleton", "Pair", "One vs two elements"),
            ("Ordered", "Unordered", "Sequence vs collection"),
            ("Countable", "Uncountable", "Listable vs not"),
            ("Dense", "Sparse", "Packed vs spread"),
            ("Closed", "Open", "Includes vs excludes boundary"),
            ("Bounded", "Unbounded", "Limited vs unlimited"),
            ("Equivalent", "Inequivalent", "Same vs different size"),
            ("Cardinal", "Ordinal", "Size vs position"),
            ("Power Set", "Base Set", "All subsets vs original"),
            ("Partition", "Cover", "Non-overlapping vs overlapping"),
            ("Bijection", "Injection", "One-to-one onto vs into"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Set Theory)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Set Theory)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_set_identities(self) -> dict[str, str]:
        """Get important set identities."""
        return {
            "commutative_union": "A ∪ B = B ∪ A",
            "commutative_intersection": "A ∩ B = B ∩ A",
            "associative_union": "(A ∪ B) ∪ C = A ∪ (B ∪ C)",
            "associative_intersection": "(A ∩ B) ∩ C = A ∩ (B ∩ C)",
            "distributive_1": "A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)",
            "distributive_2": "A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)",
            "de_morgan_1": "(A ∪ B)' = A' ∩ B'",
            "de_morgan_2": "(A ∩ B)' = A' ∪ B'",
            "identity_union": "A ∪ ∅ = A",
            "identity_intersection": "A ∩ U = A",
        }

    def demonstrate_set_balance(self) -> dict[str, Any]:
        """Demonstrate set theory balance principles."""
        return {
            "concept": "Set Equilibrium",
            "dualities": {
                "element_set": {
                    "element": 50.0,
                    "set": 50.0,
                    "meaning": "Part and whole are complementary",
                },
                "union_intersection": {
                    "union": 50.0,
                    "intersection": 50.0,
                    "meaning": "De Morgan's laws show duality",
                },
                "member_complement": {
                    "in_set": 50.0,
                    "not_in_set": 50.0,
                    "meaning": "Every element is in A or A'",
                },
            },
            "cardinality_balance": {
                "finite": 50.0,
                "infinite": 50.0,
                "description": "Both finite and infinite sets exist",
            },
            "meta_meaning": "Set Theory demonstrates META 50/50 in membership duality",
        }


def create_set_theory_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> SetTheoryDomain:
    """
    Factory function to create a fully initialized set theory domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized SetTheoryDomain
    """
    domain = SetTheoryDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_set_operations()
        domain.initialize_set_relations()
        domain.initialize_cardinalities()
        domain.initialize_function_types()
        domain.initialize_set_theory_pairs()

    return domain
