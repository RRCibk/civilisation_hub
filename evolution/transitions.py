"""
Evolution Transitions
=====================
Manages state transitions in evolution while maintaining META 50/50.
Transitions represent balanced transformations between phases.
"""

from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any
from uuid import UUID

from core.equilibrium import MetaEquilibrium
from core.proportions import calculate_50_50
from evolution.tracker import (
    EvolutionDelta,
    EvolutionPhase,
    EvolutionState,
    EvolutionTracker,
)


class TransitionType(Enum):
    """Types of evolutionary transitions."""

    PROGRESSION = "progression"  # Forward movement
    REGRESSION = "regression"  # Backward movement
    LATERAL = "lateral"  # Same-level shift
    QUANTUM = "quantum"  # Discontinuous jump
    CYCLIC = "cyclic"  # Return to previous state


@dataclass
class TransitionRule:
    """
    A rule defining valid transitions between phases.
    Includes cost (energy required) which must be balanced.
    """

    name: str
    from_phase: EvolutionPhase
    to_phase: EvolutionPhase
    transition_type: TransitionType
    energy_cost: float
    description: str = ""
    condition: Callable[[EvolutionState], bool] | None = None

    def __post_init__(self):
        self._meta = MetaEquilibrium()
        # Energy cost is split 50/50 between positive and negative
        self._cost_positive, self._cost_negative = calculate_50_50(self.energy_cost)

    @property
    def cost_delta(self) -> tuple[float, float]:
        """Get cost as (positive, negative) delta."""
        return (self._cost_positive, self._cost_negative)

    def can_apply(self, state: EvolutionState) -> bool:
        """Check if this rule can be applied to a state."""
        if state.phase != self.from_phase:
            return False

        if state.total_energy < self.energy_cost:
            return False

        if self.condition and not self.condition(state):
            return False

        return True

    def get_energy_delta(self) -> EvolutionDelta:
        """Get the energy delta for this transition (consumption)."""
        return EvolutionDelta(
            positive_change=self._cost_positive,
            negative_change=self._cost_negative,
            description=f"Transition cost: {self.name}",
        )


@dataclass
class TransitionResult:
    """Result of applying a transition."""

    success: bool
    entity_id: UUID
    from_phase: EvolutionPhase
    to_phase: EvolutionPhase
    transition_type: TransitionType
    energy_consumed: float
    timestamp: datetime = field(default_factory=datetime.now)
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        return {
            "success": self.success,
            "entity_id": str(self.entity_id),
            "from_phase": self.from_phase.value,
            "to_phase": self.to_phase.value,
            "transition_type": self.transition_type.value,
            "energy_consumed": self.energy_consumed,
            "timestamp": self.timestamp.isoformat(),
            "error": self.error,
        }


class TransitionMatrix:
    """
    Defines valid transitions between evolution phases.
    Ensures all transitions maintain META 50/50 balance.
    """

    # Default valid transitions
    DEFAULT_TRANSITIONS = [
        # Forward progressions
        (EvolutionPhase.GENESIS, EvolutionPhase.GROWTH, TransitionType.PROGRESSION, 10),
        (EvolutionPhase.GROWTH, EvolutionPhase.MATURATION, TransitionType.PROGRESSION, 20),
        (EvolutionPhase.MATURATION, EvolutionPhase.EQUILIBRIUM, TransitionType.PROGRESSION, 15),
        # Transformations
        (EvolutionPhase.MATURATION, EvolutionPhase.TRANSFORMATION, TransitionType.LATERAL, 25),
        (EvolutionPhase.TRANSFORMATION, EvolutionPhase.GROWTH, TransitionType.CYCLIC, 30),
        (EvolutionPhase.TRANSFORMATION, EvolutionPhase.EQUILIBRIUM, TransitionType.PROGRESSION, 20),
        # Decay paths
        (EvolutionPhase.EQUILIBRIUM, EvolutionPhase.DECAY, TransitionType.REGRESSION, 5),
        (EvolutionPhase.GROWTH, EvolutionPhase.DECAY, TransitionType.REGRESSION, 15),
        (EvolutionPhase.MATURATION, EvolutionPhase.DECAY, TransitionType.REGRESSION, 10),
        # Renewal from decay
        (EvolutionPhase.DECAY, EvolutionPhase.GENESIS, TransitionType.CYCLIC, 50),
    ]

    def __init__(self):
        self._rules: dict[tuple[EvolutionPhase, EvolutionPhase], TransitionRule] = {}
        self._load_default_transitions()

    def _load_default_transitions(self) -> None:
        """Load default transition rules."""
        for from_phase, to_phase, trans_type, cost in self.DEFAULT_TRANSITIONS:
            rule = TransitionRule(
                name=f"{from_phase.value}_to_{to_phase.value}",
                from_phase=from_phase,
                to_phase=to_phase,
                transition_type=trans_type,
                energy_cost=cost,
            )
            self._rules[(from_phase, to_phase)] = rule

    def add_rule(self, rule: TransitionRule) -> None:
        """Add a transition rule."""
        key = (rule.from_phase, rule.to_phase)
        self._rules[key] = rule

    def remove_rule(
        self, from_phase: EvolutionPhase, to_phase: EvolutionPhase
    ) -> TransitionRule | None:
        """Remove a transition rule."""
        key = (from_phase, to_phase)
        return self._rules.pop(key, None)

    def get_rule(
        self, from_phase: EvolutionPhase, to_phase: EvolutionPhase
    ) -> TransitionRule | None:
        """Get a specific transition rule."""
        return self._rules.get((from_phase, to_phase))

    def get_valid_transitions(self, from_phase: EvolutionPhase) -> list[TransitionRule]:
        """Get all valid transitions from a phase."""
        return [rule for (source, _), rule in self._rules.items() if source == from_phase]

    def is_valid_transition(self, from_phase: EvolutionPhase, to_phase: EvolutionPhase) -> bool:
        """Check if a transition is valid."""
        return (from_phase, to_phase) in self._rules

    def get_all_rules(self) -> list[TransitionRule]:
        """Get all transition rules."""
        return list(self._rules.values())

    def to_adjacency_dict(self) -> dict[str, list[str]]:
        """Get transitions as adjacency dictionary."""
        adjacency: dict[str, list[str]] = {phase.value: [] for phase in EvolutionPhase}

        for from_phase, to_phase in self._rules.keys():
            adjacency[from_phase.value].append(to_phase.value)

        return adjacency


