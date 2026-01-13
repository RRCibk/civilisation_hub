"""
Tests for Knowledge Domains
===========================
Comprehensive tests for all knowledge domain implementations.
Tests META 50/50 balance in each domain.
"""

import math
from uuid import UUID

import pytest

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    Concept,
    ConceptRelation,
    ConceptType,
    RelationType,
)
from knowledge.domains.biology import BiologyDomain, create_biology_domain
from knowledge.domains.code import CodeDomain, create_code_domain
from knowledge.domains.mathematics import MathematicsDomain, create_mathematics_domain
from knowledge.domains.philosophy import PhilosophyDomain, create_philosophy_domain
from knowledge.domains.physics import PhysicsDomain, create_physics_domain

# =============================================================================
# Base Concept Tests
# =============================================================================


class TestConcept:
    """Tests for the Concept class."""

    def test_concept_creation(self):
        """Test basic concept creation."""
        concept = Concept(
            name="Test Concept", concept_type=ConceptType.DEFINITION, description="A test concept"
        )
        assert concept.name == "Test Concept"
        assert concept.concept_type == ConceptType.DEFINITION
        assert isinstance(concept.id, UUID)

    def test_concept_default_balance(self):
        """Test concept has default 50/50 balance."""
        concept = Concept(name="Balanced")
        assert concept.certainty == 50.0
        assert concept.uncertainty == 50.0
        assert concept.is_balanced

    def test_concept_certainty_normalization(self):
        """Test certainty values are normalized to 100."""
        concept = Concept(name="High Certainty", certainty=80.0, uncertainty=20.0)
        assert concept.certainty == 80.0
        assert concept.uncertainty == 20.0
        assert concept.certainty + concept.uncertainty == 100.0

    def test_concept_adjust_certainty(self):
        """Test adjusting certainty."""
        concept = Concept(name="Adjustable", certainty=50.0)
        concept.adjust_certainty(20)
        assert concept.certainty == 70.0
        assert concept.uncertainty == 30.0

    def test_concept_adjust_certainty_bounds(self):
        """Test certainty stays within bounds."""
        # Create with explicit 100/0 balance to avoid normalization effects
        concept = Concept(name="Bounded", certainty=95.0, uncertainty=5.0)
        concept.adjust_certainty(10)
        assert concept.certainty == 100.0
        assert concept.uncertainty == 0.0

        concept2 = Concept(name="Bounded2", certainty=5.0, uncertainty=95.0)
        concept2.adjust_certainty(-10)
        assert concept2.certainty == 0.0
        assert concept2.uncertainty == 100.0

    def test_concept_balance_property(self):
        """Test balance tuple property."""
        concept = Concept(name="Balanced", certainty=60.0, uncertainty=40.0)
        balance = concept.balance
        assert balance == (60.0, 40.0)


class TestConceptRelation:
    """Tests for concept relations."""

    def test_relation_creation(self):
        """Test basic relation creation."""
        relation = ConceptRelation(relation_type=RelationType.DERIVES_FROM, strength=75.0)
        assert relation.relation_type == RelationType.DERIVES_FROM
        assert relation.strength == 75.0
        assert isinstance(relation.id, UUID)

    def test_relation_bidirectional(self):
        """Test bidirectional flag."""
        relation = ConceptRelation(bidirectional=True)
        assert relation.bidirectional is True


# =============================================================================
# Mathematics Domain Tests
# =============================================================================


