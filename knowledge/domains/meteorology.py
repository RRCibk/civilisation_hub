"""
Meteorology Domain
==================
Meteorological knowledge domain with META 50/50 equilibrium.
Fundamental duality: High Pressure/Low Pressure (atmospheric stability vs instability).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class MeteorologyDomain(KnowledgeDomain):
    """
    Meteorology knowledge domain.

    Fundamental Duality: High Pressure / Low Pressure
    - High Pressure: Stable, sinking air, clear skies, anticyclones
    - Low Pressure: Unstable, rising air, clouds, cyclones, storms

    Secondary Dualities:
    - Warm / Cold
    - Dry / Humid
    - Calm / Storm
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Meteorology",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of atmospheric phenomena and weather patterns",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize High Pressure/Low Pressure duality."""
        self._domain.set_duality(
            positive_name="high_pressure",
            positive_value=50,
            negative_name="low_pressure",
            negative_value=50,
            duality_name="meteorology_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental meteorological principles."""
        principles = [
            (
                "Coriolis Effect",
                "Earth's rotation deflects moving air masses",
            ),
            (
                "Ideal Gas Law",
                "Pressure, volume, and temperature are related in gases",
            ),
            (
                "Adiabatic Process",
                "Rising air cools and sinking air warms without heat exchange",
            ),
            (
                "Conservation of Angular Momentum",
                "Rotating air systems maintain angular momentum",
            ),
            (
                "Hydrostatic Balance",
                "Atmospheric pressure balances gravitational force",
            ),
            (
                "Energy Balance",
                "Solar energy input equals Earth's radiative output",
            ),
            (
                "Latent Heat Transfer",
                "Phase changes of water transfer significant energy",
            ),
            (
                "Pressure Gradient Force",
                "Air flows from high to low pressure",
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
        """Get fundamental meteorology concepts."""
        return [
            "Atmosphere",
            "Pressure",
            "Temperature",
            "Humidity",
            "Wind",
            "Cloud",
            "Precipitation",
            "Front",
            "Cyclone",
            "Anticyclone",
            "Storm",
            "Climate",
            "Weather",
            "Forecast",
            "Jet Stream",
        ]

    def initialize_branches(self) -> None:
        """Initialize major meteorology branches."""
        branches = [
            (
                "Synoptic Meteorology",
                "Large-scale weather patterns and forecasting",
                ConceptType.THEORY,
            ),
            (
                "Mesoscale Meteorology",
                "Regional weather phenomena",
                ConceptType.THEORY,
            ),
            (
                "Micrometeorology",
                "Small-scale atmospheric processes",
                ConceptType.THEORY,
            ),
            (
                "Dynamic Meteorology",
                "Physics of atmospheric motion",
                ConceptType.THEORY,
            ),
            (
                "Physical Meteorology",
                "Physical processes in the atmosphere",
                ConceptType.THEORY,
            ),
            (
                "Tropical Meteorology",
                "Weather in tropical regions",
                ConceptType.THEORY,
            ),
            (
                "Polar Meteorology",
                "Weather in polar regions",
                ConceptType.THEORY,
            ),
            (
                "Agricultural Meteorology",
                "Weather impacts on agriculture",
                ConceptType.THEORY,
            ),
            (
                "Aviation Meteorology",
                "Weather for flight operations",
                ConceptType.THEORY,
            ),
            (
                "Hydrometeorology",
                "Water in the atmosphere",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_atmospheric_layers(self) -> None:
        """Initialize atmospheric layer structure."""
        layers = [
            ("Troposphere", "Weather layer, 0-12 km", 12, -56),
            ("Stratosphere", "Ozone layer, 12-50 km", 50, 0),
            ("Mesosphere", "Meteor burning, 50-80 km", 80, -90),
            ("Thermosphere", "Aurora layer, 80-700 km", 700, 1500),
            ("Exosphere", "Transition to space, >700 km", 10000, 300),
        ]

        for name, description, top_km, temp_c in layers:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "top_altitude_km": top_km,
                "typical_temp_c": temp_c,
            })

    def initialize_cloud_types(self) -> None:
        """Initialize cloud classifications."""
        clouds = [
            ("Cirrus", "High, wispy ice clouds", "High", "Ice"),
            ("Cirrostratus", "High, thin sheet clouds", "High", "Ice"),
            ("Cirrocumulus", "High, small puffs", "High", "Ice"),
            ("Altostratus", "Middle, gray sheet", "Middle", "Mixed"),
            ("Altocumulus", "Middle, puffy masses", "Middle", "Water"),
            ("Stratus", "Low, uniform gray layer", "Low", "Water"),
            ("Stratocumulus", "Low, lumpy layer", "Low", "Water"),
            ("Cumulus", "Fair weather puffs", "Low", "Water"),
            ("Cumulonimbus", "Towering storm clouds", "Vertical", "Mixed"),
            ("Nimbostratus", "Dark rain clouds", "Low-Middle", "Water"),
        ]

        for name, description, level, composition in clouds:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "altitude_level": level,
                "composition": composition,
            })

    def initialize_weather_phenomena(self) -> None:
        """Initialize weather phenomena."""
        phenomena = [
            ("Thunderstorm", "Convective storm with lightning", "Severe"),
            ("Tornado", "Rotating column of air", "Extreme"),
            ("Hurricane", "Large rotating tropical storm", "Extreme"),
            ("Blizzard", "Severe snowstorm with high winds", "Severe"),
            ("Fog", "Low-lying cloud at surface", "Mild"),
            ("Hail", "Ice precipitation from thunderstorms", "Severe"),
            ("Drought", "Extended period of low precipitation", "Extreme"),
            ("Heat Wave", "Prolonged period of excessive heat", "Severe"),
            ("Cold Wave", "Rapid drop in temperature", "Severe"),
            ("Flash Flood", "Rapid flooding from heavy rain", "Extreme"),
        ]

        for name, description, severity in phenomena:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["severity"] = severity

    def initialize_frontal_systems(self) -> None:
        """Initialize frontal system types."""
        fronts = [
            ("Cold Front", "Cold air replacing warm", "Rapid cooling, storms possible"),
            ("Warm Front", "Warm air replacing cold", "Gradual warming, steady rain"),
            ("Stationary Front", "Neither air mass advancing", "Extended cloudiness"),
            ("Occluded Front", "Cold front overtaking warm", "Complex weather patterns"),
        ]

        for name, description, weather in fronts:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["typical_weather"] = weather

    def initialize_meteorological_pairs(self) -> None:
        """Initialize fundamental meteorological pairs with META 50/50 balance."""
        pairs = [
            ("High Pressure", "Low Pressure", "Stable vs unstable"),
            ("Warm", "Cold", "Heat vs chill"),
            ("Dry", "Humid", "Arid vs moist"),
            ("Clear", "Cloudy", "Open vs covered sky"),
            ("Calm", "Storm", "Peace vs turbulence"),
            ("Front", "Back", "Leading vs trailing edge"),
            ("Rising", "Falling", "Ascending vs descending air"),
            ("Precipitation", "Evaporation", "Falling vs rising water"),
            ("Condensation", "Vaporization", "Forming vs dispersing"),
            ("Cyclone", "Anticyclone", "Rotating low vs high"),
            ("Thunder", "Lightning", "Sound vs light"),
            ("Wind", "Calm", "Moving vs still air"),
            ("Tropical", "Polar", "Warm vs cold origin"),
            ("Maritime", "Continental", "Ocean vs land influenced"),
            ("Convection", "Radiation", "Rising vs emitting heat"),
            ("Fog", "Clear", "Obscured vs visible"),
            ("Frost", "Thaw", "Freezing vs melting"),
            ("Drought", "Flood", "Too little vs too much"),
            ("Seasonal", "Constant", "Changing vs stable"),
            ("Forecast", "Observation", "Predicted vs measured"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Meteorology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Meteorology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_beaufort_scale(self) -> dict[int, dict[str, Any]]:
        """Get Beaufort wind scale."""
        return {
            0: {"name": "Calm", "speed_kmh": 0, "description": "Smoke rises vertically"},
            1: {"name": "Light Air", "speed_kmh": 5, "description": "Smoke drift shows direction"},
            2: {"name": "Light Breeze", "speed_kmh": 11, "description": "Leaves rustle"},
            3: {"name": "Gentle Breeze", "speed_kmh": 19, "description": "Leaves in motion"},
            4: {"name": "Moderate Breeze", "speed_kmh": 28, "description": "Small branches move"},
            5: {"name": "Fresh Breeze", "speed_kmh": 38, "description": "Small trees sway"},
            6: {"name": "Strong Breeze", "speed_kmh": 49, "description": "Large branches move"},
            7: {"name": "Near Gale", "speed_kmh": 61, "description": "Whole trees in motion"},
            8: {"name": "Gale", "speed_kmh": 74, "description": "Twigs break off"},
            9: {"name": "Strong Gale", "speed_kmh": 88, "description": "Branches break"},
            10: {"name": "Storm", "speed_kmh": 102, "description": "Trees uprooted"},
            11: {"name": "Violent Storm", "speed_kmh": 117, "description": "Widespread damage"},
            12: {"name": "Hurricane", "speed_kmh": 130, "description": "Devastation"},
        }

    def demonstrate_atmospheric_balance(self) -> dict[str, Any]:
        """Demonstrate atmospheric balance principles."""
        return {
            "concept": "Atmospheric Equilibrium",
            "dualities": {
                "pressure_balance": {
                    "high_pressure": 50.0,
                    "low_pressure": 50.0,
                    "meaning": "Global atmospheric pressure averages to balance",
                },
                "energy_balance": {
                    "solar_input": 50.0,
                    "earth_radiation": 50.0,
                    "meaning": "Earth radiates as much as it receives",
                },
                "water_cycle": {
                    "evaporation": 50.0,
                    "precipitation": 50.0,
                    "meaning": "Water evaporated equals water precipitated",
                },
            },
            "thermal_balance": {
                "warming": 50.0,
                "cooling": 50.0,
                "description": "Day heating balances night cooling",
            },
            "meta_meaning": "Meteorology demonstrates META 50/50 in atmospheric balance",
        }


def create_meteorology_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> MeteorologyDomain:
    """
    Factory function to create a fully initialized meteorology domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized MeteorologyDomain
    """
    domain = MeteorologyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_atmospheric_layers()
        domain.initialize_cloud_types()
        domain.initialize_weather_phenomena()
        domain.initialize_frontal_systems()
        domain.initialize_meteorological_pairs()

    return domain
