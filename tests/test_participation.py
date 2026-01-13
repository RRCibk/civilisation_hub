"""
Tests for participation module
==============================
Tests for participation tracking and contributions with META 50/50 validation.
"""

from datetime import datetime
from uuid import uuid4

import pytest

from participation.contributions import (
    Contribution,
    ContributionCategory,
    ContributionManager,
    ContributionMatcher,
    ContributionPool,
    ContributionStatus,
)
from participation.tracker import (
    EngagementState,
    ParticipationLevel,
    ParticipationMetrics,
    ParticipationRecord,
    ParticipationSnapshot,
    ParticipationState,
    ParticipationTracker,
    ParticipationType,
)


class TestParticipationType:
    """Tests for ParticipationType enum."""

    def test_all_types_exist(self):
        """All participation types should exist."""
        assert ParticipationType.CONTRIBUTION.value == "contribution"
        assert ParticipationType.CONSUMPTION.value == "consumption"
        assert ParticipationType.COLLABORATION.value == "collaboration"
        assert ParticipationType.OBSERVATION.value == "observation"
        assert ParticipationType.FACILITATION.value == "facilitation"

    def test_type_count(self):
        """Should have exactly 5 types."""
        assert len(ParticipationType) == 5


class TestParticipationLevel:
    """Tests for ParticipationLevel enum."""

    def test_all_levels_exist(self):
        """All levels should exist."""
        assert ParticipationLevel.INACTIVE.value == "inactive"
        assert ParticipationLevel.MINIMAL.value == "minimal"
        assert ParticipationLevel.MODERATE.value == "moderate"
        assert ParticipationLevel.ACTIVE.value == "active"
        assert ParticipationLevel.INTENSIVE.value == "intensive"


class TestEngagementState:
    """Tests for EngagementState enum."""

    def test_all_states_exist(self):
        """All states should exist."""
        assert EngagementState.DORMANT.value == "dormant"
        assert EngagementState.WARMING.value == "warming"
        assert EngagementState.ENGAGED.value == "engaged"
        assert EngagementState.PEAK.value == "peak"
        assert EngagementState.COOLING.value == "cooling"


class TestParticipationRecord:
    """Tests for ParticipationRecord dataclass."""

    def test_create_balanced_record(self):
        """Should create balanced record."""
        record = ParticipationRecord(participant_id=uuid4(), given=50, received=50)
        assert record.is_balanced is True

    def test_create_unbalanced_record(self):
        """Should create unbalanced record (allowed but flagged)."""
        record = ParticipationRecord(participant_id=uuid4(), given=60, received=40)
        assert record.is_balanced is False

    def test_negative_values_raise(self):
        """Negative values should raise ValueError."""
        with pytest.raises(ValueError):
            ParticipationRecord(given=-10, received=10)

    def test_total_exchange(self):
        """Total exchange should sum given and received."""
        record = ParticipationRecord(given=30, received=20)
        assert record.total_exchange == 50

    def test_net_contribution(self):
        """Net contribution should be given - received."""
        record = ParticipationRecord(given=60, received=40)
        assert record.net_contribution == 20

    def test_validate_balanced_passes(self):
        """Balanced record should pass validation."""
        record = ParticipationRecord(given=100, received=100)
        record.validate()  # Should not raise

    def test_validate_unbalanced_raises(self):
        """Unbalanced record should raise on validation."""
        record = ParticipationRecord(given=60, received=40)
        with pytest.raises(ValueError) as exc_info:
            record.validate()
        assert "violates META 50/50" in str(exc_info.value)

    def test_timestamp_set(self):
        """Timestamp should be set on creation."""
        record = ParticipationRecord(given=10, received=10)
        assert isinstance(record.timestamp, datetime)


