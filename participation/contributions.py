"""
Contribution Management
=======================
Manages contributions while maintaining META 50/50 equilibrium.
Every contribution requires balanced reciprocation.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any
from uuid import UUID, uuid4

from core.equilibrium import MetaEquilibrium
from participation.tracker import (
    ParticipationTracker,
    ParticipationType,
)


class ContributionCategory(Enum):
    """Categories of contributions."""

    KNOWLEDGE = "knowledge"  # Information, expertise
    RESOURCE = "resource"  # Material resources
    TIME = "time"  # Time investment
    EFFORT = "effort"  # Work/labor
    CREATIVE = "creative"  # Creative works
    SOCIAL = "social"  # Social capital, connections
    FINANCIAL = "financial"  # Monetary contributions


class ContributionStatus(Enum):
    """Status of a contribution."""

    PENDING = "pending"  # Awaiting reciprocation
    PARTIAL = "partial"  # Partially reciprocated
    BALANCED = "balanced"  # Fully balanced (META 50/50)
    OVERFLOW = "overflow"  # Over-reciprocated


@dataclass
class Contribution:
    """
    A contribution that requires balanced reciprocation.
    """

    id: UUID = field(default_factory=uuid4)
    contributor_id: UUID = field(default_factory=uuid4)
    category: ContributionCategory = ContributionCategory.EFFORT
    value: float = 0.0
    reciprocated: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)
    description: str = ""
    tags: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if self.value < 0 or self.reciprocated < 0:
            raise ValueError("Contribution values cannot be negative")
        self._meta = MetaEquilibrium()

    @property
    def status(self) -> ContributionStatus:
        """Get current contribution status."""
        if self.reciprocated == 0:
            return ContributionStatus.PENDING
        elif self.reciprocated < self.value:
            return ContributionStatus.PARTIAL
        elif abs(self.reciprocated - self.value) < 0.001:
            return ContributionStatus.BALANCED
        else:
            return ContributionStatus.OVERFLOW

    @property
    def is_balanced(self) -> bool:
        """Check if contribution is balanced (META 50/50)."""
        return self._meta.verify_balance(self.value, self.reciprocated)

    @property
    def balance(self) -> tuple[float, float]:
        """Get balance ratio."""
        return self._meta.calculate_balance(self.value, self.reciprocated)

    @property
    def remaining(self) -> float:
        """Remaining value to reciprocate for balance."""
        return max(0, self.value - self.reciprocated)

    @property
    def total_exchange(self) -> float:
        """Total value in the contribution."""
        return self.value + self.reciprocated

    def reciprocate(self, amount: float) -> float:
        """
        Add reciprocation to the contribution.

        Args:
            amount: Amount to reciprocate

        Returns:
            Amount actually applied (capped at value for balance)
        """
        if amount < 0:
            raise ValueError("Reciprocation amount cannot be negative")

        # Cap at value to maintain balance
        actual = min(amount, self.remaining)
        self.reciprocated += actual
        return actual

    def force_balance(self) -> None:
        """Force the contribution to balanced state."""
        self.reciprocated = self.value


@dataclass
class ContributionPool:
    """
    A pool of contributions for a specific category or purpose.
    The pool maintains META 50/50 between total contributions and reciprocations.
    """

    id: UUID = field(default_factory=uuid4)
    name: str = ""
    category: ContributionCategory = ContributionCategory.EFFORT
    description: str = ""
    created_at: datetime = field(default_factory=datetime.now)
    _contributions: list[Contribution] = field(default_factory=list)

    def __post_init__(self):
        self._meta = MetaEquilibrium()

    @property
    def total_contributed(self) -> float:
        """Total value contributed to pool."""
        return sum(c.value for c in self._contributions)

    @property
    def total_reciprocated(self) -> float:
        """Total value reciprocated from pool."""
        return sum(c.reciprocated for c in self._contributions)

    @property
    def is_balanced(self) -> bool:
        """Check if pool is balanced."""
        return self._meta.verify_balance(self.total_contributed, self.total_reciprocated)

    @property
    def balance(self) -> tuple[float, float]:
        """Get pool balance ratio."""
        return self._meta.calculate_balance(self.total_contributed, self.total_reciprocated)

    @property
    def contribution_count(self) -> int:
        """Number of contributions in pool."""
        return len(self._contributions)

    @property
    def pending_count(self) -> int:
        """Number of pending contributions."""
        return sum(1 for c in self._contributions if c.status == ContributionStatus.PENDING)

    @property
    def balanced_count(self) -> int:
        """Number of balanced contributions."""
        return sum(1 for c in self._contributions if c.status == ContributionStatus.BALANCED)

    def add_contribution(self, contribution: Contribution) -> None:
        """Add a contribution to the pool."""
        self._contributions.append(contribution)

    def get_contribution(self, contribution_id: UUID) -> Contribution | None:
        """Get a contribution by ID."""
        for c in self._contributions:
            if c.id == contribution_id:
                return c
        return None

    def get_contributions_by_status(self, status: ContributionStatus) -> list[Contribution]:
        """Get contributions by status."""
        return [c for c in self._contributions if c.status == status]

    def get_contributions_by_contributor(self, contributor_id: UUID) -> list[Contribution]:
        """Get contributions by contributor."""
        return [c for c in self._contributions if c.contributor_id == contributor_id]

    def distribute_reciprocation(self, amount: float) -> dict[UUID, float]:
        """
        Distribute reciprocation across pending contributions.

        Args:
            amount: Total amount to distribute

        Returns:
            Dict mapping contribution IDs to amounts applied
        """
        pending = self.get_contributions_by_status(ContributionStatus.PENDING)
        pending.extend(self.get_contributions_by_status(ContributionStatus.PARTIAL))

        if not pending:
            return {}

        # Distribute proportionally based on remaining
        total_remaining = sum(c.remaining for c in pending)
        if total_remaining == 0:
            return {}

        distribution: dict[UUID, float] = {}
        remaining_amount = amount

        for contribution in pending:
            if remaining_amount <= 0:
                break

            proportion = contribution.remaining / total_remaining
            to_apply = min(contribution.remaining, amount * proportion, remaining_amount)
            applied = contribution.reciprocate(to_apply)
            distribution[contribution.id] = applied
            remaining_amount -= applied

        return distribution

    def prove_meta_meaning(self) -> dict[str, Any]:
        """Generate META proof for pool."""
        balance = self.balance

        return {
            "pool_id": str(self.id),
            "name": self.name,
            "category": self.category.value,
            "contributions": {
                "total": self.contribution_count,
                "pending": self.pending_count,
                "balanced": self.balanced_count,
            },
            "values": {
                "contributed": self.total_contributed,
                "reciprocated": self.total_reciprocated,
                "balance": f"{balance[0]:.2f}/{balance[1]:.2f}",
            },
            "meta_valid": self.is_balanced,
            "proof": (
                "Contribution pool maintains META 50/50 equilibrium"
                if self.is_balanced
                else "Contribution pool is not yet balanced"
            ),
        }


class ContributionManager:
    """
    Manages contributions and their reciprocation.
    Ensures all contributions eventually reach META 50/50 balance.
    """

    def __init__(
        self,
        participation_tracker: ParticipationTracker | None = None,
        meta_equilibrium: MetaEquilibrium | None = None,
    ):
        self._meta = meta_equilibrium or MetaEquilibrium()
        self._tracker = participation_tracker
        self._contributions: dict[UUID, Contribution] = {}
        self._pools: dict[UUID, ContributionPool] = {}
        self._contributor_contributions: dict[UUID, list[UUID]] = {}

    @property
    def contribution_count(self) -> int:
        """Total number of contributions."""
        return len(self._contributions)

    @property
    def pool_count(self) -> int:
        """Number of contribution pools."""
        return len(self._pools)

    def create_contribution(
        self,
        contributor_id: UUID,
        value: float,
        category: ContributionCategory = ContributionCategory.EFFORT,
        description: str = "",
        tags: list[str] | None = None,
        auto_balance: bool = False,
    ) -> Contribution:
        """
        Create a new contribution.

        Args:
            contributor_id: UUID of the contributor
            value: Value of the contribution
            category: Category of contribution
            description: Description
            tags: Optional tags
            auto_balance: If True, automatically balance the contribution

        Returns:
            The created Contribution
        """
        contribution = Contribution(
            contributor_id=contributor_id,
            category=category,
            value=value,
            reciprocated=value if auto_balance else 0,
            description=description,
            tags=tags or [],
        )

        self._contributions[contribution.id] = contribution

        if contributor_id not in self._contributor_contributions:
            self._contributor_contributions[contributor_id] = []
        self._contributor_contributions[contributor_id].append(contribution.id)

        # Record in participation tracker if available
        if self._tracker and auto_balance:
            try:
                self._tracker.record_balanced(
                    contributor_id,
                    value * 2,  # Total exchange
                    ParticipationType.CONTRIBUTION,
                    description,
                )
            except ValueError:
                pass  # Participant not registered

        return contribution

    def reciprocate(
        self, contribution_id: UUID, amount: float, reciprocator_id: UUID | None = None
    ) -> float:
        """
        Reciprocate a contribution.

        Args:
            contribution_id: Contribution to reciprocate
            amount: Amount to reciprocate
            reciprocator_id: Optional ID of who is reciprocating

        Returns:
            Amount actually applied
        """
        contribution = self._contributions.get(contribution_id)
        if contribution is None:
            raise ValueError(f"Contribution not found: {contribution_id}")

        applied = contribution.reciprocate(amount)

        # Record in participation tracker if available and balanced
        if self._tracker and contribution.is_balanced and reciprocator_id:
            try:
                self._tracker.record_balanced(
                    reciprocator_id,
                    applied * 2,
                    ParticipationType.CONTRIBUTION,
                    f"Reciprocation for {contribution_id}",
                )
            except ValueError:
                pass

        return applied

    def get_contribution(self, contribution_id: UUID) -> Contribution | None:
        """Get a contribution by ID."""
        return self._contributions.get(contribution_id)

    def get_contributions_by_contributor(self, contributor_id: UUID) -> list[Contribution]:
        """Get all contributions by a contributor."""
        contribution_ids = self._contributor_contributions.get(contributor_id, [])
        return [self._contributions[cid] for cid in contribution_ids if cid in self._contributions]

    def get_pending_contributions(self) -> list[Contribution]:
        """Get all pending contributions."""
        return [
            c
            for c in self._contributions.values()
            if c.status in [ContributionStatus.PENDING, ContributionStatus.PARTIAL]
        ]

    def get_balanced_contributions(self) -> list[Contribution]:
        """Get all balanced contributions."""
        return [c for c in self._contributions.values() if c.status == ContributionStatus.BALANCED]

    def create_pool(
        self,
        name: str,
        category: ContributionCategory = ContributionCategory.EFFORT,
        description: str = "",
    ) -> ContributionPool:
        """Create a contribution pool."""
        pool = ContributionPool(name=name, category=category, description=description)
        self._pools[pool.id] = pool
        return pool

    def add_to_pool(self, pool_id: UUID, contribution: Contribution) -> None:
        """Add a contribution to a pool."""
        pool = self._pools.get(pool_id)
        if pool is None:
            raise ValueError(f"Pool not found: {pool_id}")
        pool.add_contribution(contribution)

    def get_pool(self, pool_id: UUID) -> ContributionPool | None:
        """Get a pool by ID."""
        return self._pools.get(pool_id)

    def calculate_contributor_balance(self, contributor_id: UUID) -> dict[str, Any]:
        """Calculate balance for a contributor."""
        contributions = self.get_contributions_by_contributor(contributor_id)

        if not contributions:
            return {
                "contributor_id": str(contributor_id),
                "total_contributed": 0,
                "total_reciprocated": 0,
                "balance": (50.0, 50.0),
                "is_balanced": True,
                "contribution_count": 0,
            }

        total_contributed = sum(c.value for c in contributions)
        total_reciprocated = sum(c.reciprocated for c in contributions)
        balance = self._meta.calculate_balance(total_contributed, total_reciprocated)

        return {
            "contributor_id": str(contributor_id),
            "total_contributed": total_contributed,
            "total_reciprocated": total_reciprocated,
            "balance": f"{balance[0]:.2f}/{balance[1]:.2f}",
            "is_balanced": self._meta.verify_balance(total_contributed, total_reciprocated),
            "contribution_count": len(contributions),
            "pending_count": sum(
                1 for c in contributions if c.status != ContributionStatus.BALANCED
            ),
        }

    def validate_all(self) -> dict[str, Any]:
        """Validate all contributions."""
        balanced = self.get_balanced_contributions()
        pending = self.get_pending_contributions()

        # Calculate totals
        total_value = sum(c.value for c in self._contributions.values())
        total_reciprocated = sum(c.reciprocated for c in self._contributions.values())
        balance = self._meta.calculate_balance(total_value, total_reciprocated)

        return {
            "total_contributions": self.contribution_count,
            "balanced_contributions": len(balanced),
            "pending_contributions": len(pending),
            "pools": self.pool_count,
            "totals": {
                "value": total_value,
                "reciprocated": total_reciprocated,
                "balance": f"{balance[0]:.2f}/{balance[1]:.2f}",
            },
            "system_balanced": self._meta.verify_balance(total_value, total_reciprocated),
        }

    def prove_meta_meaning(self) -> dict[str, Any]:
        """Generate META proof for contribution manager."""
        validation = self.validate_all()

        pool_proofs = [pool.prove_meta_meaning() for pool in self._pools.values()]

        return {
            **validation,
            "pool_proofs": pool_proofs,
            "proof": (
                "Contribution system maintains META 50/50 equilibrium"
                if validation["system_balanced"]
                else "Contribution system is not yet balanced"
            ),
        }


class ContributionMatcher:
    """
    Matches contributions with reciprocations to achieve META 50/50.
    """

    def __init__(self, manager: ContributionManager):
        self._manager = manager
        self._meta = MetaEquilibrium()

    def find_matches(
        self, contribution: Contribution, potential_reciprocators: list[UUID]
    ) -> list[tuple[UUID, float]]:
        """
        Find potential matches for reciprocation.

        Args:
            contribution: Contribution to match
            potential_reciprocators: List of potential reciprocator IDs

        Returns:
            List of (reciprocator_id, suggested_amount) tuples
        """
        if contribution.is_balanced:
            return []

        remaining = contribution.remaining
        matches = []

        # Simple equal distribution among reciprocators
        if potential_reciprocators:
            per_reciprocator = remaining / len(potential_reciprocators)
            for reciprocator_id in potential_reciprocators:
                matches.append((reciprocator_id, per_reciprocator))

        return matches

    def auto_balance_contribution(self, contribution_id: UUID) -> bool:
        """
        Automatically balance a contribution (for testing/admin).

        Returns:
            True if contribution was balanced
        """
        contribution = self._manager.get_contribution(contribution_id)
        if contribution is None:
            return False

        contribution.force_balance()
        return True

    def balance_all_pending(self) -> int:
        """
        Balance all pending contributions.

        Returns:
            Number of contributions balanced
        """
        pending = self._manager.get_pending_contributions()
        for contribution in pending:
            contribution.force_balance()
        return len(pending)

    def calculate_system_deficit(self) -> float:
        """
        Calculate total reciprocation deficit in the system.
        """
        pending = self._manager.get_pending_contributions()
        return sum(c.remaining for c in pending)

    def generate_balance_plan(self) -> dict[str, Any]:
        """
        Generate a plan to achieve system balance.
        """
        pending = self._manager.get_pending_contributions()
        total_deficit = self.calculate_system_deficit()

        # Group by contributor
        by_contributor: dict[UUID, list[Contribution]] = {}
        for c in pending:
            if c.contributor_id not in by_contributor:
                by_contributor[c.contributor_id] = []
            by_contributor[c.contributor_id].append(c)

        contributor_plans = []
        for contributor_id, contributions in by_contributor.items():
            deficit = sum(c.remaining for c in contributions)
            contributor_plans.append(
                {
                    "contributor_id": str(contributor_id),
                    "pending_contributions": len(contributions),
                    "deficit": deficit,
                }
            )

        return {
            "total_pending": len(pending),
            "total_deficit": total_deficit,
            "contributors_affected": len(by_contributor),
            "contributor_plans": contributor_plans,
            "action_required": total_deficit > 0,
        }
