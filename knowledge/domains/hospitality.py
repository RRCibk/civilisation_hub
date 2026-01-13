"""
Hospitality Domain
==================
Hospitality knowledge domain with META 50/50 equilibrium.
Fundamental duality: Service/Profit (guest satisfaction vs business).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class HospitalityDomain(KnowledgeDomain):
    """
    Hospitality knowledge domain.

    Fundamental Duality: Service / Profit
    - Service: Guest satisfaction, experience, care
    - Profit: Business viability, revenue, efficiency

    Secondary Dualities:
    - Experience / Operations
    - Personalized / Standardized
    - Front / Back of house
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Hospitality",
            domain_type=DomainType.FUNDAMENTAL,
            description="The industry of welcoming and serving guests",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Service/Profit duality."""
        self._domain.set_duality(
            positive_name="service",
            positive_value=50,
            negative_name="profit",
            negative_value=50,
            duality_name="hospitality_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental hospitality principles."""
        principles = [
            ("Guest First", "Prioritize guest satisfaction"),
            ("Service Excellence", "Exceed expectations"),
            ("Anticipation", "Predict guest needs"),
            ("Consistency", "Reliable quality"),
            ("Personalization", "Individual attention"),
            ("Cleanliness", "Hygiene and presentation"),
            ("Safety", "Guest security"),
            ("Professionalism", "Trained, courteous staff"),
        ]

        for name, description in principles:
            self.create_concept(name, ConceptType.PRINCIPLE, description, certainty=90)

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental hospitality concepts."""
        return ["Guest", "Service", "Accommodation", "Food", "Beverage", "Revenue",
                "Occupancy", "Experience", "Staff", "Operations", "Quality",
                "Reservation", "Amenity", "Housekeeping", "Concierge"]

    def initialize_branches(self) -> None:
        """Initialize major hospitality branches."""
        branches = [
            ("Hotel Management", "Accommodation services", ConceptType.THEORY),
            ("Restaurant Management", "Food service", ConceptType.THEORY),
            ("Event Management", "Gatherings and functions", ConceptType.THEORY),
            ("Tourism Management", "Travel services", ConceptType.THEORY),
            ("Casino Management", "Gaming operations", ConceptType.THEORY),
            ("Cruise Management", "Ship hospitality", ConceptType.THEORY),
            ("Resort Management", "Destination properties", ConceptType.THEORY),
            ("Spa Management", "Wellness services", ConceptType.THEORY),
            ("Club Management", "Membership facilities", ConceptType.THEORY),
            ("Catering Management", "Off-site food service", ConceptType.THEORY),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_departments(self) -> None:
        """Initialize hotel departments."""
        departments = [
            ("Front Office", "Guest reception", "Revenue"),
            ("Housekeeping", "Room cleaning", "Operations"),
            ("Food and Beverage", "Dining services", "Revenue"),
            ("Sales and Marketing", "Business development", "Revenue"),
            ("Human Resources", "Staff management", "Support"),
            ("Engineering", "Facilities maintenance", "Operations"),
        ]

        for name, description, category in departments:
            concept = self.create_concept(name, ConceptType.DEFINITION, description)
            concept.metadata["category"] = category

    def initialize_hospitality_pairs(self) -> None:
        """Initialize fundamental hospitality pairs with META 50/50 balance."""
        pairs = [
            ("Service", "Profit", "Guest satisfaction vs business"),
            ("Experience", "Operations", "Guest-facing vs back-end"),
            ("Personalized", "Standardized", "Custom vs consistent"),
            ("Front", "Back", "Visible vs hidden"),
            ("Quality", "Cost", "Excellence vs economy"),
            ("Luxury", "Budget", "Premium vs affordable"),
            ("Full-Service", "Limited-Service", "Complete vs basic"),
            ("Leisure", "Business", "Vacation vs work travel"),
            ("Independent", "Chain", "Unique vs branded"),
            ("High-Touch", "High-Tech", "Human vs automated"),
            ("Tangible", "Intangible", "Physical vs experiential"),
            ("Peak", "Off-Peak", "Busy vs slow seasons"),
            ("Direct", "Indirect", "Own vs third-party booking"),
            ("Transient", "Group", "Individual vs bulk"),
            ("RevPAR", "ADR", "Revenue per room vs average rate"),
            ("Upsell", "Cross-sell", "Upgrade vs add-on"),
            ("Complaint", "Compliment", "Negative vs positive feedback"),
            ("Retention", "Acquisition", "Repeat vs new guests"),
            ("Local", "International", "Domestic vs foreign"),
            ("Day", "Night", "Daytime vs evening operations"),
        ]

        for positive, negative, description in pairs:
            pos = self.create_concept(f"{positive} (Hospitality)", ConceptType.DEFINITION,
                                       f"Positive pole: {description.split(' vs ')[0]}")
            neg = self.create_concept(f"{negative} (Hospitality)", ConceptType.DEFINITION,
                                       f"Negative pole: {description.split(' vs ')[1]}")
            self.create_relation(pos, neg, RelationType.CONTRADICTS, strength=50)

    def demonstrate_hospitality_balance(self) -> dict[str, Any]:
        """Demonstrate hospitality balance principles."""
        return {
            "concept": "Hospitality Equilibrium",
            "dualities": {
                "service_profit": {"service": 50.0, "profit": 50.0,
                    "meaning": "Balance guest care with business viability"},
                "quality_cost": {"quality": 50.0, "cost": 50.0,
                    "meaning": "Balance excellence with economy"},
            },
            "meta_meaning": "Hospitality demonstrates META 50/50 in service-profit balance",
        }


def create_hospitality_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> HospitalityDomain:
    domain = HospitalityDomain(meta_equilibrium)
    if initialize_all:
        domain.initialize_branches()
        domain.initialize_departments()
        domain.initialize_hospitality_pairs()
    return domain
