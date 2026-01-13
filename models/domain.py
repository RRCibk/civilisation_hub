"""
Knowledge Domain Models
=======================
Models for representing knowledge domains with META 50/50 balance.
Each domain maintains equilibrium between complementary aspects.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any
from uuid import UUID, uuid4

from core.equilibrium import MetaEquilibrium, SubParameter
from core.proportions import (
    Ratio,
    OperationalRatio,
    ProportionValidator,
    calculate_52_48,
)


class DomainType(Enum):
    """Types of knowledge domains."""
    FUNDAMENTAL = "fundamental"      # Core/base domains
    DERIVED = "derived"              # Domains derived from fundamentals
    COMPOSITE = "composite"          # Domains combining multiple others
    EMERGENT = "emergent"            # Domains emerging from interactions


class DomainState(Enum):
    """States a domain can be in."""
    NASCENT = "nascent"              # Newly created, not yet balanced
    ACTIVE = "active"                # Actively balanced and operational
    EVOLVING = "evolving"            # Undergoing transformation
    STABLE = "stable"                # Reached equilibrium state
    ARCHIVED = "archived"            # No longer active but preserved


@dataclass
class DomainPole:
    """
    Represents one pole of a domain's duality.
    Every domain has complementary poles that must balance at META 50/50.
    """
    name: str
    value: float
    description: str = ""

    def __post_init__(self):
        if self.value < 0:
            raise ValueError(f"Pole value cannot be negative: {self.name}")


@dataclass
class DomainDuality:
    """
    The fundamental duality of a knowledge domain.
    Positive and negative poles must maintain META 50/50 balance.
    """
    positive: DomainPole
    negative: DomainPole
    name: str = "duality"

    def __post_init__(self):
        self._meta = MetaEquilibrium()

    @property
    def is_balanced(self) -> bool:
        """Check if duality maintains META 50/50."""
        return self._meta.verify_balance(self.positive.value, self.negative.value)

    @property
    def balance(self) -> tuple[float, float]:
        """Get current balance ratio."""
        return self._meta.calculate_balance(self.positive.value, self.negative.value)

    @property
    def total_energy(self) -> float:
        """Total energy in the duality."""
        return self.positive.value + self.negative.value

    def validate(self) -> None:
        """Validate duality maintains META 50/50. Raises if not."""
        if not self.is_balanced:
            balance = self.balance
            raise ValueError(
                f"Duality '{self.name}' violates META 50/50: "
                f"{self.positive.name}={balance[0]:.2f}% / "
                f"{self.negative.name}={balance[1]:.2f}%"
            )

    def to_sub_parameter(self, meta: MetaEquilibrium | None = None) -> SubParameter:
        """Convert to SubParameter for registration."""
        return SubParameter(
            self.name,
            self.positive.value,
            self.negative.value,
            meta
        )


@dataclass
class DomainAttribute:
    """
    An attribute of a knowledge domain.
    Attributes have structure/flexibility distribution (52/48).
    """
    name: str
    total_value: float
    description: str = ""

    def __post_init__(self):
        self._structure, self._flexibility = calculate_52_48(self.total_value)

    @property
    def structure(self) -> float:
        """Structural component (52%)."""
        return self._structure

    @property
    def flexibility(self) -> float:
        """Flexible component (48%)."""
        return self._flexibility

    @property
    def operational_ratio(self) -> OperationalRatio:
        """Get as OperationalRatio."""
        return OperationalRatio(self._structure, self._flexibility)

    def prove_operational(self) -> dict[str, Any]:
        """Prove attribute maintains 52/48 operational ratio."""
        return {
            "name": self.name,
            "total": self.total_value,
            "structure": self._structure,
            "flexibility": self._flexibility,
            "ratio": f"{self._structure / self.total_value * 100:.0f}/{self._flexibility / self.total_value * 100:.0f}",
            "is_operational": True
        }


class Domain:
    """
    A knowledge domain with META 50/50 balance.

    Each domain contains:
    - A fundamental duality (positive/negative poles at 50/50)
    - Attributes operating at 52/48 (structure/flexibility)
    - Relationships to other domains
    """

    def __init__(
        self,
        name: str,
        domain_type: DomainType = DomainType.FUNDAMENTAL,
        description: str = "",
        meta_equilibrium: MetaEquilibrium | None = None
    ):
        self._id: UUID = uuid4()
        self._name = name
        self._type = domain_type
        self._description = description
        self._state = DomainState.NASCENT
        self._meta = meta_equilibrium or MetaEquilibrium()
        self._validator = ProportionValidator(self._meta)

        self._duality: DomainDuality | None = None
        self._attributes: dict[str, DomainAttribute] = {}
        self._sub_domains: dict[str, "Domain"] = {}
        self._relationships: dict[str, "DomainRelationship"] = {}

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
    def state(self) -> DomainState:
        return self._state

    @property
    def duality(self) -> DomainDuality | None:
        return self._duality

    @property
    def attributes(self) -> dict[str, DomainAttribute]:
        return self._attributes.copy()

    @property
    def sub_domains(self) -> dict[str, "Domain"]:
        return self._sub_domains.copy()

    def set_duality(
        self,
        positive_name: str,
        positive_value: float,
        negative_name: str,
        negative_value: float,
        duality_name: str | None = None
    ) -> None:
        """
        Set the domain's fundamental duality.
        Values must maintain META 50/50 balance.
        """
        positive = DomainPole(positive_name, positive_value)
        negative = DomainPole(negative_name, negative_value)
        duality = DomainDuality(
            positive=positive,
            negative=negative,
            name=duality_name or f"{self._name}_duality"
        )
        duality.validate()  # Raises if not balanced
        self._duality = duality
        self._meta.register_parameter(
            duality.name,
            positive_value,
            negative_value
        )

    def add_attribute(self, name: str, value: float, description: str = "") -> DomainAttribute:
        """
        Add an attribute to the domain.
        Attributes are automatically distributed at 52/48.
        """
        attr = DomainAttribute(name, value, description)
        self._attributes[name] = attr
        return attr

    def add_sub_domain(self, domain: "Domain") -> None:
        """Add a sub-domain to this domain."""
        self._sub_domains[domain.name] = domain

    def add_relationship(self, relationship: "DomainRelationship") -> None:
        """Add a relationship to another domain."""
        self._relationships[relationship.name] = relationship

    def activate(self) -> None:
        """
        Activate the domain. Requires valid duality.
        """
        if self._duality is None:
            raise ValueError(f"Domain '{self._name}' has no duality set")
        if not self._duality.is_balanced:
            raise ValueError(f"Domain '{self._name}' duality is not balanced")
        self._state = DomainState.ACTIVE

    def stabilize(self) -> None:
        """Mark domain as stable after reaching equilibrium."""
        if self._state != DomainState.ACTIVE:
            raise ValueError("Domain must be active before stabilizing")
        self._state = DomainState.STABLE

    def validate_meta_compliance(self) -> bool:
        """Check if domain maintains META 50/50."""
        if self._duality is None:
            return False
        return self._duality.is_balanced

    def prove_meta_meaning(self) -> dict[str, Any]:
        """
        Generate proof that domain maintains META 50/50 meaning.
        """
        duality_proof = None
        if self._duality:
            balance = self._duality.balance
            duality_proof = {
                "name": self._duality.name,
                "positive": {
                    "name": self._duality.positive.name,
                    "value": self._duality.positive.value,
                    "percentage": balance[0]
                },
                "negative": {
                    "name": self._duality.negative.name,
                    "value": self._duality.negative.value,
                    "percentage": balance[1]
                },
                "is_balanced": self._duality.is_balanced
            }

        attributes_proof = [
            attr.prove_operational()
            for attr in self._attributes.values()
        ]

        sub_domains_valid = all(
            sd.validate_meta_compliance()
            for sd in self._sub_domains.values()
        )

        return {
            "domain": self._name,
            "type": self._type.value,
            "state": self._state.value,
            "meta_valid": self.validate_meta_compliance(),
            "duality": duality_proof,
            "attributes": attributes_proof,
            "sub_domains_count": len(self._sub_domains),
            "sub_domains_valid": sub_domains_valid,
            "proof": (
                f"Domain '{self._name}' maintains META 50/50 equilibrium"
                if self.validate_meta_compliance()
                else f"Domain '{self._name}' violates META 50/50"
            )
        }

    def __repr__(self) -> str:
        return (
            f"Domain({self._name}, type={self._type.value}, "
            f"state={self._state.value})"
        )


@dataclass
class DomainRelationship:
    """
    Relationship between two domains.
    Relationships must maintain META 50/50 in their influence.
    """
    name: str
    source: Domain
    target: Domain
    influence_give: float
    influence_receive: float
    relationship_type: str = "bidirectional"

    def __post_init__(self):
        self._meta = MetaEquilibrium()
        self._validate()

    def _validate(self) -> None:
        """Validate relationship maintains META 50/50."""
        if not self._meta.verify_balance(self.influence_give, self.influence_receive):
            balance = self._meta.calculate_balance(
                self.influence_give,
                self.influence_receive
            )
            raise ValueError(
                f"Relationship '{self.name}' violates META 50/50: "
                f"give={balance[0]:.2f}% / receive={balance[1]:.2f}%"
            )

    @property
    def is_balanced(self) -> bool:
        """Check if relationship is balanced."""
        return self._meta.verify_balance(self.influence_give, self.influence_receive)

    @property
    def total_influence(self) -> float:
        """Total influence in the relationship."""
        return self.influence_give + self.influence_receive

    def prove_meta_meaning(self) -> dict[str, Any]:
        """Prove relationship maintains META 50/50."""
        balance = self._meta.calculate_balance(
            self.influence_give,
            self.influence_receive
        )
        return {
            "name": self.name,
            "source": self.source.name,
            "target": self.target.name,
            "type": self.relationship_type,
            "give": self.influence_give,
            "receive": self.influence_receive,
            "balance": f"{balance[0]:.2f}/{balance[1]:.2f}",
            "is_balanced": self.is_balanced,
            "proof": "Relationship maintains META 50/50 equilibrium"
        }


class DomainHierarchy:
    """
    A hierarchy of knowledge domains.
    The hierarchy itself maintains META 50/50 between levels.
    """

    def __init__(self, name: str, meta_equilibrium: MetaEquilibrium | None = None):
        self._name = name
        self._meta = meta_equilibrium or MetaEquilibrium()
        self._root_domains: dict[str, Domain] = {}
        self._all_domains: dict[UUID, Domain] = {}

    @property
    def name(self) -> str:
        return self._name

    @property
    def root_domains(self) -> dict[str, Domain]:
        return self._root_domains.copy()

    @property
    def total_domains(self) -> int:
        return len(self._all_domains)

    def add_root_domain(self, domain: Domain) -> None:
        """Add a root-level domain to the hierarchy."""
        self._root_domains[domain.name] = domain
        self._register_domain(domain)

    def _register_domain(self, domain: Domain) -> None:
        """Register a domain and all its sub-domains."""
        self._all_domains[domain.id] = domain
        for sub in domain.sub_domains.values():
            self._register_domain(sub)

    def get_domain(self, domain_id: UUID) -> Domain | None:
        """Get a domain by ID."""
        return self._all_domains.get(domain_id)

    def get_domain_by_name(self, name: str) -> Domain | None:
        """Get a domain by name (searches all domains)."""
        for domain in self._all_domains.values():
            if domain.name == name:
                return domain
        return None

    def validate_hierarchy(self) -> dict[str, Any]:
        """Validate entire hierarchy maintains META 50/50."""
        all_valid = True
        domain_reports = []

        for domain in self._all_domains.values():
            is_valid = domain.validate_meta_compliance()
            all_valid = all_valid and is_valid
            domain_reports.append({
                "name": domain.name,
                "valid": is_valid,
                "state": domain.state.value
            })

        return {
            "hierarchy": self._name,
            "total_domains": self.total_domains,
            "root_domains": len(self._root_domains),
            "all_valid": all_valid,
            "domains": domain_reports,
            "proof": (
                f"Hierarchy '{self._name}' maintains META 50/50"
                if all_valid
                else f"Hierarchy '{self._name}' has invalid domains"
            )
        }

    def prove_meta_meaning(self) -> dict[str, Any]:
        """Generate complete META proof for hierarchy."""
        validation = self.validate_hierarchy()
        root_proofs = [
            domain.prove_meta_meaning()
            for domain in self._root_domains.values()
        ]

        return {
            **validation,
            "root_domain_proofs": root_proofs
        }

    def __repr__(self) -> str:
        return f"DomainHierarchy({self._name}, domains={self.total_domains})"