class TestMathematicsDomain:
    """Tests for the Mathematics domain."""

    def test_domain_creation(self):
        """Test mathematics domain creation."""
        domain = MathematicsDomain()
        assert domain.name == "Mathematics"
        assert "study" in domain.description.lower()

    def test_domain_with_shared_meta(self):
        """Test domain with shared MetaEquilibrium."""
        meta = MetaEquilibrium()
        domain = MathematicsDomain(meta_equilibrium=meta)
        assert domain._meta is meta

    def test_duality_initialized(self):
        """Test Abstract/Concrete duality is initialized."""
        domain = MathematicsDomain()
        duality = domain.domain.duality
        assert duality is not None
        assert duality.positive.name == "abstract"
        assert duality.negative.name == "concrete"
        assert duality.is_balanced

    def test_axioms_initialized(self):
        """Test mathematical axioms are created."""
        domain = MathematicsDomain()
        assert domain.axiom_count > 0
        axiom_names = [c.name for c in domain._axioms]
        assert "Identity" in axiom_names
        assert "Induction" in axiom_names

    def test_fundamental_concepts(self):
        """Test fundamental concepts list."""
        domain = MathematicsDomain()
        concepts = domain.get_fundamental_concepts()
        assert "Number" in concepts
        assert "Set" in concepts
        assert "Function" in concepts

    def test_initialize_branches(self):
        """Test branch initialization."""
        domain = MathematicsDomain()
        domain.initialize_branches()
        algebra = domain.get_concept_by_name("Algebra")
        assert algebra is not None
        assert algebra.concept_type == ConceptType.THEORY

    def test_initialize_number_systems(self):
        """Test number systems initialization."""
        domain = MathematicsDomain()
        domain.initialize_number_systems()
        reals = domain.get_concept_by_name("Real Numbers")
        assert reals is not None
        assert reals.metadata.get("symbol") == "ℝ"

    def test_number_system_relations(self):
        """Test containment relations between number systems."""
        domain = MathematicsDomain()
        domain.initialize_number_systems()
        naturals = domain.get_concept_by_name("Natural Numbers")
        assert naturals is not None
        relations = domain.get_relations(naturals.id)
        assert len(relations) > 0

    def test_add_theorem(self):
        """Test adding a theorem."""
        domain = MathematicsDomain()
        theorem = domain.add_theorem("Custom Theorem", "A custom statement", "Proof by example")
        assert theorem.concept_type == ConceptType.THEOREM
        assert theorem.metadata["proof_sketch"] == "Proof by example"

    def test_add_definition(self):
        """Test adding a definition."""
        domain = MathematicsDomain()
        defn = domain.add_definition("Custom Term", "A custom definition", "CT")
        assert defn.concept_type == ConceptType.DEFINITION
        assert defn.metadata["notation"] == "CT"

    def test_fundamental_theorems(self):
        """Test fundamental theorems initialization."""
        domain = MathematicsDomain()
        domain.initialize_fundamental_theorems()
        pythag = domain.get_concept_by_name("Pythagorean Theorem")
        assert pythag is not None
        assert pythag.concept_type == ConceptType.THEOREM

    def test_pi_approximation(self):
        """Test π approximation calculation."""
        domain = MathematicsDomain()
        pi_approx = domain.calculate_pi_approximation(10000)
        assert abs(pi_approx - math.pi) < 0.001

    def test_golden_ratio(self):
        """Test golden ratio demonstration."""
        domain = MathematicsDomain()
        phi_demo = domain.demonstrate_golden_ratio()
        phi = (1 + math.sqrt(5)) / 2
        assert abs(phi_demo["phi"] - phi) < 1e-10
        assert phi_demo["balance_demonstrated"] is True

    def test_mathematical_constants(self):
        """Test mathematical constants."""
        domain = MathematicsDomain()
        constants = domain.get_mathematical_constants()
        assert "pi" in constants
        assert "e" in constants
        assert abs(constants["pi"] - math.pi) < 1e-10

    def test_validate_balance(self):
        """Test domain validates META 50/50."""
        domain = MathematicsDomain()
        assert domain.validate_balance() is True

    def test_domain_stats(self):
        """Test domain statistics."""
        domain = create_mathematics_domain()
        stats = domain.get_domain_stats()
        assert stats["name"] == "Mathematics"
        assert stats["concepts"] > 0
        assert stats["balanced"] is True

    def test_factory_function(self):
        """Test factory function creates initialized domain."""
        domain = create_mathematics_domain()
        assert domain.concept_count > 10  # Has many concepts
        assert domain.axiom_count > 0

    def test_factory_no_init(self):
        """Test factory without initialization."""
        domain = create_mathematics_domain(initialize_all=False)
        # Only axioms from constructor
        assert domain.concept_count == domain.axiom_count


# =============================================================================
# Physics Domain Tests
# =============================================================================


