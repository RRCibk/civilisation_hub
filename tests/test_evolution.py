"""
Tests for evolution module
==========================
Tests for evolution tracking and transitions with META 50/50 validation.
"""

from datetime import datetime
from uuid import uuid4

import pytest

from evolution.tracker import (
    EvolutionDelta,
    EvolutionDirection,
    EvolutionMetrics,
    EvolutionPhase,
    EvolutionSnapshot,
    EvolutionState,
    EvolutionTracker,
)
from evolution.transitions import (
    TransitionEngine,
    TransitionMatrix,
    TransitionRule,
    TransitionType,
)


class TestEvolutionPhase:
    """Tests for EvolutionPhase enum."""

    def test_all_phases_exist(self):
        """All evolution phases should exist."""
        assert EvolutionPhase.GENESIS.value == "genesis"
        assert EvolutionPhase.GROWTH.value == "growth"
        assert EvolutionPhase.MATURATION.value == "maturation"
        assert EvolutionPhase.TRANSFORMATION.value == "transformation"
        assert EvolutionPhase.DECAY.value == "decay"
        assert EvolutionPhase.EQUILIBRIUM.value == "equilibrium"

    def test_phase_count(self):
        """Should have exactly 6 phases."""
        assert len(EvolutionPhase) == 6


class TestEvolutionDirection:
    """Tests for EvolutionDirection enum."""

    def test_all_directions_exist(self):
        """All directions should exist."""
        assert EvolutionDirection.POSITIVE.value == "positive"
        assert EvolutionDirection.NEGATIVE.value == "negative"
        assert EvolutionDirection.NEUTRAL.value == "neutral"


class TestEvolutionDelta:
    """Tests for EvolutionDelta dataclass."""

    def test_create_balanced_delta(self):
        """Should create balanced delta."""
        delta = EvolutionDelta(10, 10, description="test")
        assert delta.positive_change == 10
        assert delta.negative_change == 10
        assert delta.is_balanced is True

    def test_create_unbalanced_delta(self):
        """Should create unbalanced delta (allowed but flagged)."""
        delta = EvolutionDelta(60, 40)
        assert delta.is_balanced is False

    def test_negative_values_raise(self):
        """Negative values should raise ValueError."""
        with pytest.raises(ValueError):
            EvolutionDelta(-10, 10)

    def test_net_change_balanced(self):
        """Net change should be 0 for balanced delta."""
        delta = EvolutionDelta(50, 50)
        assert delta.net_change == 0

    def test_net_change_positive(self):
        """Net change should be positive for growth."""
        delta = EvolutionDelta(60, 40)
        assert delta.net_change == 20

    def test_total_magnitude(self):
        """Total magnitude should sum both changes."""
        delta = EvolutionDelta(30, 20)
        assert delta.total_magnitude == 50

    def test_direction_neutral(self):
        """Balanced delta should have neutral direction."""
        delta = EvolutionDelta(50, 50)
        assert delta.direction == EvolutionDirection.NEUTRAL

    def test_direction_positive(self):
        """Growth delta should have positive direction."""
        delta = EvolutionDelta(60, 40)
        assert delta.direction == EvolutionDirection.POSITIVE

    def test_direction_negative(self):
        """Decay delta should have negative direction."""
        delta = EvolutionDelta(40, 60)
        assert delta.direction == EvolutionDirection.NEGATIVE

    def test_validate_balanced_passes(self):
        """Balanced delta should pass validation."""
        delta = EvolutionDelta(100, 100)
        delta.validate()  # Should not raise

    def test_validate_unbalanced_raises(self):
        """Unbalanced delta should raise on validation."""
        delta = EvolutionDelta(60, 40)
        with pytest.raises(ValueError) as exc_info:
            delta.validate()
        assert "violates META 50/50" in str(exc_info.value)

    def test_balance_ratio(self):
        """Balance ratio should be calculated correctly."""
        delta = EvolutionDelta(50, 50)
        assert delta.balance_ratio == (50.0, 50.0)

    def test_timestamp_set(self):
        """Timestamp should be set on creation."""
        delta = EvolutionDelta(10, 10)
        assert isinstance(delta.timestamp, datetime)


