"""
Education Domain
================
Education knowledge domain with META 50/50 equilibrium.
Fundamental duality: Teaching/Learning (instruction vs acquisition).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class EducationDomain(KnowledgeDomain):
    """
    Education knowledge domain.

    Fundamental Duality: Teaching / Learning
    - Teaching: Instruction, pedagogy, transmission
    - Learning: Acquisition, understanding, construction

    Secondary Dualities:
    - Theory / Practice
    - Formal / Informal
    - Content / Process
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Education",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of teaching, learning, and educational systems",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Teaching/Learning duality."""
        self._domain.set_duality(
            positive_name="teaching",
            positive_value=50,
            negative_name="learning",
            negative_value=50,
            duality_name="education_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental educational principles."""
        principles = [
            (
                "Zone of Proximal Development",
                "Learning occurs between current and potential level",
            ),
            (
                "Constructivism",
                "Learners construct knowledge actively",
            ),
            (
                "Multiple Intelligences",
                "Intelligence takes many forms",
            ),
            (
                "Scaffolding",
                "Support enables learning of challenging material",
            ),
            (
                "Prior Knowledge",
                "New learning builds on existing knowledge",
            ),
            (
                "Transfer",
                "Learning in one context can apply to others",
            ),
            (
                "Motivation",
                "Learning requires engagement and interest",
            ),
            (
                "Feedback",
                "Information about performance improves learning",
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
        """Get fundamental education concepts."""
        return [
            "Teaching",
            "Learning",
            "Curriculum",
            "Assessment",
            "Pedagogy",
            "Instruction",
            "Knowledge",
            "Skill",
            "Understanding",
            "Motivation",
            "Development",
            "Intelligence",
            "Literacy",
            "Competence",
            "Achievement",
        ]

    def initialize_branches(self) -> None:
        """Initialize major education branches."""
        branches = [
            (
                "Curriculum Studies",
                "What should be taught",
                ConceptType.THEORY,
            ),
            (
                "Educational Psychology",
                "Psychological aspects of learning",
                ConceptType.THEORY,
            ),
            (
                "Sociology of Education",
                "Social aspects of education",
                ConceptType.THEORY,
            ),
            (
                "Philosophy of Education",
                "Aims and values in education",
                ConceptType.THEORY,
            ),
            (
                "Comparative Education",
                "Educational systems across countries",
                ConceptType.THEORY,
            ),
            (
                "Special Education",
                "Education for diverse learners",
                ConceptType.THEORY,
            ),
            (
                "Higher Education",
                "Tertiary and university education",
                ConceptType.THEORY,
            ),
            (
                "Adult Education",
                "Lifelong learning",
                ConceptType.THEORY,
            ),
            (
                "Educational Technology",
                "Technology in education",
                ConceptType.THEORY,
            ),
            (
                "Assessment and Evaluation",
                "Measuring learning outcomes",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_learning_theories(self) -> None:
        """Initialize learning theories."""
        theories = [
            ("Behaviorism", "Skinner", "Learning as behavior change"),
            ("Cognitivism", "Piaget", "Learning as mental processing"),
            ("Constructivism", "Vygotsky", "Learning as knowledge construction"),
            ("Social Learning", "Bandura", "Learning through observation"),
            ("Experiential Learning", "Kolb", "Learning through experience"),
            ("Connectivism", "Siemens", "Learning in digital age"),
            ("Humanistic", "Rogers", "Self-directed learning"),
            ("Transformative", "Mezirow", "Learning changes perspectives"),
        ]

        for name, founder, description in theories:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.THEORY,
                description=description,
            )
            concept.metadata["founder"] = founder

    def initialize_pedagogical_approaches(self) -> None:
        """Initialize pedagogical approaches."""
        approaches = [
            ("Direct Instruction", "Teacher-centered explicit teaching", "Structured"),
            ("Inquiry-Based", "Student questions drive learning", "Discovery"),
            ("Problem-Based", "Learning through solving problems", "Authentic"),
            ("Project-Based", "Extended projects as learning", "Applied"),
            ("Cooperative Learning", "Learning in groups", "Social"),
            ("Differentiated", "Adapting to individual needs", "Personalized"),
        ]

        for name, description, characteristic in approaches:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["characteristic"] = characteristic

    def initialize_assessment_types(self) -> None:
        """Initialize assessment types."""
        assessments = [
            ("Formative", "During learning", "Feedback for improvement"),
            ("Summative", "End of learning", "Judgment of achievement"),
            ("Diagnostic", "Before learning", "Identify starting point"),
            ("Criterion-Referenced", "Against standards", "Mastery"),
            ("Norm-Referenced", "Compared to others", "Ranking"),
            ("Authentic", "Real-world tasks", "Performance"),
        ]

        for name, timing, purpose in assessments:
            concept = self.create_concept(
                name=f"{name} Assessment",
                concept_type=ConceptType.DEFINITION,
                description=f"Assessment {timing}",
            )
            concept.metadata["purpose"] = purpose

    def initialize_educational_pairs(self) -> None:
        """Initialize fundamental educational pairs with META 50/50 balance."""
        pairs = [
            ("Teaching", "Learning", "Instruction vs acquisition"),
            ("Theory", "Practice", "Knowledge vs application"),
            ("Formal", "Informal", "Structured vs unstructured"),
            ("Content", "Process", "What vs how"),
            ("Teacher", "Student", "Instructor vs learner"),
            ("Curriculum", "Pedagogy", "What vs how to teach"),
            ("Formative", "Summative", "During vs after"),
            ("Intrinsic", "Extrinsic", "Internal vs external motivation"),
            ("Individual", "Collaborative", "Alone vs together"),
            ("Cognitive", "Affective", "Thinking vs feeling"),
            ("Surface", "Deep", "Shallow vs profound learning"),
            ("Rote", "Meaningful", "Memorization vs understanding"),
            ("Transmission", "Construction", "Receive vs build knowledge"),
            ("Standards", "Autonomy", "Common vs individual goals"),
            ("Equity", "Excellence", "Fairness vs achievement"),
            ("Access", "Quality", "Availability vs excellence"),
            ("Traditional", "Progressive", "Conservative vs reform"),
            ("Breadth", "Depth", "Wide vs deep coverage"),
            ("Academic", "Vocational", "Theoretical vs practical"),
            ("Assessment", "Instruction", "Testing vs teaching"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Education)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Education)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_bloom_taxonomy(self) -> dict[str, str]:
        """Get Bloom's taxonomy of cognitive objectives."""
        return {
            "remember": "Recall facts and basic concepts",
            "understand": "Explain ideas or concepts",
            "apply": "Use information in new situations",
            "analyze": "Draw connections among ideas",
            "evaluate": "Justify a decision or course of action",
            "create": "Produce new or original work",
        }

    def demonstrate_education_balance(self) -> dict[str, Any]:
        """Demonstrate education balance principles."""
        return {
            "concept": "Education Equilibrium",
            "dualities": {
                "teaching_learning": {
                    "teaching": 50.0,
                    "learning": 50.0,
                    "meaning": "Effective education requires both",
                },
                "theory_practice": {
                    "theory": 50.0,
                    "practice": 50.0,
                    "meaning": "Knowledge and application together",
                },
                "individual_social": {
                    "individual": 50.0,
                    "social": 50.0,
                    "meaning": "Personal and collaborative learning",
                },
            },
            "pedagogical_balance": {
                "teacher_centered": 50.0,
                "student_centered": 50.0,
                "description": "Balance instruction and discovery",
            },
            "meta_meaning": "Education demonstrates META 50/50 in teaching-learning duality",
        }


def create_education_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> EducationDomain:
    """
    Factory function to create a fully initialized education domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized EducationDomain
    """
    domain = EducationDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_learning_theories()
        domain.initialize_pedagogical_approaches()
        domain.initialize_assessment_types()
        domain.initialize_educational_pairs()

    return domain