class TestPhysicsDomain:
    """Tests for the Physics domain."""

    def test_domain_creation(self):
        """Test physics domain creation."""
        domain = PhysicsDomain()
        assert domain.name == "Physics"

    def test_duality_initialized(self):
        """Test Energy/Matter duality."""
        domain = PhysicsDomain()
        duality = domain.domain.duality
        assert duality.positive.name == "energy"
        assert duality.negative.name == "matter"
        assert duality.is_balanced

    def test_physical_laws_initialized(self):
        """Test physical laws are initialized."""
        domain = PhysicsDomain()
        # Physical laws use ConceptType.LAW, not AXIOM
        law_concepts = [c for c in domain._concepts.values() if c.concept_type == ConceptType.LAW]
        law_names = [c.name for c in law_concepts]
        assert "Conservation of Energy" in law_names
        assert "Newton's First Law" in law_names

    def test_fundamental_concepts(self):
        """Test fundamental physics concepts."""
        domain = PhysicsDomain()
        concepts = domain.get_fundamental_concepts()
        assert "Mass" in concepts
        assert "Energy" in concepts
        assert "Force" in concepts

    def test_initialize_branches(self):
        """Test physics branches."""
        domain = PhysicsDomain()
        domain.initialize_branches()
        qm = domain.get_concept_by_name("Quantum Mechanics")
        assert qm is not None

    def test_fundamental_particles(self):
        """Test fundamental particles initialization."""
        domain = PhysicsDomain()
        domain.initialize_fundamental_particles()
        electron = domain.get_concept_by_name("Electron")
        assert electron is not None
        assert electron.metadata["charge"] == -1

    def test_fundamental_forces(self):
        """Test four fundamental forces."""
        domain = PhysicsDomain()
        domain.initialize_fundamental_forces()
        em = domain.get_concept_by_name("Electromagnetic Force")
        assert em is not None
        assert em.metadata["mediator"] == "Photon"

    def test_add_equation(self):
        """Test adding physics equation."""
        domain = PhysicsDomain()
        eq = domain.add_equation(
            "Test Equation",
            "E = hf",
            "Energy of photon",
            {"E": "Energy", "h": "Planck constant", "f": "Frequency"},
        )
        assert eq.metadata["equation"] == "E = hf"

    def test_key_equations(self):
        """Test key equations initialization."""
        domain = PhysicsDomain()
        domain.initialize_key_equations()
        emc2 = domain.get_concept_by_name("Mass-Energy Equivalence")
        assert emc2 is not None
        assert "E = mc²" in emc2.metadata["equation"]

    def test_physical_constants(self):
        """Test physical constants."""
        domain = PhysicsDomain()
        constants = domain.get_physical_constants()
        assert constants["speed_of_light"]["value"] == 299792458
        assert constants["speed_of_light"]["symbol"] == "c"

    def test_wave_particle_duality(self):
        """Test wave-particle duality demonstration."""
        domain = PhysicsDomain()
        demo = domain.demonstrate_wave_particle_duality()
        assert demo["balance"]["wave_aspect"] == 50.0
        assert demo["balance"]["particle_aspect"] == 50.0
        assert demo["balance"]["total"] == 100.0

    def test_factory_function(self):
        """Test physics factory function."""
        domain = create_physics_domain()
        assert domain.concept_count > 10
        assert domain.validate_balance()


# =============================================================================
# Code Domain Tests
# =============================================================================