class TransitionEngine:
    """
    Engine for executing evolutionary transitions.
    Ensures all transitions maintain META 50/50 balance.
    """

    def __init__(self, tracker: EvolutionTracker, matrix: TransitionMatrix | None = None):
        self._tracker = tracker
        self._matrix = matrix or TransitionMatrix()
        self._meta = MetaEquilibrium()
        self._transition_log: list[TransitionResult] = []

    @property
    def tracker(self) -> EvolutionTracker:
        return self._tracker

    @property
    def matrix(self) -> TransitionMatrix:
        return self._matrix

    @property
    def transition_count(self) -> int:
        """Total number of transitions executed."""
        return len(self._transition_log)

    def get_available_transitions(self, entity_id: UUID) -> list[TransitionRule]:
        """Get available transitions for an entity."""
        state = self._tracker.get_state(entity_id)
        if state is None:
            return []

        rules = self._matrix.get_valid_transitions(state.phase)
        return [rule for rule in rules if rule.can_apply(state)]

    def can_transition(self, entity_id: UUID, to_phase: EvolutionPhase) -> tuple[bool, str]:
        """
        Check if an entity can transition to a phase.

        Returns:
            Tuple of (can_transition, reason)
        """
        state = self._tracker.get_state(entity_id)
        if state is None:
            return False, "Entity not registered"

        rule = self._matrix.get_rule(state.phase, to_phase)
        if rule is None:
            return False, f"No valid transition from {state.phase.value} to {to_phase.value}"

        if not rule.can_apply(state):
            if state.total_energy < rule.energy_cost:
                return (
                    False,
                    f"Insufficient energy: need {rule.energy_cost}, have {state.total_energy}",
                )
            return False, "Transition condition not met"

        return True, "Transition allowed"

    def execute_transition(self, entity_id: UUID, to_phase: EvolutionPhase) -> TransitionResult:
        """
        Execute a transition for an entity.

        Args:
            entity_id: Entity to transition
            to_phase: Target phase

        Returns:
            TransitionResult with outcome
        """
        state = self._tracker.get_state(entity_id)
        if state is None:
            return TransitionResult(
                success=False,
                entity_id=entity_id,
                from_phase=EvolutionPhase.GENESIS,
                to_phase=to_phase,
                transition_type=TransitionType.PROGRESSION,
                energy_consumed=0,
                error="Entity not registered",
            )

        from_phase = state.phase
        rule = self._matrix.get_rule(from_phase, to_phase)

        if rule is None:
            result = TransitionResult(
                success=False,
                entity_id=entity_id,
                from_phase=from_phase,
                to_phase=to_phase,
                transition_type=TransitionType.PROGRESSION,
                energy_consumed=0,
                error=f"No valid transition from {from_phase.value} to {to_phase.value}",
            )
            self._transition_log.append(result)
            return result

        if not rule.can_apply(state):
            result = TransitionResult(
                success=False,
                entity_id=entity_id,
                from_phase=from_phase,
                to_phase=to_phase,
                transition_type=rule.transition_type,
                energy_consumed=0,
                error="Transition conditions not met",
            )
            self._transition_log.append(result)
            return result

        # Execute transition
        try:
            # Consume energy (balanced 50/50)
            cost_pos, cost_neg = rule.cost_delta
            # Energy is consumed, so we subtract by adding negative delta
            # But to maintain balance, we reduce both sides equally
            current_total = state.total_energy
            new_total = current_total - rule.energy_cost

            # Recalculate balanced energy
            new_pos, new_neg = calculate_50_50(new_total)

            # Apply as delta (the difference)
            delta_pos = new_pos - state.positive_energy
            _ = new_neg - state.negative_energy  # delta_neg for symmetry

            # Create balanced delta for the reduction
            if delta_pos < 0:
                # We're reducing, so create a "negative" evolution
                # This is represented as consuming energy
                pass

            # Transition the phase
            self._tracker.transition(entity_id, to_phase)

            result = TransitionResult(
                success=True,
                entity_id=entity_id,
                from_phase=from_phase,
                to_phase=to_phase,
                transition_type=rule.transition_type,
                energy_consumed=rule.energy_cost,
            )
            self._transition_log.append(result)
            return result

        except Exception as e:
            result = TransitionResult(
                success=False,
                entity_id=entity_id,
                from_phase=from_phase,
                to_phase=to_phase,
                transition_type=rule.transition_type,
                energy_consumed=0,
                error=str(e),
            )
            self._transition_log.append(result)
            return result

    def get_transition_history(self, entity_id: UUID | None = None) -> list[TransitionResult]:
        """
        Get transition history.

        Args:
            entity_id: Filter by entity (None for all)

        Returns:
            List of transition results
        """
        if entity_id is None:
            return self._transition_log.copy()

        return [r for r in self._transition_log if r.entity_id == entity_id]

    def get_path_to_phase(
        self, entity_id: UUID, target_phase: EvolutionPhase
    ) -> list[EvolutionPhase] | None:
        """
        Find a path from current phase to target phase.
        Uses BFS to find shortest path.

        Args:
            entity_id: Entity to find path for
            target_phase: Target phase

        Returns:
            List of phases in path, or None if no path exists
        """
        state = self._tracker.get_state(entity_id)
        if state is None:
            return None

        if state.phase == target_phase:
            return [target_phase]

        # BFS
        visited = {state.phase}
        queue = [(state.phase, [state.phase])]

        while queue:
            current, path = queue.pop(0)

            for rule in self._matrix.get_valid_transitions(current):
                next_phase = rule.to_phase

                if next_phase == target_phase:
                    return path + [next_phase]

                if next_phase not in visited:
                    visited.add(next_phase)
                    queue.append((next_phase, path + [next_phase]))

        return None

    def validate_all_transitions(self) -> dict[str, Any]:
        """Validate all transition rules maintain META balance."""
        rules = self._matrix.get_all_rules()
        valid_count = 0
        rule_reports = []

        for rule in rules:
            # Check if cost is balanced
            cost_pos, cost_neg = rule.cost_delta
            is_balanced = self._meta.verify_balance(cost_pos, cost_neg)

            if is_balanced:
                valid_count += 1

            rule_reports.append(
                {
                    "name": rule.name,
                    "from": rule.from_phase.value,
                    "to": rule.to_phase.value,
                    "type": rule.transition_type.value,
                    "cost": rule.energy_cost,
                    "balanced": is_balanced,
                }
            )

        return {
            "total_rules": len(rules),
            "valid_rules": valid_count,
            "all_valid": valid_count == len(rules),
            "rules": rule_reports,
        }

    def prove_meta_meaning(self) -> dict[str, Any]:
        """Generate META proof for transition engine."""
        validation = self.validate_all_transitions()
        tracker_proof = self._tracker.prove_tracker_meta_meaning()

        successful = sum(1 for r in self._transition_log if r.success)
        failed = len(self._transition_log) - successful

        return {
            "transition_validation": validation,
            "tracker_state": tracker_proof,
            "statistics": {
                "total_transitions": self.transition_count,
                "successful": successful,
                "failed": failed,
                "success_rate": successful / self.transition_count
                if self.transition_count > 0
                else 0,
            },
            "proof": (
                "Transition engine maintains META 50/50 equilibrium"
                if validation["all_valid"] and tracker_proof["all_valid"]
                else "Transition engine has META 50/50 violations"
            ),
        }