class TestEvolutionSnapshot:
    """Tests for EvolutionSnapshot dataclass."""

    def test_create_snapshot(self):
        """Should create snapshot with correct values."""
        entity_id = uuid4()
        snapshot = EvolutionSnapshot(
            entity_id=entity_id,
            timestamp=datetime.now(),
            phase=EvolutionPhase.GROWTH,
            positive_energy=100,
            negative_energy=100,
        )
        assert snapshot.entity_id == entity_id
        assert snapshot.phase == EvolutionPhase.GROWTH
        assert snapshot.is_balanced is True

    def test_total_energy(self):
        """Total energy should sum both energies."""
        snapshot = EvolutionSnapshot(
            entity_id=uuid4(),
            timestamp=datetime.now(),
            phase=EvolutionPhase.GENESIS,
            positive_energy=50,
            negative_energy=50,
        )
        assert snapshot.total_energy == 100

    def test_balance_property(self):
        """Balance should return correct ratio."""
        snapshot = EvolutionSnapshot(
            entity_id=uuid4(),
            timestamp=datetime.now(),
            phase=EvolutionPhase.GENESIS,
            positive_energy=100,
            negative_energy=100,
        )
        assert snapshot.balance == (50.0, 50.0)


class TestEvolutionState:
    """Tests for EvolutionState class."""

    def test_create_state(self):
        """Should create state with balanced energy."""
        entity_id = uuid4()
        state = EvolutionState(entity_id, initial_energy=100)

        assert state.entity_id == entity_id
        assert state.phase == EvolutionPhase.GENESIS
        assert state.positive_energy == 50
        assert state.negative_energy == 50
        assert state.is_balanced is True

    def test_total_energy(self):
        """Total energy should match initial."""
        state = EvolutionState(uuid4(), initial_energy=200)
        assert state.total_energy == 200

    def test_generation_starts_zero(self):
        """Generation should start at 0."""
        state = EvolutionState(uuid4())
        assert state.generation == 0

    def test_apply_delta_balanced(self):
        """Should apply balanced delta."""
        state = EvolutionState(uuid4(), initial_energy=100)
        delta = EvolutionDelta(10, 10)

        state.apply_delta(delta)

        assert state.total_energy == 120
        assert state.is_balanced is True
        assert state.generation == 1

    def test_apply_delta_unbalanced_raises(self):
        """Should raise for unbalanced delta."""
        state = EvolutionState(uuid4(), initial_energy=100)
        delta = EvolutionDelta(60, 40)

        with pytest.raises(ValueError):
            state.apply_delta(delta)

    def test_transition_phase(self):
        """Should transition to new phase."""
        state = EvolutionState(uuid4())
        state.transition_phase(EvolutionPhase.GROWTH)

        assert state.phase == EvolutionPhase.GROWTH

    def test_snapshot(self):
        """Should create snapshot of current state."""
        state = EvolutionState(uuid4(), initial_energy=100)
        snapshot = state.snapshot()

        assert snapshot.entity_id == state.entity_id
        assert snapshot.phase == state.phase
        assert snapshot.positive_energy == state.positive_energy
        assert snapshot.negative_energy == state.negative_energy

    def test_operational_ratio(self):
        """Should maintain 52/48 operational ratio."""
        state = EvolutionState(uuid4(), initial_energy=100)
        ratio = state.operational_ratio

        assert ratio[0] == pytest.approx(52.0)
        assert ratio[1] == pytest.approx(48.0)

    def test_prove_meta_meaning(self):
        """Should return META proof."""
        state = EvolutionState(uuid4(), initial_energy=100)
        proof = state.prove_meta_meaning()

        assert proof["meta_valid"] is True
        assert "energy" in proof
        assert "operational" in proof
        assert "proof" in proof


