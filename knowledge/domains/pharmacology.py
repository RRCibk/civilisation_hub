"""
Pharmacology Domain
===================
Pharmacological knowledge domain with META 50/50 equilibrium.
Fundamental duality: Therapeutic/Toxic (beneficial vs harmful effects).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class PharmacologyDomain(KnowledgeDomain):
    """
    Pharmacology knowledge domain.

    Fundamental Duality: Therapeutic / Toxic
    - Therapeutic: Beneficial effects, healing, symptom relief
    - Toxic: Harmful effects, side effects, overdose

    Secondary Dualities:
    - Agonist / Antagonist
    - Absorption / Excretion
    - Efficacy / Safety
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Pharmacology",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of drugs, their actions, and therapeutic applications",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Therapeutic/Toxic duality."""
        self._domain.set_duality(
            positive_name="therapeutic",
            positive_value=50,
            negative_name="toxic",
            negative_value=50,
            duality_name="pharmacology_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental pharmacological principles."""
        principles = [
            (
                "Dose-Response Relationship",
                "Drug effect increases with dose up to a maximum",
            ),
            (
                "Therapeutic Index",
                "Ratio of toxic dose to therapeutic dose indicates safety margin",
            ),
            (
                "Receptor Theory",
                "Drugs act by binding to specific molecular receptors",
            ),
            (
                "First-Pass Metabolism",
                "Oral drugs are metabolized by liver before systemic circulation",
            ),
            (
                "Half-Life Principle",
                "Time for drug concentration to decrease by half",
            ),
            (
                "Bioavailability",
                "Fraction of administered drug that reaches systemic circulation",
            ),
            (
                "Drug-Drug Interaction",
                "One drug can affect the action of another",
            ),
            (
                "Tolerance Development",
                "Repeated exposure can decrease drug effect",
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
        """Get fundamental pharmacology concepts."""
        return [
            "Drug",
            "Dose",
            "Receptor",
            "Agonist",
            "Antagonist",
            "Efficacy",
            "Potency",
            "Bioavailability",
            "Half-life",
            "Metabolism",
            "Excretion",
            "Toxicity",
            "Side Effect",
            "Interaction",
            "Tolerance",
        ]

    def initialize_branches(self) -> None:
        """Initialize major pharmacology branches."""
        branches = [
            (
                "Pharmacokinetics",
                "Drug absorption, distribution, metabolism, excretion",
                ConceptType.THEORY,
            ),
            (
                "Pharmacodynamics",
                "Drug effects and mechanisms of action",
                ConceptType.THEORY,
            ),
            (
                "Clinical Pharmacology",
                "Drug use in patient care",
                ConceptType.THEORY,
            ),
            (
                "Toxicology",
                "Adverse effects and poisoning",
                ConceptType.THEORY,
            ),
            (
                "Pharmacogenomics",
                "Genetic variation in drug response",
                ConceptType.THEORY,
            ),
            (
                "Neuropharmacology",
                "Drugs affecting the nervous system",
                ConceptType.THEORY,
            ),
            (
                "Cardiovascular Pharmacology",
                "Drugs affecting heart and blood vessels",
                ConceptType.THEORY,
            ),
            (
                "Chemotherapy",
                "Drugs for cancer treatment",
                ConceptType.THEORY,
            ),
            (
                "Psychopharmacology",
                "Drugs affecting mental function",
                ConceptType.THEORY,
            ),
            (
                "Pharmacoepidemiology",
                "Drug effects in populations",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_drug_classes(self) -> None:
        """Initialize major drug classifications."""
        classes = [
            ("Antibiotics", "Kill or inhibit bacteria", ["Penicillin", "Ciprofloxacin"]),
            ("Antivirals", "Inhibit viral replication", ["Acyclovir", "Oseltamivir"]),
            ("Analgesics", "Relieve pain", ["Morphine", "Ibuprofen"]),
            ("Antihypertensives", "Lower blood pressure", ["Lisinopril", "Amlodipine"]),
            ("Antidepressants", "Treat depression", ["Fluoxetine", "Sertraline"]),
            ("Antipsychotics", "Treat psychosis", ["Haloperidol", "Risperidone"]),
            ("Anxiolytics", "Reduce anxiety", ["Diazepam", "Alprazolam"]),
            ("Anticoagulants", "Prevent blood clots", ["Warfarin", "Heparin"]),
            ("Diuretics", "Increase urine output", ["Furosemide", "Hydrochlorothiazide"]),
            ("Bronchodilators", "Open airways", ["Albuterol", "Theophylline"]),
        ]

        for name, description, examples in classes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_adme_processes(self) -> None:
        """Initialize ADME (Absorption, Distribution, Metabolism, Excretion)."""
        processes = [
            ("Absorption", "Drug entry into bloodstream", ["Oral", "IV", "Topical"]),
            ("Distribution", "Drug spread throughout body", ["Plasma protein binding", "Tissue distribution"]),
            ("Metabolism", "Drug transformation in body", ["Hepatic", "Cytochrome P450"]),
            ("Excretion", "Drug elimination from body", ["Renal", "Biliary", "Pulmonary"]),
        ]

        for name, description, pathways in processes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["pathways"] = pathways

    def initialize_receptor_types(self) -> None:
        """Initialize receptor classifications."""
        receptors = [
            ("Ion Channel Receptor", "Direct ion flow control", "Nicotinic acetylcholine receptor"),
            ("G-Protein Coupled Receptor", "Signal transduction via G-proteins", "Beta-adrenergic receptor"),
            ("Enzyme-Linked Receptor", "Kinase activity", "Insulin receptor"),
            ("Nuclear Receptor", "Gene transcription regulation", "Steroid receptors"),
            ("Transporter", "Molecule transport across membrane", "Dopamine transporter"),
        ]

        for name, description, example in receptors:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["example"] = example

    def initialize_drug_actions(self) -> None:
        """Initialize types of drug actions."""
        actions = [
            ("Agonist", "Activates receptor, mimics natural ligand", "Morphine on opioid receptors"),
            ("Antagonist", "Blocks receptor, prevents activation", "Naloxone blocks opioids"),
            ("Partial Agonist", "Activates receptor with submaximal effect", "Buprenorphine"),
            ("Inverse Agonist", "Produces opposite effect to agonist", "Some benzodiazepine ligands"),
            ("Allosteric Modulator", "Modifies receptor response", "Benzodiazepines on GABA"),
            ("Enzyme Inhibitor", "Blocks enzyme activity", "ACE inhibitors"),
            ("Enzyme Inducer", "Increases enzyme production", "Rifampin"),
        ]

        for name, description, example in actions:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["example"] = example

    def initialize_pharmacological_pairs(self) -> None:
        """Initialize fundamental pharmacological pairs with META 50/50 balance."""
        pairs = [
            ("Therapeutic", "Toxic", "Healing vs harming"),
            ("Agonist", "Antagonist", "Activating vs blocking"),
            ("Dose", "Response", "Input vs effect"),
            ("Absorption", "Excretion", "Taking in vs removing"),
            ("Generic", "Brand", "Common vs proprietary"),
            ("Prescription", "Over-the-counter", "Controlled vs free"),
            ("Acute", "Chronic", "Short vs long term"),
            ("Local", "Systemic", "Site vs whole body"),
            ("Onset", "Duration", "Start vs length"),
            ("Efficacy", "Safety", "Working vs not harming"),
            ("Synergy", "Antagonism", "Enhanced vs reduced"),
            ("Tolerance", "Sensitivity", "Reduced vs increased response"),
            ("Dependence", "Independence", "Needing vs not needing"),
            ("Side Effect", "Main Effect", "Unintended vs intended"),
            ("Oral", "Injection", "Swallowed vs injected"),
            ("Natural", "Synthetic", "Plant vs lab made"),
            ("Stimulant", "Depressant", "Activating vs calming"),
            ("Antibiotic", "Antiviral", "Bacteria vs virus targeting"),
            ("Preventive", "Curative", "Avoiding vs treating"),
            ("Legal", "Controlled", "Free vs regulated"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Pharmacology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Pharmacology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_key_parameters(self) -> dict[str, dict[str, str]]:
        """Get key pharmacological parameters."""
        return {
            "ED50": {
                "name": "Effective Dose 50",
                "definition": "Dose producing 50% of maximum effect",
            },
            "LD50": {
                "name": "Lethal Dose 50",
                "definition": "Dose lethal to 50% of population",
            },
            "therapeutic_index": {
                "name": "Therapeutic Index",
                "definition": "LD50/ED50 ratio, higher is safer",
            },
            "bioavailability": {
                "name": "Bioavailability",
                "definition": "Fraction reaching systemic circulation",
            },
            "half_life": {
                "name": "Half-life",
                "definition": "Time for concentration to halve",
            },
            "clearance": {
                "name": "Clearance",
                "definition": "Volume of plasma cleared per unit time",
            },
        }

    def demonstrate_pharmacological_balance(self) -> dict[str, Any]:
        """Demonstrate pharmacological balance principles."""
        return {
            "concept": "Pharmacological Equilibrium",
            "dualities": {
                "therapeutic_toxic": {
                    "benefit": 50.0,
                    "risk": 50.0,
                    "meaning": "All drugs balance benefit against risk",
                },
                "absorption_excretion": {
                    "drug_in": 50.0,
                    "drug_out": 50.0,
                    "meaning": "Steady state when input equals output",
                },
                "receptor_balance": {
                    "agonist_effect": 50.0,
                    "antagonist_effect": 50.0,
                    "meaning": "Drug effects can be balanced or blocked",
                },
            },
            "dose_response": {
                "effect_at_ed50": 50.0,
                "remaining_effect": 50.0,
                "description": "ED50 represents halfway to maximum effect",
            },
            "meta_meaning": "Pharmacology demonstrates META 50/50 in therapeutic windows",
        }


def create_pharmacology_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> PharmacologyDomain:
    """
    Factory function to create a fully initialized pharmacology domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized PharmacologyDomain
    """
    domain = PharmacologyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_drug_classes()
        domain.initialize_adme_processes()
        domain.initialize_receptor_types()
        domain.initialize_drug_actions()
        domain.initialize_pharmacological_pairs()

    return domain
