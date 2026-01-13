"""
Anatomy Domain
==============
Anatomical knowledge domain with META 50/50 equilibrium.
Fundamental duality: Structure/Function (form vs purpose).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class AnatomyDomain(KnowledgeDomain):
    """
    Anatomy knowledge domain.

    Fundamental Duality: Structure / Function
    - Structure: Physical form, architecture, organization
    - Function: Purpose, role, physiological action

    Secondary Dualities:
    - Anterior / Posterior
    - Superior / Inferior
    - Medial / Lateral
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Anatomy",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of body structure and organization",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Structure/Function duality."""
        self._domain.set_duality(
            positive_name="structure",
            positive_value=50,
            negative_name="function",
            negative_value=50,
            duality_name="anatomy_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental anatomical principles."""
        principles = [
            (
                "Structure-Function Relationship",
                "Anatomical structure is directly related to its function",
            ),
            (
                "Bilateral Symmetry",
                "The body is largely symmetrical along the sagittal plane",
            ),
            (
                "Hierarchical Organization",
                "Cells form tissues, tissues form organs, organs form systems",
            ),
            (
                "Anatomical Position",
                "Standard reference position for anatomical description",
            ),
            (
                "Complementarity of Structure",
                "What a structure can do depends on its form",
            ),
            (
                "Surface Area Principle",
                "Increased surface area enhances exchange functions",
            ),
            (
                "Homeostatic Design",
                "Body structures support maintaining internal balance",
            ),
            (
                "Evolutionary Conservation",
                "Basic body plans are conserved across species",
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
        """Get fundamental anatomy concepts."""
        return [
            "Cell",
            "Tissue",
            "Organ",
            "System",
            "Bone",
            "Muscle",
            "Nerve",
            "Vessel",
            "Joint",
            "Ligament",
            "Tendon",
            "Fascia",
            "Cavity",
            "Membrane",
            "Gland",
        ]

    def initialize_branches(self) -> None:
        """Initialize major anatomy branches."""
        branches = [
            (
                "Gross Anatomy",
                "Study of structures visible to naked eye",
                ConceptType.THEORY,
            ),
            (
                "Microscopic Anatomy",
                "Study of structures requiring magnification",
                ConceptType.THEORY,
            ),
            (
                "Developmental Anatomy",
                "Study of structural changes from conception to death",
                ConceptType.THEORY,
            ),
            (
                "Regional Anatomy",
                "Study of body regions",
                ConceptType.THEORY,
            ),
            (
                "Systemic Anatomy",
                "Study of organ systems",
                ConceptType.THEORY,
            ),
            (
                "Surface Anatomy",
                "Study of external body features",
                ConceptType.THEORY,
            ),
            (
                "Comparative Anatomy",
                "Study of anatomical similarities across species",
                ConceptType.THEORY,
            ),
            (
                "Radiographic Anatomy",
                "Study of structures using imaging",
                ConceptType.THEORY,
            ),
            (
                "Surgical Anatomy",
                "Anatomy relevant to surgical procedures",
                ConceptType.THEORY,
            ),
            (
                "Neuroanatomy",
                "Study of nervous system structure",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_body_systems(self) -> None:
        """Initialize major body systems."""
        systems = [
            ("Skeletal System", "Bones and cartilage", ["Support", "Protection", "Movement"]),
            ("Muscular System", "Muscles", ["Movement", "Posture", "Heat production"]),
            ("Nervous System", "Brain, spinal cord, nerves", ["Control", "Coordination"]),
            ("Cardiovascular System", "Heart and blood vessels", ["Transport", "Circulation"]),
            ("Respiratory System", "Lungs and airways", ["Gas exchange"]),
            ("Digestive System", "GI tract and accessory organs", ["Nutrition", "Absorption"]),
            ("Urinary System", "Kidneys and urinary tract", ["Excretion", "Fluid balance"]),
            ("Reproductive System", "Gonads and reproductive tract", ["Reproduction"]),
            ("Endocrine System", "Hormone-producing glands", ["Chemical regulation"]),
            ("Lymphatic System", "Lymph nodes and vessels", ["Immunity", "Fluid return"]),
            ("Integumentary System", "Skin and appendages", ["Protection", "Sensation"]),
        ]

        for name, components, functions in systems:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=f"Components: {components}",
            )
            concept.metadata["functions"] = functions

    def initialize_body_regions(self) -> None:
        """Initialize body regions."""
        regions = [
            ("Head", "Cranial and facial regions", ["Skull", "Face"]),
            ("Neck", "Cervical region", ["Cervical vertebrae", "Throat"]),
            ("Thorax", "Chest region", ["Rib cage", "Heart", "Lungs"]),
            ("Abdomen", "Abdominal region", ["Digestive organs", "Kidneys"]),
            ("Pelvis", "Pelvic region", ["Hip bones", "Reproductive organs"]),
            ("Upper Limb", "Arm and hand", ["Shoulder", "Arm", "Forearm", "Hand"]),
            ("Lower Limb", "Leg and foot", ["Thigh", "Leg", "Foot"]),
            ("Back", "Dorsal region", ["Vertebral column", "Back muscles"]),
        ]

        for name, description, components in regions:
            concept = self.create_concept(
                name=f"{name} Region",
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["components"] = components

    def initialize_tissue_types(self) -> None:
        """Initialize tissue classifications."""
        tissues = [
            ("Epithelial Tissue", "Covering and lining tissue", ["Skin", "Mucosa"]),
            ("Connective Tissue", "Support and binding tissue", ["Bone", "Cartilage", "Blood"]),
            ("Muscle Tissue", "Contractile tissue", ["Skeletal", "Cardiac", "Smooth"]),
            ("Nervous Tissue", "Signal-conducting tissue", ["Neurons", "Glia"]),
        ]

        for name, description, examples in tissues:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_directional_terms(self) -> None:
        """Initialize anatomical directional terms."""
        terms = [
            ("Anterior", "Front of body", "Ventral"),
            ("Posterior", "Back of body", "Dorsal"),
            ("Superior", "Above, toward head", "Cranial"),
            ("Inferior", "Below, toward feet", "Caudal"),
            ("Medial", "Toward midline", "Middle"),
            ("Lateral", "Away from midline", "Side"),
            ("Proximal", "Closer to attachment", "Near"),
            ("Distal", "Farther from attachment", "Far"),
            ("Superficial", "Toward surface", "External"),
            ("Deep", "Away from surface", "Internal"),
        ]

        for name, description, alternative in terms:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["alternative_term"] = alternative

    def initialize_anatomical_pairs(self) -> None:
        """Initialize fundamental anatomical pairs with META 50/50 balance."""
        pairs = [
            ("Structure", "Function", "Form vs purpose"),
            ("Anterior", "Posterior", "Front vs back"),
            ("Superior", "Inferior", "Above vs below"),
            ("Medial", "Lateral", "Center vs side"),
            ("Proximal", "Distal", "Near vs far from center"),
            ("Superficial", "Deep", "Surface vs internal"),
            ("Flexion", "Extension", "Bending vs straightening"),
            ("Adduction", "Abduction", "Toward vs away from midline"),
            ("Organ", "System", "Part vs whole"),
            ("Bone", "Muscle", "Support vs movement"),
            ("Artery", "Vein", "Away vs toward heart"),
            ("Nerve", "Vessel", "Signal vs transport"),
            ("Tissue", "Cell", "Group vs individual"),
            ("Gross", "Microscopic", "Visible vs magnified"),
            ("External", "Internal", "Outside vs inside"),
            ("Bilateral", "Unilateral", "Both vs one side"),
            ("Hollow", "Solid", "Empty vs filled organ"),
            ("Voluntary", "Involuntary", "Controlled vs automatic"),
            ("Skeletal", "Smooth", "Bone vs organ muscle"),
            ("Somatic", "Visceral", "Body wall vs organ"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Anatomy)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Anatomy)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_body_cavities(self) -> dict[str, dict[str, Any]]:
        """Get major body cavities."""
        return {
            "cranial": {
                "location": "Skull",
                "contents": ["Brain"],
            },
            "thoracic": {
                "location": "Chest",
                "contents": ["Heart", "Lungs"],
            },
            "abdominal": {
                "location": "Abdomen",
                "contents": ["Digestive organs", "Kidneys"],
            },
            "pelvic": {
                "location": "Pelvis",
                "contents": ["Bladder", "Reproductive organs"],
            },
            "vertebral": {
                "location": "Spine",
                "contents": ["Spinal cord"],
            },
        }

    def demonstrate_anatomical_balance(self) -> dict[str, Any]:
        """Demonstrate anatomical balance principles."""
        return {
            "concept": "Anatomical Equilibrium",
            "dualities": {
                "structure_function": {
                    "structure": 50.0,
                    "function": 50.0,
                    "meaning": "Form and function are inseparable",
                },
                "bilateral_symmetry": {
                    "left_side": 50.0,
                    "right_side": 50.0,
                    "meaning": "Body is largely bilaterally symmetric",
                },
                "organ_systems": {
                    "individual_organs": 50.0,
                    "integrated_systems": 50.0,
                    "meaning": "Parts function as integrated wholes",
                },
            },
            "positional_balance": {
                "anterior_posterior": "50/50",
                "superior_inferior": "50/50",
                "description": "Anatomical position defines balanced reference",
            },
            "meta_meaning": "Anatomy demonstrates META 50/50 in structure-function unity",
        }


def create_anatomy_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> AnatomyDomain:
    """
    Factory function to create a fully initialized anatomy domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized AnatomyDomain
    """
    domain = AnatomyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_body_systems()
        domain.initialize_body_regions()
        domain.initialize_tissue_types()
        domain.initialize_directional_terms()
        domain.initialize_anatomical_pairs()

    return domain
