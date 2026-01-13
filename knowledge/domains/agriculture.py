"""
Agriculture Domain
==================
Agriculture knowledge domain with META 50/50 equilibrium.
Fundamental duality: Cultivation/Nature (human control vs natural processes).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class AgricultureDomain(KnowledgeDomain):
    """
    Agriculture knowledge domain.

    Fundamental Duality: Cultivation / Nature
    - Cultivation: Human intervention, farming, management
    - Nature: Natural processes, ecosystems, wild systems

    Secondary Dualities:
    - Intensive / Extensive
    - Conventional / Organic
    - Monoculture / Polyculture
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Agriculture",
            domain_type=DomainType.FUNDAMENTAL,
            description="The science and practice of farming and food production",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Cultivation/Nature duality."""
        self._domain.set_duality(
            positive_name="cultivation",
            positive_value=50,
            negative_name="nature",
            negative_value=50,
            duality_name="agriculture_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental agricultural principles."""
        principles = [
            (
                "Soil Health",
                "Healthy soil is foundation of agriculture",
            ),
            (
                "Water Management",
                "Water is essential limiting factor",
            ),
            (
                "Nutrient Cycling",
                "Nutrients must be replenished",
            ),
            (
                "Pest Management",
                "Balance pest control with ecosystem health",
            ),
            (
                "Crop Rotation",
                "Rotating crops maintains soil fertility",
            ),
            (
                "Biodiversity",
                "Diversity increases resilience",
            ),
            (
                "Sustainability",
                "Long-term productivity requires stewardship",
            ),
            (
                "Climate Adaptation",
                "Agriculture must adapt to climate",
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=85,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental agriculture concepts."""
        return [
            "Soil",
            "Crop",
            "Livestock",
            "Irrigation",
            "Fertilizer",
            "Pest",
            "Harvest",
            "Yield",
            "Seed",
            "Farm",
            "Field",
            "Season",
            "Climate",
            "Food",
            "Sustainability",
        ]

    def initialize_branches(self) -> None:
        """Initialize major agricultural branches."""
        branches = [
            (
                "Agronomy",
                "Crop production science",
                ConceptType.THEORY,
            ),
            (
                "Animal Husbandry",
                "Livestock management",
                ConceptType.THEORY,
            ),
            (
                "Horticulture",
                "Garden crops and ornamentals",
                ConceptType.THEORY,
            ),
            (
                "Soil Science",
                "Soil properties and management",
                ConceptType.THEORY,
            ),
            (
                "Agricultural Engineering",
                "Farm machinery and systems",
                ConceptType.THEORY,
            ),
            (
                "Plant Pathology",
                "Crop diseases",
                ConceptType.THEORY,
            ),
            (
                "Entomology",
                "Insect pests and beneficial insects",
                ConceptType.THEORY,
            ),
            (
                "Aquaculture",
                "Fish and aquatic farming",
                ConceptType.THEORY,
            ),
            (
                "Agroforestry",
                "Trees integrated with farming",
                ConceptType.THEORY,
            ),
            (
                "Agricultural Economics",
                "Farm business and markets",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_farming_systems(self) -> None:
        """Initialize farming systems."""
        systems = [
            ("Conventional", "High-input modern farming", "Industrial"),
            ("Organic", "Chemical-free farming", "Ecological"),
            ("Permaculture", "Permanent agriculture design", "Sustainable"),
            ("Hydroponics", "Soilless cultivation", "Controlled"),
            ("Agroecology", "Ecology-based farming", "Systems"),
            ("Precision Agriculture", "Data-driven farming", "Technology"),
        ]

        for name, description, category in systems:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["category"] = category

    def initialize_crop_types(self) -> None:
        """Initialize major crop categories."""
        crops = [
            ("Cereals", "Grain crops", "Wheat, rice, corn"),
            ("Legumes", "Nitrogen-fixing crops", "Beans, lentils, peas"),
            ("Oilseeds", "Oil-producing crops", "Soybean, canola, sunflower"),
            ("Vegetables", "Vegetable crops", "Tomato, potato, carrot"),
            ("Fruits", "Fruit crops", "Apple, citrus, grape"),
            ("Fiber Crops", "Fiber-producing plants", "Cotton, flax, hemp"),
        ]

        for name, description, examples in crops:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_agriculture_pairs(self) -> None:
        """Initialize fundamental agriculture pairs with META 50/50 balance."""
        pairs = [
            ("Cultivation", "Nature", "Control vs wild"),
            ("Intensive", "Extensive", "High-input vs low-input"),
            ("Conventional", "Organic", "Chemical vs natural"),
            ("Monoculture", "Polyculture", "Single vs multiple crops"),
            ("Irrigated", "Rainfed", "Watered vs natural rainfall"),
            ("Annual", "Perennial", "Replanted vs permanent"),
            ("Crop", "Livestock", "Plant vs animal"),
            ("Local", "Global", "Regional vs international"),
            ("Subsistence", "Commercial", "Self-sufficient vs market"),
            ("Traditional", "Modern", "Heritage vs technology"),
            ("Input", "Output", "Resources vs products"),
            ("Prevention", "Treatment", "Proactive vs reactive"),
            ("Quantity", "Quality", "Volume vs excellence"),
            ("Short-term", "Long-term", "Immediate vs sustainable"),
            ("Specialized", "Diversified", "Focused vs varied"),
            ("Mechanized", "Manual", "Machine vs hand labor"),
            ("Chemical", "Biological", "Synthetic vs living"),
            ("Centralized", "Distributed", "Large-scale vs small-scale"),
            ("Production", "Conservation", "Yield vs preservation"),
            ("Genetic", "Environmental", "Breeding vs management"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Agriculture)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Agriculture)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_sustainable_practices(self) -> dict[str, str]:
        """Get sustainable agriculture practices."""
        return {
            "crop_rotation": "Alternating crops to maintain soil health",
            "cover_cropping": "Planting to protect and enrich soil",
            "integrated_pest_management": "Combining pest control methods",
            "conservation_tillage": "Minimizing soil disturbance",
            "water_conservation": "Efficient irrigation practices",
            "composting": "Recycling organic matter",
        }

    def demonstrate_agriculture_balance(self) -> dict[str, Any]:
        """Demonstrate agriculture balance principles."""
        return {
            "concept": "Agriculture Equilibrium",
            "dualities": {
                "cultivation_nature": {
                    "cultivation": 50.0,
                    "nature": 50.0,
                    "meaning": "Working with nature, not against it",
                },
                "production_conservation": {
                    "production": 50.0,
                    "conservation": 50.0,
                    "meaning": "Balancing yield with stewardship",
                },
                "input_output": {
                    "input": 50.0,
                    "output": 50.0,
                    "meaning": "Sustainable resource cycling",
                },
            },
            "food_system_balance": {
                "quantity": 50.0,
                "quality": 50.0,
                "description": "Producing enough good food",
            },
            "meta_meaning": "Agriculture demonstrates META 50/50 in cultivation-nature harmony",
        }


def create_agriculture_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> AgricultureDomain:
    """
    Factory function to create a fully initialized agriculture domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized AgricultureDomain
    """
    domain = AgricultureDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_farming_systems()
        domain.initialize_crop_types()
        domain.initialize_agriculture_pairs()

    return domain