class TestEvolutionTracker:
    """Tests for EvolutionTracker class."""

    def test_create_tracker(self):
        """Should create empty tracker."""
        tracker = EvolutionTracker()
        assert tracker.tracked_count == 0

    def test_register_entity(self):
        """Should register entity for tracking."""
        tracker = EvolutionTracker()
        entity_id = uuid4()

        state = tracker.register(entity_id, initial_energy=100)

        assert tracker.tracked_count == 1
        assert state.entity_id == entity_id

    def test_register_duplicate_raises(self):
        """Should raise for duplicate registration."""
        tracker = EvolutionTracker()
        entity_id = uuid4()

        tracker.register(entity_id)

        with pytest.raises(ValueError):
            tracker.register(entity_id)

    def test_unregister_entity(self):
        """Should unregister entity."""
        tracker = EvolutionTracker()
        entity_id = uuid4()

        tracker.register(entity_id)
        state = tracker.unregister(entity_id)

        assert state is not None
        assert tracker.tracked_count == 0

    def test_get_state(self):
        """Should get entity state."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id)

        state = tracker.get_state(entity_id)
        assert state is not None
        assert state.entity_id == entity_id

    def test_get_history(self):
        """Should get entity history."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id)

        history = tracker.get_history(entity_id)
        assert len(history) == 1  # Initial snapshot

    def test_evolve_balanced(self):
        """Should apply balanced evolution."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id, initial_energy=100)

        delta = tracker.evolve(entity_id, 10, 10, "growth")

        assert delta.is_balanced is True
        state = tracker.get_state(entity_id)
        assert state.total_energy == 120

    def test_evolve_unbalanced_raises(self):
        """Should raise for unbalanced evolution."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id)

        with pytest.raises(ValueError):
            tracker.evolve(entity_id, 60, 40)

    def test_evolve_balanced_helper(self):
        """Should use evolve_balanced helper."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id, initial_energy=100)

        delta = tracker.evolve_balanced(entity_id, magnitude=20)

        assert delta.positive_change == 10
        assert delta.negative_change == 10
        assert delta.is_balanced is True

    def test_transition(self):
        """Should transition entity phase."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id)

        tracker.transition(entity_id, EvolutionPhase.GROWTH)

        state = tracker.get_state(entity_id)
        assert state.phase == EvolutionPhase.GROWTH

    def test_get_generation(self):
        """Should get entity generation."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id)

        assert tracker.get_generation(entity_id) == 0

        tracker.evolve_balanced(entity_id, 10)
        assert tracker.get_generation(entity_id) == 1

    def test_validate_all(self):
        """Should validate all entities."""
        tracker = EvolutionTracker()

        tracker.register(uuid4(), initial_energy=100)
        tracker.register(uuid4(), initial_energy=200)

        result = tracker.validate_all()

        assert result["tracked_entities"] == 2
        assert result["all_valid"] is True

    def test_prove_tracker_meta_meaning(self):
        """Should return META proof for tracker."""
        tracker = EvolutionTracker()
        tracker.register(uuid4())

        proof = tracker.prove_tracker_meta_meaning()

        assert "state_proofs" in proof
        assert "proof" in proof


class TestEvolutionMetrics:
    """Tests for EvolutionMetrics class."""

    def test_calculate_velocity(self):
        """Should calculate evolution velocity."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id, initial_energy=100)

        tracker.evolve_balanced(entity_id, 20)
        tracker.evolve_balanced(entity_id, 10)

        metrics = EvolutionMetrics(tracker)
        velocity = metrics.calculate_velocity(entity_id)

        assert velocity == pytest.approx(15.0)  # Average of 20 and 10

    def test_calculate_stability(self):
        """Should calculate stability (1.0 for balanced)."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id)

        metrics = EvolutionMetrics(tracker)
        stability = metrics.calculate_stability(entity_id)

        assert stability == 1.0

    def test_calculate_momentum(self):
        """Should calculate momentum (0 for balanced)."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id)
        tracker.evolve_balanced(entity_id, 20)

        metrics = EvolutionMetrics(tracker)
        momentum = metrics.calculate_momentum(entity_id)

        assert momentum == 0.0  # Balanced evolution has no net momentum

    def test_get_phase_distribution(self):
        """Should get phase distribution."""
        tracker = EvolutionTracker()
        tracker.register(uuid4())
        tracker.register(uuid4())

        e3 = uuid4()
        tracker.register(e3)
        tracker.transition(e3, EvolutionPhase.GROWTH)

        metrics = EvolutionMetrics(tracker)
        dist = metrics.get_phase_distribution()

        assert dist["genesis"] == 2
        assert dist["growth"] == 1

    def test_calculate_aggregate_balance(self):
        """Should calculate aggregate balance."""
        tracker = EvolutionTracker()
        tracker.register(uuid4(), initial_energy=100)
        tracker.register(uuid4(), initial_energy=200)

        metrics = EvolutionMetrics(tracker)
        balance = metrics.calculate_aggregate_balance()

        assert balance == (50.0, 50.0)

    def test_generate_report(self):
        """Should generate comprehensive report."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id)
        tracker.evolve_balanced(entity_id, 20)

        metrics = EvolutionMetrics(tracker)
        report = metrics.generate_report(entity_id)

        assert "current_state" in report
        assert "metrics" in report
        assert "history_summary" in report


class TestTransitionType:
    """Tests for TransitionType enum."""

    def test_all_types_exist(self):
        """All transition types should exist."""
        assert TransitionType.PROGRESSION.value == "progression"
        assert TransitionType.REGRESSION.value == "regression"
        assert TransitionType.LATERAL.value == "lateral"
        assert TransitionType.QUANTUM.value == "quantum"
        assert TransitionType.CYCLIC.value == "cyclic"


class TestTransitionRule:
    """Tests for TransitionRule dataclass."""

    def test_create_rule(self):
        """Should create transition rule."""
        rule = TransitionRule(
            name="genesis_to_growth",
            from_phase=EvolutionPhase.GENESIS,
            to_phase=EvolutionPhase.GROWTH,
            transition_type=TransitionType.PROGRESSION,
            energy_cost=10,
        )

        assert rule.name == "genesis_to_growth"
        assert rule.from_phase == EvolutionPhase.GENESIS
        assert rule.to_phase == EvolutionPhase.GROWTH

    def test_cost_delta_is_balanced(self):
        """Cost delta should be 50/50."""
        rule = TransitionRule(
            name="test",
            from_phase=EvolutionPhase.GENESIS,
            to_phase=EvolutionPhase.GROWTH,
            transition_type=TransitionType.PROGRESSION,
            energy_cost=100,
        )

        cost_pos, cost_neg = rule.cost_delta
        assert cost_pos == 50
        assert cost_neg == 50

    def test_can_apply_correct_phase(self):
        """Should allow from correct phase."""
        rule = TransitionRule(
            name="test",
            from_phase=EvolutionPhase.GENESIS,
            to_phase=EvolutionPhase.GROWTH,
            transition_type=TransitionType.PROGRESSION,
            energy_cost=10,
        )

        state = EvolutionState(uuid4(), initial_energy=100)
        assert rule.can_apply(state) is True

    def test_can_apply_wrong_phase(self):
        """Should not allow from wrong phase."""
        rule = TransitionRule(
            name="test",
            from_phase=EvolutionPhase.GROWTH,
            to_phase=EvolutionPhase.MATURATION,
            transition_type=TransitionType.PROGRESSION,
            energy_cost=10,
        )

        state = EvolutionState(uuid4())  # GENESIS phase
        assert rule.can_apply(state) is False

    def test_can_apply_insufficient_energy(self):
        """Should not allow with insufficient energy."""
        rule = TransitionRule(
            name="test",
            from_phase=EvolutionPhase.GENESIS,
            to_phase=EvolutionPhase.GROWTH,
            transition_type=TransitionType.PROGRESSION,
            energy_cost=200,
        )

        state = EvolutionState(uuid4(), initial_energy=100)
        assert rule.can_apply(state) is False


class TestTransitionMatrix:
    """Tests for TransitionMatrix class."""

    def test_create_matrix(self):
        """Should create matrix with default transitions."""
        matrix = TransitionMatrix()
        rules = matrix.get_all_rules()

        assert len(rules) > 0

    def test_get_valid_transitions_from_genesis(self):
        """Should get valid transitions from GENESIS."""
        matrix = TransitionMatrix()
        rules = matrix.get_valid_transitions(EvolutionPhase.GENESIS)

        assert len(rules) == 1
        assert rules[0].to_phase == EvolutionPhase.GROWTH

    def test_is_valid_transition(self):
        """Should check transition validity."""
        matrix = TransitionMatrix()

        assert matrix.is_valid_transition(EvolutionPhase.GENESIS, EvolutionPhase.GROWTH) is True

        assert (
            matrix.is_valid_transition(EvolutionPhase.GENESIS, EvolutionPhase.EQUILIBRIUM) is False
        )

    def test_add_rule(self):
        """Should add custom rule."""
        matrix = TransitionMatrix()
        rule = TransitionRule(
            name="custom",
            from_phase=EvolutionPhase.GENESIS,
            to_phase=EvolutionPhase.EQUILIBRIUM,
            transition_type=TransitionType.QUANTUM,
            energy_cost=100,
        )

        matrix.add_rule(rule)

        assert (
            matrix.is_valid_transition(EvolutionPhase.GENESIS, EvolutionPhase.EQUILIBRIUM) is True
        )

    def test_remove_rule(self):
        """Should remove rule."""
        matrix = TransitionMatrix()

        removed = matrix.remove_rule(EvolutionPhase.GENESIS, EvolutionPhase.GROWTH)

        assert removed is not None
        assert matrix.is_valid_transition(EvolutionPhase.GENESIS, EvolutionPhase.GROWTH) is False

    def test_to_adjacency_dict(self):
        """Should return adjacency dictionary."""
        matrix = TransitionMatrix()
        adj = matrix.to_adjacency_dict()

        assert "genesis" in adj
        assert "growth" in adj["genesis"]


class TestTransitionEngine:
    """Tests for TransitionEngine class."""

    def test_create_engine(self):
        """Should create engine with tracker."""
        tracker = EvolutionTracker()
        engine = TransitionEngine(tracker)

        assert engine.tracker is tracker
        assert engine.transition_count == 0

    def test_get_available_transitions(self):
        """Should get available transitions for entity."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id, initial_energy=100)

        engine = TransitionEngine(tracker)
        available = engine.get_available_transitions(entity_id)

        assert len(available) == 1
        assert available[0].to_phase == EvolutionPhase.GROWTH

    def test_can_transition_valid(self):
        """Should allow valid transition."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id, initial_energy=100)

        engine = TransitionEngine(tracker)
        can, reason = engine.can_transition(entity_id, EvolutionPhase.GROWTH)

        assert can is True

    def test_can_transition_invalid(self):
        """Should reject invalid transition."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id)

        engine = TransitionEngine(tracker)
        can, reason = engine.can_transition(entity_id, EvolutionPhase.EQUILIBRIUM)

        assert can is False
        assert "No valid transition" in reason

    def test_execute_transition_success(self):
        """Should execute valid transition."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id, initial_energy=100)

        engine = TransitionEngine(tracker)
        result = engine.execute_transition(entity_id, EvolutionPhase.GROWTH)

        assert result.success is True
        assert result.to_phase == EvolutionPhase.GROWTH
        assert tracker.get_state(entity_id).phase == EvolutionPhase.GROWTH

    def test_execute_transition_failure(self):
        """Should fail invalid transition."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id)

        engine = TransitionEngine(tracker)
        result = engine.execute_transition(entity_id, EvolutionPhase.EQUILIBRIUM)

        assert result.success is False
        assert result.error is not None

    def test_get_transition_history(self):
        """Should get transition history."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id, initial_energy=100)

        engine = TransitionEngine(tracker)
        engine.execute_transition(entity_id, EvolutionPhase.GROWTH)

        history = engine.get_transition_history()
        assert len(history) == 1

    def test_get_path_to_phase(self):
        """Should find path to target phase."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id)

        engine = TransitionEngine(tracker)
        path = engine.get_path_to_phase(entity_id, EvolutionPhase.MATURATION)

        assert path is not None
        assert path[0] == EvolutionPhase.GENESIS
        assert path[-1] == EvolutionPhase.MATURATION

    def test_validate_all_transitions(self):
        """Should validate all transition rules."""
        tracker = EvolutionTracker()
        engine = TransitionEngine(tracker)

        result = engine.validate_all_transitions()

        assert result["all_valid"] is True
        assert "rules" in result

    def test_prove_meta_meaning(self):
        """Should generate META proof."""
        tracker = EvolutionTracker()
        tracker.register(uuid4())

        engine = TransitionEngine(tracker)
        proof = engine.prove_meta_meaning()

        assert "transition_validation" in proof
        assert "tracker_state" in proof
        assert "statistics" in proof
        assert "proof" in proof