class TestParticipationSnapshot:
    """Tests for ParticipationSnapshot dataclass."""

    def test_create_snapshot(self):
        """Should create snapshot with correct values."""
        snapshot = ParticipationSnapshot(
            participant_id=uuid4(),
            timestamp=datetime.now(),
            level=ParticipationLevel.ACTIVE,
            engagement_state=EngagementState.ENGAGED,
            total_given=100,
            total_received=100,
            record_count=5,
        )
        assert snapshot.level == ParticipationLevel.ACTIVE
        assert snapshot.is_balanced is True

    def test_total_exchange(self):
        """Total exchange should sum given and received."""
        snapshot = ParticipationSnapshot(
            participant_id=uuid4(),
            timestamp=datetime.now(),
            level=ParticipationLevel.MINIMAL,
            engagement_state=EngagementState.DORMANT,
            total_given=50,
            total_received=50,
            record_count=1,
        )
        assert snapshot.total_exchange == 100


class TestParticipationState:
    """Tests for ParticipationState class."""

    def test_create_state(self):
        """Should create state with balanced exchange."""
        participant_id = uuid4()
        state = ParticipationState(participant_id, initial_exchange=100)

        assert state.participant_id == participant_id
        assert state.total_given == 50
        assert state.total_received == 50
        assert state.is_balanced is True

    def test_zero_initial_exchange(self):
        """Should handle zero initial exchange."""
        state = ParticipationState(uuid4(), initial_exchange=0)
        assert state.total_given == 0
        assert state.total_received == 0

    def test_level_calculation_inactive(self):
        """Should calculate INACTIVE level for 0 exchange."""
        state = ParticipationState(uuid4(), initial_exchange=0)
        assert state.level == ParticipationLevel.INACTIVE

    def test_level_calculation_moderate(self):
        """Should calculate MODERATE level for medium exchange."""
        state = ParticipationState(uuid4(), initial_exchange=100)
        assert state.level == ParticipationLevel.MODERATE

    def test_apply_record_balanced(self):
        """Should apply balanced record."""
        state = ParticipationState(uuid4(), initial_exchange=100)
        record = ParticipationRecord(given=25, received=25)

        state.apply_record(record)

        assert state.total_given == 75
        assert state.total_received == 75
        assert state.record_count == 1

    def test_apply_record_unbalanced_raises(self):
        """Should raise for unbalanced record."""
        state = ParticipationState(uuid4())
        record = ParticipationRecord(given=60, received=40)

        with pytest.raises(ValueError):
            state.apply_record(record)

    def test_set_engagement_state(self):
        """Should set engagement state."""
        state = ParticipationState(uuid4())
        state.set_engagement_state(EngagementState.PEAK)

        assert state.engagement_state == EngagementState.PEAK

    def test_snapshot(self):
        """Should create snapshot of current state."""
        state = ParticipationState(uuid4(), initial_exchange=100)
        snapshot = state.snapshot()

        assert snapshot.participant_id == state.participant_id
        assert snapshot.total_given == state.total_given
        assert snapshot.total_received == state.total_received

    def test_operational_ratio(self):
        """Should maintain 52/48 operational ratio."""
        state = ParticipationState(uuid4(), initial_exchange=100)
        ratio = state.operational_ratio

        assert ratio[0] == pytest.approx(52.0)
        assert ratio[1] == pytest.approx(48.0)

    def test_prove_meta_meaning(self):
        """Should return META proof."""
        state = ParticipationState(uuid4(), initial_exchange=100)
        proof = state.prove_meta_meaning()

        assert proof["meta_valid"] is True
        assert "exchange" in proof
        assert "operational" in proof
        assert "proof" in proof


