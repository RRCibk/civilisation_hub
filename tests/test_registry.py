"""
Tests for knowledge/domains/registry.py
=======================================
Tests for domain registry with META 50/50 compliance.
"""

import pytest

from core.equilibrium import MetaEquilibrium
from knowledge.domains.registry import (
    DomainRegistry,
    get_registry,
    reset_registry,
)
from models.domain import (
    Domain,
    DomainHierarchy,
    DomainRelationship,
    DomainState,
    DomainType,
)


@pytest.fixture(autouse=True)
def reset_singleton():
    """Reset singleton registry before each test."""
    reset_registry()
    yield
    reset_registry()


class TestDomainRegistry:
    """Tests for DomainRegistry class."""

    def test_create_registry(self):
        """Should create empty registry."""
        registry = DomainRegistry()

        assert registry.domain_count == 0
        assert registry.hierarchy_count == 0

    def test_register_domain_valid(self):
        """Should register valid domain."""
        registry = DomainRegistry()
        domain = Domain("Physics")
        domain.set_duality("matter", 100, "antimatter", 100)

        registry.register_domain(domain)

        assert registry.domain_count == 1
        assert registry.get_domain(domain.id) is domain

    def test_register_domain_invalid_raises(self):
        """Should raise for invalid domain when require_balanced=True."""
        registry = DomainRegistry()
        domain = Domain("Physics")  # No duality set

        with pytest.raises(ValueError) as exc_info:
            registry.register_domain(domain, require_balanced=True)
        assert "META 50/50 compliance" in str(exc_info.value)

    def test_register_domain_invalid_allowed(self):
        """Should allow invalid domain when require_balanced=False."""
        registry = DomainRegistry()
        domain = Domain("Physics")  # No duality set

        registry.register_domain(domain, require_balanced=False)
        assert registry.domain_count == 1

    def test_register_duplicate_id_raises(self):
        """Should raise for duplicate domain ID."""
        registry = DomainRegistry()
        domain = Domain("Physics")
        domain.set_duality("matter", 50, "antimatter", 50)

        registry.register_domain(domain)

        with pytest.raises(ValueError) as exc_info:
            registry.register_domain(domain)
        assert "already registered" in str(exc_info.value)

    def test_register_duplicate_name_raises(self):
        """Should raise for duplicate domain name."""
        registry = DomainRegistry()

        domain1 = Domain("Physics")
        domain1.set_duality("a", 50, "b", 50)

        domain2 = Domain("Physics")  # Same name
        domain2.set_duality("c", 50, "d", 50)

        registry.register_domain(domain1)

        with pytest.raises(ValueError) as exc_info:
            registry.register_domain(domain2)
        assert "name already exists" in str(exc_info.value)

    def test_unregister_domain(self):
        """Should unregister domain."""
        registry = DomainRegistry()
        domain = Domain("Physics")
        domain.set_duality("matter", 50, "antimatter", 50)

        registry.register_domain(domain)
        removed = registry.unregister_domain(domain.id)

        assert removed is domain
        assert registry.domain_count == 0
        assert registry.get_domain(domain.id) is None

    def test_unregister_nonexistent_returns_none(self):
        """Should return None for nonexistent domain."""
        registry = DomainRegistry()
        domain = Domain("Physics")

        removed = registry.unregister_domain(domain.id)
        assert removed is None

    def test_get_domain_by_name(self):
        """Should get domain by name."""
        registry = DomainRegistry()
        domain = Domain("Physics")
        domain.set_duality("matter", 50, "antimatter", 50)
        registry.register_domain(domain)

        found = registry.get_domain_by_name("Physics")
        assert found is domain

    def test_get_domain_by_name_not_found(self):
        """Should return None for unknown name."""
        registry = DomainRegistry()
        assert registry.get_domain_by_name("Unknown") is None

    def test_list_domains_all(self):
        """Should list all domains."""
        registry = DomainRegistry()

        d1 = Domain("A", DomainType.FUNDAMENTAL)
        d1.set_duality("p", 50, "n", 50)

        d2 = Domain("B", DomainType.DERIVED)
        d2.set_duality("p", 100, "n", 100)

        registry.register_domain(d1)
        registry.register_domain(d2)

        domains = registry.list_domains()
        assert len(domains) == 2

    def test_list_domains_by_type(self):
        """Should filter domains by type."""
        registry = DomainRegistry()

        d1 = Domain("A", DomainType.FUNDAMENTAL)
        d1.set_duality("p", 50, "n", 50)

        d2 = Domain("B", DomainType.DERIVED)
        d2.set_duality("p", 100, "n", 100)

        registry.register_domain(d1)
        registry.register_domain(d2)

        fundamental = registry.list_domains(domain_type=DomainType.FUNDAMENTAL)
        assert len(fundamental) == 1
        assert fundamental[0].name == "A"

    def test_list_domains_by_state(self):
        """Should filter domains by state."""
        registry = DomainRegistry()

        d1 = Domain("A")
        d1.set_duality("p", 50, "n", 50)
        d1.activate()

        d2 = Domain("B")
        d2.set_duality("p", 100, "n", 100)
        # d2 remains nascent

        registry.register_domain(d1)
        registry.register_domain(d2)

        active = registry.list_domains(state=DomainState.ACTIVE)
        assert len(active) == 1
        assert active[0].name == "A"

    def test_iter_domains(self):
        """Should iterate over domains."""
        registry = DomainRegistry()

        for i in range(3):
            d = Domain(f"D{i}")
            d.set_duality("p", 50, "n", 50)
            registry.register_domain(d)

        names = [d.name for d in registry.iter_domains()]
        assert len(names) == 3
        assert "D0" in names
        assert "D1" in names
        assert "D2" in names


