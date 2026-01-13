"""
Tests for models/domain.py
==========================
Tests for knowledge domain models with META 50/50 validation.
"""

from uuid import UUID

import pytest

from core.equilibrium import MetaEquilibrium
from models.domain import (
    Domain,
    DomainAttribute,
    DomainDuality,
    DomainHierarchy,
    DomainPole,
    DomainRelationship,
    DomainState,
    DomainType,
)


class TestDomainType:
    """Tests for DomainType enum."""

    def test_all_types_exist(self):
        """All domain types should exist."""
        assert DomainType.FUNDAMENTAL.value == "fundamental"
        assert DomainType.DERIVED.value == "derived"
        assert DomainType.COMPOSITE.value == "composite"
        assert DomainType.EMERGENT.value == "emergent"

    def test_type_count(self):
        """Should have exactly 4 domain types."""
        assert len(DomainType) == 4


class TestDomainState:
    """Tests for DomainState enum."""

    def test_all_states_exist(self):
        """All domain states should exist."""
        assert DomainState.NASCENT.value == "nascent"
        assert DomainState.ACTIVE.value == "active"
        assert DomainState.EVOLVING.value == "evolving"
        assert DomainState.STABLE.value == "stable"
        assert DomainState.ARCHIVED.value == "archived"

    def test_state_count(self):
        """Should have exactly 5 domain states."""
        assert len(DomainState) == 5


class TestDomainPole:
    """Tests for DomainPole dataclass."""

    def test_create_pole(self):
        """Should create pole with correct values."""
        pole = DomainPole("positive", 100, "A positive pole")
        assert pole.name == "positive"
        assert pole.value == 100
        assert pole.description == "A positive pole"

    def test_pole_negative_value_raises(self):
        """Negative values should raise ValueError."""
        with pytest.raises(ValueError) as exc_info:
            DomainPole("bad", -10)
        assert "cannot be negative" in str(exc_info.value)

    def test_pole_zero_value_allowed(self):
        """Zero value should be allowed."""
        pole = DomainPole("zero", 0)
        assert pole.value == 0


class TestDomainDuality:
    """Tests for DomainDuality dataclass."""

    def test_create_balanced_duality(self):
        """Should create balanced duality."""
        positive = DomainPole("light", 50)
        negative = DomainPole("dark", 50)
        duality = DomainDuality(positive, negative, "light_dark")

        assert duality.positive.name == "light"
        assert duality.negative.name == "dark"
        assert duality.name == "light_dark"

    def test_is_balanced_true(self):
        """Equal values should be balanced."""
        duality = DomainDuality(DomainPole("a", 100), DomainPole("b", 100), "test")
        assert duality.is_balanced is True

    def test_is_balanced_false(self):
        """Unequal values should not be balanced."""
        duality = DomainDuality(DomainPole("a", 60), DomainPole("b", 40), "test")
        assert duality.is_balanced is False

    def test_balance_property(self):
        """Balance should return correct percentages."""
        duality = DomainDuality(DomainPole("a", 50), DomainPole("b", 50), "test")
        assert duality.balance == (50.0, 50.0)

    def test_total_energy(self):
        """Total energy should sum both poles."""
        duality = DomainDuality(DomainPole("a", 100), DomainPole("b", 100), "test")
        assert duality.total_energy == 200

    def test_validate_balanced_passes(self):
        """Balanced duality should pass validation."""
        duality = DomainDuality(DomainPole("a", 50), DomainPole("b", 50), "test")
        duality.validate()  # Should not raise

    def test_validate_unbalanced_raises(self):
        """Unbalanced duality should raise ValueError."""
        duality = DomainDuality(DomainPole("a", 60), DomainPole("b", 40), "test")
        with pytest.raises(ValueError) as exc_info:
            duality.validate()
        assert "violates META 50/50" in str(exc_info.value)

    def test_to_sub_parameter(self):
        """Should convert to SubParameter."""
        duality = DomainDuality(DomainPole("a", 100), DomainPole("b", 100), "test")
        param = duality.to_sub_parameter()
        assert param.name == "test"
        assert param.values == (100, 100)


