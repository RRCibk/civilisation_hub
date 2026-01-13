"""
Tests for core/proportions.py
=============================
Validates PI/6 ratio, 52/48 calculations, and META 50/50 verification.
"""

import math
import pytest
from core.proportions import (
    PI_OVER_6,
    PI_OVER_6_ROUNDED,
    ProportionConstants,
    Ratio,
    OperationalRatio,
    Pi6Proportion,
    ProportionValidator,
    calculate_52_48,
    calculate_50_50,
    ratio_to_meta_meaning,
    verify_ratio_chain_maintains_meta,
)


class TestConstants:
    """Tests for fundamental constants."""

    def test_pi_over_6_value(self):
        """PI/6 should equal pi divided by 6."""
        assert PI_OVER_6 == math.pi / 6
        assert PI_OVER_6 == pytest.approx(0.5235987755982989)

    def test_pi_over_6_rounded(self):
        """Rounded PI/6 should be 0.5236."""
        assert PI_OVER_6_ROUNDED == 0.5236

    def test_proportion_constants_pi_6(self):
        """ProportionConstants should have correct PI/6 values."""
        assert ProportionConstants.PI_6 == math.pi / 6
        assert ProportionConstants.PI_6_DEGREES == 30.0

    def test_proportion_constants_operational(self):
        """ProportionConstants should have 52/48 operational values."""
        assert ProportionConstants.OPERATIONAL_STRUCTURE == 0.52
        assert ProportionConstants.OPERATIONAL_FLEXIBILITY == 0.48
        assert ProportionConstants.OPERATIONAL_RATIO == (52, 48)

    def test_proportion_constants_trig(self):
        """ProportionConstants should have correct trig values."""
        assert ProportionConstants.SIN_PI_6 == 0.5
        assert ProportionConstants.COS_PI_6 == pytest.approx(math.sqrt(3) / 2)

    def test_structure_flexibility_ratio(self):
        """Structure/flexibility ratio should be 52/48."""
        assert ProportionConstants.STRUCTURE_FLEXIBILITY_RATIO == pytest.approx(52 / 48)


class TestRatio:
    """Tests for Ratio dataclass."""

    def test_create_ratio(self):
        """Should create ratio with correct values."""
        ratio = Ratio(52, 48, "test")
        assert ratio.numerator == 52
        assert ratio.denominator == 48
        assert ratio.name == "test"

    def test_ratio_zero_denominator_raises(self):
        """Zero denominator should raise ValueError."""
        with pytest.raises(ValueError) as exc_info:
            Ratio(10, 0, "invalid")
        assert "Denominator cannot be zero" in str(exc_info.value)

    def test_ratio_value(self):
        """Value property should return correct decimal."""
        ratio = Ratio(52, 48, "test")
        assert ratio.value == pytest.approx(52 / 48)

    def test_ratio_percentage(self):
        """Percentage should return correct tuple."""
        ratio = Ratio(52, 48, "test")
        pct = ratio.percentage
        assert pct[0] == pytest.approx(52.0)
        assert pct[1] == pytest.approx(48.0)

    def test_ratio_percentage_balanced(self):
        """Balanced ratio should return 50/50 percentage."""
        ratio = Ratio(100, 100, "balanced")
        assert ratio.percentage == (50.0, 50.0)

    def test_ratio_inverse(self):
        """Inverse should swap numerator and denominator."""
        ratio = Ratio(52, 48, "original")
        inv = ratio.inverse
        assert inv.numerator == 48
        assert inv.denominator == 52
        assert inv.name == "original_inverse"

    def test_ratio_is_balanced_true(self):
        """Equal values should be balanced."""
        assert Ratio(50, 50, "balanced").is_balanced() is True
        assert Ratio(1, 1, "balanced").is_balanced() is True
        assert Ratio(0.5, 0.5, "balanced").is_balanced() is True

    def test_ratio_is_balanced_false(self):
        """Unequal values should not be balanced."""
        assert Ratio(52, 48, "unbalanced").is_balanced() is False
        assert Ratio(60, 40, "unbalanced").is_balanced() is False

    def test_ratio_distance_from_balance(self):
        """Distance should measure deviation from 50%."""
        assert Ratio(50, 50, "balanced").distance_from_balance() == 0.0
        assert Ratio(52, 48, "operational").distance_from_balance() == pytest.approx(2.0)
        assert Ratio(60, 40, "skewed").distance_from_balance() == pytest.approx(10.0)

    def test_ratio_repr(self):
        """Repr should show name, values, and decimal."""
        ratio = Ratio(52, 48, "test")
        repr_str = repr(ratio)
        assert "test" in repr_str
        assert "52" in repr_str
        assert "48" in repr_str