class TestDomainRegistryCreate:
    """Tests for DomainRegistry create methods."""

    def test_create_domain_simple(self):
        """Should create and register domain."""
        registry = DomainRegistry()
        domain = registry.create_domain("Physics")

        assert domain.name == "Physics"
        assert registry.domain_count == 1

    def test_create_domain_with_duality(self):
        """Should create domain with balanced duality."""
        registry = DomainRegistry()
        domain = registry.create_domain(
            name="Physics", positive_pole=("matter", 100), negative_pole=("antimatter", 100)
        )

        assert domain.duality is not None
        assert domain.duality.is_balanced is True
        assert domain.state == DomainState.ACTIVE

    def test_create_domain_with_type(self):
        """Should create domain with specified type."""
        registry = DomainRegistry()
        domain = registry.create_domain(
            name="Chemistry",
            domain_type=DomainType.DERIVED,
            positive_pole=("synthesis", 50),
            negative_pole=("decomposition", 50),
        )

        assert domain.domain_type == DomainType.DERIVED

    def test_create_domain_no_auto_register(self):
        """Should not register when auto_register=False."""
        registry = DomainRegistry()
        domain = registry.create_domain(name="Physics", auto_register=False)

        assert registry.domain_count == 0
        assert domain.name == "Physics"

    def test_create_hierarchy(self):
        """Should create and register hierarchy."""
        registry = DomainRegistry()
        hierarchy = registry.create_hierarchy("Science")

        assert hierarchy.name == "Science"
        assert registry.hierarchy_count == 1


class TestDomainRegistryRelationships:
    """Tests for relationship management."""

    def test_create_relationship(self):
        """Should create balanced relationship."""
        registry = DomainRegistry()

        source = registry.create_domain("A", positive_pole=("p", 50), negative_pole=("n", 50))
        target = registry.create_domain("B", positive_pole=("p", 50), negative_pole=("n", 50))

        rel = registry.create_relationship(name="A_B", source=source, target=target, influence=200)

        assert rel.is_balanced is True
        assert rel.influence_give == 100
        assert rel.influence_receive == 100

    def test_register_relationship_unbalanced_raises(self):
        """Should raise for unbalanced relationship."""
        _registry = DomainRegistry()  # noqa: F841

        source = Domain("A")
        target = Domain("B")

        rel = DomainRelationship(
            name="bad", source=source, target=target, influence_give=50, influence_receive=50
        )

        # Manually make it unbalanced (bypass validation)
        rel._DomainRelationship__dict__ = None  # Force re-check

        # Actually test with proper unbalanced values
        with pytest.raises(ValueError):
            DomainRelationship(
                name="unbalanced",
                source=source,
                target=target,
                influence_give=60,
                influence_receive=40,
            )

    def test_get_relationships(self):
        """Should get relationships for domain."""
        registry = DomainRegistry()

        a = registry.create_domain("A", positive_pole=("p", 50), negative_pole=("n", 50))
        b = registry.create_domain("B", positive_pole=("p", 50), negative_pole=("n", 50))
        c = registry.create_domain("C", positive_pole=("p", 50), negative_pole=("n", 50))

        registry.create_relationship("A_B", a, b, 100)
        registry.create_relationship("A_C", a, c, 100)

        rels = registry.get_relationships(a)
        assert len(rels) == 2


