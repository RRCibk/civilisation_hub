"""
Tests for core/equilibrium.py
=============================
Validates META 50/50 principle and OPERATIONAL 52/48 ratio.
"""

import pytest
from core.equilibrium import (
    MetaEquilibrium,
    Atom,
    AtomState,
    SubParameter,
    WaveState,
)


class TestMetaEquilibrium:
    """Tests for MetaEquilibrium class."""

    def test_meta_ratio_is_50_50(self):
        """META ratio must be exactly 50/50."""
        assert MetaEquilibrium.META_RATIO == (50, 50)

    def test_tolerance_is_zero(self):
        """META level allows no deviation."""
        assert MetaEquilibrium.TOLERANCE == 0.0

    def test_verify_balance_exact_50_50(self):
        """Exact 50/50 values should pass verification."""
        assert MetaEquilibrium.verify_balance(50, 50) is True
        assert MetaEquilibrium.verify_balance(1, 1) is True
        assert MetaEquilibrium.verify_balance(0.5, 0.5) is True
        assert MetaEquilibrium.verify_balance(1000, 1000) is True

    def test_verify_balance_rejects_imbalance(self):
        """Any deviation from 50/50 should fail."""
        assert MetaEquilibrium.verify_balance(51, 49) is False
        assert MetaEquilibrium.verify_balance(52, 48) is False
        assert MetaEquilibrium.verify_balance(60, 40) is False
        assert MetaEquilibrium.verify_balance(1, 2) is False

    def test_verify_balance_empty_state(self):
        """Empty state (0, 0) is considered balanced."""
        assert MetaEquilibrium.verify_balance(0, 0) is True

    def test_calculate_balance_exact(self):
        """Calculate balance returns correct ratios."""
        assert MetaEquilibrium.calculate_balance(50, 50) == (50.0, 50.0)
        assert MetaEquilibrium.calculate_balance(1, 1) == (50.0, 50.0)

    def test_calculate_balance_imbalanced(self):
        """Calculate balance shows actual ratios for imbalanced values."""
        assert MetaEquilibrium.calculate_balance(60, 40) == (60.0, 40.0)
        assert MetaEquilibrium.calculate_balance(75, 25) == (75.0, 25.0)

    def test_calculate_balance_empty(self):
        """Empty state returns 50/50."""
        assert MetaEquilibrium.calculate_balance(0, 0) == (50.0, 50.0)

    def test_register_parameter_valid(self):
        """Valid parameters should register successfully."""
        meta = MetaEquilibrium()
        assert meta.register_parameter("test", 100, 100) is True
        assert "test" in meta.validated_parameters

    def test_register_parameter_invalid_raises(self):
        """Invalid parameters should raise ValueError."""
        meta = MetaEquilibrium()
        with pytest.raises(ValueError) as exc_info:
            meta.register_parameter("bad_param", 60, 40)
        assert "violates META 50/50" in str(exc_info.value)
        assert "bad_param" in str(exc_info.value)

    def test_validated_parameters_immutable(self):
        """validated_parameters returns a copy, not the original."""
        meta = MetaEquilibrium()
        meta.register_parameter("test", 50, 50)
        params = meta.validated_parameters
        params["hacked"] = (100, 0)
        assert "hacked" not in meta.validated_parameters

    def test_validate_operational_enables_meta_correct_ratio(self):
        """52/48 operational ratio should validate."""
        meta = MetaEquilibrium()
        assert meta.validate_operational_enables_meta(52, 48) is True
        assert meta.validate_operational_enables_meta(0.52, 0.48) is True
        assert meta.validate_operational_enables_meta(520, 480) is True

    def test_validate_operational_enables_meta_wrong_ratio(self):
        """Non-52/48 ratios should fail."""
        meta = MetaEquilibrium()
        assert meta.validate_operational_enables_meta(50, 50) is False
        assert meta.validate_operational_enables_meta(60, 40) is False

    def test_validate_operational_empty_fails(self):
        """Empty operational values should fail."""
        meta = MetaEquilibrium()
        assert meta.validate_operational_enables_meta(0, 0) is False


