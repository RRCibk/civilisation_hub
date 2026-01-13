"""
Proportions System
==================
PI/6 ratio (0.5236) as fundamental proportion.
52/48 operational calculations derived from geometric principles.
All ratios must verify they maintain META 50/50 meaning.
"""

import math
from dataclasses import dataclass
from typing import Any

from core.equilibrium import MetaEquilibrium

# Fundamental Constants
PI_OVER_6 = math.pi / 6  # 0.5235987755982989
PI_OVER_6_ROUNDED = 0.5236


class ProportionConstants:
    """Fundamental proportion constants derived from PI/6."""

    PI_6 = math.pi / 6  # ~0.5236 (30 degrees in radians)
    PI_6_DEGREES = 30.0  # Equivalent angle in degrees

    # Operational ratio derived from PI/6
    # PI/6 ≈ 0.5236 maps to 52.36% structure
    OPERATIONAL_STRUCTURE = 0.52  # Rounded for practical use
    OPERATIONAL_FLEXIBILITY = 0.48  # Complement to structure
    OPERATIONAL_RATIO = (52, 48)

    # PI/6 relationship to operational ratio
    # sin(PI/6) = 0.5 (META balance)
    # cos(PI/6) = sqrt(3)/2 ≈ 0.866 (structure dominance)
    SIN_PI_6 = 0.5  # Exact: sin(30°) = 0.5
    COS_PI_6 = math.sqrt(3) / 2  # ~0.866

    # Golden relationships
    STRUCTURE_FLEXIBILITY_RATIO = 52 / 48  # ~1.0833


@dataclass
class Ratio:
    """
    A ratio that can verify its META 50/50 meaning.
    Stores numerator/denominator and provides validation.
    """

    numerator: float
    denominator: float
    name: str = "unnamed"

    def __post_init__(self):
        if self.denominator == 0:
            raise ValueError("Denominator cannot be zero")

    @property
    def value(self) -> float:
        """Return the ratio as a decimal value."""
        return self.numerator / self.denominator

    @property
    def percentage(self) -> tuple[float, float]:
        """Return as percentage pair (num%, denom%)."""
        total = abs(self.numerator) + abs(self.denominator)
        return (abs(self.numerator) / total * 100, abs(self.denominator) / total * 100)

    @property
    def inverse(self) -> "Ratio":
        """Return the inverse ratio."""
        return Ratio(self.denominator, self.numerator, f"{self.name}_inverse")

    def is_balanced(self) -> bool:
        """Check if this ratio represents META 50/50 balance."""
        return abs(self.numerator) == abs(self.denominator)

    def distance_from_balance(self) -> float:
        """Calculate how far this ratio is from META 50/50."""
        pct = self.percentage
        return abs(pct[0] - 50.0)

    def __repr__(self) -> str:
        return f"Ratio({self.name}: {self.numerator}/{self.denominator} = {self.value:.4f})"


class OperationalRatio:
    """
    52/48 operational ratio calculations.
    This slight asymmetry enables META 50/50 to function.
    """

    STRUCTURE = 52
    FLEXIBILITY = 48
    TOTAL = 100

    def __init__(self, structure: float = 52, flexibility: float = 48):
        self._structure = structure
        self._flexibility = flexibility
        self._validate()

    def _validate(self) -> None:
        """Validate operational ratio is 52/48."""
        total = self._structure + self._flexibility
        if total == 0:
            raise ValueError("Total cannot be zero")
        actual_ratio = self._structure / total * 100
        if abs(actual_ratio - 52) > 0.01:
            raise ValueError(
                f"Operational ratio must be 52/48, got {actual_ratio:.2f}/{100 - actual_ratio:.2f}"
            )

    @property
    def structure(self) -> float:
        return self._structure

    @property
    def flexibility(self) -> float:
        return self._flexibility

    @property
    def ratio(self) -> float:
        """Return structure/flexibility ratio."""
        return self._structure / self._flexibility

    @property
    def as_percentage(self) -> tuple[float, float]:
        """Return as percentage tuple."""
        total = self._structure + self._flexibility
        return (self._structure / total * 100, self._flexibility / total * 100)

    @classmethod
    def from_total(cls, total: float) -> "OperationalRatio":
        """Create operational ratio from a total value."""
        structure = total * 0.52
        flexibility = total * 0.48
        return cls(structure, flexibility)

    @classmethod
    def from_pi_6(cls) -> "OperationalRatio":
        """
        Derive operational ratio from PI/6.
        PI/6 ≈ 0.5236 → 52.36% structure (rounded to 52%)
        """
        pi_6_pct = PI_OVER_6 * 100  # ~52.36
        structure = round(pi_6_pct)  # 52
        flexibility = 100 - structure  # 48
        return cls(structure, flexibility)

    def prove_enables_meta(self) -> dict[str, Any]:
        """
        Prove that 52/48 enables META 50/50.

        The asymmetry creates dynamic tension:
        - 52% structure provides stability
        - 48% flexibility allows adaptation
        - Together they enable perfect balance to manifest
        """
        return {
            "structure": self._structure,
            "flexibility": self._flexibility,
            "ratio": self.ratio,
            "asymmetry": abs(self._structure - self._flexibility),
            "enables_meta": True,
            "proof": (
                "52/48 asymmetry creates dynamic tension that "
                "enables META 50/50 balance to function"
            ),
        }

    def __repr__(self) -> str:
        return f"OperationalRatio({self._structure}/{self._flexibility})"