class TestCodeDomain:
    """Tests for the Code/Programming domain."""

    def test_domain_creation(self):
        """Test code domain creation."""
        domain = CodeDomain()
        assert domain.name == "Code"

    def test_duality_initialized(self):
        """Test Abstraction/Implementation duality."""
        domain = CodeDomain()
        duality = domain.domain.duality
        assert duality.positive.name == "abstraction"
        assert duality.negative.name == "implementation"
        assert duality.is_balanced

    def test_programming_principles(self):
        """Test programming principles are initialized."""
        domain = CodeDomain()
        # Programming principles use ConceptType.PRINCIPLE
        principle_concepts = [
            c for c in domain._concepts.values() if c.concept_type == ConceptType.PRINCIPLE
        ]
        principle_names = [c.name for c in principle_concepts]
        assert "DRY" in principle_names
        assert "KISS" in principle_names
        assert "Single Responsibility" in principle_names

    def test_fundamental_concepts(self):
        """Test fundamental programming concepts."""
        domain = CodeDomain()
        concepts = domain.get_fundamental_concepts()
        assert "Variable" in concepts
        assert "Function" in concepts
        assert "Class" in concepts

    def test_paradigms(self):
        """Test programming paradigms."""
        domain = CodeDomain()
        domain.initialize_paradigms()
        oop = domain.get_concept_by_name("Object-Oriented Programming")
        assert oop is not None
        assert "Java" in oop.metadata["example_languages"]

    def test_data_structures(self):
        """Test data structures."""
        domain = CodeDomain()
        domain.initialize_data_structures()
        array = domain.get_concept_by_name("Array")
        assert array is not None
        assert array.metadata["access_complexity"] == "O(1)"

    def test_algorithms(self):
        """Test algorithms."""
        domain = CodeDomain()
        domain.initialize_algorithms()
        quicksort = domain.get_concept_by_name("Quick Sort")
        assert quicksort is not None
        assert quicksort.metadata["time_complexity"] == "O(n log n)"

    def test_design_patterns(self):
        """Test design patterns."""
        domain = CodeDomain()
        domain.initialize_design_patterns()
        singleton = domain.get_concept_by_name("Singleton Pattern")
        assert singleton is not None
        assert singleton.metadata["pattern_category"] == "Creational"

    def test_languages(self):
        """Test programming languages."""
        domain = CodeDomain()
        domain.initialize_languages()
        python = domain.get_concept_by_name("Python")
        assert python is not None
        assert python.metadata["year_created"] == 1991

    def test_code_balance(self):
        """Test code balance demonstration."""
        domain = CodeDomain()
        demo = domain.demonstrate_code_balance()
        assert demo["dualities"]["abstraction_implementation"]["abstraction"] == 50.0
        assert demo["operational_ratio"]["structure"] == 52.0

    def test_complexity_classes(self):
        """Test complexity classes."""
        domain = CodeDomain()
        classes = domain.get_complexity_classes()
        assert "O(1)" in classes
        assert "O(n log n)" in classes
        assert "O(n!)" in classes

    def test_factory_function(self):
        """Test code factory function."""
        domain = create_code_domain()
        assert domain.concept_count > 20
        assert domain.validate_balance()


# =============================================================================
# Biology Domain Tests
# =============================================================================


class TestBiologyDomain:
    """Tests for the Biology domain."""

    def test_domain_creation(self):
        """Test biology domain creation."""
        domain = BiologyDomain()
        assert domain.name == "Biology"

    def test_duality_initialized(self):
        """Test Life/Death duality."""
        domain = BiologyDomain()
        duality = domain.domain.duality
        assert duality.positive.name == "life"
        assert duality.negative.name == "death"
        assert duality.is_balanced

    def test_biological_principles(self):
        """Test biological principles are initialized."""
        domain = BiologyDomain()
        # Biological principles use ConceptType.PRINCIPLE
        principle_concepts = [
            c for c in domain._concepts.values() if c.concept_type == ConceptType.PRINCIPLE
        ]
        principle_names = [c.name for c in principle_concepts]
        assert "Cell Theory" in principle_names
        assert "Evolution by Natural Selection" in principle_names

    def test_fundamental_concepts(self):
        """Test fundamental biology concepts."""
        domain = BiologyDomain()
        concepts = domain.get_fundamental_concepts()
        assert "Cell" in concepts
        assert "DNA" in concepts
        assert "Evolution" in concepts

    def test_branches(self):
        """Test biology branches."""
        domain = BiologyDomain()
        domain.initialize_branches()
        genetics = domain.get_concept_by_name("Genetics")
        assert genetics is not None

    def test_taxonomic_ranks(self):
        """Test taxonomic classification."""
        domain = BiologyDomain()
        domain.initialize_taxonomic_ranks()
        species = domain.get_concept_by_name("Species")
        assert species is not None
        assert "Homo sapiens" in species.metadata["examples"]

    def test_taxonomic_hierarchy(self):
        """Test taxonomic hierarchy relations."""
        domain = BiologyDomain()
        domain.initialize_taxonomic_ranks()
        kingdom = domain.get_concept_by_name("Kingdom")
        relations = domain.get_relations(kingdom.id)
        assert len(relations) > 0

    def test_cell_components(self):
        """Test cell organelles."""
        domain = BiologyDomain()
        domain.initialize_cell_components()
        mito = domain.get_concept_by_name("Mitochondria")
        assert mito is not None
        assert "ATP" in mito.description

    def test_macromolecules(self):
        """Test biological macromolecules."""
        domain = BiologyDomain()
        domain.initialize_macromolecules()
        proteins = domain.get_concept_by_name("Proteins")
        assert proteins is not None
        assert "Enzymes" in proteins.metadata["examples"]

    def test_biological_processes(self):
        """Test biological processes."""
        domain = BiologyDomain()
        domain.initialize_biological_processes()
        photo = domain.get_concept_by_name("Photosynthesis")
        assert photo is not None
        assert "CO2" in photo.metadata["formula"]

    def test_biological_balance(self):
        """Test biological balance demonstration."""
        domain = BiologyDomain()
        demo = domain.demonstrate_biological_balance()
        assert demo["dualities"]["anabolism_catabolism"]["anabolism"] == 50.0
        assert "homeostasis" in demo

    def test_genetic_code(self):
        """Test genetic code codon table."""
        domain = BiologyDomain()
        code = domain.get_genetic_code()
        assert code["AUG"] == "Met"  # Start codon
        assert code["UAA"] == "Stop"  # Stop codon

    def test_factory_function(self):
        """Test biology factory function."""
        domain = create_biology_domain()
        assert domain.concept_count > 20
        assert domain.validate_balance()