class TestIntegration:
    """Integration tests for evolution module."""

    def test_full_evolution_lifecycle(self):
        """Test complete evolution lifecycle."""
        tracker = EvolutionTracker()
        engine = TransitionEngine(tracker)

        # Create entity
        entity_id = uuid4()
        tracker.register(entity_id, initial_energy=100)

        # Evolve with balanced changes
        tracker.evolve_balanced(entity_id, 50)
        tracker.evolve_balanced(entity_id, 30)

        # Transition through phases
        engine.execute_transition(entity_id, EvolutionPhase.GROWTH)
        engine.execute_transition(entity_id, EvolutionPhase.MATURATION)
        engine.execute_transition(entity_id, EvolutionPhase.EQUILIBRIUM)

        state = tracker.get_state(entity_id)
        assert state.phase == EvolutionPhase.EQUILIBRIUM
        assert state.is_balanced is True
        assert state.generation == 2

    def test_metrics_after_evolution(self):
        """Test metrics calculation after evolution."""
        tracker = EvolutionTracker()
        entity_id = uuid4()
        tracker.register(entity_id, initial_energy=100)

        for _ in range(5):
            tracker.evolve_balanced(entity_id, 20)

        metrics = EvolutionMetrics(tracker)

        assert metrics.calculate_velocity(entity_id) == 20.0
        assert metrics.calculate_stability(entity_id) == 1.0
        assert metrics.calculate_momentum(entity_id) == 0.0

    def test_system_maintains_meta_balance(self):
        """Test that entire system maintains META 50/50."""
        tracker = EvolutionTracker()
        engine = TransitionEngine(tracker)

        # Register multiple entities
        for i in range(5):
            entity_id = uuid4()
            tracker.register(entity_id, initial_energy=100 * (i + 1))
            tracker.evolve_balanced(entity_id, 20)

        # Validate all
        tracker_valid = tracker.validate_all()
        engine_valid = engine.validate_all_transitions()

        assert tracker_valid["all_valid"] is True
        assert engine_valid["all_valid"] is True

        # Check aggregate balance
        metrics = EvolutionMetrics(tracker)
        balance = metrics.calculate_aggregate_balance()
        assert balance == (50.0, 50.0)