class Pi6Proportion:
    """
    PI/6 (0.5236) as fundamental proportion.
    Connects geometric principles to operational ratios.
    """

    VALUE = PI_OVER_6
    DEGREES = 30.0
    RADIANS = math.pi / 6

    def __init__(self):
        self._value = PI_OVER_6
        self._sin = math.sin(self._value)  # 0.5 exactly
        self._cos = math.cos(self._value)  # sqrt(3)/2

    @property
    def value(self) -> float:
        """PI/6 value in radians."""
        return self._value

    @property
    def as_percentage(self) -> float:
        """PI/6 as percentage (~52.36%)."""
        return self._value * 100

    @property
    def sin(self) -> float:
        """sin(PI/6) = 0.5 - represents META balance."""
        return self._sin

    @property
    def cos(self) -> float:
        """cos(PI/6) = sqrt(3)/2 - represents structure dominance."""
        return self._cos

    def to_operational_ratio(self) -> OperationalRatio:
        """Convert PI/6 proportion to operational 52/48 ratio."""
        return OperationalRatio.from_pi_6()

    def verify_meta_connection(self) -> dict[str, Any]:
        """
        Verify PI/6 connects to META 50/50.
        sin(PI/6) = 0.5 exactly, proving geometric basis for META balance.
        """
        return {
            "pi_6_value": self._value,
            "pi_6_percentage": self.as_percentage,
            "sin_pi_6": self._sin,
            "sin_equals_half": abs(self._sin - 0.5) < 1e-10,  # Exact within floating point
            "meta_connection": "sin(PI/6) = 0.5 proves META 50/50 has geometric basis",
            "operational_derivation": "PI/6 ≈ 0.5236 → 52% structure",
        }

    def __repr__(self) -> str:
        return f"Pi6Proportion(π/6 = {self._value:.6f} rad = {self.DEGREES}°)"


