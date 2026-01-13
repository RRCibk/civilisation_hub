"""
Nutrition Science Domain
========================
Nutrition science knowledge domain with META 50/50 equilibrium.
Fundamental duality: Intake/Output (consumption vs expenditure).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class NutritionScienceDomain(KnowledgeDomain):
    """
    Nutrition Science knowledge domain.

    Fundamental Duality: Intake / Output
    - Intake: Consumption, nutrients, diet
    - Output: Expenditure, metabolism, activity

    Secondary Dualities:
    - Macro / Micro
    - Quality / Quantity
    - Individual / Population
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="NutritionScience",
            domain_type=DomainType.FUNDAMENTAL,
            description="The science of food, nutrients, and their effects on health",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Intake/Output duality."""
        self._domain.set_duality(
            positive_name="intake",
            positive_value=50,
            negative_name="output",
            negative_value=50,
            duality_name="nutrition_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental nutrition principles."""
        principles = [
            (
                "Energy Balance",
                "Intake equals output for weight maintenance",
            ),
            (
                "Essential Nutrients",
                "Some nutrients must come from diet",
            ),
            (
                "Variety",
                "Diverse diet provides complete nutrition",
            ),
            (
                "Moderation",
                "Excess of any nutrient can be harmful",
            ),
            (
                "Individual Variation",
                "Nutritional needs vary by person",
            ),
            (
                "Food as Medicine",
                "Nutrition affects health outcomes",
            ),
            (
                "Whole Foods",
                "Minimally processed foods retain nutrients",
            ),
            (
                "Timing Matters",
                "When you eat affects metabolism",
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
        """Get fundamental nutrition concepts."""
        return [
            "Nutrient",
            "Calorie",
            "Metabolism",
            "Diet",
            "Macronutrient",
            "Micronutrient",
            "Vitamin",
            "Mineral",
            "Protein",
            "Carbohydrate",
            "Fat",
            "Fiber",
            "Hydration",
            "Digestion",
            "Absorption",
        ]

    def initialize_branches(self) -> None:
        """Initialize major nutrition science branches."""
        branches = [
            (
                "Clinical Nutrition",
                "Nutrition in healthcare",
                ConceptType.THEORY,
            ),
            (
                "Sports Nutrition",
                "Nutrition for athletes",
                ConceptType.THEORY,
            ),
            (
                "Public Health Nutrition",
                "Population nutrition",
                ConceptType.THEORY,
            ),
            (
                "Nutritional Biochemistry",
                "Nutrient metabolism",
                ConceptType.THEORY,
            ),
            (
                "Food Science",
                "Food composition and processing",
                ConceptType.THEORY,
            ),
            (
                "Dietetics",
                "Diet therapy",
                ConceptType.THEORY,
            ),
            (
                "Nutrigenomics",
                "Nutrition and genes",
                ConceptType.THEORY,
            ),
            (
                "Pediatric Nutrition",
                "Child nutrition",
                ConceptType.THEORY,
            ),
            (
                "Geriatric Nutrition",
                "Elderly nutrition",
                ConceptType.THEORY,
            ),
            (
                "Functional Foods",
                "Foods with health benefits",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_macronutrients(self) -> None:
        """Initialize macronutrients."""
        macros = [
            ("Carbohydrates", "Energy source", "4 cal/g"),
            ("Proteins", "Building blocks", "4 cal/g"),
            ("Fats", "Energy storage", "9 cal/g"),
            ("Fiber", "Digestive health", "Non-caloric"),
            ("Water", "Essential solvent", "Non-caloric"),
            ("Alcohol", "Empty calories", "7 cal/g"),
        ]

        for name, function, energy in macros:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=function,
            )
            concept.metadata["energy"] = energy

    def initialize_micronutrients(self) -> None:
        """Initialize micronutrients."""
        micros = [
            ("Vitamins", "Organic compounds", "Catalysts"),
            ("Minerals", "Inorganic elements", "Structure"),
            ("Antioxidants", "Free radical neutralizers", "Protection"),
            ("Phytochemicals", "Plant compounds", "Health benefits"),
            ("Probiotics", "Beneficial bacteria", "Gut health"),
            ("Enzymes", "Catalytic proteins", "Digestion"),
        ]

        for name, description, function in micros:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["function"] = function

    def initialize_nutrition_pairs(self) -> None:
        """Initialize fundamental nutrition pairs with META 50/50 balance."""
        pairs = [
            ("Intake", "Output", "Consumption vs expenditure"),
            ("Macro", "Micro", "Large vs small nutrients"),
            ("Quality", "Quantity", "Type vs amount"),
            ("Individual", "Population", "Person vs group"),
            ("Essential", "Non-essential", "Required vs optional"),
            ("Deficiency", "Excess", "Too little vs too much"),
            ("Natural", "Processed", "Whole vs modified"),
            ("Animal", "Plant", "Meat vs vegetable"),
            ("Soluble", "Insoluble", "Dissolves vs does not dissolve"),
            ("Absorption", "Excretion", "Taking in vs expelling"),
            ("Anabolic", "Catabolic", "Building vs breaking"),
            ("Fasting", "Fed", "Without vs with food"),
            ("Acute", "Chronic", "Short vs long term"),
            ("Health", "Disease", "Wellness vs illness"),
            ("Hunger", "Satiety", "Empty vs full"),
            ("Simple", "Complex", "Basic vs elaborate foods"),
            ("Raw", "Cooked", "Unheated vs heated"),
            ("Organic", "Conventional", "Natural vs industrial"),
            ("Supplement", "Food", "Pills vs meals"),
            ("Prevention", "Treatment", "Avoiding vs managing"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Nutrition)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Nutrition)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_dietary_guidelines(self) -> dict[str, str]:
        """Get general dietary guidelines."""
        return {
            "variety": "Eat a variety of foods",
            "fruits_vegetables": "Emphasize fruits and vegetables",
            "whole_grains": "Choose whole grains",
            "lean_protein": "Select lean protein sources",
            "limit_sugar": "Reduce added sugars",
            "limit_sodium": "Reduce sodium intake",
        }

    def demonstrate_nutrition_balance(self) -> dict[str, Any]:
        """Demonstrate nutrition science balance principles."""
        return {
            "concept": "Nutrition Science Equilibrium",
            "dualities": {
                "intake_output": {
                    "intake": 50.0,
                    "output": 50.0,
                    "meaning": "Energy balance is fundamental",
                },
                "macro_micro": {
                    "macro": 50.0,
                    "micro": 50.0,
                    "meaning": "Both large and small nutrients essential",
                },
                "quality_quantity": {
                    "quality": 50.0,
                    "quantity": 50.0,
                    "meaning": "What and how much both matter",
                },
            },
            "diet_balance": {
                "variety": 50.0,
                "moderation": 50.0,
                "description": "Diverse and moderate eating optimal",
            },
            "meta_meaning": "Nutrition Science demonstrates META 50/50 in intake-output equilibrium",
        }


def create_nutrition_science_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> NutritionScienceDomain:
    """
    Factory function to create a fully initialized nutrition science domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized NutritionScienceDomain
    """
    domain = NutritionScienceDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_macronutrients()
        domain.initialize_micronutrients()
        domain.initialize_nutrition_pairs()

    return domain
