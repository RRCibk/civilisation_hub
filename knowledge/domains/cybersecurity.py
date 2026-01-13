"""
Cybersecurity Domain
====================
Cybersecurity knowledge domain with META 50/50 equilibrium.
Fundamental duality: Attack/Defense (offense vs protection).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class CybersecurityDomain(KnowledgeDomain):
    """
    Cybersecurity knowledge domain.

    Fundamental Duality: Attack / Defense
    - Attack: Threats, exploits, offensive security
    - Defense: Protection, mitigation, defensive security

    Secondary Dualities:
    - Confidentiality / Availability
    - Prevention / Detection
    - Technical / Human
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Cybersecurity",
            domain_type=DomainType.FUNDAMENTAL,
            description="The protection of digital systems and information",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Attack/Defense duality."""
        self._domain.set_duality(
            positive_name="attack",
            positive_value=50,
            negative_name="defense",
            negative_value=50,
            duality_name="cybersecurity_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental cybersecurity principles."""
        principles = [
            (
                "Defense in Depth",
                "Multiple layers of security",
            ),
            (
                "Least Privilege",
                "Minimum necessary access",
            ),
            (
                "CIA Triad",
                "Confidentiality, Integrity, Availability",
            ),
            (
                "Assume Breach",
                "Plan for successful attacks",
            ),
            (
                "Zero Trust",
                "Never trust, always verify",
            ),
            (
                "Security by Design",
                "Build security in from start",
            ),
            (
                "Human Factor",
                "People are critical security component",
            ),
            (
                "Continuous Monitoring",
                "Always watch for threats",
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=90,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental cybersecurity concepts."""
        return [
            "Threat",
            "Vulnerability",
            "Risk",
            "Attack",
            "Defense",
            "Encryption",
            "Authentication",
            "Authorization",
            "Firewall",
            "Malware",
            "Intrusion",
            "Incident",
            "Compliance",
            "Privacy",
            "Access Control",
        ]

    def initialize_branches(self) -> None:
        """Initialize major cybersecurity branches."""
        branches = [
            (
                "Network Security",
                "Protecting network infrastructure",
                ConceptType.THEORY,
            ),
            (
                "Application Security",
                "Securing software applications",
                ConceptType.THEORY,
            ),
            (
                "Cloud Security",
                "Cloud environment protection",
                ConceptType.THEORY,
            ),
            (
                "Endpoint Security",
                "Device protection",
                ConceptType.THEORY,
            ),
            (
                "Identity Management",
                "Access and identity",
                ConceptType.THEORY,
            ),
            (
                "Cryptography",
                "Encryption and secure communication",
                ConceptType.THEORY,
            ),
            (
                "Incident Response",
                "Handling security incidents",
                ConceptType.THEORY,
            ),
            (
                "Security Operations",
                "Day-to-day security management",
                ConceptType.THEORY,
            ),
            (
                "Penetration Testing",
                "Ethical hacking",
                ConceptType.THEORY,
            ),
            (
                "Governance and Compliance",
                "Security governance",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_threats(self) -> None:
        """Initialize cybersecurity threats."""
        threats = [
            ("Malware", "Malicious software", "Technical"),
            ("Phishing", "Social engineering", "Human"),
            ("Ransomware", "Encryption extortion", "Criminal"),
            ("DDoS", "Denial of service", "Availability"),
            ("APT", "Advanced persistent threat", "Nation-state"),
            ("Insider Threat", "Internal actors", "Human"),
        ]

        for name, description, category in threats:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_controls(self) -> None:
        """Initialize security controls."""
        controls = [
            ("Encryption", "Data protection", "Technical"),
            ("Firewalls", "Network filtering", "Technical"),
            ("MFA", "Multi-factor authentication", "Access"),
            ("SIEM", "Security monitoring", "Detection"),
            ("Training", "Security awareness", "Human"),
            ("Backup", "Data recovery", "Resilience"),
        ]

        for name, description, category in controls:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_cybersecurity_pairs(self) -> None:
        """Initialize fundamental cybersecurity pairs with META 50/50 balance."""
        pairs = [
            ("Attack", "Defense", "Offense vs protection"),
            ("Confidentiality", "Availability", "Secret vs accessible"),
            ("Prevention", "Detection", "Stop vs find"),
            ("Technical", "Human", "Technology vs people"),
            ("Proactive", "Reactive", "Before vs after"),
            ("Internal", "External", "Inside vs outside threat"),
            ("Known", "Unknown", "Identified vs zero-day"),
            ("Automated", "Manual", "Machine vs human response"),
            ("Open", "Closed", "Accessible vs restricted"),
            ("Trust", "Verify", "Assume vs check"),
            ("Compliance", "Security", "Checkbox vs real protection"),
            ("Simple", "Complex", "Easy vs sophisticated"),
            ("Permissive", "Restrictive", "Allow vs deny"),
            ("Centralized", "Distributed", "Unified vs spread"),
            ("Encrypted", "Plaintext", "Secured vs exposed"),
            ("Authenticated", "Anonymous", "Known vs unknown identity"),
            ("Static", "Dynamic", "Fixed vs adaptive"),
            ("Risk", "Reward", "Danger vs benefit"),
            ("Privacy", "Surveillance", "Hidden vs monitored"),
            ("Red Team", "Blue Team", "Attackers vs defenders"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Security)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Security)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_cia_triad(self) -> dict[str, str]:
        """Get CIA triad components."""
        return {
            "confidentiality": "Information accessible only to authorized",
            "integrity": "Information accurate and unmodified",
            "availability": "Information accessible when needed",
        }

    def demonstrate_cybersecurity_balance(self) -> dict[str, Any]:
        """Demonstrate cybersecurity balance principles."""
        return {
            "concept": "Cybersecurity Equilibrium",
            "dualities": {
                "attack_defense": {
                    "attack": 50.0,
                    "defense": 50.0,
                    "meaning": "Understanding both offense and defense essential",
                },
                "prevention_detection": {
                    "prevention": 50.0,
                    "detection": 50.0,
                    "meaning": "Stop and find threats equally important",
                },
                "technical_human": {
                    "technical": 50.0,
                    "human": 50.0,
                    "meaning": "Technology and people both critical",
                },
            },
            "security_balance": {
                "confidentiality": 33.3,
                "integrity": 33.3,
                "availability": 33.3,
                "description": "CIA triad must balance",
            },
            "meta_meaning": "Cybersecurity demonstrates META 50/50 in attack-defense equilibrium",
        }


def create_cybersecurity_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> CybersecurityDomain:
    """
    Factory function to create a fully initialized cybersecurity domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized CybersecurityDomain
    """
    domain = CybersecurityDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_threats()
        domain.initialize_controls()
        domain.initialize_cybersecurity_pairs()

    return domain