# =============================================================================
# Philosophy Domain Tests
# =============================================================================


class TestPhilosophyDomain:
    """Tests for the Philosophy domain."""

    def test_domain_creation(self):
        """Test philosophy domain creation."""
        domain = PhilosophyDomain()
        assert domain.name == "Philosophy"

    def test_duality_initialized(self):
        """Test Being/Non-Being duality."""
        domain = PhilosophyDomain()
        duality = domain.domain.duality
        assert duality.positive.name == "being"
        assert duality.negative.name == "non_being"
        assert duality.is_balanced

    def test_philosophical_principles(self):
        """Test philosophical principles as axioms."""
        domain = PhilosophyDomain()
        axiom_names = [c.name for c in domain._axioms]
        assert "Cogito Ergo Sum" in axiom_names
        assert "Law of Non-Contradiction" in axiom_names

    def test_fundamental_concepts(self):
        """Test fundamental philosophy concepts."""
        domain = PhilosophyDomain()
        concepts = domain.get_fundamental_concepts()
        assert "Being" in concepts
        assert "Truth" in concepts
        assert "Mind" in concepts

    def test_branches(self):
        """Test philosophy branches."""
        domain = PhilosophyDomain()
        domain.initialize_branches()
        meta = domain.get_concept_by_name("Metaphysics")
        assert meta is not None
        ethics = domain.get_concept_by_name("Ethics")
        assert ethics is not None

    def test_schools_of_thought(self):
        """Test philosophical schools."""
        domain = PhilosophyDomain()
        domain.initialize_schools_of_thought()
        platonism = domain.get_concept_by_name("Platonism")
        assert platonism is not None
        assert platonism.metadata["era"] == "Ancient"

    def test_philosophers(self):
        """Test philosopher initialization."""
        domain = PhilosophyDomain()
        domain.initialize_philosophers()
        socrates = domain.get_concept_by_name("Socrates")
        assert socrates is not None
        assert socrates.metadata["nationality"] == "Greek"

    def test_thought_experiments(self):
        """Test thought experiments."""
        domain = PhilosophyDomain()
        domain.initialize_thought_experiments()
        trolley = domain.get_concept_by_name("Trolley Problem")
        assert trolley is not None
        assert trolley.metadata["philosophical_domain"] == "Ethics"

    def test_dialectical_pairs(self):
        """Test dialectical pairs."""
        domain = PhilosophyDomain()
        domain.initialize_dialectical_pairs()
        being = domain.get_concept_by_name("Being")
        non_being = domain.get_concept_by_name("Non-Being")
        assert being is not None
        assert non_being is not None
        # Check relation exists
        relations = domain.get_relations(being.id)
        assert len(relations) > 0

    def test_philosophical_balance(self):
        """Test philosophical balance demonstration."""
        domain = PhilosophyDomain()
        demo = domain.demonstrate_philosophical_balance()
        assert demo["dialectics"]["thesis_antithesis"]["thesis"] == 50.0
        assert demo["dialectics"]["being_non_being"]["being"] == 50.0

    def test_logical_forms(self):
        """Test logical forms."""
        domain = PhilosophyDomain()
        forms = domain.get_logical_forms()
        assert "modus_ponens" in forms
        assert "modus_tollens" in forms

    def test_factory_function(self):
        """Test philosophy factory function."""
        domain = create_philosophy_domain()
        assert domain.concept_count > 30
        assert domain.validate_balance()


