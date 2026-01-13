"""
Tests for verification module
=============================
Tests for verification and validation with META 50/50 awareness.
"""

import pytest

from verification.validators import (
    BalanceValidator,
    CompositeValidator,
    MetaEquilibriumValidator,
    ProportionRatioValidator,
    RangeValidator,
    SchemaValidator,
    ValidationIssue,
    ValidationReport,
    ValidationSeverity,
)
from verification.verifier import (
    VerificationChain,
    VerificationClaim,
    VerificationResult,
    VerificationRule,
    VerificationStatus,
    VerificationType,
    Verifier,
)


class TestVerificationStatus:
    """Tests for VerificationStatus enum."""

    def test_all_statuses_exist(self):
        assert VerificationStatus.PENDING.value == "pending"
        assert VerificationStatus.IN_PROGRESS.value == "in_progress"
        assert VerificationStatus.VERIFIED.value == "verified"
        assert VerificationStatus.FAILED.value == "failed"
        assert VerificationStatus.INCONCLUSIVE.value == "inconclusive"


class TestVerificationType:
    """Tests for VerificationType enum."""

    def test_all_types_exist(self):
        assert VerificationType.BALANCE.value == "balance"
        assert VerificationType.PROPORTION.value == "proportion"
        assert VerificationType.CONSISTENCY.value == "consistency"
        assert VerificationType.COMPLETENESS.value == "completeness"


class TestVerificationClaim:
    """Tests for VerificationClaim dataclass."""

    def test_create_claim(self):
        claim = VerificationClaim(statement="Test claim", evidence_for=50, evidence_against=50)
        assert claim.statement == "Test claim"
        assert claim.is_balanced is True

    def test_negative_evidence_raises(self):
        with pytest.raises(ValueError):
            VerificationClaim(evidence_for=-10, evidence_against=10)

    def test_total_evidence(self):
        claim = VerificationClaim(evidence_for=60, evidence_against=40)
        assert claim.total_evidence == 100

    def test_net_evidence(self):
        claim = VerificationClaim(evidence_for=70, evidence_against=30)
        assert claim.net_evidence == 40

    def test_add_evidence(self):
        claim = VerificationClaim(evidence_for=50, evidence_against=50)
        claim.add_evidence(25, 25)
        assert claim.evidence_for == 75
        assert claim.evidence_against == 75


class TestVerificationResult:
    """Tests for VerificationResult dataclass."""

    def test_create_result(self):
        result = VerificationResult(
            status=VerificationStatus.VERIFIED, score_verified=100, score_falsified=0
        )
        assert result.status == VerificationStatus.VERIFIED

    def test_is_balanced(self):
        balanced = VerificationResult(score_verified=50, score_falsified=50)
        unbalanced = VerificationResult(score_verified=80, score_falsified=20)
        assert balanced.is_balanced is True
        assert unbalanced.is_balanced is False

    def test_to_dict(self):
        result = VerificationResult(
            status=VerificationStatus.VERIFIED, score_verified=100, score_falsified=0
        )
        d = result.to_dict()
        assert "status" in d
        assert "scores" in d


class TestVerificationRule:
    """Tests for VerificationRule class."""

    def test_create_rule(self):
        rule = VerificationRule(
            name="test_rule",
            verification_type=VerificationType.BALANCE,
            validator=lambda x: (True, 100, 0),
            description="Test",
        )
        assert rule.name == "test_rule"

    def test_verify(self):
        rule = VerificationRule(
            name="always_pass",
            verification_type=VerificationType.BALANCE,
            validator=lambda x: (True, 100, 0),
        )
        passed, score_for, score_against = rule.verify({})
        assert passed is True
        assert score_for == 100


class TestVerifier:
    """Tests for Verifier class."""

    def test_create_verifier(self):
        verifier = Verifier()
        assert verifier.rule_count > 0  # Default rules loaded

    def test_create_claim(self):
        verifier = Verifier()
        claim = verifier.create_claim("Test statement", VerificationType.BALANCE)
        assert verifier.claim_count == 1
        assert claim.statement == "Test statement"

    def test_verify_balance_pass(self):
        verifier = Verifier()
        result = verifier.verify_balance(50, 50)
        assert result.status == VerificationStatus.VERIFIED

    def test_verify_balance_fail(self):
        verifier = Verifier()
        result = verifier.verify_balance(70, 30)
        assert result.status == VerificationStatus.FAILED

    def test_verify_proportion(self):
        verifier = Verifier()
        result = verifier.verify_proportion(52, 52, tolerance=0.5)
        assert result.status == VerificationStatus.VERIFIED

    def test_register_rule(self):
        verifier = Verifier()
        initial_count = verifier.rule_count
        rule = VerificationRule(
            name="custom",
            verification_type=VerificationType.INTEGRITY,
            validator=lambda x: (True, 100, 0),
        )
        verifier.register_rule(rule)
        assert verifier.rule_count == initial_count + 1

    def test_batch_verify(self):
        verifier = Verifier()
        c1 = verifier.create_claim("A", VerificationType.BALANCE)
        c2 = verifier.create_claim("B", VerificationType.BALANCE)

        results = verifier.batch_verify(
            [(c1.id, {"positive": 50, "negative": 50}), (c2.id, {"positive": 50, "negative": 50})],
            "meta_balance",
        )

        assert len(results) == 2
        assert all(r.status == VerificationStatus.VERIFIED for r in results)

    def test_get_verification_stats(self):
        verifier = Verifier()
        verifier.verify_balance(50, 50)
        verifier.verify_balance(70, 30)

        stats = verifier.get_verification_stats()
        assert stats["total"] == 2
        assert stats["verified"] == 1
        assert stats["failed"] == 1

    def test_validate_all(self):
        verifier = Verifier()
        verifier.verify_balance(50, 50)
        result = verifier.validate_all()
        assert "claims" in result
        assert "statistics" in result