class TestAtomState:
    """Tests for AtomState dataclass."""

    def test_create_valid_state(self):
        """Valid states should be created successfully."""
        state = AtomState(w_minus=0.5, w_zero=0.0, w_plus=0.5)
        assert state.w_minus == 0.5
        assert state.w_zero == 0.0
        assert state.w_plus == 0.5

    def test_negative_values_rejected(self):
        """Negative state values should raise ValueError."""
        with pytest.raises(ValueError) as exc_info:
            AtomState(w_minus=-0.1, w_zero=0.0, w_plus=0.5)
        assert "cannot be negative" in str(exc_info.value)

    def test_total_property(self):
        """Total should sum all three states."""
        state = AtomState(w_minus=0.3, w_zero=0.4, w_plus=0.3)
        assert state.total == pytest.approx(1.0)

    def test_polar_balance_50_50(self):
        """Equal polar values should give 50/50 balance."""
        state = AtomState(w_minus=0.5, w_zero=0.2, w_plus=0.5)
        assert state.polar_balance == (50.0, 50.0)

    def test_polar_balance_ignores_neutral(self):
        """Neutral state should not affect polar balance."""
        state1 = AtomState(w_minus=1.0, w_zero=0.0, w_plus=1.0)
        state2 = AtomState(w_minus=1.0, w_zero=100.0, w_plus=1.0)
        assert state1.polar_balance == state2.polar_balance

    def test_polar_balance_empty(self):
        """Zero polar values should return 50/50."""
        state = AtomState(w_minus=0.0, w_zero=1.0, w_plus=0.0)
        assert state.polar_balance == (50.0, 50.0)


class TestWaveState:
    """Tests for WaveState enum."""

    def test_wave_states_exist(self):
        """All three wave states should exist."""
        assert WaveState.W_MINUS.value == "w⁻"
        assert WaveState.W_ZERO.value == "w⁰"
        assert WaveState.W_PLUS.value == "w⁺"

    def test_wave_state_count(self):
        """Should have exactly 3 wave states."""
        assert len(WaveState) == 3


class TestAtom:
    """Tests for Atom class."""

    def test_operational_ratio_is_52_48(self):
        """Atom operates at 52/48 ratio."""
        assert Atom.OPERATIONAL_RATIO == (52, 48)
        assert Atom.STRUCTURE_COMPONENT == 0.52
        assert Atom.FLEXIBILITY_COMPONENT == 0.48

    def test_default_state_is_balanced(self):
        """Default atom state should be META 50/50 balanced."""
        atom = Atom()
        assert atom.state.w_minus == 0.5
        assert atom.state.w_plus == 0.5
        assert atom.validate_meta_compliance() is True

    def test_set_state_valid_balance(self):
        """Setting balanced polar states should succeed."""
        atom = Atom()
        atom.set_state(w_minus=1.0, w_zero=0.5, w_plus=1.0)
        assert atom.state.w_minus == 1.0
        assert atom.state.w_zero == 0.5
        assert atom.state.w_plus == 1.0

    def test_set_state_invalid_balance_raises(self):
        """Setting imbalanced polar states should raise ValueError."""
        atom = Atom()
        with pytest.raises(ValueError) as exc_info:
            atom.set_state(w_minus=0.6, w_zero=0.0, w_plus=0.4)
        assert "META 50/50" in str(exc_info.value)

    def test_validate_meta_compliance(self):
        """Meta compliance validation should work correctly."""
        atom = Atom()
        assert atom.validate_meta_compliance() is True

    def test_validate_operational_compliance(self):
        """Operational compliance validation should work correctly."""
        atom = Atom()
        assert atom.validate_operational_compliance() is True

    def test_operational_ratio_property(self):
        """Operational ratio should return 52/48."""
        atom = Atom()
        ratio = atom.operational_ratio
        assert ratio[0] == pytest.approx(52.0)
        assert ratio[1] == pytest.approx(48.0)

    def test_prove_meta_meaning_structure(self):
        """prove_meta_meaning should return complete validation report."""
        atom = Atom()
        proof = atom.prove_meta_meaning()

        assert "meta_valid" in proof
        assert "meta_balance" in proof
        assert "operational_valid" in proof
        assert "operational_ratio" in proof
        assert "state" in proof

        assert proof["meta_valid"] is True
        assert proof["operational_valid"] is True
        assert proof["meta_balance"]["is_50_50"] is True
        assert proof["operational_ratio"]["is_52_48"] is True

    def test_prove_meta_meaning_state_values(self):
        """prove_meta_meaning should include state values."""
        atom = Atom()
        atom.set_state(w_minus=2.0, w_zero=1.0, w_plus=2.0)
        proof = atom.prove_meta_meaning()

        assert proof["state"]["w⁻"] == 2.0
        assert proof["state"]["w⁰"] == 1.0
        assert proof["state"]["w⁺"] == 2.0

    def test_atom_repr(self):
        """Atom repr should show state and ratio."""
        atom = Atom()
        repr_str = repr(atom)
        assert "w⁻=" in repr_str
        assert "w⁰=" in repr_str
        assert "w⁺=" in repr_str
        assert "52/48" in repr_str

    def test_atom_with_shared_meta_equilibrium(self):
        """Multiple atoms can share a MetaEquilibrium instance."""
        meta = MetaEquilibrium()
        atom1 = Atom(meta)
        atom2 = Atom(meta)

        atom1.set_state(1, 0, 1)
        atom2.set_state(2, 0, 2)

        assert atom1.validate_meta_compliance() is True
        assert atom2.validate_meta_compliance() is True


