"""
Equilibrium System
==================
META level: 50/50 (absolute balance)
OPERATIONAL level: 52/48 (structure/flexibility) enables META to function
All sub-parameters must validate against META 50/50 principle.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any


class MetaEquilibrium:
    """
    Verifies and maintains the 50/50 meta balance principle.
    All systems must prove they preserve this fundamental equilibrium.
    """

    META_RATIO = (50, 50)
    TOLERANCE = 0.0  # META level allows no deviation

    def __init__(self):
        self._validated_parameters: dict[str, tuple[float, float]] = {}

    @classmethod
    def verify_balance(cls, positive: float, negative: float) -> bool:
        """Verify that values maintain 50/50 meta balance."""
        total = abs(positive) + abs(negative)
        if total == 0:
            return True  # Empty state is balanced
        ratio_positive = abs(positive) / total * 100
        ratio_negative = abs(negative) / total * 100
        return ratio_positive == 50.0 and ratio_negative == 50.0

    @classmethod
    def calculate_balance(cls, positive: float, negative: float) -> tuple[float, float]:
        """Calculate the balance ratio between two values."""
        total = abs(positive) + abs(negative)
        if total == 0:
            return (50.0, 50.0)
        return (abs(positive) / total * 100, abs(negative) / total * 100)

    def register_parameter(self, name: str, positive: float, negative: float) -> bool:
        """
        Register a sub-parameter and validate it maintains meta 50/50.
        Returns True if parameter is valid, raises ValueError if not.
        """
        if not self.verify_balance(positive, negative):
            balance = self.calculate_balance(positive, negative)
            raise ValueError(
                f"Parameter '{name}' violates META 50/50: got {balance[0]:.2f}/{balance[1]:.2f}"
            )
        self._validated_parameters[name] = (positive, negative)
        return True

    def validate_operational_enables_meta(
        self, structure: float, flexibility: float, operational_ratio: tuple[int, int] = (52, 48)
    ) -> bool:
        """
        Validate that operational 52/48 ratio enables meta 50/50.
        The slight asymmetry (structure > flexibility) creates the
        dynamic tension that allows perfect balance to manifest.
        """
        total = structure + flexibility
        if total == 0:
            return False
        actual_structure = structure / total * 100
        actual_flexibility = flexibility / total * 100
        expected_structure, expected_flexibility = operational_ratio
        return (
            abs(actual_structure - expected_structure) < 0.01
            and abs(actual_flexibility - expected_flexibility) < 0.01
        )

    @property
    def validated_parameters(self) -> dict[str, tuple[float, float]]:
        """Return all validated parameters."""
        return self._validated_parameters.copy()


class WaveState(Enum):
    """Atom wave states: negative, neutral, positive."""

    W_MINUS = "w⁻"  # Negative wave state
    W_ZERO = "w⁰"  # Neutral wave state
    W_PLUS = "w⁺"  # Positive wave state


@dataclass
class AtomState:
    """Represents the current state distribution of an Atom."""

    w_minus: float  # Negative component
    w_zero: float  # Neutral component
    w_plus: float  # Positive component

    def __post_init__(self):
        """Validate state maintains proper distribution."""
        if any(v < 0 for v in [self.w_minus, self.w_zero, self.w_plus]):
            raise ValueError("State values cannot be negative")

    @property
    def total(self) -> float:
        return self.w_minus + self.w_zero + self.w_plus

    @property
    def polar_balance(self) -> tuple[float, float]:
        """Return balance between w⁻ and w⁺ (ignoring neutral)."""
        polar_total = self.w_minus + self.w_plus
        if polar_total == 0:
            return (50.0, 50.0)
        return (self.w_minus / polar_total * 100, self.w_plus / polar_total * 100)


class Atom:
    """
    Fundamental unit operating at 52/48 (structure/flexibility).
    Contains three wave states: [w⁻|w⁰|w⁺]

    The operational 52/48 ratio provides the slight structural bias
    that ENABLES the meta 50/50 balance to function dynamically.
    """

    OPERATIONAL_RATIO = (52, 48)  # Structure / Flexibility
    STRUCTURE_COMPONENT = 0.52
    FLEXIBILITY_COMPONENT = 0.48

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        self._meta = meta_equilibrium or MetaEquilibrium()
        self._state = AtomState(w_minus=0.5, w_zero=0.0, w_plus=0.5)
        self._structure = self.STRUCTURE_COMPONENT
        self._flexibility = self.FLEXIBILITY_COMPONENT

    @property
    def state(self) -> AtomState:
        """Current atom state [w⁻|w⁰|w⁺]."""
        return self._state

    @property
    def operational_ratio(self) -> tuple[float, float]:
        """Return current operational ratio (structure/flexibility)."""
        total = self._structure + self._flexibility
        return (self._structure / total * 100, self._flexibility / total * 100)

    def set_state(self, w_minus: float, w_zero: float, w_plus: float) -> None:
        """
        Set atom state. Validates that polar components (w⁻, w⁺)
        maintain meta 50/50 balance.
        """
        new_state = AtomState(w_minus, w_zero, w_plus)
        if not self._meta.verify_balance(w_minus, w_plus):
            balance = self._meta.calculate_balance(w_minus, w_plus)
            raise ValueError(
                f"Polar states must maintain META 50/50: "
                f"got w⁻={balance[0]:.2f}% / w⁺={balance[1]:.2f}%"
            )
        self._state = new_state

    def validate_meta_compliance(self) -> bool:
        """Verify this atom's polar balance maintains META 50/50."""
        return self._meta.verify_balance(self._state.w_minus, self._state.w_plus)

    def validate_operational_compliance(self) -> bool:
        """Verify this atom operates at 52/48 ratio."""
        return self._meta.validate_operational_enables_meta(
            self._structure, self._flexibility, self.OPERATIONAL_RATIO
        )

    def prove_meta_meaning(self) -> dict[str, Any]:
        """
        Prove this atom maintains meta 50/50 meaning.
        Returns validation report for all sub-parameters.
        """
        polar_balance = self._state.polar_balance
        operational = self.operational_ratio

        return {
            "meta_valid": self.validate_meta_compliance(),
            "meta_balance": {
                "w_minus": polar_balance[0],
                "w_plus": polar_balance[1],
                "is_50_50": polar_balance == (50.0, 50.0),
            },
            "operational_valid": self.validate_operational_compliance(),
            "operational_ratio": {
                "structure": operational[0],
                "flexibility": operational[1],
                "is_52_48": abs(operational[0] - 52) < 0.01,
            },
            "state": {
                "w⁻": self._state.w_minus,
                "w⁰": self._state.w_zero,
                "w⁺": self._state.w_plus,
            },
        }

    def __repr__(self) -> str:
        return (
            f"Atom[w⁻={self._state.w_minus}|"
            f"w⁰={self._state.w_zero}|"
            f"w⁺={self._state.w_plus}] "
            f"@{self.OPERATIONAL_RATIO[0]}/{self.OPERATIONAL_RATIO[1]}"
        )