class TestVerificationChain:
    """Tests for VerificationChain class."""

    def test_create_chain(self):
        verifier = Verifier()
        chain = VerificationChain("test_chain", verifier)
        assert chain.name == "test_chain"
        assert chain.step_count == 0

    def test_add_step(self):
        verifier = Verifier()
        chain = VerificationChain("test", verifier)
        chain.add_step("step1", lambda x: x, "meta_balance")
        assert chain.step_count == 1

    def test_execute_chain_pass(self):
        verifier = Verifier()
        chain = VerificationChain("test", verifier)
        chain.add_step("balance_check", lambda x: x, "meta_balance")

        passed, results = chain.execute({"positive": 50, "negative": 50})
        assert passed is True
        assert len(results) == 1

    def test_execute_chain_fail(self):
        verifier = Verifier()
        chain = VerificationChain("test", verifier)
        chain.add_step("balance_check", lambda x: x, "meta_balance")

        passed, results = chain.execute({"positive": 70, "negative": 30})
        assert passed is False

    def test_get_summary(self):
        verifier = Verifier()
        chain = VerificationChain("test", verifier)
        chain.add_step("step1", lambda x: x, "meta_balance")
        chain.execute({"positive": 50, "negative": 50})

        summary = chain.get_summary()
        assert summary["chain"] == "test"
        assert summary["complete"] is True


class TestValidationSeverity:
    """Tests for ValidationSeverity enum."""

    def test_all_severities_exist(self):
        assert ValidationSeverity.INFO.value == "info"
        assert ValidationSeverity.WARNING.value == "warning"
        assert ValidationSeverity.ERROR.value == "error"
        assert ValidationSeverity.CRITICAL.value == "critical"


class TestValidationIssue:
    """Tests for ValidationIssue dataclass."""

    def test_create_issue(self):
        issue = ValidationIssue(
            code="TEST_ERROR",
            message="Test error message",
            severity=ValidationSeverity.ERROR,
            field="test_field",
        )
        assert issue.code == "TEST_ERROR"
        assert issue.severity == ValidationSeverity.ERROR

    def test_to_dict(self):
        issue = ValidationIssue(code="TEST", message="Test", severity=ValidationSeverity.WARNING)
        d = issue.to_dict()
        assert d["code"] == "TEST"
        assert d["severity"] == "warning"


class TestValidationReport:
    """Tests for ValidationReport dataclass."""

    def test_create_report(self):
        from datetime import datetime

        report = ValidationReport(valid=True, issues=[], score=100.0, timestamp=datetime.now())
        assert report.valid is True
        assert report.score == 100.0

    def test_error_count(self):
        from datetime import datetime

        issues = [
            ValidationIssue("E1", "Error 1", ValidationSeverity.ERROR),
            ValidationIssue("E2", "Error 2", ValidationSeverity.ERROR),
            ValidationIssue("W1", "Warning 1", ValidationSeverity.WARNING),
        ]
        report = ValidationReport(False, issues, 50.0, datetime.now())
        assert report.error_count == 2
        assert report.warning_count == 1


class TestBalanceValidator:
    """Tests for BalanceValidator class."""

    def test_validate_balanced(self):
        validator = BalanceValidator()
        report = validator.validate({"positive": 50, "negative": 50})
        assert report.valid is True
        assert report.score == 100.0

    def test_validate_unbalanced(self):
        validator = BalanceValidator()
        report = validator.validate({"positive": 70, "negative": 30})
        assert report.valid is False

    def test_validate_missing_fields(self):
        validator = BalanceValidator()
        report = validator.validate({"positive": 50})
        assert report.valid is False
        assert report.error_count > 0

    def test_validate_negative_values(self):
        validator = BalanceValidator()
        report = validator.validate({"positive": -10, "negative": 50})
        assert report.valid is False