class TestParticipationTracker:
    """Tests for ParticipationTracker class."""

    def test_create_tracker(self):
        """Should create empty tracker."""
        tracker = ParticipationTracker()
        assert tracker.participant_count == 0

    def test_register_participant(self):
        """Should register participant."""
        tracker = ParticipationTracker()
        participant_id = uuid4()

        state = tracker.register(participant_id, initial_exchange=100)

        assert tracker.participant_count == 1
        assert state.participant_id == participant_id

    def test_register_duplicate_raises(self):
        """Should raise for duplicate registration."""
        tracker = ParticipationTracker()
        participant_id = uuid4()

        tracker.register(participant_id)

        with pytest.raises(ValueError):
            tracker.register(participant_id)

    def test_unregister_participant(self):
        """Should unregister participant."""
        tracker = ParticipationTracker()
        participant_id = uuid4()

        tracker.register(participant_id)
        state = tracker.unregister(participant_id)

        assert state is not None
        assert tracker.participant_count == 0

    def test_record_participation(self):
        """Should record balanced participation."""
        tracker = ParticipationTracker()
        participant_id = uuid4()
        tracker.register(participant_id, initial_exchange=100)

        record = tracker.record_participation(participant_id, 25, 25)

        assert record.is_balanced is True
        state = tracker.get_state(participant_id)
        assert state.total_exchange == 150

    def test_record_unbalanced_raises(self):
        """Should raise for unbalanced participation."""
        tracker = ParticipationTracker()
        participant_id = uuid4()
        tracker.register(participant_id)

        with pytest.raises(ValueError):
            tracker.record_participation(participant_id, 60, 40)

    def test_record_balanced_helper(self):
        """Should use record_balanced helper."""
        tracker = ParticipationTracker()
        participant_id = uuid4()
        tracker.register(participant_id, initial_exchange=100)

        record = tracker.record_balanced(participant_id, 50)

        assert record.given == 25
        assert record.received == 25

    def test_get_level(self):
        """Should get participation level."""
        tracker = ParticipationTracker()
        participant_id = uuid4()
        tracker.register(participant_id, initial_exchange=100)

        level = tracker.get_level(participant_id)
        assert level == ParticipationLevel.MODERATE

    def test_validate_all(self):
        """Should validate all participants."""
        tracker = ParticipationTracker()

        tracker.register(uuid4(), initial_exchange=100)
        tracker.register(uuid4(), initial_exchange=200)

        result = tracker.validate_all()

        assert result["tracked_participants"] == 2
        assert result["all_valid"] is True


class TestParticipationMetrics:
    """Tests for ParticipationMetrics class."""

    def test_calculate_exchange_velocity(self):
        """Should calculate exchange velocity."""
        tracker = ParticipationTracker()
        participant_id = uuid4()
        tracker.register(participant_id, initial_exchange=100)

        tracker.record_balanced(participant_id, 50)
        tracker.record_balanced(participant_id, 30)

        metrics = ParticipationMetrics(tracker)
        velocity = metrics.calculate_exchange_velocity(participant_id)

        assert velocity == pytest.approx(40.0)  # Average of 50 and 30

    def test_calculate_balance_stability(self):
        """Should calculate balance stability (1.0 for balanced)."""
        tracker = ParticipationTracker()
        participant_id = uuid4()
        tracker.register(participant_id, initial_exchange=100)

        metrics = ParticipationMetrics(tracker)
        stability = metrics.calculate_balance_stability(participant_id)

        assert stability == 1.0

    def test_get_level_distribution(self):
        """Should get level distribution."""
        tracker = ParticipationTracker()
        tracker.register(uuid4(), initial_exchange=0)
        tracker.register(uuid4(), initial_exchange=100)

        metrics = ParticipationMetrics(tracker)
        dist = metrics.get_level_distribution()

        assert dist["inactive"] == 1
        assert dist["moderate"] == 1

    def test_calculate_aggregate_balance(self):
        """Should calculate aggregate balance."""
        tracker = ParticipationTracker()
        tracker.register(uuid4(), initial_exchange=100)
        tracker.register(uuid4(), initial_exchange=200)

        metrics = ParticipationMetrics(tracker)
        balance = metrics.calculate_aggregate_balance()

        assert balance == (50.0, 50.0)

    def test_generate_report(self):
        """Should generate comprehensive report."""
        tracker = ParticipationTracker()
        participant_id = uuid4()
        tracker.register(participant_id, initial_exchange=100)
        tracker.record_balanced(participant_id, 50)

        metrics = ParticipationMetrics(tracker)
        report = metrics.generate_report(participant_id)

        assert "current_state" in report
        assert "metrics" in report
        assert "participation_types" in report


