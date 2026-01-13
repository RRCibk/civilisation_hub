"""
Microbiology Domain
===================
Microbiological knowledge domain with META 50/50 equilibrium.
Fundamental duality: Pathogen/Symbiont (harmful vs beneficial microorganisms).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class MicrobiologyDomain(KnowledgeDomain):
    """
    Microbiology knowledge domain.

    Fundamental Duality: Pathogen / Symbiont
    - Pathogen: Disease-causing, harmful, parasitic microorganisms
    - Symbiont: Beneficial, mutualistic, commensal microorganisms

    Secondary Dualities:
    - Bacteria / Virus
    - Aerobic / Anaerobic
    - Infection / Immunity
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Microbiology",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of microscopic organisms and their interactions",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Pathogen/Symbiont duality."""
        self._domain.set_duality(
            positive_name="pathogen",
            positive_value=50,
            negative_name="symbiont",
            negative_value=50,
            duality_name="microbiology_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental microbiological principles."""
        principles = [
            (
                "Germ Theory",
                "Microorganisms cause infectious diseases",
            ),
            (
                "Koch's Postulates",
                "Criteria for establishing causative relationship between microbe and disease",
            ),
            (
                "Spontaneous Generation Refuted",
                "Life arises only from existing life",
            ),
            (
                "Microbial Ubiquity",
                "Microorganisms are found in virtually all environments",
            ),
            (
                "Binary Fission",
                "Bacteria reproduce by dividing into two identical cells",
            ),
            (
                "Horizontal Gene Transfer",
                "Bacteria can transfer genes between cells",
            ),
            (
                "Antibiotic Resistance Evolution",
                "Bacteria evolve resistance to antibiotics through selection",
            ),
            (
                "Microbiome Importance",
                "Microbial communities are essential for host health",
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
        """Get fundamental microbiology concepts."""
        return [
            "Bacteria",
            "Virus",
            "Fungi",
            "Protozoa",
            "Archaea",
            "Cell",
            "Membrane",
            "Metabolism",
            "Infection",
            "Immunity",
            "Antibiotic",
            "Vaccine",
            "Culture",
            "Sterilization",
            "Microbiome",
        ]

    def initialize_branches(self) -> None:
        """Initialize major microbiology branches."""
        branches = [
            (
                "Bacteriology",
                "Study of bacteria",
                ConceptType.THEORY,
            ),
            (
                "Virology",
                "Study of viruses",
                ConceptType.THEORY,
            ),
            (
                "Mycology",
                "Study of fungi",
                ConceptType.THEORY,
            ),
            (
                "Parasitology",
                "Study of parasites",
                ConceptType.THEORY,
            ),
            (
                "Immunology",
                "Study of immune responses",
                ConceptType.THEORY,
            ),
            (
                "Medical Microbiology",
                "Microbes in human disease",
                ConceptType.THEORY,
            ),
            (
                "Environmental Microbiology",
                "Microbes in natural environments",
                ConceptType.THEORY,
            ),
            (
                "Industrial Microbiology",
                "Microbes in manufacturing",
                ConceptType.THEORY,
            ),
            (
                "Food Microbiology",
                "Microbes in food production and safety",
                ConceptType.THEORY,
            ),
            (
                "Molecular Microbiology",
                "Molecular mechanisms in microbes",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_microorganism_types(self) -> None:
        """Initialize types of microorganisms."""
        types = [
            ("Bacteria", "Prokaryotic single-celled organisms", True, ["E. coli", "Streptococcus"]),
            ("Archaea", "Prokaryotes distinct from bacteria", True, ["Methanogens", "Halophiles"]),
            ("Viruses", "Acellular obligate parasites", False, ["Influenza", "HIV", "Coronavirus"]),
            ("Fungi", "Eukaryotic heterotrophs", True, ["Yeast", "Mold", "Mushrooms"]),
            ("Protozoa", "Single-celled eukaryotes", True, ["Amoeba", "Paramecium", "Plasmodium"]),
            ("Algae", "Photosynthetic eukaryotes", True, ["Chlorella", "Diatoms"]),
        ]

        for name, description, has_cells, examples in types:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "cellular": has_cells,
                "examples": examples,
            })

    def initialize_bacterial_structures(self) -> None:
        """Initialize bacterial cell structures."""
        structures = [
            ("Cell Wall", "Rigid outer structure", "Protection and shape"),
            ("Cell Membrane", "Phospholipid bilayer", "Selective permeability"),
            ("Cytoplasm", "Gel-like interior", "Metabolic reactions"),
            ("Ribosome", "Protein synthesis machinery", "Translation"),
            ("Nucleoid", "Circular chromosome region", "Genetic material"),
            ("Plasmid", "Extra-chromosomal DNA", "Accessory genes"),
            ("Flagellum", "Whip-like appendage", "Motility"),
            ("Pilus", "Hair-like projection", "Attachment and conjugation"),
            ("Capsule", "Outer polysaccharide layer", "Protection from immune system"),
            ("Endospore", "Dormant resistant structure", "Survival"),
        ]

        for name, description, function in structures:
            concept = self.create_concept(
                name=f"Bacterial {name}",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["function"] = function

    def initialize_viral_components(self) -> None:
        """Initialize virus components and types."""
        components = [
            ("Capsid", "Protein coat", "Protects genetic material"),
            ("Envelope", "Lipid membrane", "Host cell recognition"),
            ("Spike Protein", "Surface glycoprotein", "Cell entry"),
            ("Genome", "DNA or RNA", "Genetic instructions"),
            ("Matrix", "Protein layer", "Structural support"),
        ]

        for name, description, function in components:
            concept = self.create_concept(
                name=f"Viral {name}",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["function"] = function

    def initialize_antimicrobial_agents(self) -> None:
        """Initialize antimicrobial agents."""
        agents = [
            ("Antibiotics", "Kill or inhibit bacteria", "Penicillin, Streptomycin"),
            ("Antivirals", "Inhibit viral replication", "Acyclovir, Remdesivir"),
            ("Antifungals", "Kill or inhibit fungi", "Fluconazole, Amphotericin"),
            ("Antiparasitics", "Kill parasites", "Chloroquine, Ivermectin"),
            ("Disinfectants", "Kill microbes on surfaces", "Bleach, Alcohol"),
            ("Antiseptics", "Kill microbes on skin", "Iodine, Chlorhexidine"),
        ]

        for name, description, examples in agents:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_microbiological_pairs(self) -> None:
        """Initialize fundamental microbiological pairs with META 50/50 balance."""
        pairs = [
            ("Pathogen", "Symbiont", "Harmful vs helpful"),
            ("Bacteria", "Virus", "Cellular vs acellular"),
            ("Aerobic", "Anaerobic", "Oxygen using vs avoiding"),
            ("Gram Positive", "Gram Negative", "Thick vs thin wall"),
            ("Infectious", "Dormant", "Active vs inactive"),
            ("Antibiotic", "Resistant", "Killed vs surviving"),
            ("Commensal", "Pathogenic", "Neutral vs harmful"),
            ("Probiotic", "Antibiotic", "Life promoting vs killing"),
            ("Spore", "Vegetative", "Dormant vs active form"),
            ("Lytic", "Lysogenic", "Bursting vs integrating"),
            ("Host", "Parasite", "Supporting vs exploiting"),
            ("Infection", "Immunity", "Attack vs defense"),
            ("Epidemic", "Endemic", "Spreading vs stable"),
            ("Culture", "Sterile", "Growing vs empty"),
            ("Fermentation", "Respiration", "Anaerobic vs aerobic"),
            ("Toxin", "Antitoxin", "Poison vs cure"),
            ("Colony", "Individual", "Group vs single"),
            ("Mutation", "Wild Type", "Changed vs original"),
            ("Conjugation", "Division", "Gene transfer vs copying"),
            ("Microbiome", "Pathosphere", "Beneficial vs harmful community"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Microbiology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Microbiology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_microbial_metabolism_types(self) -> dict[str, dict[str, str]]:
        """Get microbial metabolism classifications."""
        return {
            "phototroph": {
                "energy_source": "Light",
                "example": "Cyanobacteria",
            },
            "chemotroph": {
                "energy_source": "Chemical compounds",
                "example": "E. coli",
            },
            "autotroph": {
                "carbon_source": "CO2",
                "example": "Nitrifying bacteria",
            },
            "heterotroph": {
                "carbon_source": "Organic compounds",
                "example": "Most bacteria",
            },
            "lithotroph": {
                "electron_source": "Inorganic compounds",
                "example": "Iron-oxidizing bacteria",
            },
            "organotroph": {
                "electron_source": "Organic compounds",
                "example": "Fermenters",
            },
        }

    def demonstrate_microbial_balance(self) -> dict[str, Any]:
        """Demonstrate microbial balance principles."""
        return {
            "concept": "Microbial Equilibrium",
            "dualities": {
                "pathogen_symbiont": {
                    "pathogens": 50.0,
                    "symbionts": 50.0,
                    "meaning": "Most microbes are not harmful; balance is key",
                },
                "growth_death": {
                    "cell_division": 50.0,
                    "cell_death": 50.0,
                    "meaning": "Microbial populations reach equilibrium",
                },
                "infection_immunity": {
                    "microbial_attack": 50.0,
                    "immune_defense": 50.0,
                    "meaning": "Host-pathogen arms race",
                },
            },
            "ecosystem_balance": {
                "producers": 50.0,
                "decomposers": 50.0,
                "description": "Microbes cycle nutrients in ecosystems",
            },
            "meta_meaning": "Microbiology demonstrates META 50/50 in host-microbe relations",
        }


def create_microbiology_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> MicrobiologyDomain:
    """
    Factory function to create a fully initialized microbiology domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized MicrobiologyDomain
    """
    domain = MicrobiologyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_microorganism_types()
        domain.initialize_bacterial_structures()
        domain.initialize_viral_components()
        domain.initialize_antimicrobial_agents()
        domain.initialize_microbiological_pairs()

    return domain