class TestProportionRatioValidator:
    """Tests for ProportionRatioValidator class."""

    def test_validate_52_48(self):
        validator = ProportionRatioValidator((52, 48))
        report = validator.validate({"numerator": 52, "denominator": 48})
        assert report.valid is True

    def test_validate_wrong_ratio(self):
        validator = ProportionRatioValidator((52, 48))
        report = validator.validate({"numerator": 60, "denominator": 40})
        assert report.valid is False

    def test_validate_zero_denominator(self):
        validator = ProportionRatioValidator()
        report = validator.validate({"numerator": 50, "denominator": 0})
        assert report.valid is False


class TestSchemaValidator:
    """Tests for SchemaValidator class."""

    def test_validate_valid_schema(self):
        schema = {"name": str, "value": (int, float)}
        validator = SchemaValidator(schema)
        report = validator.validate({"name": "test", "value": 42})
        assert report.valid is True

    def test_validate_missing_field(self):
        schema = {"name": str, "value": int}
        validator = SchemaValidator(schema)
        report = validator.validate({"name": "test"})
        assert report.valid is False

    def test_validate_wrong_type(self):
        schema = {"name": str, "value": int}
        validator = SchemaValidator(schema)
        report = validator.validate({"name": "test", "value": "not int"})
        assert report.valid is False


class TestRangeValidator:
    """Tests for RangeValidator class."""

    def test_validate_in_range(self):
        validator = RangeValidator(min_value=0, max_value=100)
        report = validator.validate(50)
        assert report.valid is True

    def test_validate_below_min(self):
        validator = RangeValidator(min_value=0, max_value=100)
        report = validator.validate(-10)
        assert report.valid is False

    def test_validate_above_max(self):
        validator = RangeValidator(min_value=0, max_value=100)
        report = validator.validate(150)
        assert report.valid is False

    def test_validate_invalid_type(self):
        validator = RangeValidator(min_value=0)
        report = validator.validate("not a number")
        assert report.valid is False


class TestCompositeValidator:
    """Tests for CompositeValidator class."""

    def test_create_composite(self):
        validator = CompositeValidator("test")
        assert validator.name == "test"

    def test_add_validator(self):
        composite = CompositeValidator()
        balance_v = BalanceValidator()
        composite.add_validator("balance", balance_v)
        # Chaining should work
        composite.add_validator("balance2", balance_v)

    def test_validate_all_pass(self):
        composite = CompositeValidator()
        composite.add_validator("balance", BalanceValidator(), lambda x: x["balance"])

        data = {"balance": {"positive": 50, "negative": 50}}
        report = composite.validate(data)
        assert report.valid is True

    def test_validate_empty_composite(self):
        composite = CompositeValidator()
        report = composite.validate({})
        assert report.valid is True
        assert report.score == 100.0


class TestMetaEquilibriumValidator:
    """Tests for MetaEquilibriumValidator class."""

    def test_validate_dict(self):
        validator = MetaEquilibriumValidator()
        report = validator.validate({"positive": 50, "negative": 50})
        assert report.valid is True

    def test_validate_unbalanced_dict(self):
        validator = MetaEquilibriumValidator()
        report = validator.validate({"positive": 70, "negative": 30})
        assert report.valid is False

    def test_validate_object_with_is_balanced(self):
        class MockBalanced:
            is_balanced = True
            balance = (50.0, 50.0)

        validator = MetaEquilibriumValidator()
        report = validator.validate(MockBalanced())
        assert report.valid is True

    def test_validate_unknown_format(self):
        validator = MetaEquilibriumValidator()
        report = validator.validate("unknown")
        assert report.warning_count > 0


class TestIntegration:
    """Integration tests for verification module."""

    def test_full_verification_workflow(self):
        verifier = Verifier()

        # Create and verify multiple claims
        claims = []
        for i in range(5):
            claim = verifier.create_claim(f"Claim {i}", VerificationType.BALANCE)
            claims.append(claim)

        # Verify with mixed results
        verifier.verify_balance(50, 50)  # Pass
        verifier.verify_balance(50, 50)  # Pass
        verifier.verify_balance(70, 30)  # Fail

        stats = verifier.get_verification_stats()
        assert stats["total"] >= 3

    def test_chain_with_validators(self):
        verifier = Verifier()

        # Register custom rule using validator
        balance_validator = BalanceValidator()

        def validate_with_balance(data):
            report = balance_validator.validate(data)
            return report.valid, report.score, 100 - report.score

        verifier.register_rule(
            VerificationRule("custom_balance", VerificationType.BALANCE, validate_with_balance)
        )

        result = verifier.verify_claim(
            verifier.create_claim("Test", VerificationType.BALANCE).id,
            {"positive": 50, "negative": 50},
            "custom_balance",
        )

        assert result.status == VerificationStatus.VERIFIED

    def test_composite_validation_system(self):
        # Build composite validator
        composite = CompositeValidator("full_system")
        composite.add_validator("balance", BalanceValidator())
        composite.add_validator(
            "range", RangeValidator(min_value=0, max_value=200), lambda x: x.get("total", 0)
        )

        # Test with valid data
        data = {"positive": 50, "negative": 50, "total": 100}
        report = composite.validate(data)
        assert report.valid is True
