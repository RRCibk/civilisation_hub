"""
Participation Tracker
=====================
Tracks participation of entities while maintaining META 50/50 equilibrium.
Participation represents balanced exchange: giving/receiving at 50/50.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Generic, TypeVar
from uuid import UUID, uuid4

from core.equilibrium import MetaEquilibrium
from core.proportions import (
    ProportionValidator,
    calculate_50_50,
    calculate_52_48,
)

T = TypeVar("T")


class ParticipationType(Enum):
    """Types of participation."""

    CONTRIBUTION = "contribution"  # Adding value
    CONSUMPTION = "consumption"  # Using value
    COLLABORATION = "collaboration"  # Joint effort
    OBSERVATION = "observation"  # Passive engagement
    FACILITATION = "facilitation"  # Enabling others


class ParticipationLevel(Enum):
    """Levels of participation engagement."""

    INACTIVE = "inactive"  # No participation
    MINIMAL = "minimal"  # Low engagement
    MODERATE = "moderate"  # Medium engagement
    ACTIVE = "active"  # High engagement
    INTENSIVE = "intensive"  # Very high engagement


class EngagementState(Enum):
    """States of engagement."""

    DORMANT = "dormant"  # Not currently engaged
    WARMING = "warming"  # Beginning to engage
    ENGAGED = "engaged"  # Actively participating
    PEAK = "peak"  # Maximum engagement
    COOLING = "cooling"  # Reducing engagement


@dataclass
class ParticipationRecord:
    """
    A record of participation activity.
    Must maintain META 50/50 between giving and receiving.
    """

    id: UUID = field(default_factory=uuid4)
    participant_id: UUID = field(default_factory=uuid4)
    participation_type: ParticipationType = ParticipationType.CONTRIBUTION
    given: float = 0.0
    received: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)
    description: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if self.given < 0 or self.received < 0:
            raise ValueError("Participation values cannot be negative")
        self._meta = MetaEquilibrium()

    @property
    def is_balanced(self) -> bool:
        """Check if record maintains META 50/50."""
        return self._meta.verify_balance(self.given, self.received)

    @property
    def balance(self) -> tuple[float, float]:
        """Get balance ratio."""
        return self._meta.calculate_balance(self.given, self.received)

    @property
    def total_exchange(self) -> float:
        """Total value exchanged."""
        return self.given + self.received

    @property
    def net_contribution(self) -> float:
        """Net contribution (given - received)."""
        return self.given - self.received

    def validate(self) -> None:
        """Validate record maintains META 50/50."""
        if not self.is_balanced:
            ratio = self.balance
            raise ValueError(
                f"Participation violates META 50/50: given={ratio[0]:.2f}%/received={ratio[1]:.2f}%"
            )


@dataclass
class ParticipationSnapshot:
    """Snapshot of participation state at a point in time."""

    participant_id: UUID
    timestamp: datetime
    level: ParticipationLevel
    engagement_state: EngagementState
    total_given: float
    total_received: float
    record_count: int
    attributes: dict[str, float] = field(default_factory=dict)

    def __post_init__(self):
        self._meta = MetaEquilibrium()

    @property
    def is_balanced(self) -> bool:
        """Check if snapshot is META balanced."""
        return self._meta.verify_balance(self.total_given, self.total_received)

    @property
    def balance(self) -> tuple[float, float]:
        """Get balance ratio."""
        return self._meta.calculate_balance(self.total_given, self.total_received)

    @property
    def total_exchange(self) -> float:
        """Total value exchanged."""
        return self.total_given + self.total_received


class ParticipationState:
    """
    Current participation state of an entity.
    Maintains META 50/50 balance between giving and receiving.
    """

    # Thresholds for level determination (total exchange)
    LEVEL_THRESHOLDS = {
        ParticipationLevel.INACTIVE: 0,
        ParticipationLevel.MINIMAL: 10,
        ParticipationLevel.MODERATE: 50,
        ParticipationLevel.ACTIVE: 200,
        ParticipationLevel.INTENSIVE: 500,
    }

    def __init__(self, participant_id: UUID, initial_exchange: float = 0.0):
        self._participant_id = participant_id
        self._meta = MetaEquilibrium()

        # Initialize with balanced exchange
        given, received = calculate_50_50(initial_exchange)
        self._total_given = given
        self._total_received = received

        # Operational split for structure/flexibility
        self._structure, self._flexibility = calculate_52_48(
            initial_exchange if initial_exchange > 0 else 100
        )

        self._level = self._calculate_level()
        self._engagement_state = EngagementState.DORMANT
        self._record_count = 0
        self._created_at = datetime.now()
        self._updated_at = self._created_at

    @property
    def participant_id(self) -> UUID:
        return self._participant_id

    @property
    def total_given(self) -> float:
        return self._total_given

    @property
    def total_received(self) -> float:
        return self._total_received

    @property
    def total_exchange(self) -> float:
        return self._total_given + self._total_received

    @property
    def level(self) -> ParticipationLevel:
        return self._level

    @property
    def engagement_state(self) -> EngagementState:
        return self._engagement_state

    @property
    def record_count(self) -> int:
        return self._record_count

    @property
    def is_balanced(self) -> bool:
        """Check if state maintains META 50/50."""
        return self._meta.verify_balance(self._total_given, self._total_received)

    @property
    def balance(self) -> tuple[float, float]:
        """Get current balance ratio."""
        return self._meta.calculate_balance(self._total_given, self._total_received)

    @property
    def operational_ratio(self) -> tuple[float, float]:
        """Get operational 52/48 ratio."""
        total = self._structure + self._flexibility
        if total == 0:
            return (52.0, 48.0)
        return (self._structure / total * 100, self._flexibility / total * 100)

    def _calculate_level(self) -> ParticipationLevel:
        """Calculate participation level based on total exchange."""
        exchange = self.total_exchange
        level = ParticipationLevel.INACTIVE

        for lvl, threshold in sorted(
            self.LEVEL_THRESHOLDS.items(), key=lambda x: x[1], reverse=True
        ):
            if exchange >= threshold:
                level = lvl
                break

        return level

    def apply_record(self, record: ParticipationRecord) -> None:
        """
        Apply a participation record to the state.
        Record must be balanced to maintain META 50/50.
        """
        record.validate()  # Raises if not balanced

        self._total_given += record.given
        self._total_received += record.received

        # Update operational components
        self._structure, self._flexibility = calculate_52_48(self.total_exchange)

        self._level = self._calculate_level()
        self._record_count += 1
        self._updated_at = datetime.now()

        # Update engagement state based on activity
        self._update_engagement_state()

    def _update_engagement_state(self) -> None:
        """Update engagement state based on recent activity."""
        if self._record_count == 0:
            self._engagement_state = EngagementState.DORMANT
        elif self._record_count < 3:
            self._engagement_state = EngagementState.WARMING
        elif self._level in [ParticipationLevel.ACTIVE, ParticipationLevel.INTENSIVE]:
            self._engagement_state = EngagementState.PEAK
        else:
            self._engagement_state = EngagementState.ENGAGED

    def set_engagement_state(self, state: EngagementState) -> None:
        """Manually set engagement state."""
        self._engagement_state = state
        self._updated_at = datetime.now()

    def snapshot(self) -> ParticipationSnapshot:
        """Create a snapshot of current state."""
        return ParticipationSnapshot(
            participant_id=self._participant_id,
            timestamp=datetime.now(),
            level=self._level,
            engagement_state=self._engagement_state,
            total_given=self._total_given,
            total_received=self._total_received,
            record_count=self._record_count,
            attributes={"structure": self._structure, "flexibility": self._flexibility},
        )

    def prove_meta_meaning(self) -> dict[str, Any]:
        """Generate META compliance proof."""
        balance = self.balance
        operational = self.operational_ratio

        return {
            "participant_id": str(self._participant_id),
            "level": self._level.value,
            "engagement_state": self._engagement_state.value,
            "exchange": {
                "given": self._total_given,
                "received": self._total_received,
                "total": self.total_exchange,
                "balance": f"{balance[0]:.2f}/{balance[1]:.2f}",
            },
            "meta_valid": self.is_balanced,
            "operational": {
                "structure": self._structure,
                "flexibility": self._flexibility,
                "ratio": f"{operational[0]:.2f}/{operational[1]:.2f}",
            },
            "record_count": self._record_count,
            "proof": (
                "Participation state maintains META 50/50 equilibrium"
                if self.is_balanced
                else "Participation state violates META 50/50"
            ),
        }


class ParticipationTracker(Generic[T]):
    """
    Tracks participation of entities.
    Ensures all participation maintains META 50/50 balance.
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        self._meta = meta_equilibrium or MetaEquilibrium()
        self._validator = ProportionValidator(self._meta)
        self._states: dict[UUID, ParticipationState] = {}
        self._records: dict[UUID, list[ParticipationRecord]] = {}
        self._history: dict[UUID, list[ParticipationSnapshot]] = {}

    @property
    def participant_count(self) -> int:
        """Number of participants being tracked."""
        return len(self._states)

    @property
    def total_records(self) -> int:
        """Total number of participation records."""
        return sum(len(records) for records in self._records.values())

    def register(self, participant_id: UUID, initial_exchange: float = 0.0) -> ParticipationState:
        """
        Register a participant for tracking.

        Args:
            participant_id: UUID of the participant
            initial_exchange: Starting exchange (split 50/50)

        Returns:
            The created ParticipationState
        """
        if participant_id in self._states:
            raise ValueError(f"Participant already registered: {participant_id}")

        state = ParticipationState(participant_id, initial_exchange)
        self._states[participant_id] = state
        self._records[participant_id] = []
        self._history[participant_id] = [state.snapshot()]

        return state

    def unregister(self, participant_id: UUID) -> ParticipationState | None:
        """Remove a participant from tracking."""
        state = self._states.pop(participant_id, None)
        if state:
            self._records.pop(participant_id, None)
            self._history.pop(participant_id, None)
        return state

    def get_state(self, participant_id: UUID) -> ParticipationState | None:
        """Get current participation state."""
        return self._states.get(participant_id)

    def get_records(self, participant_id: UUID) -> list[ParticipationRecord]:
        """Get all participation records for a participant."""
        return self._records.get(participant_id, []).copy()

    def get_history(self, participant_id: UUID) -> list[ParticipationSnapshot]:
        """Get participation history."""
        return self._history.get(participant_id, []).copy()

    def record_participation(
        self,
        participant_id: UUID,
        given: float,
        received: float,
        participation_type: ParticipationType = ParticipationType.CONTRIBUTION,
        description: str = "",
    ) -> ParticipationRecord:
        """
        Record a participation activity.
        Must be balanced (META 50/50).

        Args:
            participant_id: Participant UUID
            given: Value given
            received: Value received
            participation_type: Type of participation
            description: Description of activity

        Returns:
            The created ParticipationRecord
        """
        state = self._states.get(participant_id)
        if state is None:
            raise ValueError(f"Participant not registered: {participant_id}")

        record = ParticipationRecord(
            participant_id=participant_id,
            participation_type=participation_type,
            given=given,
            received=received,
            description=description,
        )

        # Apply to state (validates internally)
        state.apply_record(record)

        # Store record and snapshot
        self._records[participant_id].append(record)
        self._history[participant_id].append(state.snapshot())

        return record

    def record_balanced(
        self,
        participant_id: UUID,
        exchange_amount: float,
        participation_type: ParticipationType = ParticipationType.CONTRIBUTION,
        description: str = "",
    ) -> ParticipationRecord:
        """
        Record a balanced participation (automatically 50/50 split).

        Args:
            participant_id: Participant UUID
            exchange_amount: Total exchange amount
            participation_type: Type of participation
            description: Description

        Returns:
            The created ParticipationRecord
        """
        half = exchange_amount / 2
        return self.record_participation(
            participant_id, half, half, participation_type, description
        )

    def get_level(self, participant_id: UUID) -> ParticipationLevel:
        """Get current participation level."""
        state = self._states.get(participant_id)
        return state.level if state else ParticipationLevel.INACTIVE

    def get_engagement_state(self, participant_id: UUID) -> EngagementState:
        """Get current engagement state."""
        state = self._states.get(participant_id)
        return state.engagement_state if state else EngagementState.DORMANT

    def set_engagement_state(self, participant_id: UUID, state: EngagementState) -> None:
        """Set engagement state for a participant."""
        participant_state = self._states.get(participant_id)
        if participant_state is None:
            raise ValueError(f"Participant not registered: {participant_id}")
        participant_state.set_engagement_state(state)

    def validate_all(self) -> dict[str, Any]:
        """Validate all participants maintain META 50/50."""
        valid_count = 0
        invalid_count = 0
        participant_reports = []

        for participant_id, state in self._states.items():
            is_valid = state.is_balanced
            if is_valid:
                valid_count += 1
            else:
                invalid_count += 1

            participant_reports.append(
                {
                    "participant_id": str(participant_id),
                    "level": state.level.value,
                    "engagement": state.engagement_state.value,
                    "balanced": is_valid,
                }
            )

        return {
            "tracked_participants": self.participant_count,
            "total_records": self.total_records,
            "valid": valid_count,
            "invalid": invalid_count,
            "all_valid": invalid_count == 0,
            "participants": participant_reports,
        }

    def prove_tracker_meta_meaning(self) -> dict[str, Any]:
        """Generate META proof for entire tracker."""
        validation = self.validate_all()
        state_proofs = [state.prove_meta_meaning() for state in self._states.values()]

        return {
            **validation,
            "state_proofs": state_proofs,
            "proof": (
                "Participation tracker maintains META 50/50 equilibrium"
                if validation["all_valid"]
                else "Participation tracker has participants violating META 50/50"
            ),
        }