class TestOperationalRatio:
    """Tests for OperationalRatio class."""

    def test_default_values(self):
        """Default should be 52/48."""
        op = OperationalRatio()
        assert op.structure == 52
        assert op.flexibility == 48

    def test_class_constants(self):
        """Class constants should be correct."""
        assert OperationalRatio.STRUCTURE == 52
        assert OperationalRatio.FLEXIBILITY == 48
        assert OperationalRatio.TOTAL == 100

    def test_custom_values_valid(self):
        """Custom values maintaining 52/48 ratio should work."""
        op = OperationalRatio(520, 480)
        assert op.structure == 520
        assert op.flexibility == 480

    def test_custom_values_invalid_raises(self):
        """Values not maintaining 52/48 should raise."""
        with pytest.raises(ValueError) as exc_info:
            OperationalRatio(50, 50)
        assert "must be 52/48" in str(exc_info.value)

    def test_zero_total_raises(self):
        """Zero total should raise ValueError."""
        with pytest.raises(ValueError) as exc_info:
            OperationalRatio(0, 0)
        assert "Total cannot be zero" in str(exc_info.value)

    def test_ratio_property(self):
        """Ratio should return structure/flexibility."""
        op = OperationalRatio()
        assert op.ratio == pytest.approx(52 / 48)

    def test_as_percentage(self):
        """Should return percentage tuple."""
        op = OperationalRatio()
        pct = op.as_percentage
        assert pct[0] == pytest.approx(52.0)
        assert pct[1] == pytest.approx(48.0)

    def test_from_total(self):
        """Should create correct ratio from total."""
        op = OperationalRatio.from_total(1000)
        assert op.structure == pytest.approx(520)
        assert op.flexibility == pytest.approx(480)

    def test_from_pi_6(self):
        """Should derive 52/48 from PI/6."""
        op = OperationalRatio.from_pi_6()
        assert op.structure == 52
        assert op.flexibility == 48

    def test_prove_enables_meta(self):
        """Proof should contain correct information."""
        op = OperationalRatio()
        proof = op.prove_enables_meta()

        assert proof["structure"] == 52
        assert proof["flexibility"] == 48
        assert proof["ratio"] == pytest.approx(52 / 48)
        assert proof["asymmetry"] == 4
        assert proof["enables_meta"] is True
        assert "proof" in proof

    def test_repr(self):
        """Repr should show ratio."""
        op = OperationalRatio()
        assert "52" in repr(op)
        assert "48" in repr(op)


class TestPi6Proportion:
    """Tests for Pi6Proportion class."""

    def test_value(self):
        """Value should be PI/6."""
        pi6 = Pi6Proportion()
        assert pi6.value == math.pi / 6

    def test_class_constants(self):
        """Class constants should be correct."""
        assert Pi6Proportion.VALUE == math.pi / 6
        assert Pi6Proportion.DEGREES == 30.0
        assert Pi6Proportion.RADIANS == math.pi / 6

    def test_as_percentage(self):
        """Should return ~52.36%."""
        pi6 = Pi6Proportion()
        assert pi6.as_percentage == pytest.approx(52.36, rel=0.01)

    def test_sin_is_half(self):
        """sin(PI/6) should be 0.5 (META connection)."""
        pi6 = Pi6Proportion()
        assert pi6.sin == pytest.approx(0.5)

    def test_cos_value(self):
        """cos(PI/6) should be sqrt(3)/2."""
        pi6 = Pi6Proportion()
        assert pi6.cos == pytest.approx(math.sqrt(3) / 2)

    def test_to_operational_ratio(self):
        """Should convert to 52/48 operational ratio."""
        pi6 = Pi6Proportion()
        op = pi6.to_operational_ratio()
        assert op.structure == 52
        assert op.flexibility == 48

    def test_verify_meta_connection(self):
        """Meta connection verification should be correct."""
        pi6 = Pi6Proportion()
        result = pi6.verify_meta_connection()

        assert result["pi_6_value"] == pytest.approx(math.pi / 6)
        assert result["sin_pi_6"] == pytest.approx(0.5)
        assert result["sin_equals_half"] is True
        assert "meta_connection" in result
        assert "operational_derivation" in result

    def test_repr(self):
        """Repr should show value and degrees."""
        pi6 = Pi6Proportion()
        repr_str = repr(pi6)
        assert "π/6" in repr_str or "pi" in repr_str.lower()
        assert "30" in repr_str


