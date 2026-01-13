"""
Verification System
===================
Verifies claims, data, and states maintain META 50/50 equilibrium.
All verification produces balanced proof/disproof at 50/50.
"""

from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, TypeVar
from uuid import UUID, uuid4

from core.equilibrium import MetaEquilibrium
from core.proportions import ProportionValidator

T = TypeVar("T")


class VerificationStatus(Enum):
    """Status of a verification."""

    PENDING = "pending"  # Not yet verified
    IN_PROGRESS = "in_progress"  # Verification underway
    VERIFIED = "verified"  # Passed verification
    FAILED = "failed"  # Failed verification
    INCONCLUSIVE = "inconclusive"  # Cannot determine


class VerificationType(Enum):
    """Types of verification."""

    BALANCE = "balance"  # META 50/50 balance check
    PROPORTION = "proportion"  # Ratio verification
    CONSISTENCY = "consistency"  # Internal consistency
    COMPLETENESS = "completeness"  # Data completeness
    INTEGRITY = "integrity"  # Data integrity
    COMPLIANCE = "compliance"  # Rule compliance


class ConfidenceLevel(Enum):
    """Confidence levels for verification results."""

    NONE = "none"  # 0% confidence
    LOW = "low"  # 25% confidence
    MEDIUM = "medium"  # 50% confidence
    HIGH = "high"  # 75% confidence
    ABSOLUTE = "absolute"  # 100% confidence


@dataclass
class VerificationClaim:
    """
    A claim to be verified.
    """

    id: UUID = field(default_factory=uuid4)
    subject_id: UUID | None = None
    claim_type: VerificationType = VerificationType.BALANCE
    statement: str = ""
    evidence_for: float = 0.0
    evidence_against: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if self.evidence_for < 0 or self.evidence_against < 0:
            raise ValueError("Evidence values cannot be negative")
        self._meta = MetaEquilibrium()

    @property
    def is_balanced(self) -> bool:
        """Check if evidence is balanced (META 50/50)."""
        return self._meta.verify_balance(self.evidence_for, self.evidence_against)

    @property
    def balance(self) -> tuple[float, float]:
        """Get evidence balance ratio."""
        return self._meta.calculate_balance(self.evidence_for, self.evidence_against)

    @property
    def total_evidence(self) -> float:
        """Total evidence weight."""
        return self.evidence_for + self.evidence_against

    @property
    def net_evidence(self) -> float:
        """Net evidence (for - against)."""
        return self.evidence_for - self.evidence_against

    def add_evidence(self, support: float, opposition: float) -> None:
        """Add evidence to the claim."""
        if support < 0 or opposition < 0:
            raise ValueError("Evidence cannot be negative")
        self.evidence_for += support
        self.evidence_against += opposition


@dataclass
class VerificationResult:
    """
    Result of a verification process.
    Results should ideally be balanced (verification/falsification at 50/50).
    """

    id: UUID = field(default_factory=uuid4)
    claim_id: UUID = field(default_factory=uuid4)
    status: VerificationStatus = VerificationStatus.PENDING
    verification_type: VerificationType = VerificationType.BALANCE
    confidence: ConfidenceLevel = ConfidenceLevel.NONE
    score_verified: float = 0.0
    score_falsified: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)
    details: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)

    def __post_init__(self):
        self._meta = MetaEquilibrium()

    @property
    def is_balanced(self) -> bool:
        """Check if result is balanced."""
        return self._meta.verify_balance(self.score_verified, self.score_falsified)

    @property
    def balance(self) -> tuple[float, float]:
        """Get result balance."""
        return self._meta.calculate_balance(self.score_verified, self.score_falsified)

    @property
    def total_score(self) -> float:
        """Total verification score."""
        return self.score_verified + self.score_falsified

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        return {
            "id": str(self.id),
            "claim_id": str(self.claim_id),
            "status": self.status.value,
            "type": self.verification_type.value,
            "confidence": self.confidence.value,
            "scores": {
                "verified": self.score_verified,
                "falsified": self.score_falsified,
                "balance": f"{self.balance[0]:.2f}/{self.balance[1]:.2f}",
            },
            "balanced": self.is_balanced,
            "timestamp": self.timestamp.isoformat(),
            "errors": self.errors,
        }


