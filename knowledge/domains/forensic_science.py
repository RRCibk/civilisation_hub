"""
Forensic Science Domain
=======================
Forensic science knowledge domain with META 50/50 equilibrium.
Fundamental duality: Evidence/Interpretation (facts vs analysis).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class ForensicScienceDomain(KnowledgeDomain):
    """
    Forensic Science knowledge domain.

    Fundamental Duality: Evidence / Interpretation
    - Evidence: Physical facts, specimens, traces
    - Interpretation: Analysis, conclusions, expert opinion

    Secondary Dualities:
    - Class / Individual
    - Known / Unknown
    - Prosecution / Defense
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="ForensicScience",
            domain_type=DomainType.FUNDAMENTAL,
            description="The application of science to legal investigations",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Evidence/Interpretation duality."""
        self._domain.set_duality(
            positive_name="evidence",
            positive_value=50,
            negative_name="interpretation",
            negative_value=50,
            duality_name="forensic_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental forensic science principles."""
        principles = [
            (
                "Locard's Exchange",
                "Every contact leaves a trace",
            ),
            (
                "Chain of Custody",
                "Evidence must be tracked continuously",
            ),
            (
                "Scientific Method",
                "Apply rigorous scientific approach",
            ),
            (
                "Objectivity",
                "Analysis must be unbiased",
            ),
            (
                "Reproducibility",
                "Results must be reproducible",
            ),
            (
                "Documentation",
                "Everything must be documented",
            ),
            (
                "Quality Assurance",
                "Standards ensure reliability",
            ),
            (
                "Expert Testimony",
                "Communicate findings clearly",
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
        """Get fundamental forensic science concepts."""
        return [
            "Evidence",
            "Crime Scene",
            "Analysis",
            "Identification",
            "Comparison",
            "Chain of Custody",
            "Expert Witness",
            "Testimony",
            "Report",
            "DNA",
            "Fingerprint",
            "Trace Evidence",
            "Autopsy",
            "Ballistics",
            "Toxicology",
        ]

    def initialize_branches(self) -> None:
        """Initialize major forensic science branches."""
        branches = [
            (
                "Forensic Biology",
                "DNA and biological evidence",
                ConceptType.THEORY,
            ),
            (
                "Forensic Chemistry",
                "Chemical analysis",
                ConceptType.THEORY,
            ),
            (
                "Forensic Toxicology",
                "Drugs and poisons",
                ConceptType.THEORY,
            ),
            (
                "Forensic Pathology",
                "Cause of death",
                ConceptType.THEORY,
            ),
            (
                "Forensic Anthropology",
                "Skeletal remains",
                ConceptType.THEORY,
            ),
            (
                "Forensic Odontology",
                "Dental identification",
                ConceptType.THEORY,
            ),
            (
                "Digital Forensics",
                "Electronic evidence",
                ConceptType.THEORY,
            ),
            (
                "Ballistics",
                "Firearms evidence",
                ConceptType.THEORY,
            ),
            (
                "Document Examination",
                "Questioned documents",
                ConceptType.THEORY,
            ),
            (
                "Trace Evidence",
                "Microscopic evidence",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_evidence_types(self) -> None:
        """Initialize types of forensic evidence."""
        types = [
            ("Physical", "Tangible objects", "Material"),
            ("Biological", "DNA, blood, tissue", "Living"),
            ("Chemical", "Drugs, accelerants", "Chemical"),
            ("Digital", "Electronic data", "Digital"),
            ("Documentary", "Documents, writings", "Written"),
            ("Testimonial", "Witness statements", "Verbal"),
        ]

        for name, description, category in types:
            concept = self.create_concept(
                name=f"{name} Evidence",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_techniques(self) -> None:
        """Initialize forensic techniques."""
        techniques = [
            ("DNA Profiling", "Genetic identification", "Biology"),
            ("Fingerprint Analysis", "Ridge comparison", "Pattern"),
            ("Chromatography", "Chemical separation", "Chemistry"),
            ("Spectroscopy", "Material identification", "Chemistry"),
            ("Microscopy", "Trace examination", "Physical"),
            ("Autopsy", "Death investigation", "Pathology"),
        ]

        for name, description, category in techniques:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_forensic_pairs(self) -> None:
        """Initialize fundamental forensic pairs with META 50/50 balance."""
        pairs = [
            ("Evidence", "Interpretation", "Facts vs analysis"),
            ("Class", "Individual", "Group vs unique"),
            ("Known", "Unknown", "Reference vs questioned"),
            ("Prosecution", "Defense", "State vs accused"),
            ("Inclusion", "Exclusion", "Match vs no match"),
            ("Presence", "Absence", "Found vs not found"),
            ("Direct", "Circumstantial", "Proves vs suggests"),
            ("Physical", "Testimonial", "Object vs statement"),
            ("Primary", "Secondary", "First vs transferred"),
            ("Fresh", "Degraded", "Intact vs damaged"),
            ("Visible", "Latent", "Seen vs hidden"),
            ("Original", "Copy", "First vs reproduction"),
            ("Qualitative", "Quantitative", "Type vs amount"),
            ("Objective", "Subjective", "Measurable vs opinion"),
            ("Certain", "Probable", "Definite vs likely"),
            ("Scene", "Lab", "Field vs laboratory"),
            ("Collection", "Analysis", "Gathering vs testing"),
            ("Inculpatory", "Exculpatory", "Incriminating vs clearing"),
            ("Pattern", "Chemical", "Physical vs molecular"),
            ("Identification", "Comparison", "What vs matching"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Forensic)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Forensic)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_locard_principle(self) -> dict[str, str]:
        """Get Locard's Exchange Principle details."""
        return {
            "principle": "Every contact leaves a trace",
            "transfer": "Material moves between objects/people",
            "persistence": "Traces may remain over time",
            "significance": "Foundation of trace evidence",
        }

    def demonstrate_forensic_balance(self) -> dict[str, Any]:
        """Demonstrate forensic science balance principles."""
        return {
            "concept": "Forensic Science Equilibrium",
            "dualities": {
                "evidence_interpretation": {
                    "evidence": 50.0,
                    "interpretation": 50.0,
                    "meaning": "Facts and analysis equally important",
                },
                "class_individual": {
                    "class": 50.0,
                    "individual": 50.0,
                    "meaning": "Group and unique characteristics both valuable",
                },
                "known_unknown": {
                    "known": 50.0,
                    "unknown": 50.0,
                    "meaning": "Reference and questioned samples both needed",
                },
            },
            "justice_balance": {
                "prosecution": 50.0,
                "defense": 50.0,
                "description": "Science serves both sides equally",
            },
            "meta_meaning": "Forensic Science demonstrates META 50/50 in evidence-interpretation synthesis",
        }


def create_forensic_science_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> ForensicScienceDomain:
    """
    Factory function to create a fully initialized forensic science domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized ForensicScienceDomain
    """
    domain = ForensicScienceDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_evidence_types()
        domain.initialize_techniques()
        domain.initialize_forensic_pairs()

    return domain