class ParticipationMetrics:
    """
    Calculates participation metrics while maintaining META 50/50 awareness.
    """

    def __init__(self, tracker: ParticipationTracker):
        self._tracker = tracker
        self._meta = MetaEquilibrium()

    def calculate_engagement_rate(self, participant_id: UUID) -> float:
        """
        Calculate engagement rate (records per time unit).
        """
        records = self._tracker.get_records(participant_id)
        if len(records) < 2:
            return 0.0

        first = records[0].timestamp
        last = records[-1].timestamp
        duration = (last - first).total_seconds()

        if duration == 0:
            return float(len(records))

        return len(records) / (duration / 3600)  # Records per hour

    def calculate_exchange_velocity(self, participant_id: UUID) -> float:
        """
        Calculate exchange velocity (exchange per record).
        """
        records = self._tracker.get_records(participant_id)
        if not records:
            return 0.0

        total_exchange = sum(r.total_exchange for r in records)
        return total_exchange / len(records)

    def calculate_balance_stability(self, participant_id: UUID) -> float:
        """
        Calculate balance stability (0-1 scale).
        Higher stability = closer to META 50/50.
        """
        state = self._tracker.get_state(participant_id)
        if state is None:
            return 0.0

        balance = state.balance
        deviation = abs(balance[0] - 50.0)
        return max(0.0, 1.0 - (deviation / 50.0))

    def calculate_contribution_ratio(self, participant_id: UUID) -> float:
        """
        Calculate ratio of contributions to total records.
        """
        records = self._tracker.get_records(participant_id)
        if not records:
            return 0.0

        contributions = sum(
            1 for r in records if r.participation_type == ParticipationType.CONTRIBUTION
        )
        return contributions / len(records)

    def get_level_distribution(self) -> dict[str, int]:
        """Get distribution of participants across levels."""
        distribution: dict[str, int] = {level.value: 0 for level in ParticipationLevel}

        for state in self._tracker._states.values():
            distribution[state.level.value] += 1

        return distribution

    def get_engagement_distribution(self) -> dict[str, int]:
        """Get distribution of participants across engagement states."""
        distribution: dict[str, int] = {state.value: 0 for state in EngagementState}

        for state in self._tracker._states.values():
            distribution[state.engagement_state.value] += 1

        return distribution

    def calculate_aggregate_balance(self) -> tuple[float, float]:
        """
        Calculate aggregate balance across all participants.
        Should maintain META 50/50 at system level.
        """
        total_given = 0.0
        total_received = 0.0

        for state in self._tracker._states.values():
            total_given += state.total_given
            total_received += state.total_received

        return self._meta.calculate_balance(total_given, total_received)

    def get_top_participants(self, n: int = 10, by: str = "exchange") -> list[tuple[UUID, float]]:
        """
        Get top N participants by specified metric.

        Args:
            n: Number of participants to return
            by: Metric to sort by ("exchange", "records", "given", "received")

        Returns:
            List of (participant_id, metric_value) tuples
        """
        metrics = []

        for participant_id, state in self._tracker._states.items():
            if by == "exchange":
                value = state.total_exchange
            elif by == "records":
                value = float(state.record_count)
            elif by == "given":
                value = state.total_given
            elif by == "received":
                value = state.total_received
            else:
                value = state.total_exchange

            metrics.append((participant_id, value))

        metrics.sort(key=lambda x: x[1], reverse=True)
        return metrics[:n]

    def generate_report(self, participant_id: UUID) -> dict[str, Any]:
        """Generate comprehensive participation report."""
        state = self._tracker.get_state(participant_id)
        if state is None:
            return {"error": f"Participant not found: {participant_id}"}

        records = self._tracker.get_records(participant_id)
        history = self._tracker.get_history(participant_id)

        # Type distribution
        type_dist: dict[str, int] = {t.value: 0 for t in ParticipationType}
        for record in records:
            type_dist[record.participation_type.value] += 1

        return {
            "participant_id": str(participant_id),
            "current_state": state.prove_meta_meaning(),
            "metrics": {
                "engagement_rate": self.calculate_engagement_rate(participant_id),
                "exchange_velocity": self.calculate_exchange_velocity(participant_id),
                "balance_stability": self.calculate_balance_stability(participant_id),
                "contribution_ratio": self.calculate_contribution_ratio(participant_id),
                "total_records": len(records),
                "snapshots": len(history),
            },
            "participation_types": type_dist,
            "history_summary": {
                "first_activity": records[0].timestamp.isoformat() if records else None,
                "last_activity": records[-1].timestamp.isoformat() if records else None,
                "levels_achieved": list({s.level.value for s in history}),
            },
        }