class SubParameter:
    """
    A sub-parameter that must validate against META 50/50 principle.
    Every sub-parameter carries proof of its meta compliance.
    """

    def __init__(
        self,
        name: str,
        positive_value: float,
        negative_value: float,
        meta_equilibrium: MetaEquilibrium | None = None,
    ):
        self._meta = meta_equilibrium or MetaEquilibrium()
        self._name = name
        self._positive = positive_value
        self._negative = negative_value
        self._validate()

    def _validate(self) -> None:
        """Validate this parameter maintains META 50/50."""
        self._meta.register_parameter(self._name, self._positive, self._negative)

    @property
    def name(self) -> str:
        return self._name

    @property
    def values(self) -> tuple[float, float]:
        """Return (positive, negative) values."""
        return (self._positive, self._negative)

    @property
    def balance(self) -> tuple[float, float]:
        """Return balance ratio."""
        return self._meta.calculate_balance(self._positive, self._negative)

    def prove_meta_meaning(self) -> dict[str, Any]:
        """Prove this sub-parameter maintains META 50/50 meaning."""
        balance = self.balance
        return {
            "name": self._name,
            "positive": self._positive,
            "negative": self._negative,
            "balance": f"{balance[0]:.2f}/{balance[1]:.2f}",
            "meta_valid": balance == (50.0, 50.0),
            "proof": "Maintains META 50/50 equilibrium",
        }

    def __repr__(self) -> str:
        return f"SubParameter({self._name}: +{self._positive}/-{self._negative})"
