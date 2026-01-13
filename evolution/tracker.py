"""
Evolution Tracker
=================
Tracks evolution of entities while maintaining META 50/50 equilibrium.
Evolution represents balanced change: growth/decay at 50/50.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Generic, TypeVar
from uuid import UUID

from core.equilibrium import MetaEquilibrium
from core.proportions import (
    ProportionValidator,
    calculate_50_50,
    calculate_52_48,
)

T = TypeVar("T")


class EvolutionPhase(Enum):
    """Phases of evolution."""

    GENESIS = "genesis"  # Initial creation
    GROWTH = "growth"  # Expansion phase
    MATURATION = "maturation"  # Stabilization phase
    TRANSFORMATION = "transformation"  # Major change phase
    DECAY = "decay"  # Reduction phase
    EQUILIBRIUM = "equilibrium"  # Balanced state


class EvolutionDirection(Enum):
    """Direction of evolutionary change."""

    POSITIVE = "positive"  # Growth/expansion
    NEGATIVE = "negative"  # Decay/contraction
    NEUTRAL = "neutral"  # No net change (balanced)


@dataclass
class EvolutionDelta:
    """
    Represents a change in evolution.
    Deltas must maintain META 50/50 between positive and negative components.
    """

    positive_change: float
    negative_change: float
    timestamp: datetime = field(default_factory=datetime.now)
    description: str = ""

    def __post_init__(self):
        if self.positive_change < 0 or self.negative_change < 0:
            raise ValueError("Change values cannot be negative")
        self._meta = MetaEquilibrium()

    @property
    def is_balanced(self) -> bool:
        """Check if delta maintains META 50/50."""
        return self._meta.verify_balance(self.positive_change, self.negative_change)

    @property
    def net_change(self) -> float:
        """Net change (should be 0 for balanced evolution)."""
        return self.positive_change - self.negative_change

    @property
    def total_magnitude(self) -> float:
        """Total magnitude of change."""
        return self.positive_change + self.negative_change

    @property
    def direction(self) -> EvolutionDirection:
        """Determine direction of change."""
        if self.net_change > 0:
            return EvolutionDirection.POSITIVE
        elif self.net_change < 0:
            return EvolutionDirection.NEGATIVE
        return EvolutionDirection.NEUTRAL

    @property
    def balance_ratio(self) -> tuple[float, float]:
        """Get balance ratio."""
        return self._meta.calculate_balance(self.positive_change, self.negative_change)

    def validate(self) -> None:
        """Validate delta maintains META 50/50."""
        if not self.is_balanced:
            ratio = self.balance_ratio
            raise ValueError(
                f"Evolution delta violates META 50/50: +{ratio[0]:.2f}%/-{ratio[1]:.2f}%"
            )


@dataclass
class EvolutionSnapshot:
    """
    A snapshot of an entity's evolutionary state at a point in time.
    """

    entity_id: UUID
    timestamp: datetime
    phase: EvolutionPhase
    positive_energy: float
    negative_energy: float
    attributes: dict[str, float] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        self._meta = MetaEquilibrium()

    @property
    def is_balanced(self) -> bool:
        """Check if snapshot is META balanced."""
        return self._meta.verify_balance(self.positive_energy, self.negative_energy)

    @property
    def total_energy(self) -> float:
        """Total energy in the snapshot."""
        return self.positive_energy + self.negative_energy

    @property
    def balance(self) -> tuple[float, float]:
        """Get energy balance ratio."""
        return self._meta.calculate_balance(self.positive_energy, self.negative_energy)


class EvolutionState:
    """
    Current evolutionary state of an entity.
    Maintains META 50/50 balance between positive and negative energy.
    """

    def __init__(
        self,
        entity_id: UUID,
        initial_energy: float = 100.0,
        phase: EvolutionPhase = EvolutionPhase.GENESIS,
    ):
        self._entity_id = entity_id
        self._phase = phase
        self._meta = MetaEquilibrium()

        # Initialize with balanced energy
        pos, neg = calculate_50_50(initial_energy)
        self._positive_energy = pos
        self._negative_energy = neg

        # Operational split for structure/flexibility
        self._structure, self._flexibility = calculate_52_48(initial_energy)

        self._created_at = datetime.now()
        self._updated_at = self._created_at
        self._generation = 0

    @property
    def entity_id(self) -> UUID:
        return self._entity_id

    @property
    def phase(self) -> EvolutionPhase:
        return self._phase

    @property
    def positive_energy(self) -> float:
        return self._positive_energy

    @property
    def negative_energy(self) -> float:
        return self._negative_energy

    @property
    def total_energy(self) -> float:
        return self._positive_energy + self._negative_energy

    @property
    def generation(self) -> int:
        return self._generation

    @property
    def is_balanced(self) -> bool:
        """Check if state maintains META 50/50."""
        return self._meta.verify_balance(self._positive_energy, self._negative_energy)

    @property
    def balance(self) -> tuple[float, float]:
        """Get current balance ratio."""
        return self._meta.calculate_balance(self._positive_energy, self._negative_energy)

    @property
    def operational_ratio(self) -> tuple[float, float]:
        """Get operational 52/48 ratio."""
        total = self._structure + self._flexibility
        if total == 0:
            return (52.0, 48.0)
        return (self._structure / total * 100, self._flexibility / total * 100)

    def apply_delta(self, delta: EvolutionDelta) -> None:
        """
        Apply an evolution delta to the state.
        Delta must be balanced to maintain META 50/50.
        """
        delta.validate()  # Raises if not balanced

        self._positive_energy += delta.positive_change
        self._negative_energy += delta.negative_change

        # Update operational components proportionally
        self._structure, self._flexibility = calculate_52_48(self.total_energy)

        self._updated_at = datetime.now()
        self._generation += 1

    def transition_phase(self, new_phase: EvolutionPhase) -> None:
        """Transition to a new evolution phase."""
        self._phase = new_phase
        self._updated_at = datetime.now()

    def snapshot(self) -> EvolutionSnapshot:
        """Create a snapshot of current state."""
        return EvolutionSnapshot(
            entity_id=self._entity_id,
            timestamp=datetime.now(),
            phase=self._phase,
            positive_energy=self._positive_energy,
            negative_energy=self._negative_energy,
            attributes={
                "structure": self._structure,
                "flexibility": self._flexibility,
                "generation": self._generation,
            },
            metadata={
                "created_at": self._created_at.isoformat(),
                "updated_at": self._updated_at.isoformat(),
            },
        )

    def prove_meta_meaning(self) -> dict[str, Any]:
        """Generate META compliance proof."""
        balance = self.balance
        operational = self.operational_ratio

        return {
            "entity_id": str(self._entity_id),
            "phase": self._phase.value,
            "generation": self._generation,
            "energy": {
                "positive": self._positive_energy,
                "negative": self._negative_energy,
                "total": self.total_energy,
                "balance": f"{balance[0]:.2f}/{balance[1]:.2f}",
            },
            "meta_valid": self.is_balanced,
            "operational": {
                "structure": self._structure,
                "flexibility": self._flexibility,
                "ratio": f"{operational[0]:.2f}/{operational[1]:.2f}",
            },
            "proof": (
                "Evolution state maintains META 50/50 equilibrium"
                if self.is_balanced
                else "Evolution state violates META 50/50"
            ),
        }


class EvolutionTracker(Generic[T]):
    """
    Tracks evolution of entities over time.
    Ensures all evolutionary changes maintain META 50/50 balance.
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        self._meta = meta_equilibrium or MetaEquilibrium()
        self._validator = ProportionValidator(self._meta)
        self._states: dict[UUID, EvolutionState] = {}
        self._history: dict[UUID, list[EvolutionSnapshot]] = {}
        self._deltas: dict[UUID, list[EvolutionDelta]] = {}

    @property
    def tracked_count(self) -> int:
        """Number of entities being tracked."""
        return len(self._states)

    def register(
        self,
        entity_id: UUID,
        initial_energy: float = 100.0,
        phase: EvolutionPhase = EvolutionPhase.GENESIS,
    ) -> EvolutionState:
        """
        Register an entity for evolution tracking.

        Args:
            entity_id: UUID of the entity
            initial_energy: Starting energy (split 50/50)
            phase: Initial evolution phase

        Returns:
            The created EvolutionState
        """
        if entity_id in self._states:
            raise ValueError(f"Entity already registered: {entity_id}")

        state = EvolutionState(entity_id, initial_energy, phase)
        self._states[entity_id] = state
        self._history[entity_id] = [state.snapshot()]
        self._deltas[entity_id] = []

        return state

    def unregister(self, entity_id: UUID) -> EvolutionState | None:
        """Remove an entity from tracking."""
        state = self._states.pop(entity_id, None)
        if state:
            self._history.pop(entity_id, None)
            self._deltas.pop(entity_id, None)
        return state

    def get_state(self, entity_id: UUID) -> EvolutionState | None:
        """Get current evolution state of an entity."""
        return self._states.get(entity_id)

    def get_history(self, entity_id: UUID) -> list[EvolutionSnapshot]:
        """Get evolution history of an entity."""
        return self._history.get(entity_id, []).copy()

    def get_deltas(self, entity_id: UUID) -> list[EvolutionDelta]:
        """Get all deltas applied to an entity."""
        return self._deltas.get(entity_id, []).copy()

    def evolve(
        self, entity_id: UUID, positive_change: float, negative_change: float, description: str = ""
    ) -> EvolutionDelta:
        """
        Apply evolution to an entity.
        Changes must be balanced (META 50/50).

        Args:
            entity_id: Entity to evolve
            positive_change: Positive energy change
            negative_change: Negative energy change
            description: Description of the change

        Returns:
            The applied EvolutionDelta

        Raises:
            ValueError: If entity not found or delta unbalanced
        """
        state = self._states.get(entity_id)
        if state is None:
            raise ValueError(f"Entity not registered: {entity_id}")

        delta = EvolutionDelta(
            positive_change=positive_change,
            negative_change=negative_change,
            description=description,
        )

        # Apply delta (validates internally)
        state.apply_delta(delta)

        # Record history
        self._history[entity_id].append(state.snapshot())
        self._deltas[entity_id].append(delta)

        return delta

    def evolve_balanced(
        self, entity_id: UUID, magnitude: float, description: str = ""
    ) -> EvolutionDelta:
        """
        Apply balanced evolution (automatically 50/50 split).

        Args:
            entity_id: Entity to evolve
            magnitude: Total magnitude of change
            description: Description of the change

        Returns:
            The applied EvolutionDelta
        """
        half = magnitude / 2
        return self.evolve(entity_id, half, half, description)

    def transition(self, entity_id: UUID, new_phase: EvolutionPhase) -> None:
        """
        Transition an entity to a new evolution phase.

        Args:
            entity_id: Entity to transition
            new_phase: New evolution phase
        """
        state = self._states.get(entity_id)
        if state is None:
            raise ValueError(f"Entity not registered: {entity_id}")

        state.transition_phase(new_phase)
        self._history[entity_id].append(state.snapshot())

    def get_generation(self, entity_id: UUID) -> int:
        """Get current generation of an entity."""
        state = self._states.get(entity_id)
        return state.generation if state else -1

    def validate_all(self) -> dict[str, Any]:
        """Validate all tracked entities maintain META 50/50."""
        valid_count = 0
        invalid_count = 0
        entity_reports = []

        for entity_id, state in self._states.items():
            is_valid = state.is_balanced
            if is_valid:
                valid_count += 1
            else:
                invalid_count += 1

            entity_reports.append(
                {
                    "entity_id": str(entity_id),
                    "phase": state.phase.value,
                    "generation": state.generation,
                    "balanced": is_valid,
                }
            )

        return {
            "tracked_entities": self.tracked_count,
            "valid": valid_count,
            "invalid": invalid_count,
            "all_valid": invalid_count == 0,
            "entities": entity_reports,
        }

    def prove_tracker_meta_meaning(self) -> dict[str, Any]:
        """Generate META proof for entire tracker."""
        validation = self.validate_all()
        state_proofs = [state.prove_meta_meaning() for state in self._states.values()]

        return {
            **validation,
            "state_proofs": state_proofs,
            "proof": (
                "Evolution tracker maintains META 50/50 equilibrium"
                if validation["all_valid"]
                else "Evolution tracker has entities violating META 50/50"
            ),
        }


