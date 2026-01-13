"""
Geometry Domain
===============
Geometric knowledge domain with META 50/50 equilibrium.
Fundamental duality: Point/Space (location vs extension).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class GeometryDomain(KnowledgeDomain):
    """
    Geometry knowledge domain.

    Fundamental Duality: Point / Space
    - Point: Dimensionless location, singularity, position
    - Space: Extended region, continuum, volume

    Secondary Dualities:
    - Finite / Infinite
    - Straight / Curved
    - Interior / Exterior
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Geometry",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of shapes, sizes, positions, and properties of space",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Point/Space duality."""
        self._domain.set_duality(
            positive_name="point",
            positive_value=50,
            negative_name="space",
            negative_value=50,
            duality_name="geometry_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental geometric axioms (Euclid's postulates)."""
        axioms = [
            (
                "Point-Line Axiom",
                "A straight line can be drawn between any two points",
            ),
            (
                "Line Extension Axiom",
                "A finite line can be extended indefinitely",
            ),
            (
                "Circle Axiom",
                "A circle can be drawn with any center and radius",
            ),
            (
                "Right Angle Axiom",
                "All right angles are equal to one another",
            ),
            (
                "Parallel Postulate",
                "Through a point not on a line, exactly one parallel line exists",
            ),
            (
                "Congruence Axiom",
                "Figures with same shape and size are congruent",
            ),
            (
                "Similarity Axiom",
                "Figures with same shape but different size are similar",
            ),
            (
                "Continuity Axiom",
                "Space is continuous, not discrete",
            ),
        ]

        for name, description in axioms:
            self.create_concept(
                name=name,
                concept_type=ConceptType.AXIOM,
                description=description,
                certainty=100,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental geometry concepts."""
        return [
            "Point",
            "Line",
            "Plane",
            "Angle",
            "Triangle",
            "Circle",
            "Polygon",
            "Area",
            "Volume",
            "Perimeter",
            "Symmetry",
            "Congruence",
            "Similarity",
            "Dimension",
            "Coordinate",
        ]

    def initialize_branches(self) -> None:
        """Initialize major geometry branches."""
        branches = [
            (
                "Euclidean Geometry",
                "Classical plane and solid geometry",
                ConceptType.THEORY,
            ),
            (
                "Non-Euclidean Geometry",
                "Geometry with different parallel postulate",
                ConceptType.THEORY,
            ),
            (
                "Analytic Geometry",
                "Geometry using coordinates and algebra",
                ConceptType.THEORY,
            ),
            (
                "Differential Geometry",
                "Geometry using calculus",
                ConceptType.THEORY,
            ),
            (
                "Projective Geometry",
                "Study of properties invariant under projection",
                ConceptType.THEORY,
            ),
            (
                "Topology",
                "Study of properties preserved under continuous deformation",
                ConceptType.THEORY,
            ),
            (
                "Algebraic Geometry",
                "Geometry using abstract algebra",
                ConceptType.THEORY,
            ),
            (
                "Computational Geometry",
                "Algorithms for geometric problems",
                ConceptType.THEORY,
            ),
            (
                "Fractal Geometry",
                "Study of self-similar structures",
                ConceptType.THEORY,
            ),
            (
                "Convex Geometry",
                "Study of convex sets and functions",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_shapes_2d(self) -> None:
        """Initialize 2D shapes."""
        shapes = [
            ("Triangle", 3, "180°", "½bh"),
            ("Square", 4, "360°", "s²"),
            ("Rectangle", 4, "360°", "lw"),
            ("Pentagon", 5, "540°", "½Pa"),
            ("Hexagon", 6, "720°", "½Pa"),
            ("Circle", 0, "N/A", "πr²"),
            ("Ellipse", 0, "N/A", "πab"),
            ("Parallelogram", 4, "360°", "bh"),
            ("Trapezoid", 4, "360°", "½(a+b)h"),
            ("Rhombus", 4, "360°", "½d₁d₂"),
        ]

        for name, sides, angle_sum, area in shapes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=f"2D shape with {sides} sides" if sides > 0 else "Curved 2D shape",
            )
            concept.metadata.update({
                "sides": sides,
                "interior_angle_sum": angle_sum,
                "area_formula": area,
            })

    def initialize_shapes_3d(self) -> None:
        """Initialize 3D shapes."""
        shapes = [
            ("Cube", 6, 12, 8, "s³"),
            ("Sphere", 0, 0, 0, "4/3πr³"),
            ("Cylinder", 3, 2, 0, "πr²h"),
            ("Cone", 2, 1, 1, "1/3πr²h"),
            ("Tetrahedron", 4, 6, 4, "√2/12 a³"),
            ("Prism", "n+2", "3n", "2n", "Bh"),
            ("Pyramid", "n+1", "2n", "n+1", "1/3Bh"),
            ("Torus", 1, 0, 0, "2π²Rr²"),
        ]

        for name, faces, edges, vertices, volume in shapes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=f"3D solid with {faces} faces",
            )
            concept.metadata.update({
                "faces": faces,
                "edges": edges,
                "vertices": vertices,
                "volume_formula": volume,
            })

    def initialize_transformations(self) -> None:
        """Initialize geometric transformations."""
        transformations = [
            ("Translation", "Sliding without rotation", "Position changes"),
            ("Rotation", "Turning around a point", "Orientation changes"),
            ("Reflection", "Mirror image across a line", "Handedness changes"),
            ("Scaling", "Enlarging or shrinking", "Size changes"),
            ("Shear", "Slanting transformation", "Shape distorts"),
            ("Projection", "Mapping to lower dimension", "Dimension reduces"),
        ]

        for name, description, effect in transformations:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["effect"] = effect

    def initialize_theorems(self) -> None:
        """Initialize fundamental geometry theorems."""
        theorems = [
            ("Pythagorean Theorem", "a² + b² = c² for right triangles"),
            ("Thales' Theorem", "Angle in semicircle is 90°"),
            ("Triangle Angle Sum", "Interior angles sum to 180°"),
            ("Exterior Angle Theorem", "Exterior angle equals sum of remote interior angles"),
            ("Isosceles Triangle Theorem", "Base angles of isosceles triangle are equal"),
            ("Circle Theorems", "Central angle is twice inscribed angle"),
            ("Euler's Formula", "V - E + F = 2 for polyhedra"),
            ("Jordan Curve Theorem", "Simple closed curve divides plane into two regions"),
        ]

        for name, statement in theorems:
            self.create_concept(
                name=name,
                concept_type=ConceptType.THEOREM,
                description=statement,
            )

    def initialize_geometric_pairs(self) -> None:
        """Initialize fundamental geometric pairs with META 50/50 balance."""
        pairs = [
            ("Point", "Space", "Location vs extension"),
            ("Line", "Plane", "One vs two dimensions"),
            ("Finite", "Infinite", "Bounded vs unbounded"),
            ("Straight", "Curved", "Linear vs nonlinear"),
            ("Parallel", "Perpendicular", "Never vs always meeting"),
            ("Convex", "Concave", "Bulging vs indented"),
            ("Interior", "Exterior", "Inside vs outside"),
            ("Congruent", "Similar", "Same vs proportional"),
            ("Acute", "Obtuse", "Sharp vs blunt angle"),
            ("Regular", "Irregular", "Uniform vs varied"),
            ("Euclidean", "Non-Euclidean", "Flat vs curved space"),
            ("Vertex", "Edge", "Corner vs side"),
            ("Radius", "Circumference", "Center to edge vs around"),
            ("Area", "Perimeter", "Inside vs boundary"),
            ("Volume", "Surface", "Inside vs outside"),
            ("Symmetry", "Asymmetry", "Balanced vs unbalanced"),
            ("Translation", "Rotation", "Sliding vs turning"),
            ("Origin", "Infinity", "Start vs endless"),
            ("Dimension", "Projection", "Full vs reduced"),
            ("Topology", "Metric", "Shape vs distance"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Geometry)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Geometry)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_geometric_constants(self) -> dict[str, float]:
        """Get important geometric constants."""
        import math
        return {
            "pi": math.pi,
            "tau": 2 * math.pi,
            "golden_ratio": (1 + math.sqrt(5)) / 2,
            "sqrt_2": math.sqrt(2),
            "sqrt_3": math.sqrt(3),
            "e": math.e,
        }

    def demonstrate_geometric_balance(self) -> dict[str, Any]:
        """Demonstrate geometric balance principles."""
        return {
            "concept": "Geometric Equilibrium",
            "dualities": {
                "point_space": {
                    "point": 50.0,
                    "space": 50.0,
                    "meaning": "Position and extension are complementary",
                },
                "interior_exterior": {
                    "interior": 50.0,
                    "exterior": 50.0,
                    "meaning": "Every closed curve divides plane equally",
                },
                "symmetry": {
                    "left": 50.0,
                    "right": 50.0,
                    "meaning": "Bilateral symmetry shows perfect balance",
                },
            },
            "circle_balance": {
                "radius_constant": True,
                "description": "All points equidistant from center",
            },
            "meta_meaning": "Geometry demonstrates META 50/50 in spatial balance",
        }


def create_geometry_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> GeometryDomain:
    """
    Factory function to create a fully initialized geometry domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized GeometryDomain
    """
    domain = GeometryDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_shapes_2d()
        domain.initialize_shapes_3d()
        domain.initialize_transformations()
        domain.initialize_theorems()
        domain.initialize_geometric_pairs()

    return domain
