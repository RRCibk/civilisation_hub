"""
Base Knowledge Domain
=====================
Base class for all knowledge domains.
Each domain maintains META 50/50 equilibrium in its structure.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, TypeVar
from uuid import UUID, uuid4

from core.equilibrium import MetaEquilibrium
from models.domain import Domain, DomainType

T = TypeVar("T")


class ConceptType(Enum):
    """Types of concepts within a domain."""

    AXIOM = "axiom"  # Fundamental truth
    THEOREM = "theorem"  # Proven statement
    HYPOTHESIS = "hypothesis"  # Unproven statement
    DEFINITION = "definition"  # Term definition
    PRINCIPLE = "principle"  # Guiding principle
    LAW = "law"  # Established law
    THEORY = "theory"  # Comprehensive theory
    MODEL = "model"  # Conceptual model


class RelationType(Enum):
    """Types of relationships between concepts."""

    DERIVES_FROM = "derives_from"
    IMPLIES = "implies"
    CONTRADICTS = "contradicts"
    SUPPORTS = "supports"
    EXTENDS = "extends"
    SPECIALIZES = "specializes"
    GENERALIZES = "generalizes"
    EQUIVALENT = "equivalent"


@dataclass
class Concept:
    """
    A concept within a knowledge domain.
    Concepts maintain balance between certainty and uncertainty.
    """

    id: UUID = field(default_factory=uuid4)
    name: str = ""
    concept_type: ConceptType = ConceptType.DEFINITION
    description: str = ""
    certainty: float = 50.0  # 0-100, balanced with uncertainty
    uncertainty: float = 50.0  # 0-100, balanced with certainty
    domain_id: UUID | None = None
    created_at: datetime = field(default_factory=datetime.now)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        self._meta = MetaEquilibrium()
        # Ensure certainty + uncertainty = 100
        total = self.certainty + self.uncertainty
        if total > 0:
            self.certainty = self.certainty / total * 100
            self.uncertainty = self.uncertainty / total * 100

    @property
    def is_balanced(self) -> bool:
        """Check if certainty/uncertainty is balanced."""
        return abs(self.certainty - 50.0) < 0.01

    @property
    def balance(self) -> tuple[float, float]:
        """Get certainty/uncertainty balance."""
        return (self.certainty, self.uncertainty)

    def adjust_certainty(self, delta: float) -> None:
        """Adjust certainty (uncertainty adjusts inversely)."""
        self.certainty = max(0, min(100, self.certainty + delta))
        self.uncertainty = 100 - self.certainty


@dataclass
class ConceptRelation:
    """Relationship between two concepts."""

    id: UUID = field(default_factory=uuid4)
    source_id: UUID = field(default_factory=uuid4)
    target_id: UUID = field(default_factory=uuid4)
    relation_type: RelationType = RelationType.DERIVES_FROM
    strength: float = 50.0  # Relationship strength (0-100)
    bidirectional: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)


class KnowledgeDomain(ABC):
    """
    Abstract base class for knowledge domains.
    All domains must define their fundamental duality and maintain META 50/50.
    """

    def __init__(
        self,
        name: str,
        domain_type: DomainType = DomainType.FUNDAMENTAL,
        description: str = "",
        meta_equilibrium: MetaEquilibrium | None = None,
    ):
        self._id = uuid4()
        self._name = name
        self._type = domain_type
        self._description = description
        self._meta = meta_equilibrium or MetaEquilibrium()

        # Initialize domain model
        self._domain = Domain(name, domain_type, description, self._meta)

        # Storage
        self._concepts: dict[UUID, Concept] = {}
        self._relations: dict[UUID, ConceptRelation] = {}
        self._axioms: list[Concept] = []

        # Initialize domain-specific content
        self._initialize_duality()
        self._initialize_axioms()

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def domain_type(self) -> DomainType:
        return self._type

    @property
    def description(self) -> str:
        return self._description

    @property
    def domain(self) -> Domain:
        return self._domain

    @property
    def concept_count(self) -> int:
        return len(self._concepts)

    @property
    def axiom_count(self) -> int:
        return len(self._axioms)

    @abstractmethod
    def _initialize_duality(self) -> None:
        """Initialize the domain's fundamental duality. Must be implemented."""
        pass

    @abstractmethod
    def _initialize_axioms(self) -> None:
        """Initialize domain axioms. Must be implemented."""
        pass

    @abstractmethod
    def get_fundamental_concepts(self) -> list[str]:
        """Get list of fundamental concept names for this domain."""
        pass

    def add_concept(self, concept: Concept) -> None:
        """Add a concept to the domain."""
        concept.domain_id = self._id
        self._concepts[concept.id] = concept
        if concept.concept_type == ConceptType.AXIOM:
            self._axioms.append(concept)

    def get_concept(self, concept_id: UUID) -> Concept | None:
        """Get a concept by ID."""
        return self._concepts.get(concept_id)

    def get_concept_by_name(self, name: str) -> Concept | None:
        """Get a concept by name."""
        for concept in self._concepts.values():
            if concept.name.lower() == name.lower():
                return concept
        return None

    def add_relation(self, relation: ConceptRelation) -> None:
        """Add a relation between concepts."""
        self._relations[relation.id] = relation

    def get_relations(self, concept_id: UUID) -> list[ConceptRelation]:
        """Get all relations involving a concept."""
        return [
            r
            for r in self._relations.values()
            if r.source_id == concept_id or r.target_id == concept_id
        ]

    def create_concept(
        self, name: str, concept_type: ConceptType, description: str = "", certainty: float = 50.0
    ) -> Concept:
        """Create and add a concept."""
        concept = Concept(
            name=name,
            concept_type=concept_type,
            description=description,
            certainty=certainty,
            uncertainty=100 - certainty,
        )
        self.add_concept(concept)
        return concept

    def create_relation(
        self,
        source: Concept | UUID,
        target: Concept | UUID,
        relation_type: RelationType,
        strength: float = 50.0,
    ) -> ConceptRelation:
        """Create and add a relation."""
        source_id = source.id if isinstance(source, Concept) else source
        target_id = target.id if isinstance(target, Concept) else target

        relation = ConceptRelation(
            source_id=source_id, target_id=target_id, relation_type=relation_type, strength=strength
        )
        self.add_relation(relation)
        return relation

    def validate_balance(self) -> bool:
        """Validate domain maintains META 50/50."""
        if self._domain.duality is None:
            return False
        return self._domain.duality.is_balanced

    def get_domain_stats(self) -> dict[str, Any]:
        """Get domain statistics."""
        concepts_by_type: dict[str, int] = {}
        for concept in self._concepts.values():
            t = concept.concept_type.value
            concepts_by_type[t] = concepts_by_type.get(t, 0) + 1

        avg_certainty = 0.0
        if self._concepts:
            avg_certainty = sum(c.certainty for c in self._concepts.values()) / len(self._concepts)

        return {
            "name": self._name,
            "type": self._type.value,
            "concepts": self.concept_count,
            "axioms": self.axiom_count,
            "relations": len(self._relations),
            "concepts_by_type": concepts_by_type,
            "average_certainty": avg_certainty,
            "balanced": self.validate_balance(),
        }

    def prove_meta_meaning(self) -> dict[str, Any]:
        """Generate META proof for the domain."""
        stats = self.get_domain_stats()
        duality_proof = None

        if self._domain.duality:
            duality_proof = {
                "positive": self._domain.duality.positive.name,
                "negative": self._domain.duality.negative.name,
                "balanced": self._domain.duality.is_balanced,
                "balance": self._domain.duality.balance,
            }

        return {
            "domain": self._name,
            "statistics": stats,
            "duality": duality_proof,
            "meta_valid": self.validate_balance(),
            "proof": (
                f"Domain '{self._name}' maintains META 50/50 equilibrium"
                if self.validate_balance()
                else f"Domain '{self._name}' requires balance adjustment"
            ),
        }

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._name}, concepts={self.concept_count})"