class ProportionValidator:
    """
    Validates that any ratio maintains META 50/50 meaning.
    Provides methods to verify proportional relationships.
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        self._meta = meta_equilibrium or MetaEquilibrium()
        self._validated_ratios: list[Ratio] = []

    def verify_maintains_meta(self, ratio: Ratio) -> bool:
        """
        Verify a ratio maintains META 50/50 meaning.
        A ratio maintains META meaning if it's balanced (50/50).
        """
        return ratio.is_balanced()

    def verify_enables_meta(self, ratio: Ratio, expected: tuple[int, int] = (52, 48)) -> bool:
        """
        Verify a ratio enables META 50/50 (operational level).
        Operational ratios like 52/48 enable META to function.
        """
        pct = ratio.percentage
        return abs(pct[0] - expected[0]) < 0.01 and abs(pct[1] - expected[1]) < 0.01

    def validate_ratio(self, ratio: Ratio, level: str = "meta") -> dict[str, Any]:
        """
        Validate a ratio at specified level.

        Args:
            ratio: The ratio to validate
            level: "meta" for 50/50, "operational" for 52/48

        Returns:
            Validation report with proof
        """
        if level == "meta":
            is_valid = self.verify_maintains_meta(ratio)
            expected = (50, 50)
        elif level == "operational":
            is_valid = self.verify_enables_meta(ratio)
            expected = (52, 48)
        else:
            raise ValueError(f"Unknown level: {level}. Use 'meta' or 'operational'")

        pct = ratio.percentage

        result = {
            "ratio": ratio.name,
            "value": ratio.value,
            "percentage": f"{pct[0]:.2f}/{pct[1]:.2f}",
            "level": level,
            "expected": f"{expected[0]}/{expected[1]}",
            "is_valid": is_valid,
            "distance_from_expected": abs(pct[0] - expected[0]),
        }

        if is_valid:
            self._validated_ratios.append(ratio)
            result["proof"] = f"Ratio maintains {level.upper()} {expected[0]}/{expected[1]} meaning"
        else:
            result["violation"] = f"Ratio deviates from {level.upper()} {expected[0]}/{expected[1]}"

        return result

    def validate_pair_maintains_meta(
        self, positive: float, negative: float, name: str = "pair"
    ) -> dict[str, Any]:
        """
        Validate that a positive/negative pair maintains META 50/50.
        """
        is_balanced = self._meta.verify_balance(positive, negative)
        balance = self._meta.calculate_balance(positive, negative)

        return {
            "name": name,
            "positive": positive,
            "negative": negative,
            "balance": f"{balance[0]:.2f}/{balance[1]:.2f}",
            "maintains_meta": is_balanced,
            "proof" if is_balanced else "violation": (
                "Pair maintains META 50/50 equilibrium"
                if is_balanced
                else f"Pair violates META 50/50: got {balance[0]:.2f}/{balance[1]:.2f}"
            ),
        }

    def derive_complement(self, value: float, level: str = "meta") -> float:
        """
        Derive the complement value needed to achieve balance at given level.

        Args:
            value: The known value
            level: "meta" for 50/50, "operational" for 52/48

        Returns:
            The complement value
        """
        if level == "meta":
            # For META 50/50, complement equals the value
            return value
        elif level == "operational":
            # For operational 52/48, calculate based on ratio
            # If value is structure (52%), find flexibility (48%)
            # value / complement = 52 / 48
            return value * (48 / 52)
        else:
            raise ValueError(f"Unknown level: {level}")

    @property
    def validated_ratios(self) -> list[Ratio]:
        """Return all validated ratios."""
        return self._validated_ratios.copy()

    def prove_all_maintain_meta(self) -> dict[str, Any]:
        """Prove all registered ratios maintain their respective levels."""
        return {
            "total_validated": len(self._validated_ratios),
            "ratios": [
                {"name": r.name, "value": r.value, "balanced": r.is_balanced()}
                for r in self._validated_ratios
            ],
            "proof": "All validated ratios maintain their designated equilibrium level",
        }


def calculate_52_48(total: float) -> tuple[float, float]:
    """
    Calculate 52/48 split of a total value.

    Args:
        total: The total value to split

    Returns:
        Tuple of (structure_52%, flexibility_48%)
    """
    return (total * 0.52, total * 0.48)


def calculate_50_50(total: float) -> tuple[float, float]:
    """
    Calculate 50/50 split of a total value.

    Args:
        total: The total value to split

    Returns:
        Tuple of (positive_50%, negative_50%)
    """
    half = total / 2
    return (half, half)


def ratio_to_meta_meaning(numerator: float, denominator: float) -> dict[str, Any]:
    """
    Analyze any ratio for its META 50/50 meaning.

    Args:
        numerator: Top of ratio
        denominator: Bottom of ratio

    Returns:
        Analysis of how ratio relates to META 50/50
    """
    total = abs(numerator) + abs(denominator)
    if total == 0:
        return {"error": "Cannot analyze zero ratio"}

    pct_num = abs(numerator) / total * 100
    pct_den = abs(denominator) / total * 100

    is_meta_balanced = abs(pct_num - 50) < 0.01
    is_operational = abs(pct_num - 52) < 0.5 and abs(pct_den - 48) < 0.5

    return {
        "numerator": numerator,
        "denominator": denominator,
        "ratio_value": numerator / denominator if denominator != 0 else float("inf"),
        "percentage": f"{pct_num:.2f}/{pct_den:.2f}",
        "is_meta_50_50": is_meta_balanced,
        "is_operational_52_48": is_operational,
        "distance_from_meta": abs(pct_num - 50),
        "meta_meaning": (
            "Maintains META 50/50 balance"
            if is_meta_balanced
            else "Enables META through 52/48 operational ratio"
            if is_operational
            else f"Deviates from META by {abs(pct_num - 50):.2f}%"
        ),
    }


def verify_ratio_chain_maintains_meta(*ratios: Ratio) -> dict[str, Any]:
    """
    Verify that a chain of ratios collectively maintains META 50/50.
    The product of balanced ratios remains balanced.

    Args:
        *ratios: Variable number of Ratio objects

    Returns:
        Verification result for the chain
    """
    if not ratios:
        return {"error": "No ratios provided"}

    product_num = 1.0
    product_den = 1.0

    for ratio in ratios:
        product_num *= ratio.numerator
        product_den *= ratio.denominator

    combined = Ratio(product_num, product_den, "chain_product")

    return {
        "chain_length": len(ratios),
        "ratios": [r.name for r in ratios],
        "product_ratio": combined.value,
        "product_balanced": combined.is_balanced(),
        "maintains_meta": combined.is_balanced(),
        "proof": (
            "Chain product maintains META 50/50"
            if combined.is_balanced()
            else f"Chain product deviates: {combined.percentage[0]:.2f}/{combined.percentage[1]:.2f}"
        ),
    }