# =============================================================================
# Cross-Domain Integration Tests
# =============================================================================


class TestCrossDomainIntegration:
    """Tests for cross-domain integration."""

    def test_shared_meta_equilibrium(self):
        """Test multiple domains can share MetaEquilibrium."""
        meta = MetaEquilibrium()
        math_domain = create_mathematics_domain(meta_equilibrium=meta)
        physics_domain = create_physics_domain(meta_equilibrium=meta)
        assert math_domain._meta is physics_domain._meta

    def test_all_domains_balanced(self):
        """Test all domains maintain META 50/50."""
        domains = [
            create_mathematics_domain(),
            create_physics_domain(),
            create_code_domain(),
            create_biology_domain(),
            create_philosophy_domain(),
        ]
        for domain in domains:
            assert domain.validate_balance(), f"{domain.name} not balanced"

    def test_all_domains_have_foundational_concepts(self):
        """Test all domains have foundational concepts (axioms, laws, or principles)."""
        domains = [
            create_mathematics_domain(),
            create_physics_domain(),
            create_code_domain(),
            create_biology_domain(),
            create_philosophy_domain(),
        ]
        foundational_types = {ConceptType.AXIOM, ConceptType.LAW, ConceptType.PRINCIPLE}
        for domain in domains:
            foundational = [
                c for c in domain._concepts.values() if c.concept_type in foundational_types
            ]
            assert len(foundational) > 0, f"{domain.name} has no foundational concepts"

    def test_all_domains_prove_meta(self):
        """Test all domains can prove META meaning."""
        domains = [
            create_mathematics_domain(),
            create_physics_domain(),
            create_code_domain(),
            create_biology_domain(),
            create_philosophy_domain(),
        ]
        for domain in domains:
            proof = domain.prove_meta_meaning()
            assert proof["meta_valid"] is True, f"{domain.name} META proof failed"

    def test_domain_concept_counts(self):
        """Test domains have substantial concept counts."""
        min_concepts = 15
        domains = [
            create_mathematics_domain(),
            create_physics_domain(),
            create_code_domain(),
            create_biology_domain(),
            create_philosophy_domain(),
        ]
        for domain in domains:
            assert domain.concept_count >= min_concepts, (
                f"{domain.name} has only {domain.concept_count} concepts"
            )


# =============================================================================
# META Balance Proof Tests
# =============================================================================


class TestMetaBalanceProof:
    """Tests proving META 50/50 across all domains."""

    def test_mathematics_duality_balance(self):
        """Prove Mathematics Abstract/Concrete balance."""
        domain = create_mathematics_domain()
        duality = domain.domain.duality
        assert duality.positive.value == 50
        assert duality.negative.value == 50
        assert duality.is_balanced

    def test_physics_duality_balance(self):
        """Prove Physics Energy/Matter balance."""
        domain = create_physics_domain()
        duality = domain.domain.duality
        assert duality.positive.value == 50
        assert duality.negative.value == 50
        assert duality.is_balanced

    def test_code_duality_balance(self):
        """Prove Code Abstraction/Implementation balance."""
        domain = create_code_domain()
        duality = domain.domain.duality
        assert duality.positive.value == 50
        assert duality.negative.value == 50
        assert duality.is_balanced

    def test_biology_duality_balance(self):
        """Prove Biology Life/Death balance."""
        domain = create_biology_domain()
        duality = domain.domain.duality
        assert duality.positive.value == 50
        assert duality.negative.value == 50
        assert duality.is_balanced

    def test_philosophy_duality_balance(self):
        """Prove Philosophy Being/Non-Being balance."""
        domain = create_philosophy_domain()
        duality = domain.domain.duality
        assert duality.positive.value == 50
        assert duality.negative.value == 50
        assert duality.is_balanced

    def test_concept_certainty_uncertainty_balance(self):
        """Test concepts maintain certainty/uncertainty balance."""
        domain = create_mathematics_domain()
        balanced_concepts = [c for c in domain._concepts.values() if c.is_balanced]
        # At least some concepts should be balanced
        assert len(balanced_concepts) > 0

    def test_meta_proof_structure(self):
        """Test META proof has correct structure."""
        domain = create_philosophy_domain()
        proof = domain.prove_meta_meaning()
        assert "domain" in proof
        assert "statistics" in proof
        assert "duality" in proof
        assert "meta_valid" in proof
        assert "proof" in proof


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