class TestContributionCategory:
    """Tests for ContributionCategory enum."""

    def test_all_categories_exist(self):
        """All categories should exist."""
        assert ContributionCategory.KNOWLEDGE.value == "knowledge"
        assert ContributionCategory.RESOURCE.value == "resource"
        assert ContributionCategory.TIME.value == "time"
        assert ContributionCategory.EFFORT.value == "effort"
        assert ContributionCategory.CREATIVE.value == "creative"
        assert ContributionCategory.SOCIAL.value == "social"
        assert ContributionCategory.FINANCIAL.value == "financial"


class TestContributionStatus:
    """Tests for ContributionStatus enum."""

    def test_all_statuses_exist(self):
        """All statuses should exist."""
        assert ContributionStatus.PENDING.value == "pending"
        assert ContributionStatus.PARTIAL.value == "partial"
        assert ContributionStatus.BALANCED.value == "balanced"
        assert ContributionStatus.OVERFLOW.value == "overflow"


class TestContribution:
    """Tests for Contribution dataclass."""

    def test_create_contribution(self):
        """Should create contribution."""
        contribution = Contribution(
            contributor_id=uuid4(), value=100, category=ContributionCategory.KNOWLEDGE
        )
        assert contribution.value == 100
        assert contribution.reciprocated == 0
        assert contribution.status == ContributionStatus.PENDING

    def test_negative_values_raise(self):
        """Negative values should raise ValueError."""
        with pytest.raises(ValueError):
            Contribution(value=-100)

    def test_status_pending(self):
        """Should be PENDING when not reciprocated."""
        contribution = Contribution(value=100, reciprocated=0)
        assert contribution.status == ContributionStatus.PENDING

    def test_status_partial(self):
        """Should be PARTIAL when partially reciprocated."""
        contribution = Contribution(value=100, reciprocated=50)
        assert contribution.status == ContributionStatus.PARTIAL

    def test_status_balanced(self):
        """Should be BALANCED when fully reciprocated."""
        contribution = Contribution(value=100, reciprocated=100)
        assert contribution.status == ContributionStatus.BALANCED

    def test_is_balanced(self):
        """Should check META 50/50 balance."""
        balanced = Contribution(value=100, reciprocated=100)
        unbalanced = Contribution(value=100, reciprocated=50)

        assert balanced.is_balanced is True
        assert unbalanced.is_balanced is False

    def test_remaining(self):
        """Should calculate remaining for balance."""
        contribution = Contribution(value=100, reciprocated=30)
        assert contribution.remaining == 70

    def test_reciprocate(self):
        """Should add reciprocation."""
        contribution = Contribution(value=100, reciprocated=0)

        applied = contribution.reciprocate(50)

        assert applied == 50
        assert contribution.reciprocated == 50

    def test_reciprocate_caps_at_value(self):
        """Should cap reciprocation at value."""
        contribution = Contribution(value=100, reciprocated=80)

        applied = contribution.reciprocate(50)

        assert applied == 20  # Only 20 remaining
        assert contribution.reciprocated == 100

    def test_force_balance(self):
        """Should force balance."""
        contribution = Contribution(value=100, reciprocated=0)
        contribution.force_balance()

        assert contribution.is_balanced is True


