"""
Validators
==========
Specialized validators for different data types and structures.
All validators produce balanced results aligned with META 50/50.
"""

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Generic, TypeVar

from core.equilibrium import MetaEquilibrium

T = TypeVar("T")


class ValidationSeverity(Enum):
    """Severity levels for validation issues."""

    INFO = "info"  # Informational
    WARNING = "warning"  # Warning, non-blocking
    ERROR = "error"  # Error, blocking
    CRITICAL = "critical"  # Critical, system failure


@dataclass
class ValidationIssue:
    """A single validation issue."""

    code: str
    message: str
    severity: ValidationSeverity
    field: str | None = None
    value: Any = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "code": self.code,
            "message": self.message,
            "severity": self.severity.value,
            "field": self.field,
            "value": str(self.value) if self.value is not None else None,
        }


@dataclass
class ValidationReport:
    """Complete validation report."""

    valid: bool
    issues: list[ValidationIssue]
    score: float  # 0-100
    timestamp: datetime

    @property
    def error_count(self) -> int:
        return sum(
            1
            for i in self.issues
            if i.severity in [ValidationSeverity.ERROR, ValidationSeverity.CRITICAL]
        )

    @property
    def warning_count(self) -> int:
        return sum(1 for i in self.issues if i.severity == ValidationSeverity.WARNING)

    def to_dict(self) -> dict[str, Any]:
        return {
            "valid": self.valid,
            "score": self.score,
            "errors": self.error_count,
            "warnings": self.warning_count,
            "issues": [i.to_dict() for i in self.issues],
            "timestamp": self.timestamp.isoformat(),
        }


class BaseValidator(Generic[T]):
    """
    Base validator class.
    All validators inherit from this.
    """

    def __init__(self, name: str = "base"):
        self._name = name
        self._meta = MetaEquilibrium()

    @property
    def name(self) -> str:
        return self._name

    def validate(self, data: T) -> ValidationReport:
        """
        Validate data. Override in subclasses.

        Args:
            data: Data to validate

        Returns:
            ValidationReport
        """
        raise NotImplementedError("Subclasses must implement validate()")

    def _create_report(
        self, valid: bool, issues: list[ValidationIssue], score: float
    ) -> ValidationReport:
        """Create a validation report."""
        return ValidationReport(valid=valid, issues=issues, score=score, timestamp=datetime.now())


class BalanceValidator(BaseValidator[dict]):
    """
    Validates META 50/50 balance.
    """

    def __init__(self):
        super().__init__("balance")

    def validate(self, data: dict) -> ValidationReport:
        """
        Validate balance data.

        Expected data format:
        {"positive": float, "negative": float}
        """
        issues = []
        score = 100.0

        # Check required fields
        if "positive" not in data:
            issues.append(
                ValidationIssue(
                    code="MISSING_POSITIVE",
                    message="Missing 'positive' field",
                    severity=ValidationSeverity.ERROR,
                    field="positive",
                )
            )
            score -= 50

        if "negative" not in data:
            issues.append(
                ValidationIssue(
                    code="MISSING_NEGATIVE",
                    message="Missing 'negative' field",
                    severity=ValidationSeverity.ERROR,
                    field="negative",
                )
            )
            score -= 50

        if score < 100:
            return self._create_report(False, issues, max(0, score))

        positive = data["positive"]
        negative = data["negative"]

        # Check types
        if not isinstance(positive, int | float):
            issues.append(
                ValidationIssue(
                    code="INVALID_TYPE",
                    message="'positive' must be numeric",
                    severity=ValidationSeverity.ERROR,
                    field="positive",
                    value=positive,
                )
            )
            score -= 30

        if not isinstance(negative, int | float):
            issues.append(
                ValidationIssue(
                    code="INVALID_TYPE",
                    message="'negative' must be numeric",
                    severity=ValidationSeverity.ERROR,
                    field="negative",
                    value=negative,
                )
            )
            score -= 30

        if issues:
            return self._create_report(False, issues, max(0, score))

        # Check non-negative
        if positive < 0:
            issues.append(
                ValidationIssue(
                    code="NEGATIVE_VALUE",
                    message="'positive' cannot be negative",
                    severity=ValidationSeverity.ERROR,
                    field="positive",
                    value=positive,
                )
            )
            score -= 20

        if negative < 0:
            issues.append(
                ValidationIssue(
                    code="NEGATIVE_VALUE",
                    message="'negative' cannot be negative",
                    severity=ValidationSeverity.ERROR,
                    field="negative",
                    value=negative,
                )
            )
            score -= 20

        if issues:
            return self._create_report(False, issues, max(0, score))

        # Check balance
        is_balanced = self._meta.verify_balance(positive, negative)
        if not is_balanced:
            balance = self._meta.calculate_balance(positive, negative)
            deviation = abs(balance[0] - 50)
            issues.append(
                ValidationIssue(
                    code="UNBALANCED",
                    message=f"Not META 50/50 balanced: {balance[0]:.2f}/{balance[1]:.2f}",
                    severity=ValidationSeverity.ERROR,
                    field="balance",
                    value=balance,
                )
            )
            score -= deviation * 2

        valid = (
            len(
                [
                    i
                    for i in issues
                    if i.severity in [ValidationSeverity.ERROR, ValidationSeverity.CRITICAL]
                ]
            )
            == 0
        )
        return self._create_report(valid, issues, max(0, score))


