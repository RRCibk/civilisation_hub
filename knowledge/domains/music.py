"""
Music Domain
============
Music knowledge domain with META 50/50 equilibrium.
Fundamental duality: Sound/Silence (tone vs rest).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class MusicDomain(KnowledgeDomain):
    """
    Music knowledge domain.

    Fundamental Duality: Sound / Silence
    - Sound: Tone, pitch, vibration, presence
    - Silence: Rest, pause, absence

    Secondary Dualities:
    - Melody / Harmony
    - Rhythm / Meter
    - Consonance / Dissonance
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Music",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of organized sound in time",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Sound/Silence duality."""
        self._domain.set_duality(
            positive_name="sound",
            positive_value=50,
            negative_name="silence",
            negative_value=50,
            duality_name="music_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental music principles."""
        principles = [
            (
                "Temporal Art",
                "Music unfolds in time",
            ),
            (
                "Harmonic Series",
                "Overtones determine timbre and consonance",
            ),
            (
                "Rhythmic Organization",
                "Music requires temporal structure",
            ),
            (
                "Melodic Contour",
                "Pitch patterns create melody",
            ),
            (
                "Tension and Resolution",
                "Music creates and resolves tension",
            ),
            (
                "Repetition and Variation",
                "Music balances familiar and new",
            ),
            (
                "Expression",
                "Music communicates emotion",
            ),
            (
                "Cultural Embeddedness",
                "Music reflects cultural context",
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
        """Get fundamental music concepts."""
        return [
            "Sound",
            "Pitch",
            "Rhythm",
            "Melody",
            "Harmony",
            "Timbre",
            "Dynamics",
            "Tempo",
            "Meter",
            "Key",
            "Scale",
            "Chord",
            "Interval",
            "Form",
            "Texture",
        ]

    def initialize_branches(self) -> None:
        """Initialize major music branches."""
        branches = [
            (
                "Music Theory",
                "Structure and elements of music",
                ConceptType.THEORY,
            ),
            (
                "Musicology",
                "Historical study of music",
                ConceptType.THEORY,
            ),
            (
                "Ethnomusicology",
                "Music in cultural context",
                ConceptType.THEORY,
            ),
            (
                "Music Psychology",
                "Perception and cognition of music",
                ConceptType.THEORY,
            ),
            (
                "Music Education",
                "Teaching and learning music",
                ConceptType.THEORY,
            ),
            (
                "Composition",
                "Creating music",
                ConceptType.THEORY,
            ),
            (
                "Performance Practice",
                "Historical performance",
                ConceptType.THEORY,
            ),
            (
                "Acoustics",
                "Physics of sound",
                ConceptType.THEORY,
            ),
            (
                "Music Technology",
                "Technology in music",
                ConceptType.THEORY,
            ),
            (
                "Popular Music Studies",
                "Non-classical music",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_periods(self) -> None:
        """Initialize music history periods."""
        periods = [
            ("Medieval", "500-1400", "Gregorian chant, early polyphony"),
            ("Renaissance", "1400-1600", "Polyphony, secular music"),
            ("Baroque", "1600-1750", "Ornamentation, basso continuo"),
            ("Classical", "1750-1820", "Balance, clarity, form"),
            ("Romantic", "1820-1900", "Emotion, nationalism"),
            ("Modern", "1900-1970", "Experimentation, atonality"),
            ("Contemporary", "1970-present", "Pluralism, technology"),
        ]

        for name, dates, characteristics in periods:
            concept = self.create_concept(
                name=f"{name} Period",
                concept_type=ConceptType.DEFINITION,
                description=characteristics,
            )
            concept.metadata["dates"] = dates

    def initialize_elements(self) -> None:
        """Initialize music elements."""
        elements = [
            ("Pitch", "Frequency of sound", "Notes on staff"),
            ("Duration", "Length of sound", "Note values"),
            ("Dynamics", "Volume of sound", "Loud/soft"),
            ("Timbre", "Quality of sound", "Tone color"),
            ("Texture", "Layers of sound", "Monophonic/polyphonic"),
        ]

        for name, description, aspect in elements:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["aspect"] = aspect

    def initialize_forms(self) -> None:
        """Initialize musical forms."""
        forms = [
            ("Sonata", "Exposition-development-recapitulation", "Instrumental"),
            ("Symphony", "Multi-movement orchestral", "Large form"),
            ("Fugue", "Imitative counterpoint", "Baroque"),
            ("Rondo", "A-B-A-C-A pattern", "Recurring theme"),
            ("Theme and Variations", "Theme with alterations", "Variation form"),
            ("Song Form", "Verse-chorus structure", "Popular music"),
        ]

        for name, structure, category in forms:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=structure,
            )
            concept.metadata["category"] = category

    def initialize_music_pairs(self) -> None:
        """Initialize fundamental music pairs with META 50/50 balance."""
        pairs = [
            ("Sound", "Silence", "Tone vs rest"),
            ("Melody", "Harmony", "Horizontal vs vertical"),
            ("Rhythm", "Meter", "Pattern vs pulse"),
            ("Consonance", "Dissonance", "Stable vs unstable"),
            ("Major", "Minor", "Bright vs dark"),
            ("Tension", "Resolution", "Instability vs stability"),
            ("Strong", "Weak", "Accented vs unaccented"),
            ("High", "Low", "Treble vs bass"),
            ("Fast", "Slow", "Quick vs gradual"),
            ("Loud", "Soft", "Forte vs piano"),
            ("Thick", "Thin", "Many vs few voices"),
            ("Simple", "Complex", "Basic vs elaborate"),
            ("Diatonic", "Chromatic", "In key vs all notes"),
            ("Tonal", "Atonal", "Centered vs uncentered"),
            ("Monophonic", "Polyphonic", "One vs many voices"),
            ("Homophonic", "Contrapuntal", "Chordal vs independent"),
            ("Vocal", "Instrumental", "Sung vs played"),
            ("Live", "Recorded", "Present vs captured"),
            ("Composed", "Improvised", "Written vs spontaneous"),
            ("Western", "Non-Western", "European vs other traditions"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Music)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Music)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_circle_of_fifths(self) -> dict[str, str]:
        """Get circle of fifths relationships."""
        return {
            "C_major": "No sharps or flats",
            "G_major": "1 sharp (F#)",
            "D_major": "2 sharps",
            "A_major": "3 sharps",
            "E_major": "4 sharps",
            "B_major": "5 sharps",
            "F_major": "1 flat (Bb)",
        }

    def demonstrate_music_balance(self) -> dict[str, Any]:
        """Demonstrate music balance principles."""
        return {
            "concept": "Music Equilibrium",
            "dualities": {
                "sound_silence": {
                    "sound": 50.0,
                    "silence": 50.0,
                    "meaning": "Music is defined by both presence and absence",
                },
                "tension_resolution": {
                    "tension": 50.0,
                    "resolution": 50.0,
                    "meaning": "Music creates and resolves expectation",
                },
                "consonance_dissonance": {
                    "consonance": 50.0,
                    "dissonance": 50.0,
                    "meaning": "Stability and instability create movement",
                },
            },
            "harmonic_balance": {
                "tonic": 50.0,
                "dominant": 50.0,
                "description": "Home and away create musical journey",
            },
            "meta_meaning": "Music demonstrates META 50/50 in sound-silence alternation",
        }


def create_music_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> MusicDomain:
    """
    Factory function to create a fully initialized music domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized MusicDomain
    """
    domain = MusicDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_periods()
        domain.initialize_elements()
        domain.initialize_forms()
        domain.initialize_music_pairs()

    return domain
