"""
Film Domain
===========
Film knowledge domain with META 50/50 equilibrium.
Fundamental duality: Image/Sound (visual vs audio).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class FilmDomain(KnowledgeDomain):
    """
    Film knowledge domain.

    Fundamental Duality: Image / Sound
    - Image: Visual, picture, mise-en-scène
    - Sound: Audio, music, dialogue

    Secondary Dualities:
    - Narrative / Spectacle
    - Fiction / Documentary
    - Art / Commerce
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Film",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of motion pictures as art form and medium",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Image/Sound duality."""
        self._domain.set_duality(
            positive_name="image",
            positive_value=50,
            negative_name="sound",
            negative_value=50,
            duality_name="film_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental film principles."""
        principles = [
            (
                "Persistence of Vision",
                "Eye retains image allowing motion illusion",
            ),
            (
                "Montage",
                "Meaning created through editing juxtaposition",
            ),
            (
                "Mise-en-scène",
                "Everything in the frame contributes meaning",
            ),
            (
                "Diegesis",
                "Story world exists coherently",
            ),
            (
                "Suture",
                "Viewer is stitched into film's perspective",
            ),
            (
                "Apparatus Theory",
                "Cinema apparatus shapes experience",
            ),
            (
                "Auteur Theory",
                "Director as creative author",
            ),
            (
                "Genre Convention",
                "Genres have recognizable patterns",
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
        """Get fundamental film concepts."""
        return [
            "Shot",
            "Scene",
            "Sequence",
            "Editing",
            "Camera",
            "Lighting",
            "Sound",
            "Music",
            "Dialogue",
            "Mise-en-scène",
            "Narrative",
            "Character",
            "Genre",
            "Style",
            "Director",
        ]

    def initialize_branches(self) -> None:
        """Initialize major film branches."""
        branches = [
            (
                "Film Theory",
                "Theoretical approaches to cinema",
                ConceptType.THEORY,
            ),
            (
                "Film History",
                "Historical development of cinema",
                ConceptType.THEORY,
            ),
            (
                "Film Criticism",
                "Analysis and evaluation",
                ConceptType.THEORY,
            ),
            (
                "Film Production",
                "Making films",
                ConceptType.THEORY,
            ),
            (
                "Cinematography",
                "Camera and lighting",
                ConceptType.THEORY,
            ),
            (
                "Film Editing",
                "Assembling footage",
                ConceptType.THEORY,
            ),
            (
                "Sound Design",
                "Audio elements",
                ConceptType.THEORY,
            ),
            (
                "Screenwriting",
                "Script creation",
                ConceptType.THEORY,
            ),
            (
                "Documentary Studies",
                "Non-fiction film",
                ConceptType.THEORY,
            ),
            (
                "Animation Studies",
                "Animated film",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_genres(self) -> None:
        """Initialize film genres."""
        genres = [
            ("Drama", "Serious narrative", "Character-driven"),
            ("Comedy", "Humorous narrative", "Entertainment"),
            ("Action", "Physical conflict", "Spectacle"),
            ("Horror", "Fear and dread", "Suspense"),
            ("Science Fiction", "Speculative futures", "Technology"),
            ("Documentary", "Non-fiction", "Reality"),
            ("Animation", "Frame-by-frame creation", "Visual style"),
            ("Western", "American frontier", "Genre conventions"),
        ]

        for name, description, characteristic in genres:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["characteristic"] = characteristic

    def initialize_techniques(self) -> None:
        """Initialize film techniques."""
        techniques = [
            ("Close-up", "Tight framing", "Emotional emphasis"),
            ("Long Shot", "Wide framing", "Context"),
            ("Tracking Shot", "Camera moves with subject", "Movement"),
            ("Cross-cutting", "Parallel editing", "Simultaneous action"),
            ("Fade", "Gradual transition", "Time passage"),
            ("Montage", "Rapid editing", "Compression"),
        ]

        for name, description, function in techniques:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["function"] = function

    def initialize_movements(self) -> None:
        """Initialize film movements."""
        movements = [
            ("German Expressionism", "1920s", "Stylized, psychological"),
            ("Soviet Montage", "1920s", "Editing as meaning"),
            ("Italian Neorealism", "1940s", "Location, non-actors"),
            ("French New Wave", "1960s", "Personal, innovative"),
            ("New Hollywood", "1970s", "Director-driven"),
            ("Dogme 95", "1990s", "Back to basics"),
        ]

        for name, period, description in movements:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["period"] = period

    def initialize_film_pairs(self) -> None:
        """Initialize fundamental film pairs with META 50/50 balance."""
        pairs = [
            ("Image", "Sound", "Visual vs audio"),
            ("Narrative", "Spectacle", "Story vs display"),
            ("Fiction", "Documentary", "Imagined vs actual"),
            ("Art", "Commerce", "Aesthetic vs profit"),
            ("Diegetic", "Non-diegetic", "In-world vs outside"),
            ("Shot", "Edit", "Filming vs cutting"),
            ("Objective", "Subjective", "External vs internal"),
            ("Continuity", "Discontinuity", "Smooth vs jarring"),
            ("Realism", "Formalism", "Natural vs stylized"),
            ("On-screen", "Off-screen", "Visible vs implied"),
            ("Synchronous", "Asynchronous", "Matched vs unmatched"),
            ("High Key", "Low Key", "Bright vs dark lighting"),
            ("Long Take", "Rapid Cutting", "Extended vs quick"),
            ("Close-up", "Long Shot", "Tight vs wide"),
            ("Static", "Mobile", "Fixed vs moving camera"),
            ("Silent", "Sound", "Pre vs post 1927"),
            ("Black and White", "Color", "Monochrome vs chromatic"),
            ("2D", "3D", "Flat vs depth"),
            ("Theatrical", "Streaming", "Cinema vs home"),
            ("Auteur", "Studio", "Director vs system"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Film)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Film)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_shot_types(self) -> dict[str, str]:
        """Get basic shot types."""
        return {
            "extreme_close_up": "Very tight, detail",
            "close_up": "Face fills frame",
            "medium_shot": "Waist up",
            "full_shot": "Full body",
            "long_shot": "Figure in environment",
            "extreme_long_shot": "Figure small in landscape",
        }

    def demonstrate_film_balance(self) -> dict[str, Any]:
        """Demonstrate film balance principles."""
        return {
            "concept": "Film Equilibrium",
            "dualities": {
                "image_sound": {
                    "image": 50.0,
                    "sound": 50.0,
                    "meaning": "Visual and audio equally create meaning",
                },
                "narrative_spectacle": {
                    "narrative": 50.0,
                    "spectacle": 50.0,
                    "meaning": "Story and display work together",
                },
                "art_commerce": {
                    "art": 50.0,
                    "commerce": 50.0,
                    "meaning": "Film is both art and industry",
                },
            },
            "audiovisual_balance": {
                "seeing": 50.0,
                "hearing": 50.0,
                "description": "Cinema engages multiple senses",
            },
            "meta_meaning": "Film demonstrates META 50/50 in image-sound synthesis",
        }


def create_film_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> FilmDomain:
    """
    Factory function to create a fully initialized film domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized FilmDomain
    """
    domain = FilmDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_genres()
        domain.initialize_techniques()
        domain.initialize_movements()
        domain.initialize_film_pairs()

    return domain