class ProportionRatioValidator(BaseValidator[dict]):
    """
    Validates proportion ratios (52/48 operational, etc.).
    """

    def __init__(self, expected_ratio: tuple[float, float] = (52, 48)):
        super().__init__("proportion")
        self._expected = expected_ratio

    def validate(self, data: dict) -> ValidationReport:
        """
        Validate proportion data.

        Expected data format:
        {"numerator": float, "denominator": float}
        """
        issues = []
        score = 100.0

        if "numerator" not in data or "denominator" not in data:
            issues.append(
                ValidationIssue(
                    code="MISSING_FIELDS",
                    message="Missing 'numerator' or 'denominator'",
                    severity=ValidationSeverity.ERROR,
                )
            )
            return self._create_report(False, issues, 0)

        num = data["numerator"]
        den = data["denominator"]

        if den == 0:
            issues.append(
                ValidationIssue(
                    code="ZERO_DENOMINATOR",
                    message="Denominator cannot be zero",
                    severity=ValidationSeverity.CRITICAL,
                    field="denominator",
                    value=0,
                )
            )
            return self._create_report(False, issues, 0)

        # Calculate actual ratio
        total = abs(num) + abs(den)
        actual_ratio = (abs(num) / total * 100, abs(den) / total * 100)

        # Check against expected
        deviation_num = abs(actual_ratio[0] - self._expected[0])
        deviation_den = abs(actual_ratio[1] - self._expected[1])

        if deviation_num > 0.5 or deviation_den > 0.5:
            issues.append(
                ValidationIssue(
                    code="RATIO_MISMATCH",
                    message=f"Ratio {actual_ratio[0]:.2f}/{actual_ratio[1]:.2f} differs from expected {self._expected[0]}/{self._expected[1]}",
                    severity=ValidationSeverity.WARNING
                    if deviation_num < 5
                    else ValidationSeverity.ERROR,
                    field="ratio",
                    value=actual_ratio,
                )
            )
            score -= (deviation_num + deviation_den) * 2

        valid = (
            len(
                [
                    i
                    for i in issues
                    if i.severity in [ValidationSeverity.ERROR, ValidationSeverity.CRITICAL]
                ]
            )
            == 0
        )
        return self._create_report(valid, issues, max(0, score))


class SchemaValidator(BaseValidator[dict]):
    """
    Validates data against a schema.
    """

    def __init__(self, schema: dict[str, type | tuple[type, ...]]):
        super().__init__("schema")
        self._schema = schema

    def validate(self, data: dict) -> ValidationReport:
        """
        Validate data against schema.

        Schema format:
        {"field_name": expected_type, ...}
        """
        issues = []
        score = 100.0
        field_weight = 100.0 / len(self._schema) if self._schema else 100.0

        for field, expected_type in self._schema.items():
            if field not in data:
                issues.append(
                    ValidationIssue(
                        code="MISSING_FIELD",
                        message=f"Missing required field: {field}",
                        severity=ValidationSeverity.ERROR,
                        field=field,
                    )
                )
                score -= field_weight
            elif not isinstance(data[field], expected_type):
                issues.append(
                    ValidationIssue(
                        code="TYPE_MISMATCH",
                        message=f"Field '{field}' expected {expected_type}, got {type(data[field])}",
                        severity=ValidationSeverity.ERROR,
                        field=field,
                        value=data[field],
                    )
                )
                score -= field_weight

        valid = (
            len(
                [
                    i
                    for i in issues
                    if i.severity in [ValidationSeverity.ERROR, ValidationSeverity.CRITICAL]
                ]
            )
            == 0
        )
        return self._create_report(valid, issues, max(0, score))


class RangeValidator(BaseValidator[float]):
    """
    Validates numeric values are within a range.
    """

    def __init__(
        self, min_value: float | None = None, max_value: float | None = None, name: str = "range"
    ):
        super().__init__(name)
        self._min = min_value
        self._max = max_value

    def validate(self, data: float) -> ValidationReport:
        """Validate value is within range."""
        issues = []
        score = 100.0

        if not isinstance(data, int | float):
            issues.append(
                ValidationIssue(
                    code="INVALID_TYPE",
                    message=f"Expected numeric value, got {type(data)}",
                    severity=ValidationSeverity.ERROR,
                    value=data,
                )
            )
            return self._create_report(False, issues, 0)

        if self._min is not None and data < self._min:
            deviation = self._min - data
            issues.append(
                ValidationIssue(
                    code="BELOW_MINIMUM",
                    message=f"Value {data} is below minimum {self._min}",
                    severity=ValidationSeverity.ERROR,
                    value=data,
                )
            )
            score -= min(50, deviation / abs(self._min) * 100 if self._min != 0 else 50)

        if self._max is not None and data > self._max:
            deviation = data - self._max
            issues.append(
                ValidationIssue(
                    code="ABOVE_MAXIMUM",
                    message=f"Value {data} is above maximum {self._max}",
                    severity=ValidationSeverity.ERROR,
                    value=data,
                )
            )
            score -= min(50, deviation / abs(self._max) * 100 if self._max != 0 else 50)

        valid = (
            len(
                [
                    i
                    for i in issues
                    if i.severity in [ValidationSeverity.ERROR, ValidationSeverity.CRITICAL]
                ]
            )
            == 0
        )
        return self._create_report(valid, issues, max(0, score))