class EvolutionMetrics:
    """
    Calculates evolution metrics while maintaining META 50/50 awareness.
    """

    def __init__(self, tracker: EvolutionTracker):
        self._tracker = tracker
        self._meta = MetaEquilibrium()

    def calculate_velocity(self, entity_id: UUID) -> float:
        """
        Calculate evolution velocity (change per generation).
        Returns average delta magnitude per generation.
        """
        deltas = self._tracker.get_deltas(entity_id)
        if not deltas:
            return 0.0

        total_magnitude = sum(d.total_magnitude for d in deltas)
        return total_magnitude / len(deltas)

    def calculate_stability(self, entity_id: UUID) -> float:
        """
        Calculate evolution stability (0-1 scale).
        Higher stability = closer to META 50/50 balance.
        """
        state = self._tracker.get_state(entity_id)
        if state is None:
            return 0.0

        balance = state.balance
        # Perfect balance (50/50) = 1.0 stability
        deviation = abs(balance[0] - 50.0)
        return max(0.0, 1.0 - (deviation / 50.0))

    def calculate_momentum(self, entity_id: UUID, window: int = 5) -> float:
        """
        Calculate recent evolution momentum.
        Positive = growing, Negative = decaying, Zero = balanced.
        """
        deltas = self._tracker.get_deltas(entity_id)
        if not deltas:
            return 0.0

        recent = deltas[-window:] if len(deltas) >= window else deltas
        return sum(d.net_change for d in recent) / len(recent)

    def get_phase_distribution(self) -> dict[str, int]:
        """Get distribution of entities across phases."""
        distribution: dict[str, int] = {phase.value: 0 for phase in EvolutionPhase}

        for state in self._tracker._states.values():
            distribution[state.phase.value] += 1

        return distribution

    def calculate_aggregate_balance(self) -> tuple[float, float]:
        """
        Calculate aggregate balance across all tracked entities.
        Should maintain META 50/50 at system level.
        """
        total_positive = 0.0
        total_negative = 0.0

        for state in self._tracker._states.values():
            total_positive += state.positive_energy
            total_negative += state.negative_energy

        return self._meta.calculate_balance(total_positive, total_negative)

    def generate_report(self, entity_id: UUID) -> dict[str, Any]:
        """Generate comprehensive evolution report for an entity."""
        state = self._tracker.get_state(entity_id)
        if state is None:
            return {"error": f"Entity not found: {entity_id}"}

        history = self._tracker.get_history(entity_id)
        deltas = self._tracker.get_deltas(entity_id)

        return {
            "entity_id": str(entity_id),
            "current_state": state.prove_meta_meaning(),
            "metrics": {
                "velocity": self.calculate_velocity(entity_id),
                "stability": self.calculate_stability(entity_id),
                "momentum": self.calculate_momentum(entity_id),
                "generations": state.generation,
                "snapshots": len(history),
                "deltas_applied": len(deltas),
            },
            "history_summary": {
                "first_snapshot": history[0].timestamp.isoformat() if history else None,
                "last_snapshot": history[-1].timestamp.isoformat() if history else None,
                "phases_visited": list({s.phase.value for s in history}),
            },
        }