class TestProportionValidator:
    """Tests for ProportionValidator class."""

    def test_verify_maintains_meta_balanced(self):
        """Balanced ratio should maintain META."""
        validator = ProportionValidator()
        balanced = Ratio(100, 100, "balanced")
        assert validator.verify_maintains_meta(balanced) is True

    def test_verify_maintains_meta_unbalanced(self):
        """Unbalanced ratio should not maintain META."""
        validator = ProportionValidator()
        unbalanced = Ratio(52, 48, "unbalanced")
        assert validator.verify_maintains_meta(unbalanced) is False

    def test_verify_enables_meta_correct(self):
        """52/48 ratio should enable META."""
        validator = ProportionValidator()
        operational = Ratio(52, 48, "operational")
        assert validator.verify_enables_meta(operational) is True

    def test_verify_enables_meta_incorrect(self):
        """Non-52/48 ratio should not enable META."""
        validator = ProportionValidator()
        wrong = Ratio(60, 40, "wrong")
        assert validator.verify_enables_meta(wrong) is False

    def test_verify_enables_meta_custom_ratio(self):
        """Should accept custom expected ratio."""
        validator = ProportionValidator()
        custom = Ratio(60, 40, "custom")
        assert validator.verify_enables_meta(custom, expected=(60, 40)) is True

    def test_validate_ratio_meta_valid(self):
        """Valid META ratio should pass validation."""
        validator = ProportionValidator()
        balanced = Ratio(50, 50, "balanced")
        result = validator.validate_ratio(balanced, level="meta")

        assert result["is_valid"] is True
        assert result["level"] == "meta"
        assert "proof" in result

    def test_validate_ratio_meta_invalid(self):
        """Invalid META ratio should fail validation."""
        validator = ProportionValidator()
        unbalanced = Ratio(60, 40, "unbalanced")
        result = validator.validate_ratio(unbalanced, level="meta")

        assert result["is_valid"] is False
        assert "violation" in result

    def test_validate_ratio_operational_valid(self):
        """Valid operational ratio should pass validation."""
        validator = ProportionValidator()
        operational = Ratio(52, 48, "operational")
        result = validator.validate_ratio(operational, level="operational")

        assert result["is_valid"] is True
        assert result["level"] == "operational"
        assert "proof" in result

    def test_validate_ratio_operational_invalid(self):
        """Invalid operational ratio should fail validation."""
        validator = ProportionValidator()
        wrong = Ratio(50, 50, "wrong")
        result = validator.validate_ratio(wrong, level="operational")

        assert result["is_valid"] is False
        assert "violation" in result

    def test_validate_ratio_unknown_level_raises(self):
        """Unknown level should raise ValueError."""
        validator = ProportionValidator()
        ratio = Ratio(50, 50, "test")
        with pytest.raises(ValueError) as exc_info:
            validator.validate_ratio(ratio, level="unknown")
        assert "Unknown level" in str(exc_info.value)

    def test_validate_pair_maintains_meta_balanced(self):
        """Balanced pair should maintain META."""
        validator = ProportionValidator()
        result = validator.validate_pair_maintains_meta(100, 100, "energy")

        assert result["maintains_meta"] is True
        assert result["balance"] == "50.00/50.00"
        assert "proof" in result

    def test_validate_pair_maintains_meta_unbalanced(self):
        """Unbalanced pair should violate META."""
        validator = ProportionValidator()
        result = validator.validate_pair_maintains_meta(60, 40, "energy")

        assert result["maintains_meta"] is False
        assert "violation" in result

    def test_derive_complement_meta(self):
        """META complement should equal value."""
        validator = ProportionValidator()
        assert validator.derive_complement(100, level="meta") == 100
        assert validator.derive_complement(0.5, level="meta") == 0.5

    def test_derive_complement_operational(self):
        """Operational complement should be 48/52 of value."""
        validator = ProportionValidator()
        complement = validator.derive_complement(52, level="operational")
        assert complement == pytest.approx(48)

    def test_derive_complement_unknown_level_raises(self):
        """Unknown level should raise ValueError."""
        validator = ProportionValidator()
        with pytest.raises(ValueError) as exc_info:
            validator.derive_complement(100, level="unknown")
        assert "Unknown level" in str(exc_info.value)

    def test_validated_ratios_tracking(self):
        """Validated ratios should be tracked."""
        validator = ProportionValidator()
        r1 = Ratio(50, 50, "first")
        r2 = Ratio(100, 100, "second")

        validator.validate_ratio(r1, level="meta")
        validator.validate_ratio(r2, level="meta")

        assert len(validator.validated_ratios) == 2

    def test_validated_ratios_immutable(self):
        """validated_ratios should return a copy."""
        validator = ProportionValidator()
        validator.validate_ratio(Ratio(50, 50, "test"), level="meta")
        ratios = validator.validated_ratios
        ratios.append(Ratio(1, 2, "hack"))
        assert len(validator.validated_ratios) == 1

    def test_prove_all_maintain_meta(self):
        """Should return proof for all validated ratios."""
        validator = ProportionValidator()
        validator.validate_ratio(Ratio(50, 50, "a"), level="meta")
        validator.validate_ratio(Ratio(100, 100, "b"), level="meta")

        proof = validator.prove_all_maintain_meta()
        assert proof["total_validated"] == 2
        assert len(proof["ratios"]) == 2
        assert "proof" in proof