class CompositeValidator(BaseValidator[Any]):
    """
    Combines multiple validators.
    """

    def __init__(self, name: str = "composite"):
        super().__init__(name)
        self._validators: list[tuple[str, BaseValidator, Callable[[Any], Any] | None]] = []

    def add_validator(
        self, name: str, validator: BaseValidator, extractor: Callable[[Any], Any] | None = None
    ) -> "CompositeValidator":
        """
        Add a validator to the composite.

        Args:
            name: Validator name
            validator: The validator
            extractor: Optional function to extract relevant data

        Returns:
            Self for chaining
        """
        self._validators.append((name, validator, extractor))
        return self

    def validate(self, data: Any) -> ValidationReport:
        """Validate data with all validators."""
        all_issues = []
        total_score = 0.0
        validator_count = len(self._validators)

        if validator_count == 0:
            return self._create_report(True, [], 100.0)

        for name, validator, extractor in self._validators:
            try:
                target_data = extractor(data) if extractor else data
                report = validator.validate(target_data)
                all_issues.extend(report.issues)
                total_score += report.score
            except Exception as e:
                all_issues.append(
                    ValidationIssue(
                        code="VALIDATOR_ERROR",
                        message=f"Validator '{name}' failed: {str(e)}",
                        severity=ValidationSeverity.ERROR,
                    )
                )
                total_score += 0

        avg_score = total_score / validator_count
        valid = (
            len(
                [
                    i
                    for i in all_issues
                    if i.severity in [ValidationSeverity.ERROR, ValidationSeverity.CRITICAL]
                ]
            )
            == 0
        )
        return self._create_report(valid, all_issues, avg_score)


class MetaEquilibriumValidator(BaseValidator[Any]):
    """
    Comprehensive META 50/50 validator.
    Validates any object that has balance properties.
    """

    def __init__(self):
        super().__init__("meta_equilibrium")

    def validate(self, data: Any) -> ValidationReport:
        """
        Validate META compliance.

        Data can be:
        - dict with "positive"/"negative" keys
        - Object with is_balanced property
        - Object with balance property
        """
        issues = []
        score = 100.0

        # Try different interfaces
        if isinstance(data, dict):
            if "positive" in data and "negative" in data:
                is_balanced = self._meta.verify_balance(data["positive"], data["negative"])
                if not is_balanced:
                    balance = self._meta.calculate_balance(data["positive"], data["negative"])
                    issues.append(
                        ValidationIssue(
                            code="META_VIOLATION",
                            message=f"META 50/50 violated: {balance[0]:.2f}/{balance[1]:.2f}",
                            severity=ValidationSeverity.ERROR,
                            value=balance,
                        )
                    )
                    score -= abs(balance[0] - 50) * 2

        elif hasattr(data, "is_balanced"):
            if not data.is_balanced:
                if hasattr(data, "balance"):
                    balance = data.balance
                    issues.append(
                        ValidationIssue(
                            code="META_VIOLATION",
                            message=f"Object not balanced: {balance[0]:.2f}/{balance[1]:.2f}",
                            severity=ValidationSeverity.ERROR,
                            value=balance,
                        )
                    )
                    score -= abs(balance[0] - 50) * 2
                else:
                    issues.append(
                        ValidationIssue(
                            code="META_VIOLATION",
                            message="Object is not balanced",
                            severity=ValidationSeverity.ERROR,
                        )
                    )
                    score = 0

        elif hasattr(data, "balance"):
            balance = data.balance
            if balance[0] != 50.0 or balance[1] != 50.0:
                issues.append(
                    ValidationIssue(
                        code="META_VIOLATION",
                        message=f"Balance is {balance[0]:.2f}/{balance[1]:.2f}, expected 50/50",
                        severity=ValidationSeverity.ERROR,
                        value=balance,
                    )
                )
                score -= abs(balance[0] - 50) * 2

        else:
            issues.append(
                ValidationIssue(
                    code="UNKNOWN_FORMAT",
                    message="Cannot determine balance from data format",
                    severity=ValidationSeverity.WARNING,
                )
            )
            score -= 10

        valid = (
            len(
                [
                    i
                    for i in issues
                    if i.severity in [ValidationSeverity.ERROR, ValidationSeverity.CRITICAL]
                ]
            )
            == 0
        )
        return self._create_report(valid, issues, max(0, score))