class TestContributionPool:
    """Tests for ContributionPool dataclass."""

    def test_create_pool(self):
        """Should create empty pool."""
        pool = ContributionPool(name="Test Pool")
        assert pool.name == "Test Pool"
        assert pool.contribution_count == 0

    def test_add_contribution(self):
        """Should add contribution to pool."""
        pool = ContributionPool(name="Test")
        contribution = Contribution(value=100)

        pool.add_contribution(contribution)

        assert pool.contribution_count == 1

    def test_total_contributed(self):
        """Should sum all contributions."""
        pool = ContributionPool(name="Test")
        pool.add_contribution(Contribution(value=100, reciprocated=100))
        pool.add_contribution(Contribution(value=50, reciprocated=50))

        assert pool.total_contributed == 150
        assert pool.total_reciprocated == 150

    def test_is_balanced(self):
        """Should check pool balance."""
        pool = ContributionPool(name="Test")
        pool.add_contribution(Contribution(value=100, reciprocated=100))

        assert pool.is_balanced is True

    def test_get_contributions_by_status(self):
        """Should filter by status."""
        pool = ContributionPool(name="Test")
        pool.add_contribution(Contribution(value=100, reciprocated=0))
        pool.add_contribution(Contribution(value=100, reciprocated=100))

        pending = pool.get_contributions_by_status(ContributionStatus.PENDING)
        balanced = pool.get_contributions_by_status(ContributionStatus.BALANCED)

        assert len(pending) == 1
        assert len(balanced) == 1

    def test_prove_meta_meaning(self):
        """Should return META proof."""
        pool = ContributionPool(name="Test")
        pool.add_contribution(Contribution(value=100, reciprocated=100))

        proof = pool.prove_meta_meaning()

        assert proof["meta_valid"] is True
        assert "contributions" in proof


class TestContributionManager:
    """Tests for ContributionManager class."""

    def test_create_manager(self):
        """Should create empty manager."""
        manager = ContributionManager()
        assert manager.contribution_count == 0

    def test_create_contribution(self):
        """Should create contribution."""
        manager = ContributionManager()
        contributor_id = uuid4()

        contribution = manager.create_contribution(
            contributor_id=contributor_id, value=100, category=ContributionCategory.EFFORT
        )

        assert manager.contribution_count == 1
        assert contribution.value == 100

    def test_create_contribution_auto_balance(self):
        """Should auto-balance contribution."""
        manager = ContributionManager()

        contribution = manager.create_contribution(
            contributor_id=uuid4(), value=100, auto_balance=True
        )

        assert contribution.is_balanced is True

    def test_reciprocate(self):
        """Should reciprocate contribution."""
        manager = ContributionManager()
        contributor_id = uuid4()

        contribution = manager.create_contribution(contributor_id=contributor_id, value=100)

        applied = manager.reciprocate(contribution.id, 50)

        assert applied == 50
        assert contribution.reciprocated == 50

    def test_get_pending_contributions(self):
        """Should get pending contributions."""
        manager = ContributionManager()

        manager.create_contribution(uuid4(), value=100)
        manager.create_contribution(uuid4(), value=100, auto_balance=True)

        pending = manager.get_pending_contributions()
        assert len(pending) == 1

    def test_create_pool(self):
        """Should create contribution pool."""
        manager = ContributionManager()

        pool = manager.create_pool(name="Test Pool", category=ContributionCategory.KNOWLEDGE)

        assert manager.pool_count == 1
        assert pool.name == "Test Pool"

    def test_calculate_contributor_balance(self):
        """Should calculate contributor balance."""
        manager = ContributionManager()
        contributor_id = uuid4()

        manager.create_contribution(contributor_id, value=100, auto_balance=True)
        manager.create_contribution(contributor_id, value=50, auto_balance=True)

        balance = manager.calculate_contributor_balance(contributor_id)

        assert balance["total_contributed"] == 150
        assert balance["total_reciprocated"] == 150
        assert balance["is_balanced"] is True

    def test_validate_all(self):
        """Should validate all contributions."""
        manager = ContributionManager()

        manager.create_contribution(uuid4(), value=100, auto_balance=True)
        manager.create_contribution(uuid4(), value=100)  # Pending

        result = manager.validate_all()

        assert result["total_contributions"] == 2
        assert result["balanced_contributions"] == 1
        assert result["pending_contributions"] == 1