class VerificationRule:
    """
    A rule for verification.
    Rules define how to verify specific types of claims.
    """

    def __init__(
        self,
        name: str,
        verification_type: VerificationType,
        validator: Callable[[Any], tuple[bool, float, float]],
        description: str = "",
    ):
        self._name = name
        self._type = verification_type
        self._validator = validator
        self._description = description

    @property
    def name(self) -> str:
        return self._name

    @property
    def verification_type(self) -> VerificationType:
        return self._type

    @property
    def description(self) -> str:
        return self._description

    def verify(self, data: Any) -> tuple[bool, float, float]:
        """
        Verify data against this rule.

        Returns:
            Tuple of (passed, score_for, score_against)
        """
        return self._validator(data)


class Verifier:
    """
    Main verification engine.
    Verifies claims and data while maintaining META 50/50 awareness.
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        self._meta = meta_equilibrium or MetaEquilibrium()
        self._validator = ProportionValidator(self._meta)
        self._rules: dict[str, VerificationRule] = {}
        self._claims: dict[UUID, VerificationClaim] = {}
        self._results: dict[UUID, VerificationResult] = {}
        self._history: list[VerificationResult] = []

        # Load default rules
        self._load_default_rules()

    def _load_default_rules(self) -> None:
        """Load default verification rules."""

        # Balance rule
        def check_balance(data: dict) -> tuple[bool, float, float]:
            if "positive" not in data or "negative" not in data:
                return False, 0, 100
            is_balanced = self._meta.verify_balance(data["positive"], data["negative"])
            if is_balanced:
                return True, 100, 0
            balance = self._meta.calculate_balance(data["positive"], data["negative"])
            deviation = abs(balance[0] - 50)
            return False, 100 - deviation * 2, deviation * 2

        self.register_rule(
            VerificationRule(
                "meta_balance",
                VerificationType.BALANCE,
                check_balance,
                "Verifies META 50/50 balance",
            )
        )

        # Proportion rule
        def check_proportion(data: dict) -> tuple[bool, float, float]:
            if "ratio" not in data or "expected" not in data:
                return False, 0, 100
            actual = data["ratio"]
            expected = data["expected"]
            tolerance = data.get("tolerance", 0.01)
            if abs(actual - expected) <= tolerance:
                return True, 100, 0
            deviation = abs(actual - expected) / expected * 100
            return False, max(0, 100 - deviation), min(100, deviation)

        self.register_rule(
            VerificationRule(
                "proportion_check",
                VerificationType.PROPORTION,
                check_proportion,
                "Verifies ratio proportions",
            )
        )

        # Completeness rule
        def check_completeness(data: dict) -> tuple[bool, float, float]:
            if "required" not in data or "present" not in data:
                return False, 0, 100
            required = set(data["required"])
            present = set(data["present"])
            missing = required - present
            completeness = len(present & required) / len(required) * 100 if required else 100
            return len(missing) == 0, completeness, 100 - completeness

        self.register_rule(
            VerificationRule(
                "completeness_check",
                VerificationType.COMPLETENESS,
                check_completeness,
                "Verifies data completeness",
            )
        )

    @property
    def rule_count(self) -> int:
        """Number of registered rules."""
        return len(self._rules)

    @property
    def claim_count(self) -> int:
        """Number of claims."""
        return len(self._claims)

    @property
    def result_count(self) -> int:
        """Number of results."""
        return len(self._results)

    def register_rule(self, rule: VerificationRule) -> None:
        """Register a verification rule."""
        self._rules[rule.name] = rule

    def get_rule(self, name: str) -> VerificationRule | None:
        """Get a rule by name."""
        return self._rules.get(name)

    def create_claim(
        self,
        statement: str,
        claim_type: VerificationType = VerificationType.BALANCE,
        subject_id: UUID | None = None,
        initial_evidence_for: float = 0.0,
        initial_evidence_against: float = 0.0,
    ) -> VerificationClaim:
        """Create a new verification claim."""
        claim = VerificationClaim(
            subject_id=subject_id,
            claim_type=claim_type,
            statement=statement,
            evidence_for=initial_evidence_for,
            evidence_against=initial_evidence_against,
        )
        self._claims[claim.id] = claim
        return claim

    def get_claim(self, claim_id: UUID) -> VerificationClaim | None:
        """Get a claim by ID."""
        return self._claims.get(claim_id)

    def verify_claim(
        self, claim_id: UUID, data: Any, rule_name: str | None = None
    ) -> VerificationResult:
        """
        Verify a claim using specified or matching rule.

        Args:
            claim_id: Claim to verify
            data: Data to verify against
            rule_name: Specific rule to use (optional)

        Returns:
            VerificationResult
        """
        claim = self._claims.get(claim_id)
        if claim is None:
            result = VerificationResult(
                claim_id=claim_id, status=VerificationStatus.FAILED, errors=["Claim not found"]
            )
            self._history.append(result)
            return result

        # Find matching rule
        rule = None
        if rule_name:
            rule = self._rules.get(rule_name)
        else:
            # Find first matching rule by type
            for r in self._rules.values():
                if r.verification_type == claim.claim_type:
                    rule = r
                    break

        if rule is None:
            result = VerificationResult(
                claim_id=claim_id,
                status=VerificationStatus.FAILED,
                verification_type=claim.claim_type,
                errors=["No matching verification rule found"],
            )
            self._history.append(result)
            return result

        # Execute verification
        try:
            passed, score_for, score_against = rule.verify(data)

            # Determine confidence
            if score_for >= 90:
                confidence = ConfidenceLevel.ABSOLUTE
            elif score_for >= 75:
                confidence = ConfidenceLevel.HIGH
            elif score_for >= 50:
                confidence = ConfidenceLevel.MEDIUM
            elif score_for >= 25:
                confidence = ConfidenceLevel.LOW
            else:
                confidence = ConfidenceLevel.NONE

            result = VerificationResult(
                claim_id=claim_id,
                status=VerificationStatus.VERIFIED if passed else VerificationStatus.FAILED,
                verification_type=rule.verification_type,
                confidence=confidence,
                score_verified=score_for,
                score_falsified=score_against,
                details={"rule": rule.name, "data": str(data)[:100]},
            )

        except Exception as e:
            result = VerificationResult(
                claim_id=claim_id,
                status=VerificationStatus.FAILED,
                verification_type=claim.claim_type,
                errors=[str(e)],
            )

        self._results[result.id] = result
        self._history.append(result)
        return result

    def verify_balance(
        self, positive: float, negative: float, create_claim: bool = True
    ) -> VerificationResult:
        """
        Verify META 50/50 balance directly.

        Args:
            positive: Positive value
            negative: Negative value
            create_claim: Whether to create a claim record

        Returns:
            VerificationResult
        """
        claim_id = uuid4()
        if create_claim:
            claim = self.create_claim(
                f"Balance check: {positive}/{negative}", VerificationType.BALANCE
            )
            claim_id = claim.id

        return self.verify_claim(
            claim_id, {"positive": positive, "negative": negative}, "meta_balance"
        )

    def verify_proportion(
        self, actual_ratio: float, expected_ratio: float, tolerance: float = 0.01
    ) -> VerificationResult:
        """
        Verify a proportion/ratio.

        Args:
            actual_ratio: Actual ratio value
            expected_ratio: Expected ratio value
            tolerance: Acceptable deviation

        Returns:
            VerificationResult
        """
        claim = self.create_claim(
            f"Proportion check: {actual_ratio} vs {expected_ratio}", VerificationType.PROPORTION
        )

        return self.verify_claim(
            claim.id,
            {"ratio": actual_ratio, "expected": expected_ratio, "tolerance": tolerance},
            "proportion_check",
        )

    def batch_verify(
        self, items: list[tuple[UUID, Any]], rule_name: str
    ) -> list[VerificationResult]:
        """
        Verify multiple items with the same rule.

        Args:
            items: List of (claim_id, data) tuples
            rule_name: Rule to use

        Returns:
            List of VerificationResults
        """
        results = []
        for claim_id, data in items:
            result = self.verify_claim(claim_id, data, rule_name)
            results.append(result)
        return results

    def get_results_by_status(self, status: VerificationStatus) -> list[VerificationResult]:
        """Get results by status."""
        return [r for r in self._results.values() if r.status == status]

    def get_verification_stats(self) -> dict[str, Any]:
        """Get verification statistics."""
        total = len(self._results)
        if total == 0:
            return {"total": 0, "verified": 0, "failed": 0, "rate": 0.0}

        verified = len(self.get_results_by_status(VerificationStatus.VERIFIED))
        failed = len(self.get_results_by_status(VerificationStatus.FAILED))

        return {
            "total": total,
            "verified": verified,
            "failed": failed,
            "inconclusive": total - verified - failed,
            "rate": verified / total * 100 if total > 0 else 0,
        }

    def validate_all(self) -> dict[str, Any]:
        """Validate all claims and results."""
        stats = self.get_verification_stats()

        # Check if results are balanced
        total_verified = sum(r.score_verified for r in self._results.values())
        total_falsified = sum(r.score_falsified for r in self._results.values())
        balance = self._meta.calculate_balance(total_verified, total_falsified)

        return {
            "claims": self.claim_count,
            "results": self.result_count,
            "rules": self.rule_count,
            "statistics": stats,
            "aggregate_balance": f"{balance[0]:.2f}/{balance[1]:.2f}",
            "system_balanced": self._meta.verify_balance(total_verified, total_falsified),
        }

    def prove_meta_meaning(self) -> dict[str, Any]:
        """Generate META proof for verifier."""
        validation = self.validate_all()

        return {
            **validation,
            "proof": (
                "Verification system maintains META 50/50 equilibrium"
                if validation.get("system_balanced", False)
                else "Verification system aggregate is not balanced (expected in practice)"
            ),
        }


class VerificationChain:
    """
    Chain of verifications for complex validation.
    Each step must pass for the chain to succeed.
    """

    def __init__(self, name: str, verifier: Verifier):
        self._name = name
        self._verifier = verifier
        self._steps: list[tuple[str, Callable[[Any], Any], str]] = []
        self._results: list[VerificationResult] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def step_count(self) -> int:
        return len(self._steps)

    @property
    def results(self) -> list[VerificationResult]:
        return self._results.copy()

    def add_step(self, name: str, transformer: Callable[[Any], Any], rule_name: str) -> None:
        """
        Add a verification step.

        Args:
            name: Step name
            transformer: Function to transform input for verification
            rule_name: Rule to use for verification
        """
        self._steps.append((name, transformer, rule_name))

    def execute(self, initial_data: Any) -> tuple[bool, list[VerificationResult]]:
        """
        Execute the verification chain.

        Args:
            initial_data: Starting data

        Returns:
            Tuple of (all_passed, results)
        """
        self._results = []
        current_data = initial_data
        all_passed = True

        for step_name, transformer, rule_name in self._steps:
            # Transform data for this step
            try:
                step_data = transformer(current_data)
            except Exception as e:
                result = VerificationResult(
                    status=VerificationStatus.FAILED,
                    errors=[f"Transform error in {step_name}: {str(e)}"],
                )
                self._results.append(result)
                all_passed = False
                break

            # Create claim and verify
            claim = self._verifier.create_claim(
                f"Chain step: {step_name}", VerificationType.COMPLIANCE
            )
            result = self._verifier.verify_claim(claim.id, step_data, rule_name)
            self._results.append(result)

            if result.status != VerificationStatus.VERIFIED:
                all_passed = False
                break

            current_data = step_data

        return all_passed, self._results

    def get_summary(self) -> dict[str, Any]:
        """Get chain execution summary."""
        passed = sum(1 for r in self._results if r.status == VerificationStatus.VERIFIED)
        failed = sum(1 for r in self._results if r.status == VerificationStatus.FAILED)

        return {
            "chain": self._name,
            "total_steps": self.step_count,
            "executed": len(self._results),
            "passed": passed,
            "failed": failed,
            "complete": len(self._results) == self.step_count and failed == 0,
        }