class TestDomainAttribute:
    """Tests for DomainAttribute dataclass."""

    def test_create_attribute(self):
        """Should create attribute with 52/48 split."""
        attr = DomainAttribute("energy", 100, "Energy attribute")
        assert attr.name == "energy"
        assert attr.total_value == 100
        assert attr.description == "Energy attribute"

    def test_structure_is_52_percent(self):
        """Structure should be 52% of total."""
        attr = DomainAttribute("test", 100)
        assert attr.structure == 52

    def test_flexibility_is_48_percent(self):
        """Flexibility should be 48% of total."""
        attr = DomainAttribute("test", 100)
        assert attr.flexibility == 48

    def test_operational_ratio(self):
        """Should return valid OperationalRatio."""
        attr = DomainAttribute("test", 100)
        ratio = attr.operational_ratio
        assert ratio.structure == 52
        assert ratio.flexibility == 48

    def test_prove_operational(self):
        """Should return operational proof."""
        attr = DomainAttribute("energy", 1000)
        proof = attr.prove_operational()

        assert proof["name"] == "energy"
        assert proof["total"] == 1000
        assert proof["structure"] == 520
        assert proof["flexibility"] == 480
        assert proof["is_operational"] is True


class TestDomain:
    """Tests for Domain class."""

    def test_create_domain(self):
        """Should create domain with correct initial state."""
        domain = Domain("Physics", DomainType.FUNDAMENTAL, "Study of physics")

        assert domain.name == "Physics"
        assert domain.domain_type == DomainType.FUNDAMENTAL
        assert domain.description == "Study of physics"
        assert domain.state == DomainState.NASCENT
        assert isinstance(domain.id, UUID)

    def test_set_duality_balanced(self):
        """Should set balanced duality."""
        domain = Domain("Physics")
        domain.set_duality("matter", 100, "antimatter", 100)

        assert domain.duality is not None
        assert domain.duality.is_balanced is True

    def test_set_duality_unbalanced_raises(self):
        """Should raise for unbalanced duality."""
        domain = Domain("Physics")
        with pytest.raises(ValueError) as exc_info:
            domain.set_duality("matter", 60, "antimatter", 40)
        assert "violates META 50/50" in str(exc_info.value)

    def test_add_attribute(self):
        """Should add attribute with 52/48 split."""
        domain = Domain("Physics")
        attr = domain.add_attribute("energy", 1000, "Energy level")

        assert "energy" in domain.attributes
        assert attr.structure == 520
        assert attr.flexibility == 480

    def test_add_sub_domain(self):
        """Should add sub-domain."""
        parent = Domain("Science")
        child = Domain("Physics")
        parent.add_sub_domain(child)

        assert "Physics" in parent.sub_domains
        assert parent.sub_domains["Physics"] is child

    def test_activate_with_duality(self):
        """Should activate domain with valid duality."""
        domain = Domain("Physics")
        domain.set_duality("matter", 50, "antimatter", 50)
        domain.activate()

        assert domain.state == DomainState.ACTIVE

    def test_activate_without_duality_raises(self):
        """Should raise when activating without duality."""
        domain = Domain("Physics")
        with pytest.raises(ValueError) as exc_info:
            domain.activate()
        assert "no duality set" in str(exc_info.value)

    def test_stabilize_active_domain(self):
        """Should stabilize active domain."""
        domain = Domain("Physics")
        domain.set_duality("matter", 50, "antimatter", 50)
        domain.activate()
        domain.stabilize()

        assert domain.state == DomainState.STABLE

    def test_stabilize_nascent_raises(self):
        """Should raise when stabilizing nascent domain."""
        domain = Domain("Physics")
        with pytest.raises(ValueError) as exc_info:
            domain.stabilize()
        assert "must be active" in str(exc_info.value)

    def test_validate_meta_compliance_with_duality(self):
        """Should validate META compliance."""
        domain = Domain("Physics")
        domain.set_duality("matter", 100, "antimatter", 100)

        assert domain.validate_meta_compliance() is True

    def test_validate_meta_compliance_without_duality(self):
        """Should fail validation without duality."""
        domain = Domain("Physics")
        assert domain.validate_meta_compliance() is False

    def test_prove_meta_meaning(self):
        """Should return META proof."""
        domain = Domain("Physics", DomainType.FUNDAMENTAL)
        domain.set_duality("matter", 100, "antimatter", 100)
        domain.add_attribute("energy", 1000)

        proof = domain.prove_meta_meaning()

        assert proof["domain"] == "Physics"
        assert proof["type"] == "fundamental"
        assert proof["meta_valid"] is True
        assert proof["duality"]["is_balanced"] is True
        assert len(proof["attributes"]) == 1
        assert "proof" in proof

    def test_shared_meta_equilibrium(self):
        """Domains can share MetaEquilibrium."""
        meta = MetaEquilibrium()
        domain1 = Domain("A", meta_equilibrium=meta)
        domain2 = Domain("B", meta_equilibrium=meta)

        domain1.set_duality("p1", 50, "n1", 50)
        domain2.set_duality("p2", 100, "n2", 100)

        # Both registered in same meta
        assert "A_duality" in meta.validated_parameters
        assert "B_duality" in meta.validated_parameters

    def test_repr(self):
        """Repr should show name, type, and state."""
        domain = Domain("Physics", DomainType.FUNDAMENTAL)
        repr_str = repr(domain)

        assert "Physics" in repr_str
        assert "fundamental" in repr_str
        assert "nascent" in repr_str