class TestContributionMatcher:
    """Tests for ContributionMatcher class."""

    def test_auto_balance_contribution(self):
        """Should auto-balance contribution."""
        manager = ContributionManager()
        contribution = manager.create_contribution(uuid4(), value=100)
        matcher = ContributionMatcher(manager)

        result = matcher.auto_balance_contribution(contribution.id)

        assert result is True
        assert contribution.is_balanced is True

    def test_balance_all_pending(self):
        """Should balance all pending contributions."""
        manager = ContributionManager()
        manager.create_contribution(uuid4(), value=100)
        manager.create_contribution(uuid4(), value=50)

        matcher = ContributionMatcher(manager)
        count = matcher.balance_all_pending()

        assert count == 2
        assert len(manager.get_pending_contributions()) == 0

    def test_calculate_system_deficit(self):
        """Should calculate system deficit."""
        manager = ContributionManager()
        manager.create_contribution(uuid4(), value=100)
        manager.create_contribution(uuid4(), value=50, auto_balance=True)

        matcher = ContributionMatcher(manager)
        deficit = matcher.calculate_system_deficit()

        assert deficit == 100

    def test_generate_balance_plan(self):
        """Should generate balance plan."""
        manager = ContributionManager()
        contributor = uuid4()
        manager.create_contribution(contributor, value=100)
        manager.create_contribution(contributor, value=50)

        matcher = ContributionMatcher(manager)
        plan = matcher.generate_balance_plan()

        assert plan["total_pending"] == 2
        assert plan["total_deficit"] == 150
        assert plan["action_required"] is True


class TestIntegration:
    """Integration tests for participation module."""

    def test_full_participation_lifecycle(self):
        """Test complete participation lifecycle."""
        tracker = ParticipationTracker()

        # Register participant
        participant_id = uuid4()
        tracker.register(participant_id, initial_exchange=100)

        # Record balanced participation
        tracker.record_balanced(participant_id, 50, ParticipationType.CONTRIBUTION)
        tracker.record_balanced(participant_id, 30, ParticipationType.COLLABORATION)

        state = tracker.get_state(participant_id)
        assert state.is_balanced is True
        assert state.record_count == 2

    def test_participation_with_contributions(self):
        """Test participation tracker with contribution manager."""
        tracker = ParticipationTracker()
        participant_id = uuid4()
        tracker.register(participant_id)

        manager = ContributionManager(tracker)

        # Create auto-balanced contribution
        manager.create_contribution(contributor_id=participant_id, value=100, auto_balance=True)

        # Both systems should be valid
        tracker_valid = tracker.validate_all()
        manager_valid = manager.validate_all()

        assert tracker_valid["all_valid"] is True
        assert manager_valid["system_balanced"] is True

    def test_metrics_after_participation(self):
        """Test metrics calculation after participation."""
        tracker = ParticipationTracker()
        participant_id = uuid4()
        tracker.register(participant_id, initial_exchange=100)

        for _ in range(5):
            tracker.record_balanced(participant_id, 20)

        metrics = ParticipationMetrics(tracker)

        assert metrics.calculate_balance_stability(participant_id) == 1.0
        assert metrics.calculate_exchange_velocity(participant_id) == 20.0

    def test_system_maintains_meta_balance(self):
        """Test that entire system maintains META 50/50."""
        tracker = ParticipationTracker()
        manager = ContributionManager(tracker)

        # Multiple participants
        for i in range(5):
            participant_id = uuid4()
            tracker.register(participant_id, initial_exchange=100 * (i + 1))
            tracker.record_balanced(participant_id, 50)
            manager.create_contribution(participant_id, value=50, auto_balance=True)

        # Validate all
        tracker_valid = tracker.validate_all()
        manager_valid = manager.validate_all()

        assert tracker_valid["all_valid"] is True
        assert manager_valid["system_balanced"] is True

        # Check aggregate balance
        metrics = ParticipationMetrics(tracker)
        balance = metrics.calculate_aggregate_balance()
        assert balance == (50.0, 50.0)
