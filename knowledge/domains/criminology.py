"""
Criminology Domain
==================
Criminology knowledge domain with META 50/50 equilibrium.
Fundamental duality: Crime/Justice (offense vs response).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class CriminologyDomain(KnowledgeDomain):
    """
    Criminology knowledge domain.

    Fundamental Duality: Crime / Justice
    - Crime: Offense, violation, deviant behavior
    - Justice: Response, punishment, rehabilitation

    Secondary Dualities:
    - Offender / Victim
    - Punishment / Rehabilitation
    - Control / Prevention
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Criminology",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of crime, criminals, and criminal justice systems",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Crime/Justice duality."""
        self._domain.set_duality(
            positive_name="crime",
            positive_value=50,
            negative_name="justice",
            negative_value=50,
            duality_name="criminology_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental criminological principles."""
        principles = [
            (
                "Social Construction of Crime",
                "What counts as crime varies across societies",
            ),
            (
                "Multiple Causation",
                "Crime results from multiple interacting factors",
            ),
            (
                "Differential Association",
                "Criminal behavior is learned through interaction",
            ),
            (
                "Rational Choice",
                "Offenders weigh costs and benefits",
            ),
            (
                "Labeling Effect",
                "Being labeled criminal affects behavior",
            ),
            (
                "Social Control",
                "Strong bonds to society prevent crime",
            ),
            (
                "Strain Theory",
                "Gap between goals and means creates crime",
            ),
            (
                "Routine Activities",
                "Crime requires opportunity, motivation, absence of guardians",
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=80,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental criminology concepts."""
        return [
            "Crime",
            "Criminal",
            "Victim",
            "Justice",
            "Punishment",
            "Deterrence",
            "Rehabilitation",
            "Recidivism",
            "Deviance",
            "Delinquency",
            "Incarceration",
            "Probation",
            "Parole",
            "Prevention",
            "Policing",
        ]

    def initialize_branches(self) -> None:
        """Initialize major criminology branches."""
        branches = [
            (
                "Classical Criminology",
                "Rational choice and deterrence",
                ConceptType.THEORY,
            ),
            (
                "Biological Criminology",
                "Biological factors in crime",
                ConceptType.THEORY,
            ),
            (
                "Psychological Criminology",
                "Individual psychological factors",
                ConceptType.THEORY,
            ),
            (
                "Sociological Criminology",
                "Social factors in crime",
                ConceptType.THEORY,
            ),
            (
                "Critical Criminology",
                "Power, inequality, and crime",
                ConceptType.THEORY,
            ),
            (
                "Feminist Criminology",
                "Gender and crime",
                ConceptType.THEORY,
            ),
            (
                "Environmental Criminology",
                "Crime and physical environment",
                ConceptType.THEORY,
            ),
            (
                "Victimology",
                "Study of crime victims",
                ConceptType.THEORY,
            ),
            (
                "Penology",
                "Study of punishment",
                ConceptType.THEORY,
            ),
            (
                "Forensic Criminology",
                "Criminal investigation science",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_theories(self) -> None:
        """Initialize criminological theories."""
        theories = [
            ("Strain Theory", "Merton", "Gap between goals and means"),
            ("Social Learning", "Akers", "Crime learned through reinforcement"),
            ("Labeling Theory", "Becker", "Deviance created by reaction"),
            ("Control Theory", "Hirschi", "Weak bonds lead to crime"),
            ("Routine Activities", "Cohen/Felson", "Opportunity theory"),
            ("General Theory of Crime", "Gottfredson/Hirschi", "Low self-control"),
            ("Life-Course Theory", "Sampson/Laub", "Trajectories and transitions"),
            ("Broken Windows", "Wilson/Kelling", "Disorder invites crime"),
        ]

        for name, founder, description in theories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_crime_types(self) -> None:
        """Initialize crime type categories."""
        types = [
            ("Violent Crime", "Harm to persons", "Murder, assault, robbery"),
            ("Property Crime", "Taking or damaging property", "Theft, burglary"),
            ("White-Collar Crime", "Business and professional", "Fraud, embezzlement"),
            ("Organized Crime", "Criminal enterprises", "Mafia, cartels"),
            ("Cybercrime", "Computer-based", "Hacking, identity theft"),
            ("Victimless Crime", "No direct victim", "Drug use, prostitution"),
        ]

        for name, description, examples in types:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["examples"] = examples

    def initialize_justice_models(self) -> None:
        """Initialize criminal justice models."""
        models = [
            ("Retributive Justice", "Punishment proportional to crime", "Desert"),
            ("Rehabilitative Justice", "Reform the offender", "Treatment"),
            ("Restorative Justice", "Repair harm done", "Victim-offender mediation"),
            ("Incapacitation", "Prevent future crime", "Imprisonment"),
            ("Deterrence", "Discourage future crime", "Swift, certain punishment"),
        ]

        for name, description, key_element in models:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["key_element"] = key_element

    def initialize_criminological_pairs(self) -> None:
        """Initialize fundamental criminological pairs with META 50/50 balance."""
        pairs = [
            ("Crime", "Justice", "Offense vs response"),
            ("Offender", "Victim", "Perpetrator vs harmed"),
            ("Punishment", "Rehabilitation", "Penalty vs reform"),
            ("Control", "Prevention", "After vs before"),
            ("Individual", "Social", "Person vs society factors"),
            ("Formal", "Informal", "Legal vs social control"),
            ("Deterrence", "Incapacitation", "Discourage vs prevent"),
            ("Retribution", "Restoration", "Punish vs repair"),
            ("Classical", "Positivist", "Choice vs determinism"),
            ("Street Crime", "Suite Crime", "Common vs elite"),
            ("Reported", "Unreported", "Known vs dark figure"),
            ("Juvenile", "Adult", "Young vs mature offender"),
            ("Violent", "Property", "Harm vs theft"),
            ("Recidivism", "Desistance", "Repeat vs stop"),
            ("Incarceration", "Community", "Prison vs alternatives"),
            ("Police", "Courts", "Enforcement vs adjudication"),
            ("Guilt", "Innocence", "Culpable vs not"),
            ("Intent", "Accident", "Purposeful vs unintentional"),
            ("Primary", "Secondary", "Direct vs indirect crime"),
            ("Opportunity", "Motivation", "Chance vs drive"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Criminology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Criminology)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_crime_triangle(self) -> dict[str, str]:
        """Get routine activities crime triangle."""
        return {
            "motivated_offender": "Person willing to commit crime",
            "suitable_target": "Person or object to victimize",
            "absence_of_guardian": "No capable protector present",
            "crime_occurrence": "All three must converge in time and space",
        }

    def demonstrate_criminology_balance(self) -> dict[str, Any]:
        """Demonstrate criminology balance principles."""
        return {
            "concept": "Criminology Equilibrium",
            "dualities": {
                "crime_justice": {
                    "crime": 50.0,
                    "justice": 50.0,
                    "meaning": "Crime and response are interdependent",
                },
                "punishment_rehabilitation": {
                    "punishment": 50.0,
                    "rehabilitation": 50.0,
                    "meaning": "Both penalty and reform needed",
                },
                "offender_victim": {
                    "offender": 50.0,
                    "victim": 50.0,
                    "meaning": "Both perspectives matter in justice",
                },
            },
            "justice_balance": {
                "retribution": 50.0,
                "restoration": 50.0,
                "description": "Punishment and healing both required",
            },
            "meta_meaning": "Criminology demonstrates META 50/50 in crime-justice balance",
        }


def create_criminology_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> CriminologyDomain:
    """
    Factory function to create a fully initialized criminology domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized CriminologyDomain
    """
    domain = CriminologyDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_theories()
        domain.initialize_crime_types()
        domain.initialize_justice_models()
        domain.initialize_criminological_pairs()

    return domain