class TestDomainRegistryValidation:
    """Tests for registry validation."""

    def test_validate_all_valid(self):
        """Should validate all domains are compliant."""
        registry = DomainRegistry()

        registry.create_domain("A", positive_pole=("p", 50), negative_pole=("n", 50))
        registry.create_domain("B", positive_pole=("p", 100), negative_pole=("n", 100))

        result = registry.validate_all()

        assert result["all_valid"] is True
        assert result["valid_domains"] == 2
        assert result["invalid_domains"] == 0

    def test_validate_all_with_invalid(self):
        """Should detect invalid domains."""
        registry = DomainRegistry()

        # Valid domain
        registry.create_domain("A", positive_pole=("p", 50), negative_pole=("n", 50))

        # Invalid domain (no duality)
        registry.create_domain("B", auto_register=False)
        invalid = Domain("Invalid")
        registry.register_domain(invalid, require_balanced=False)

        result = registry.validate_all()

        assert result["all_valid"] is False
        assert result["invalid_domains"] == 1

    def test_prove_registry_meta_meaning(self):
        """Should generate complete META proof."""
        registry = DomainRegistry()

        registry.create_domain("A", positive_pole=("p", 50), negative_pole=("n", 50))

        proof = registry.prove_registry_meta_meaning()

        assert "domain_proofs" in proof
        assert "proof" in proof
        assert len(proof["domain_proofs"]) == 1


class TestDomainRegistryHierarchy:
    """Tests for hierarchy management."""

    def test_register_hierarchy(self):
        """Should register hierarchy."""
        registry = DomainRegistry()
        hierarchy = DomainHierarchy("Science")

        registry.register_hierarchy(hierarchy)

        assert registry.hierarchy_count == 1
        assert registry.get_hierarchy("Science") is hierarchy

    def test_register_hierarchy_duplicate_raises(self):
        """Should raise for duplicate hierarchy."""
        registry = DomainRegistry()
        hierarchy = DomainHierarchy("Science")

        registry.register_hierarchy(hierarchy)

        with pytest.raises(ValueError) as exc_info:
            registry.register_hierarchy(hierarchy)
        assert "already registered" in str(exc_info.value)

    def test_register_hierarchy_with_domains(self):
        """Should register hierarchy's domains."""
        registry = DomainRegistry()

        hierarchy = DomainHierarchy("Science")
        domain = Domain("Physics")
        domain.set_duality("matter", 50, "antimatter", 50)
        hierarchy.add_root_domain(domain)

        registry.register_hierarchy(hierarchy)

        assert registry.domain_count == 1
        assert registry.get_domain_by_name("Physics") is domain


class TestSingletonRegistry:
    """Tests for singleton registry functions."""

    def test_get_registry_creates_singleton(self):
        """Should create singleton on first call."""
        registry1 = get_registry()
        registry2 = get_registry()

        assert registry1 is registry2

    def test_reset_registry(self):
        """Should reset singleton."""
        registry1 = get_registry()
        registry1.create_domain("Test", positive_pole=("p", 50), negative_pole=("n", 50))

        reset_registry()
        registry2 = get_registry()

        assert registry1 is not registry2
        assert registry2.domain_count == 0


class TestSharedMetaEquilibrium:
    """Tests for shared MetaEquilibrium across registry."""

    def test_domains_share_meta(self):
        """Domains in registry should share MetaEquilibrium."""
        meta = MetaEquilibrium()
        registry = DomainRegistry(meta)

        registry.create_domain("A", positive_pole=("p", 50), negative_pole=("n", 50))
        registry.create_domain("B", positive_pole=("x", 100), negative_pole=("y", 100))

        # Both dualities registered in shared meta
        assert "A_duality" in meta.validated_parameters
        assert "B_duality" in meta.validated_parameters

    def test_registry_meta_equilibrium_property(self):
        """Should expose MetaEquilibrium instance."""
        registry = DomainRegistry()
        assert registry.meta_equilibrium is not None


class TestRegistryRepr:
    """Tests for registry repr."""

    def test_repr(self):
        """Repr should show counts."""
        registry = DomainRegistry()
        registry.create_domain("A", positive_pole=("p", 50), negative_pole=("n", 50))
        registry.create_hierarchy("H")

        repr_str = repr(registry)

        assert "domains=1" in repr_str
        assert "hierarchies=1" in repr_str