class TestSubParameter:
    """Tests for SubParameter class."""

    def test_create_valid_parameter(self):
        """Valid 50/50 parameters should be created."""
        param = SubParameter("energy", 100, 100)
        assert param.name == "energy"
        assert param.values == (100, 100)

    def test_create_invalid_parameter_raises(self):
        """Invalid parameters should raise ValueError on creation."""
        with pytest.raises(ValueError) as exc_info:
            SubParameter("bad", 60, 40)
        assert "violates META 50/50" in str(exc_info.value)

    def test_balance_property(self):
        """Balance should return 50/50 for valid parameters."""
        param = SubParameter("test", 50, 50)
        assert param.balance == (50.0, 50.0)

    def test_prove_meta_meaning(self):
        """prove_meta_meaning should return complete proof."""
        param = SubParameter("force", 200, 200)
        proof = param.prove_meta_meaning()

        assert proof["name"] == "force"
        assert proof["positive"] == 200
        assert proof["negative"] == 200
        assert proof["balance"] == "50.00/50.00"
        assert proof["meta_valid"] is True
        assert "proof" in proof

    def test_parameter_repr(self):
        """SubParameter repr should show name and values."""
        param = SubParameter("mass", 10, 10)
        repr_str = repr(param)
        assert "mass" in repr_str
        assert "+10" in repr_str
        assert "-10" in repr_str

    def test_parameter_registered_in_meta(self):
        """Parameters should be registered in MetaEquilibrium."""
        meta = MetaEquilibrium()
        SubParameter("param1", 5, 5, meta)
        SubParameter("param2", 10, 10, meta)

        assert "param1" in meta.validated_parameters
        assert "param2" in meta.validated_parameters

    def test_parameter_with_decimals(self):
        """Decimal values maintaining 50/50 should be valid."""
        param = SubParameter("precise", 0.123456, 0.123456)
        assert param.balance == (50.0, 50.0)


class TestIntegration:
    """Integration tests for the equilibrium system."""

    def test_full_system_validation(self):
        """Test complete system with META and atoms."""
        meta = MetaEquilibrium()

        # Create atoms
        atom1 = Atom(meta)
        atom2 = Atom(meta)

        # Set states
        atom1.set_state(w_minus=1.0, w_zero=0.5, w_plus=1.0)
        atom2.set_state(w_minus=2.0, w_zero=1.0, w_plus=2.0)

        # Register sub-parameters
        meta.register_parameter("system_energy", 500, 500)
        meta.register_parameter("system_charge", 100, 100)

        # Validate all
        assert atom1.validate_meta_compliance() is True
        assert atom2.validate_meta_compliance() is True
        assert atom1.validate_operational_compliance() is True
        assert atom2.validate_operational_compliance() is True
        assert len(meta.validated_parameters) == 2

    def test_operational_enables_meta(self):
        """Verify that 52/48 operational ratio enables 50/50 META."""
        atom = Atom()

        # Atom operates at 52/48
        assert atom.operational_ratio == (52.0, 48.0)

        # But maintains META 50/50 in polar states
        assert atom.state.polar_balance == (50.0, 50.0)

        # Both validations pass
        proof = atom.prove_meta_meaning()
        assert proof["meta_valid"] is True
        assert proof["operational_valid"] is True

    def test_meta_violation_prevented(self):
        """System should prevent any META 50/50 violations."""
        meta = MetaEquilibrium()
        atom = Atom(meta)

        # Cannot set imbalanced states
        with pytest.raises(ValueError):
            atom.set_state(0.51, 0, 0.49)

        # Cannot register imbalanced parameters
        with pytest.raises(ValueError):
            meta.register_parameter("invalid", 51, 49)

        # Cannot create imbalanced sub-parameters
        with pytest.raises(ValueError):
            SubParameter("invalid", 100, 99, meta)

    def test_neutral_state_freedom(self):
        """Neutral state (w⁰) should be unconstrained."""
        atom = Atom()

        # Can set any neutral value while maintaining polar balance
        atom.set_state(w_minus=1.0, w_zero=0.0, w_plus=1.0)
        assert atom.validate_meta_compliance() is True

        atom.set_state(w_minus=1.0, w_zero=100.0, w_plus=1.0)
        assert atom.validate_meta_compliance() is True

        atom.set_state(w_minus=1.0, w_zero=0.001, w_plus=1.0)
        assert atom.validate_meta_compliance() is True