class TestDomainRelationship:
    """Tests for DomainRelationship dataclass."""

    def test_create_balanced_relationship(self):
        """Should create balanced relationship."""
        source = Domain("A")
        target = Domain("B")

        rel = DomainRelationship(
            name="A_to_B", source=source, target=target, influence_give=50, influence_receive=50
        )

        assert rel.name == "A_to_B"
        assert rel.is_balanced is True

    def test_create_unbalanced_relationship_raises(self):
        """Should raise for unbalanced relationship."""
        source = Domain("A")
        target = Domain("B")

        with pytest.raises(ValueError) as exc_info:
            DomainRelationship(
                name="bad", source=source, target=target, influence_give=60, influence_receive=40
            )
        assert "violates META 50/50" in str(exc_info.value)

    def test_total_influence(self):
        """Should return total influence."""
        source = Domain("A")
        target = Domain("B")

        rel = DomainRelationship(
            name="test", source=source, target=target, influence_give=100, influence_receive=100
        )

        assert rel.total_influence == 200

    def test_prove_meta_meaning(self):
        """Should return META proof."""
        source = Domain("A")
        target = Domain("B")

        rel = DomainRelationship(
            name="test", source=source, target=target, influence_give=50, influence_receive=50
        )

        proof = rel.prove_meta_meaning()

        assert proof["name"] == "test"
        assert proof["source"] == "A"
        assert proof["target"] == "B"
        assert proof["is_balanced"] is True
        assert "proof" in proof


class TestDomainHierarchy:
    """Tests for DomainHierarchy class."""

    def test_create_hierarchy(self):
        """Should create empty hierarchy."""
        hierarchy = DomainHierarchy("Science")

        assert hierarchy.name == "Science"
        assert hierarchy.total_domains == 0

    def test_add_root_domain(self):
        """Should add root domain."""
        hierarchy = DomainHierarchy("Science")
        domain = Domain("Physics")
        domain.set_duality("matter", 50, "antimatter", 50)

        hierarchy.add_root_domain(domain)

        assert "Physics" in hierarchy.root_domains
        assert hierarchy.total_domains == 1

    def test_add_domain_with_sub_domains(self):
        """Should register domain and all sub-domains."""
        hierarchy = DomainHierarchy("Science")

        parent = Domain("Physics")
        parent.set_duality("matter", 50, "antimatter", 50)

        child = Domain("Quantum")
        child.set_duality("wave", 100, "particle", 100)
        parent.add_sub_domain(child)

        hierarchy.add_root_domain(parent)

        assert hierarchy.total_domains == 2

    def test_get_domain(self):
        """Should get domain by ID."""
        hierarchy = DomainHierarchy("Science")
        domain = Domain("Physics")
        domain.set_duality("matter", 50, "antimatter", 50)
        hierarchy.add_root_domain(domain)

        found = hierarchy.get_domain(domain.id)
        assert found is domain

    def test_get_domain_by_name(self):
        """Should get domain by name."""
        hierarchy = DomainHierarchy("Science")
        domain = Domain("Physics")
        domain.set_duality("matter", 50, "antimatter", 50)
        hierarchy.add_root_domain(domain)

        found = hierarchy.get_domain_by_name("Physics")
        assert found is domain

    def test_validate_hierarchy_all_valid(self):
        """Should validate all domains are META compliant."""
        hierarchy = DomainHierarchy("Science")

        physics = Domain("Physics")
        physics.set_duality("matter", 50, "antimatter", 50)

        chemistry = Domain("Chemistry")
        chemistry.set_duality("bond", 100, "break", 100)

        hierarchy.add_root_domain(physics)
        hierarchy.add_root_domain(chemistry)

        result = hierarchy.validate_hierarchy()

        assert result["all_valid"] is True
        assert result["total_domains"] == 2

    def test_prove_meta_meaning(self):
        """Should generate complete META proof."""
        hierarchy = DomainHierarchy("Science")
        domain = Domain("Physics")
        domain.set_duality("matter", 50, "antimatter", 50)
        hierarchy.add_root_domain(domain)

        proof = hierarchy.prove_meta_meaning()

        assert proof["hierarchy"] == "Science"
        assert "root_domain_proofs" in proof

    def test_repr(self):
        """Repr should show name and domain count."""
        hierarchy = DomainHierarchy("Science")
        repr_str = repr(hierarchy)

        assert "Science" in repr_str
        assert "domains=0" in repr_str