class TestUtilityFunctions:
    """Tests for utility functions."""

    def test_calculate_52_48(self):
        """Should split total into 52/48."""
        structure, flexibility = calculate_52_48(100)
        assert structure == 52
        assert flexibility == 48

    def test_calculate_52_48_large(self):
        """Should work with large numbers."""
        structure, flexibility = calculate_52_48(10000)
        assert structure == 5200
        assert flexibility == 4800

    def test_calculate_52_48_decimal(self):
        """Should work with decimals."""
        structure, flexibility = calculate_52_48(1.0)
        assert structure == pytest.approx(0.52)
        assert flexibility == pytest.approx(0.48)

    def test_calculate_50_50(self):
        """Should split total into equal halves."""
        pos, neg = calculate_50_50(100)
        assert pos == 50
        assert neg == 50

    def test_calculate_50_50_odd(self):
        """Should handle odd numbers."""
        pos, neg = calculate_50_50(101)
        assert pos == 50.5
        assert neg == 50.5

    def test_ratio_to_meta_meaning_balanced(self):
        """50/50 should be identified as META balanced."""
        result = ratio_to_meta_meaning(50, 50)
        assert result["is_meta_50_50"] is True
        assert result["is_operational_52_48"] is False
        assert "Maintains META" in result["meta_meaning"]

    def test_ratio_to_meta_meaning_operational(self):
        """52/48 should be identified as operational."""
        result = ratio_to_meta_meaning(52, 48)
        assert result["is_meta_50_50"] is False
        assert result["is_operational_52_48"] is True
        assert "Enables META" in result["meta_meaning"]

    def test_ratio_to_meta_meaning_neither(self):
        """60/40 should be neither META nor operational."""
        result = ratio_to_meta_meaning(60, 40)
        assert result["is_meta_50_50"] is False
        assert result["is_operational_52_48"] is False
        assert "Deviates" in result["meta_meaning"]

    def test_ratio_to_meta_meaning_zero(self):
        """Zero ratio should return error."""
        result = ratio_to_meta_meaning(0, 0)
        assert "error" in result

    def test_ratio_to_meta_meaning_distance(self):
        """Should calculate correct distance from META."""
        result = ratio_to_meta_meaning(60, 40)
        assert result["distance_from_meta"] == pytest.approx(10.0)


