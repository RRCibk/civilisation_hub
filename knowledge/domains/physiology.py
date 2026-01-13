"""
Physiology Domain
=================
Physiological knowledge domain with META 50/50 equilibrium.
Fundamental duality: Anabolic/Catabolic (building vs breaking processes).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class PhysiologyDomain(KnowledgeDomain):
    """
    Physiology knowledge domain.

    Fundamental Duality: Anabolic / Catabolic
    - Anabolic: Building processes, synthesis, energy storage
    - Catabolic: Breaking processes, degradation, energy release

    Secondary Dualities:
    - Homeostasis / Imbalance
    - Systole / Diastole
    - Inspiration / Expiration
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Physiology",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of body functions and processes",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Anabolic/Catabolic duality."""
        self._domain.set_duality(
            positive_name="anabolic",
            positive_value=50,
            negative_name="catabolic",
            negative_value=50,
            duality_name="physiology_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental physiological principles."""
        principles = [
            (
                "Homeostasis",
                "The body maintains stable internal conditions",
            ),
            (
                "Negative Feedback",
                "Most regulatory mechanisms use negative feedback loops",
            ),
            (
                "Cell Theory",
                "The cell is the basic unit of physiological function",
            ),
            (
                "Energy Conservation",
                "Energy is neither created nor destroyed in metabolic processes",
            ),
            (
                "Gradient-Driven Transport",
                "Movement occurs down concentration and electrical gradients",
            ),
            (
                "Membrane Permeability",
                "Cell membranes selectively control what enters and exits",
            ),
            (
                "Integration of Systems",
                "Body systems work together to maintain function",
            ),
            (
                "Adaptation Response",
                "The body adapts to changing demands",
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=95,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental physiology concepts."""
        return [
            "Metabolism",
            "Homeostasis",
            "Respiration",
            "Circulation",
            "Digestion",
            "Excretion",
            "Reproduction",
            "Movement",
            "Sensation",
            "Regulation",
            "Feedback",
            "Transport",
            "Secretion",
            "Contraction",
            "Conduction",
        ]

    def initialize_branches(self) -> None:
        """Initialize major physiology branches."""
        branches = [
            (
                "Cell Physiology",
                "Functions at the cellular level",
                ConceptType.THEORY,
            ),
            (
                "Cardiovascular Physiology",
                "Heart and blood vessel function",
                ConceptType.THEORY,
            ),
            (
                "Respiratory Physiology",
                "Breathing and gas exchange",
                ConceptType.THEORY,
            ),
            (
                "Renal Physiology",
                "Kidney function and fluid balance",
                ConceptType.THEORY,
            ),
            (
                "Gastrointestinal Physiology",
                "Digestion and absorption",
                ConceptType.THEORY,
            ),
            (
                "Neurophysiology",
                "Nervous system function",
                ConceptType.THEORY,
            ),
            (
                "Endocrine Physiology",
                "Hormone function and regulation",
                ConceptType.THEORY,
            ),
            (
                "Muscle Physiology",
                "Muscle contraction and function",
                ConceptType.THEORY,
            ),
            (
                "Reproductive Physiology",
                "Reproductive system function",
                ConceptType.THEORY,
            ),
            (
                "Exercise Physiology",
                "Body function during physical activity",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_metabolic_processes(self) -> None:
        """Initialize metabolic processes."""
        processes = [
            ("Glycolysis", "Glucose breakdown to pyruvate", "Cytoplasm", 2),
            ("Krebs Cycle", "Acetyl-CoA oxidation", "Mitochondria", 2),
            ("Electron Transport Chain", "ATP synthesis from electron flow", "Mitochondria", 34),
            ("Gluconeogenesis", "Glucose synthesis from non-carbs", "Liver", 0),
            ("Glycogenesis", "Glycogen synthesis", "Liver, Muscle", 0),
            ("Glycogenolysis", "Glycogen breakdown", "Liver, Muscle", 0),
            ("Lipogenesis", "Fat synthesis", "Adipose tissue", 0),
            ("Lipolysis", "Fat breakdown", "Adipose tissue", 0),
            ("Protein Synthesis", "Building proteins from amino acids", "Ribosomes", 0),
            ("Proteolysis", "Protein breakdown", "Various tissues", 0),
        ]

        for name, description, location, atp in processes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "location": location,
                "atp_yield": atp,
            })

    def initialize_vital_functions(self) -> None:
        """Initialize vital physiological functions."""
        functions = [
            ("Heart Rate", "Number of heartbeats per minute", 60, 100, "bpm"),
            ("Blood Pressure", "Force of blood against vessel walls", 90, 120, "mmHg systolic"),
            ("Respiratory Rate", "Breaths per minute", 12, 20, "breaths/min"),
            ("Body Temperature", "Core body temperature", 36.1, 37.2, "°C"),
            ("Oxygen Saturation", "Hemoglobin oxygen saturation", 95, 100, "%"),
            ("Blood Glucose", "Blood sugar level", 70, 100, "mg/dL fasting"),
            ("Blood pH", "Acid-base balance", 7.35, 7.45, "pH units"),
        ]

        for name, description, low, high, unit in functions:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "normal_low": low,
                "normal_high": high,
                "unit": unit,
            })

    def initialize_regulatory_mechanisms(self) -> None:
        """Initialize regulatory mechanisms."""
        mechanisms = [
            ("Negative Feedback", "Output reduces input, maintains stability", "Thermoregulation"),
            ("Positive Feedback", "Output amplifies input", "Blood clotting"),
            ("Hormonal Regulation", "Chemical messengers coordinate function", "Insulin-glucose"),
            ("Neural Regulation", "Nervous system controls function", "Heart rate control"),
            ("Local Regulation", "Local factors control nearby function", "Vasodilation"),
            ("Circadian Rhythm", "24-hour biological cycles", "Sleep-wake cycle"),
        ]

        for name, description, example in mechanisms:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["example"] = example

    def initialize_transport_mechanisms(self) -> None:
        """Initialize cellular transport mechanisms."""
        transport = [
            ("Passive Diffusion", "Movement down concentration gradient", False),
            ("Facilitated Diffusion", "Protein-assisted down gradient", False),
            ("Active Transport", "Movement against gradient using ATP", True),
            ("Osmosis", "Water movement across membrane", False),
            ("Endocytosis", "Cell engulfs material", True),
            ("Exocytosis", "Cell releases material", True),
        ]

        for name, description, requires_energy in transport:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["requires_energy"] = requires_energy

    def initialize_physiological_pairs(self) -> None:
        """Initialize fundamental physiological pairs with META 50/50 balance."""
        pairs = [
            ("Anabolic", "Catabolic", "Building vs breaking"),
            ("Homeostasis", "Imbalance", "Stable vs unstable"),
            ("Systole", "Diastole", "Contraction vs relaxation"),
            ("Inspiration", "Expiration", "Breathing in vs out"),
            ("Absorption", "Secretion", "Taking in vs releasing"),
            ("Synthesis", "Degradation", "Making vs destroying"),
            ("Activation", "Inhibition", "Starting vs stopping"),
            ("Feedback Positive", "Feedback Negative", "Amplifying vs dampening"),
            ("Aerobic", "Anaerobic", "With vs without oxygen"),
            ("Voluntary", "Involuntary", "Conscious vs automatic"),
            ("Rest", "Activity", "Recovery vs exertion"),
            ("Fasting", "Fed", "Empty vs full state"),
            ("Hydration", "Dehydration", "Water full vs depleted"),
            ("Acid", "Alkaline", "Low vs high pH"),
            ("Hyper", "Hypo", "Too much vs too little"),
            ("Acute", "Chronic", "Sudden vs lasting"),
            ("Local", "Systemic", "Site vs whole body"),
            ("Efferent", "Afferent", "Outgoing vs incoming"),
            ("Excretion", "Retention", "Removing vs keeping"),
            ("Growth", "Atrophy", "Building vs wasting"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Physiology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Physiology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_homeostatic_ranges(self) -> dict[str, dict[str, Any]]:
        """Get normal homeostatic ranges."""
        return {
            "blood_ph": {"low": 7.35, "high": 7.45, "unit": "pH"},
            "body_temp": {"low": 36.1, "high": 37.2, "unit": "°C"},
            "blood_glucose": {"low": 70, "high": 100, "unit": "mg/dL"},
            "blood_oxygen": {"low": 95, "high": 100, "unit": "%"},
            "sodium": {"low": 136, "high": 145, "unit": "mEq/L"},
            "potassium": {"low": 3.5, "high": 5.0, "unit": "mEq/L"},
            "calcium": {"low": 8.5, "high": 10.5, "unit": "mg/dL"},
        }

    def demonstrate_physiological_balance(self) -> dict[str, Any]:
        """Demonstrate physiological balance principles."""
        return {
            "concept": "Physiological Equilibrium",
            "dualities": {
                "anabolic_catabolic": {
                    "anabolism": 50.0,
                    "catabolism": 50.0,
                    "meaning": "Metabolic balance maintains body mass",
                },
                "cardiac_cycle": {
                    "systole": 50.0,
                    "diastole": 50.0,
                    "meaning": "Heart contraction and relaxation are balanced",
                },
                "respiratory_cycle": {
                    "inspiration": 50.0,
                    "expiration": 50.0,
                    "meaning": "Air in equals air out",
                },
            },
            "homeostatic_balance": {
                "input": 50.0,
                "output": 50.0,
                "description": "Steady state when input equals output",
            },
            "meta_meaning": "Physiology demonstrates META 50/50 in homeostasis",
        }


def create_physiology_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> PhysiologyDomain:
    """
    Factory function to create a fully initialized physiology domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized PhysiologyDomain
    """
    domain = PhysiologyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_metabolic_processes()
        domain.initialize_vital_functions()
        domain.initialize_regulatory_mechanisms()
        domain.initialize_transport_mechanisms()
        domain.initialize_physiological_pairs()

    return domain
