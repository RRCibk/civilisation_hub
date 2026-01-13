"""
Logistics Domain
================
Logistics knowledge domain with META 50/50 equilibrium.
Fundamental duality: Flow/Storage (movement vs holding).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class LogisticsDomain(KnowledgeDomain):
    """
    Logistics knowledge domain.

    Fundamental Duality: Flow / Storage
    - Flow: Movement, transportation, distribution
    - Storage: Holding, inventory, warehousing

    Secondary Dualities:
    - Inbound / Outbound
    - Cost / Service
    - Push / Pull
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Logistics",
            domain_type=DomainType.FUNDAMENTAL,
            description="The management of material and information flow",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Flow/Storage duality."""
        self._domain.set_duality(
            positive_name="flow",
            positive_value=50,
            negative_name="storage",
            negative_value=50,
            duality_name="logistics_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental logistics principles."""
        principles = [
            ("Right Product", "Correct item delivered"),
            ("Right Place", "Correct destination"),
            ("Right Time", "On schedule"),
            ("Right Quantity", "Correct amount"),
            ("Right Condition", "Undamaged"),
            ("Right Cost", "Economical"),
            ("Right Customer", "Correct recipient"),
            ("Visibility", "Track throughout chain"),
        ]

        for name, description in principles:
            self.create_concept(name, ConceptType.PRINCIPLE, description, certainty=90)

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental logistics concepts."""
        return ["Transportation", "Warehousing", "Inventory", "Distribution",
                "Supply Chain", "Fulfillment", "Freight", "Carrier", "Lead Time",
                "Throughput", "Order", "Shipment", "Routing", "Tracking", "Last Mile"]

    def initialize_branches(self) -> None:
        """Initialize major logistics branches."""
        branches = [
            ("Transportation Management", "Moving goods", ConceptType.THEORY),
            ("Warehouse Management", "Storage operations", ConceptType.THEORY),
            ("Inventory Management", "Stock control", ConceptType.THEORY),
            ("Distribution Management", "Delivery networks", ConceptType.THEORY),
            ("Reverse Logistics", "Returns and recycling", ConceptType.THEORY),
            ("Third-Party Logistics", "Outsourced logistics", ConceptType.THEORY),
            ("Global Logistics", "International movement", ConceptType.THEORY),
            ("Cold Chain", "Temperature-controlled", ConceptType.THEORY),
            ("E-commerce Logistics", "Online fulfillment", ConceptType.THEORY),
            ("Green Logistics", "Sustainable practices", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_modes(self) -> None:
        """Initialize transportation modes."""
        modes = [
            ("Road", "Truck transport", "Flexible"),
            ("Rail", "Train transport", "Efficient bulk"),
            ("Sea", "Ocean freight", "International bulk"),
            ("Air", "Aircraft freight", "Fast, expensive"),
            ("Pipeline", "Liquid/gas transport", "Specialized"),
            ("Intermodal", "Combined modes", "Optimized"),
        ]

        for name, description, characteristic in modes:
            concept = self.create_concept(name, ConceptType.DEFINITION, description)
            concept.metadata["characteristic"] = characteristic

    def initialize_logistics_pairs(self) -> None:
        """Initialize fundamental logistics pairs with META 50/50 balance."""
        pairs = [
            ("Flow", "Storage", "Movement vs holding"),
            ("Inbound", "Outbound", "Receiving vs shipping"),
            ("Cost", "Service", "Economy vs quality"),
            ("Push", "Pull", "Forecast vs demand driven"),
            ("Speed", "Economy", "Fast vs cheap"),
            ("Centralized", "Distributed", "Single vs multiple locations"),
            ("Direct", "Indirect", "Straight vs through hub"),
            ("Owned", "Outsourced", "In-house vs third-party"),
            ("Bulk", "Break-Bulk", "Large vs small shipments"),
            ("Forward", "Reverse", "Outgoing vs returns"),
            ("Domestic", "International", "Local vs global"),
            ("Scheduled", "On-Demand", "Regular vs as-needed"),
            ("Full Load", "Less-than-Load", "FTL vs LTL"),
            ("Stock", "Flow-Through", "Hold vs cross-dock"),
            ("Manual", "Automated", "Human vs machine"),
            ("Visibility", "Uncertainty", "Known vs unknown"),
            ("Origin", "Destination", "Source vs target"),
            ("First Mile", "Last Mile", "Pickup vs delivery"),
            ("Peak", "Off-Peak", "Busy vs slow periods"),
            ("Physical", "Digital", "Goods vs information"),
        ]

        for positive, negative, description in pairs:
            pos = self.create_concept(f"{positive} (Logistics)", ConceptType.DEFINITION,
                                       f"Positive pole: {description.split(' vs ')[0]}")
            neg = self.create_concept(f"{negative} (Logistics)", ConceptType.DEFINITION,
                                       f"Negative pole: {description.split(' vs ')[1]}")
            self.create_relation(pos, neg, RelationType.CONTRADICTS, strength=50)

    def demonstrate_logistics_balance(self) -> dict[str, Any]:
        """Demonstrate logistics balance principles."""
        return {
            "concept": "Logistics Equilibrium",
            "dualities": {
                "flow_storage": {"flow": 50.0, "storage": 50.0,
                    "meaning": "Movement and holding balance"},
                "cost_service": {"cost": 50.0, "service": 50.0,
                    "meaning": "Economy and quality trade-off"},
            },
            "meta_meaning": "Logistics demonstrates META 50/50 in flow-storage balance",
        }


def create_logistics_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> LogisticsDomain:
    domain = LogisticsDomain(meta_equilibrium)
    if initialize_all:
        domain.initialize_branches()
        domain.initialize_modes()
        domain.initialize_logistics_pairs()
    return domain