class TestVerifyRatioChain:
    """Tests for verify_ratio_chain_maintains_meta."""

    def test_empty_chain(self):
        """Empty chain should return error."""
        result = verify_ratio_chain_maintains_meta()
        assert "error" in result

    def test_single_balanced_ratio(self):
        """Single balanced ratio should maintain META."""
        r = Ratio(50, 50, "balanced")
        result = verify_ratio_chain_maintains_meta(r)
        assert result["maintains_meta"] is True
        assert result["chain_length"] == 1

    def test_multiple_balanced_ratios(self):
        """Multiple balanced ratios should maintain META."""
        r1 = Ratio(2, 2, "a")
        r2 = Ratio(3, 3, "b")
        r3 = Ratio(5, 5, "c")
        result = verify_ratio_chain_maintains_meta(r1, r2, r3)
        assert result["maintains_meta"] is True
        assert result["chain_length"] == 3

    def test_unbalanced_chain(self):
        """Unbalanced ratios should not maintain META."""
        r1 = Ratio(2, 1, "a")
        r2 = Ratio(3, 3, "b")
        result = verify_ratio_chain_maintains_meta(r1, r2)
        assert result["maintains_meta"] is False

    def test_compensating_ratios(self):
        """Ratios that compensate each other should maintain META."""
        r1 = Ratio(2, 1, "double")
        r2 = Ratio(1, 2, "half")
        result = verify_ratio_chain_maintains_meta(r1, r2)
        assert result["maintains_meta"] is True
        assert result["product_ratio"] == pytest.approx(1.0)

    def test_chain_ratios_listed(self):
        """Result should list all ratio names."""
        r1 = Ratio(1, 1, "first")
        r2 = Ratio(2, 2, "second")
        result = verify_ratio_chain_maintains_meta(r1, r2)
        assert "first" in result["ratios"]
        assert "second" in result["ratios"]


class TestIntegration:
    """Integration tests for proportions system."""

    def test_pi6_to_operational_to_meta(self):
        """PI/6 should derive operational which enables META."""
        pi6 = Pi6Proportion()

        # PI/6 derives operational ratio
        op = pi6.to_operational_ratio()
        assert op.structure == 52
        assert op.flexibility == 48

        # Operational enables META
        proof = op.prove_enables_meta()
        assert proof["enables_meta"] is True

        # sin(PI/6) = 0.5 connects to META 50/50
        assert pi6.sin == pytest.approx(0.5)

    def test_validator_with_equilibrium(self):
        """Validator should work with MetaEquilibrium."""
        from core.equilibrium import MetaEquilibrium

        meta = MetaEquilibrium()
        validator = ProportionValidator(meta)

        # Validate balanced pair
        result = validator.validate_pair_maintains_meta(100, 100, "energy")
        assert result["maintains_meta"] is True

    def test_full_validation_chain(self):
        """Complete validation from ratio to META proof."""
        validator = ProportionValidator()

        # Create and validate operational ratio
        op_ratio = Ratio(52, 48, "operational")
        op_result = validator.validate_ratio(op_ratio, level="operational")
        assert op_result["is_valid"] is True

        # Create and validate META ratio
        meta_ratio = Ratio(100, 100, "meta")
        meta_result = validator.validate_ratio(meta_ratio, level="meta")
        assert meta_result["is_valid"] is True

        # Prove all maintain their levels
        proof = validator.prove_all_maintain_meta()
        assert proof["total_validated"] == 2

    def test_52_48_split_validates(self):
        """52/48 split should validate as operational."""
        total = 1000
        s, f = calculate_52_48(total)

        validator = ProportionValidator()
        ratio = Ratio(s, f, "split")
        result = validator.validate_ratio(ratio, level="operational")

        assert result["is_valid"] is True

    def test_50_50_split_validates(self):
        """50/50 split should validate as META."""
        total = 1000
        pos, neg = calculate_50_50(total)

        validator = ProportionValidator()
        ratio = Ratio(pos, neg, "split")
        result = validator.validate_ratio(ratio, level="meta")

        assert result["is_valid"] is True
