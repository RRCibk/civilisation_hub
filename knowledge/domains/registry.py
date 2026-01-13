"""
Knowledge Domain Registry
=========================
Central registry for managing knowledge domains.
Ensures all registered domains maintain META 50/50 compliance.
"""

from collections.abc import Iterator
from typing import Any
from uuid import UUID

from core.equilibrium import MetaEquilibrium
from core.proportions import ProportionValidator
from models.domain import (
    Domain,
    DomainHierarchy,
    DomainRelationship,
    DomainState,
    DomainType,
)


class DomainRegistry:
    """
    Central registry for knowledge domains.
    All domains must validate META 50/50 compliance before registration.
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        self._meta = meta_equilibrium or MetaEquilibrium()
        self._validator = ProportionValidator(self._meta)
        self._domains: dict[UUID, Domain] = {}
        self._domains_by_name: dict[str, Domain] = {}
        self._hierarchies: dict[str, DomainHierarchy] = {}
        self._relationships: list[DomainRelationship] = []

    @property
    def meta_equilibrium(self) -> MetaEquilibrium:
        """Get the shared MetaEquilibrium instance."""
        return self._meta

    @property
    def domain_count(self) -> int:
        """Total number of registered domains."""
        return len(self._domains)

    @property
    def hierarchy_count(self) -> int:
        """Total number of hierarchies."""
        return len(self._hierarchies)

    def register_domain(self, domain: Domain, require_balanced: bool = True) -> None:
        """
        Register a domain in the registry.

        Args:
            domain: The domain to register
            require_balanced: If True, domain must have balanced duality

        Raises:
            ValueError: If domain is invalid or already registered
        """
        if domain.id in self._domains:
            raise ValueError(f"Domain already registered: {domain.name}")

        if domain.name in self._domains_by_name:
            raise ValueError(f"Domain name already exists: {domain.name}")

        if require_balanced and not domain.validate_meta_compliance():
            raise ValueError(f"Domain '{domain.name}' does not maintain META 50/50 compliance")

        self._domains[domain.id] = domain
        self._domains_by_name[domain.name] = domain

    def unregister_domain(self, domain_id: UUID) -> Domain | None:
        """
        Remove a domain from the registry.

        Args:
            domain_id: UUID of the domain to remove

        Returns:
            The removed domain, or None if not found
        """
        domain = self._domains.pop(domain_id, None)
        if domain:
            self._domains_by_name.pop(domain.name, None)
        return domain

    def get_domain(self, domain_id: UUID) -> Domain | None:
        """Get a domain by its UUID."""
        return self._domains.get(domain_id)

    def get_domain_by_name(self, name: str) -> Domain | None:
        """Get a domain by its name."""
        return self._domains_by_name.get(name)

    def list_domains(
        self, domain_type: DomainType | None = None, state: DomainState | None = None
    ) -> list[Domain]:
        """
        List domains, optionally filtered by type and/or state.

        Args:
            domain_type: Filter by domain type
            state: Filter by domain state

        Returns:
            List of matching domains
        """
        domains = list(self._domains.values())

        if domain_type is not None:
            domains = [d for d in domains if d.domain_type == domain_type]

        if state is not None:
            domains = [d for d in domains if d.state == state]

        return domains

    def iter_domains(self) -> Iterator[Domain]:
        """Iterate over all registered domains."""
        return iter(self._domains.values())

    def create_domain(
        self,
        name: str,
        domain_type: DomainType = DomainType.FUNDAMENTAL,
        description: str = "",
        positive_pole: tuple[str, float] | None = None,
        negative_pole: tuple[str, float] | None = None,
        auto_register: bool = True,
    ) -> Domain:
        """
        Create a new domain with optional duality.

        Args:
            name: Domain name
            domain_type: Type of domain
            description: Domain description
            positive_pole: Tuple of (name, value) for positive pole
            negative_pole: Tuple of (name, value) for negative pole
            auto_register: If True, automatically register the domain

        Returns:
            The created domain
        """
        domain = Domain(
            name=name, domain_type=domain_type, description=description, meta_equilibrium=self._meta
        )

        if positive_pole and negative_pole:
            domain.set_duality(
                positive_name=positive_pole[0],
                positive_value=positive_pole[1],
                negative_name=negative_pole[0],
                negative_value=negative_pole[1],
            )
            domain.activate()

        if auto_register:
            require_balanced = positive_pole is not None and negative_pole is not None
            self.register_domain(domain, require_balanced=require_balanced)

        return domain

    def register_hierarchy(self, hierarchy: DomainHierarchy) -> None:
        """Register a domain hierarchy."""
        if hierarchy.name in self._hierarchies:
            raise ValueError(f"Hierarchy already registered: {hierarchy.name}")
        self._hierarchies[hierarchy.name] = hierarchy

        # Register all domains in the hierarchy
        for domain in hierarchy.root_domains.values():
            if domain.id not in self._domains:
                self.register_domain(domain, require_balanced=False)

    def get_hierarchy(self, name: str) -> DomainHierarchy | None:
        """Get a hierarchy by name."""
        return self._hierarchies.get(name)

    def create_hierarchy(self, name: str) -> DomainHierarchy:
        """Create and register a new hierarchy."""
        hierarchy = DomainHierarchy(name, self._meta)
        self.register_hierarchy(hierarchy)
        return hierarchy

    def register_relationship(self, relationship: DomainRelationship) -> None:
        """
        Register a relationship between domains.
        Relationship must maintain META 50/50.
        """
        if not relationship.is_balanced:
            raise ValueError(f"Relationship '{relationship.name}' does not maintain META 50/50")
        self._relationships.append(relationship)

    def create_relationship(
        self,
        name: str,
        source: Domain,
        target: Domain,
        influence: float,
        relationship_type: str = "bidirectional",
    ) -> DomainRelationship:
        """
        Create a balanced relationship between domains.
        Influence is automatically balanced (50/50 give/receive).

        Args:
            name: Relationship name
            source: Source domain
            target: Target domain
            influence: Total influence (split 50/50)
            relationship_type: Type of relationship

        Returns:
            The created relationship
        """
        half = influence / 2
        relationship = DomainRelationship(
            name=name,
            source=source,
            target=target,
            influence_give=half,
            influence_receive=half,
            relationship_type=relationship_type,
        )
        self.register_relationship(relationship)
        source.add_relationship(relationship)
        return relationship

    def get_relationships(self, domain: Domain) -> list[DomainRelationship]:
        """Get all relationships involving a domain."""
        return [
            r for r in self._relationships if r.source.id == domain.id or r.target.id == domain.id
        ]

    def validate_all(self) -> dict[str, Any]:
        """
        Validate all registered domains maintain META 50/50.

        Returns:
            Validation report for all domains
        """
        valid_count = 0
        invalid_count = 0
        domain_reports = []

        for domain in self._domains.values():
            is_valid = domain.validate_meta_compliance()
            if is_valid:
                valid_count += 1
            else:
                invalid_count += 1

            domain_reports.append(
                {
                    "name": domain.name,
                    "type": domain.domain_type.value,
                    "state": domain.state.value,
                    "meta_valid": is_valid,
                }
            )

        relationship_reports = [
            {"name": r.name, "balanced": r.is_balanced} for r in self._relationships
        ]

        return {
            "total_domains": self.domain_count,
            "valid_domains": valid_count,
            "invalid_domains": invalid_count,
            "all_valid": invalid_count == 0,
            "domains": domain_reports,
            "relationships": relationship_reports,
            "hierarchies": list(self._hierarchies.keys()),
        }

    def prove_registry_meta_meaning(self) -> dict[str, Any]:
        """Generate META proof for entire registry."""
        validation = self.validate_all()

        domain_proofs = [domain.prove_meta_meaning() for domain in self._domains.values()]

        hierarchy_proofs = [h.prove_meta_meaning() for h in self._hierarchies.values()]

        relationship_proofs = [r.prove_meta_meaning() for r in self._relationships]

        return {
            **validation,
            "domain_proofs": domain_proofs,
            "hierarchy_proofs": hierarchy_proofs,
            "relationship_proofs": relationship_proofs,
            "proof": (
                "Registry maintains META 50/50 equilibrium"
                if validation["all_valid"]
                else "Registry contains domains violating META 50/50"
            ),
        }

    def __repr__(self) -> str:
        return f"DomainRegistry(domains={self.domain_count}, hierarchies={self.hierarchy_count})"


# Singleton registry instance
_default_registry: DomainRegistry | None = None


def get_registry() -> DomainRegistry:
    """Get the default domain registry singleton."""
    global _default_registry
    if _default_registry is None:
        _default_registry = DomainRegistry()
    return _default_registry


def reset_registry() -> None:
    """Reset the default registry (mainly for testing)."""
    global _default_registry
    _default_registry = None
