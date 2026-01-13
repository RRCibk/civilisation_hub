"""
Tests for Database Module
=========================
Tests for database models, engine, session, and repositories.
Verifies META 50/50 balance is maintained in persistence.
"""

import pytest

from database.engine import (
    DatabaseEngine,
    get_engine,
    reset_engine,
)
from database.models import (
    ConceptModel,
    DomainModel,
    DualityModel,
    RelationModel,
)
from database.repository import (
    ConceptRepository,
    DomainRepository,
    RelationRepository,
)
from database.session import (
    SessionManager,
    reset_session_manager,
)

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def engine():
    """Create in-memory database engine for testing."""
    reset_engine()
    reset_session_manager()
    eng = get_engine(in_memory=True, reset=True)
    eng.create_all_tables()
    yield eng
    eng.drop_all_tables()
    reset_engine()
    reset_session_manager()


@pytest.fixture
def session_manager(engine):
    """Create session manager with test engine."""
    return SessionManager(engine)


@pytest.fixture
def session(session_manager):
    """Create database session."""
    session = session_manager.create_session()
    yield session
    session.close()


# =============================================================================
# DualityModel Tests
# =============================================================================


class TestDualityModel:
    """Tests for DualityModel."""

    def test_create_duality(self, session):
        """Test creating a balanced duality."""
        duality = DualityModel(
            name="test_duality",
            positive_name="positive",
            positive_value=50.0,
            negative_name="negative",
            negative_value=50.0,
        )
        session.add(duality)
        session.commit()

        assert duality.id is not None
        assert duality.uuid is not None
        assert duality.is_balanced is True

    def test_duality_validates_balance(self, session):
        """Test duality validates META 50/50 balance."""
        duality = DualityModel(
            name="balanced",
            positive_name="pos",
            positive_value=50.0,
            negative_name="neg",
            negative_value=50.0,
        )
        assert duality.validate_balance() is True
        assert duality.is_balanced is True

    def test_duality_detects_imbalance(self, session):
        """Test duality detects imbalance."""
        duality = DualityModel(
            name="imbalanced",
            positive_name="pos",
            positive_value=60.0,
            negative_name="neg",
            negative_value=40.0,
        )
        assert duality.validate_balance() is False
        assert duality.is_balanced is False

    def test_duality_to_dict(self, session):
        """Test duality serialization."""
        duality = DualityModel(
            name="test",
            positive_name="pos",
            positive_value=50.0,
            negative_name="neg",
            negative_value=50.0,
        )
        d = duality.to_dict()
        assert d["name"] == "test"
        assert d["positive"]["name"] == "pos"
        assert d["negative"]["value"] == 50.0


# =============================================================================
# DomainModel Tests
# =============================================================================


class TestDomainModel:
    """Tests for DomainModel."""

    def test_create_domain(self, session):
        """Test creating a domain."""
        domain = DomainModel(
            name="TestDomain", domain_type="fundamental", description="A test domain"
        )
        session.add(domain)
        session.commit()

        assert domain.id is not None
        assert domain.uuid is not None
        assert domain.name == "TestDomain"

    def test_domain_with_duality(self, session):
        """Test domain with duality relationship."""
        duality = DualityModel(
            name="test_duality",
            positive_name="abstract",
            positive_value=50.0,
            negative_name="concrete",
            negative_value=50.0,
        )
        domain = DomainModel(name="Mathematics", domain_type="fundamental", duality=duality)
        session.add(domain)
        session.commit()

        assert domain.duality is not None
        assert domain.duality.positive_name == "abstract"
        assert domain.meta_compliant is True

    def test_domain_meta_compliance(self, session):
        """Test domain META compliance validation."""
        duality = DualityModel(
            name="balanced",
            positive_name="pos",
            positive_value=50.0,
            negative_name="neg",
            negative_value=50.0,
        )
        domain = DomainModel(name="Balanced", duality=duality)
        session.add(domain)
        session.commit()

        assert domain.validate_meta_compliance() is True

    def test_domain_without_duality_not_compliant(self, session):
        """Test domain without duality is not META compliant."""
        domain = DomainModel(name="NoDuality")
        session.add(domain)
        session.commit()

        assert domain.validate_meta_compliance() is False

    def test_domain_concept_count(self, session):
        """Test domain concept count property."""
        domain = DomainModel(name="WithConcepts")
        session.add(domain)
        session.flush()

        concept1 = ConceptModel(name="C1", domain_id=domain.id)
        concept2 = ConceptModel(name="C2", domain_id=domain.id)
        session.add_all([concept1, concept2])
        session.commit()

        assert domain.concept_count == 2

    def test_domain_to_dict(self, session):
        """Test domain serialization."""
        duality = DualityModel(
            name="test",
            positive_name="pos",
            positive_value=50.0,
            negative_name="neg",
            negative_value=50.0,
        )
        domain = DomainModel(name="Test", domain_type="fundamental", duality=duality)
        session.add(domain)
        session.commit()

        d = domain.to_dict()
        assert d["name"] == "Test"
        assert d["duality"] is not None
        assert d["duality"]["positive"]["value"] == 50.0


# =============================================================================
# ConceptModel Tests
# =============================================================================


class TestConceptModel:
    """Tests for ConceptModel."""

    def test_create_concept(self, session):
        """Test creating a concept."""
        domain = DomainModel(name="TestDomain")
        session.add(domain)
        session.flush()

        concept = ConceptModel(
            name="TestConcept",
            concept_type="definition",
            description="A test concept",
            domain_id=domain.id,
        )
        session.add(concept)
        session.commit()

        assert concept.id is not None
        assert concept.uuid is not None
        assert concept.certainty == 50.0
        assert concept.uncertainty == 50.0

    def test_concept_balance(self, session):
        """Test concept certainty/uncertainty balance."""
        domain = DomainModel(name="TestDomain")
        session.add(domain)
        session.flush()

        concept = ConceptModel(
            name="Balanced", certainty=50.0, uncertainty=50.0, domain_id=domain.id
        )
        assert concept.validate_balance() is True
        assert concept.is_balanced is True

    def test_concept_imbalance_detected(self, session):
        """Test concept imbalance detection."""
        domain = DomainModel(name="TestDomain")
        session.add(domain)
        session.flush()

        concept = ConceptModel(
            name="Imbalanced", certainty=80.0, uncertainty=20.0, domain_id=domain.id
        )
        assert concept.validate_balance() is False
        assert concept.is_balanced is False

    def test_concept_to_dict(self, session):
        """Test concept serialization."""
        domain = DomainModel(name="TestDomain")
        session.add(domain)
        session.flush()

        concept = ConceptModel(name="Test", concept_type="theorem", domain_id=domain.id)
        session.add(concept)
        session.commit()

        d = concept.to_dict()
        assert d["name"] == "Test"
        assert d["concept_type"] == "theorem"
        assert d["certainty"] == 50.0


# =============================================================================
# RelationModel Tests
# =============================================================================


class TestRelationModel:
    """Tests for RelationModel."""

    def test_create_relation(self, session):
        """Test creating a domain relation."""
        domain1 = DomainModel(name="Domain1")
        domain2 = DomainModel(name="Domain2")
        session.add_all([domain1, domain2])
        session.flush()

        relation = RelationModel(
            name="test_relation",
            source_domain_id=domain1.id,
            target_domain_id=domain2.id,
            influence_give=50.0,
            influence_receive=50.0,
        )
        session.add(relation)
        session.commit()

        assert relation.id is not None
        assert relation.is_balanced is True

    def test_relation_balance_validation(self, session):
        """Test relation balance validation."""
        domain1 = DomainModel(name="D1")
        domain2 = DomainModel(name="D2")
        session.add_all([domain1, domain2])
        session.flush()

        balanced = RelationModel(
            name="balanced",
            source_domain_id=domain1.id,
            target_domain_id=domain2.id,
            influence_give=50.0,
            influence_receive=50.0,
        )
        assert balanced.validate_balance() is True

        imbalanced = RelationModel(
            name="imbalanced",
            source_domain_id=domain1.id,
            target_domain_id=domain2.id,
            influence_give=70.0,
            influence_receive=30.0,
        )
        assert imbalanced.validate_balance() is False


# =============================================================================
# DatabaseEngine Tests
# =============================================================================


class TestDatabaseEngine:
    """Tests for DatabaseEngine."""

    def test_create_engine(self):
        """Test engine creation."""
        engine = DatabaseEngine(in_memory=True)
        assert engine is not None
        assert "memory" in engine.url

    def test_create_tables(self, engine):
        """Test table creation."""
        tables = engine.get_table_names()
        assert "domains" in tables
        assert "concepts" in tables
        assert "dualities" in tables

    def test_table_info(self, engine):
        """Test getting table info."""
        info = engine.get_table_info("domains")
        assert info["name"] == "domains"
        column_names = [c["name"] for c in info["columns"]]
        assert "name" in column_names
        assert "uuid" in column_names


# =============================================================================
# SessionManager Tests
# =============================================================================


class TestSessionManager:
    """Tests for SessionManager."""

    def test_create_session(self, session_manager):
        """Test session creation."""
        session = session_manager.create_session()
        assert session is not None
        session.close()

    def test_session_scope(self, session_manager):
        """Test session scope context manager."""
        with session_manager.session_scope() as session:
            domain = DomainModel(name="ScopeTest")
            session.add(domain)

        # Verify committed
        with session_manager.session_scope() as session:
            result = session.query(DomainModel).filter_by(name="ScopeTest").first()
            assert result is not None

    def test_session_scope_rollback(self, session_manager):
        """Test session scope rollback on error."""
        try:
            with session_manager.session_scope() as session:
                domain = DomainModel(name="RollbackTest")
                session.add(domain)
                raise ValueError("Test error")
        except ValueError:
            pass

        # Verify rolled back
        with session_manager.session_scope() as session:
            result = session.query(DomainModel).filter_by(name="RollbackTest").first()
            assert result is None


# =============================================================================
# DomainRepository Tests
# =============================================================================


class TestDomainRepository:
    """Tests for DomainRepository."""

    def test_create_domain(self, session):
        """Test creating domain through repository."""
        repo = DomainRepository()
        domain = repo.create(session, name="RepoTest", domain_type="fundamental")
        session.commit()

        assert domain.id is not None
        assert domain.name == "RepoTest"

    def test_create_with_duality(self, session):
        """Test creating domain with duality."""
        repo = DomainRepository()
        domain = repo.create_with_duality(
            session,
            name="WithDuality",
            positive_name="abstract",
            positive_value=50.0,
            negative_name="concrete",
            negative_value=50.0,
        )
        session.commit()

        assert domain.duality is not None
        assert domain.duality.is_balanced is True

    def test_get_by_name(self, session):
        """Test getting domain by name."""
        repo = DomainRepository()
        repo.create(session, name="FindMe")
        session.commit()

        found = repo.get_by_name(session, "FindMe")
        assert found is not None
        assert found.name == "FindMe"

    def test_get_all(self, session):
        """Test getting all domains."""
        repo = DomainRepository()
        repo.create(session, name="D1")
        repo.create(session, name="D2")
        repo.create(session, name="D3")
        session.commit()

        all_domains = repo.get_all(session)
        assert len(all_domains) == 3

    def test_update_domain(self, session):
        """Test updating domain."""
        repo = DomainRepository()
        domain = repo.create(session, name="Original")
        session.commit()

        repo.update(session, domain, description="Updated description")
        session.commit()

        found = repo.get_by_id(session, domain.id)
        assert found.description == "Updated description"

    def test_delete_domain(self, session):
        """Test deleting domain."""
        repo = DomainRepository()
        domain = repo.create(session, name="ToDelete")
        session.commit()
        domain_id = domain.id

        repo.delete(session, domain)
        session.commit()

        assert repo.get_by_id(session, domain_id) is None

    def test_count(self, session):
        """Test counting domains."""
        repo = DomainRepository()
        repo.create(session, name="D1")
        repo.create(session, name="D2")
        session.commit()

        assert repo.count(session) == 2

    def test_activate_domain(self, session):
        """Test activating domain."""
        repo = DomainRepository()
        domain = repo.create(session, name="Inactive")
        session.commit()

        repo.activate_domain(session, domain)
        session.commit()

        assert domain.is_active is True
        assert domain.state == "active"

    def test_validate_all_domains(self, session):
        """Test validating all domains."""
        repo = DomainRepository()

        # Create compliant domain
        repo.create_with_duality(
            session,
            name="Compliant",
            positive_name="pos",
            positive_value=50.0,
            negative_name="neg",
            negative_value=50.0,
        )

        # Create non-compliant domain
        repo.create(session, name="NonCompliant")

        session.commit()

        report = repo.validate_all_domains(session)
        assert report["total"] == 2
        assert report["valid"] == 1
        assert report["invalid"] == 1


# =============================================================================
# ConceptRepository Tests
# =============================================================================


class TestConceptRepository:
    """Tests for ConceptRepository."""

    def test_create_concept(self, session):
        """Test creating concept."""
        domain = DomainModel(name="TestDomain")
        session.add(domain)
        session.flush()

        repo = ConceptRepository()
        concept = repo.create_concept(
            session, domain_id=domain.id, name="TestConcept", concept_type="definition"
        )
        session.commit()

        assert concept.id is not None
        assert concept.certainty == 50.0

    def test_get_by_domain(self, session):
        """Test getting concepts by domain."""
        domain = DomainModel(name="TestDomain")
        session.add(domain)
        session.flush()

        repo = ConceptRepository()
        repo.create_concept(session, domain.id, "C1")
        repo.create_concept(session, domain.id, "C2")
        session.commit()

        concepts = repo.get_by_domain(session, domain.id)
        assert len(concepts) == 2

    def test_get_by_type(self, session):
        """Test getting concepts by type."""
        domain = DomainModel(name="TestDomain")
        session.add(domain)
        session.flush()

        repo = ConceptRepository()
        repo.create_concept(session, domain.id, "Theorem1", "theorem")
        repo.create_concept(session, domain.id, "Def1", "definition")
        repo.create_concept(session, domain.id, "Theorem2", "theorem")
        session.commit()

        theorems = repo.get_by_type(session, "theorem")
        assert len(theorems) == 2

    def test_count_by_domain(self, session):
        """Test counting concepts in domain."""
        domain = DomainModel(name="TestDomain")
        session.add(domain)
        session.flush()

        repo = ConceptRepository()
        repo.create_concept(session, domain.id, "C1")
        repo.create_concept(session, domain.id, "C2")
        repo.create_concept(session, domain.id, "C3")
        session.commit()

        count = repo.count_by_domain(session, domain.id)
        assert count == 3


# =============================================================================
# RelationRepository Tests
# =============================================================================


class TestRelationRepository:
    """Tests for RelationRepository."""

    def test_create_balanced_relation(self, session):
        """Test creating balanced relation."""
        domain1 = DomainModel(name="D1")
        domain2 = DomainModel(name="D2")
        session.add_all([domain1, domain2])
        session.flush()

        repo = RelationRepository()
        relation = repo.create_balanced_relation(
            session,
            source_domain_id=domain1.id,
            target_domain_id=domain2.id,
            name="TestRelation",
            total_influence=100.0,
        )
        session.commit()

        assert relation.influence_give == 50.0
        assert relation.influence_receive == 50.0
        assert relation.is_balanced is True

    def test_get_relations_for_domain(self, session):
        """Test getting relations for domain."""
        domain1 = DomainModel(name="D1")
        domain2 = DomainModel(name="D2")
        domain3 = DomainModel(name="D3")
        session.add_all([domain1, domain2, domain3])
        session.flush()

        repo = RelationRepository()
        repo.create_balanced_relation(session, domain1.id, domain2.id, "R1")
        repo.create_balanced_relation(session, domain1.id, domain3.id, "R2")
        session.commit()

        relations = repo.get_relations_for_domain(session, domain1.id)
        assert len(relations) == 2


# =============================================================================
# Integration Tests
# =============================================================================


class TestDatabaseIntegration:
    """Integration tests for database module."""

    def test_full_domain_persistence(self, session):
        """Test full domain persistence workflow."""
        # Create domain with duality
        domain_repo = DomainRepository()
        domain = domain_repo.create_with_duality(
            session,
            name="Mathematics",
            domain_type="fundamental",
            description="Study of numbers and structures",
            positive_name="abstract",
            positive_value=50.0,
            negative_name="concrete",
            negative_value=50.0,
        )
        session.flush()

        # Add concepts
        concept_repo = ConceptRepository()
        concept_repo.create_concept(
            session, domain.id, "Number", "definition", "A mathematical object"
        )
        concept_repo.create_concept(
            session, domain.id, "Set", "definition", "A collection of objects"
        )
        concept_repo.create_concept(
            session, domain.id, "Pythagorean Theorem", "theorem", "a² + b² = c²"
        )
        session.commit()

        # Verify
        assert domain.concept_count == 3
        assert domain.meta_compliant is True

    def test_domain_deletion_cascades(self, session):
        """Test domain deletion cascades to concepts."""
        domain = DomainModel(name="ToDelete")
        session.add(domain)
        session.flush()

        concept = ConceptModel(name="Child", domain_id=domain.id)
        session.add(concept)
        session.commit()

        concept_id = concept.id
        session.delete(domain)
        session.commit()

        # Concept should be deleted
        assert session.get(ConceptModel, concept_id) is None

    def test_meta_balance_maintained(self, session):
        """Test META 50/50 balance is maintained across operations."""
        domain_repo = DomainRepository()

        # Create multiple balanced domains
        for name in ["Math", "Physics", "Code"]:
            domain_repo.create_with_duality(
                session,
                name=name,
                positive_name="pos",
                positive_value=50.0,
                negative_name="neg",
                negative_value=50.0,
            )
        session.commit()

        # Validate all
        report = domain_repo.validate_all_domains(session)
        assert report["all_compliant"] is True
        assert report["valid"] == 3


# =============================================================================
# Persistence Service Tests
# =============================================================================


class TestDomainPersistenceService:
    """Tests for DomainPersistenceService."""

    def test_save_domain(self, engine):
        """Test saving a knowledge domain."""
        from database.persistence import DomainPersistenceService
        from knowledge.domains.mathematics import create_mathematics_domain

        service = DomainPersistenceService(auto_init=False)
        domain = create_mathematics_domain()

        db_domain = service.save_domain(domain)
        assert db_domain is not None
        assert db_domain.name == "Mathematics"

        # Check concept count by loading (since session is closed)
        loaded = service.load_domain("Mathematics")
        assert loaded["concept_count"] > 0

    def test_load_domain(self, engine):
        """Test loading a saved domain."""
        from database.persistence import DomainPersistenceService
        from knowledge.domains.physics import create_physics_domain

        service = DomainPersistenceService(auto_init=False)
        domain = create_physics_domain()
        service.save_domain(domain)

        loaded = service.load_domain("Physics")
        assert loaded is not None
        assert loaded["name"] == "Physics"
        assert loaded["duality"] is not None
        assert loaded["duality"]["is_balanced"] is True

    def test_list_domains(self, engine):
        """Test listing persisted domains."""
        from database.persistence import DomainPersistenceService
        from knowledge.domains.code import create_code_domain
        from knowledge.domains.mathematics import create_mathematics_domain

        service = DomainPersistenceService(auto_init=False)
        service.save_domain(create_mathematics_domain())
        service.save_domain(create_code_domain())

        domains = service.list_domains()
        assert len(domains) == 2
        names = [d["name"] for d in domains]
        assert "Mathematics" in names
        assert "Code" in names

    def test_delete_domain(self, engine):
        """Test deleting a domain."""
        from database.persistence import DomainPersistenceService
        from knowledge.domains.biology import create_biology_domain

        service = DomainPersistenceService(auto_init=False)
        service.save_domain(create_biology_domain())

        assert service.delete_domain("Biology") is True
        assert service.load_domain("Biology") is None

    def test_persistence_stats(self, engine):
        """Test persistence statistics."""
        from database.persistence import DomainPersistenceService
        from knowledge.domains.philosophy import create_philosophy_domain

        service = DomainPersistenceService(auto_init=False)
        service.save_domain(create_philosophy_domain())

        stats = service.get_persistence_stats()
        assert stats["total_domains"] == 1
        assert stats["total_concepts"] > 0
        assert stats["compliance_rate"] == 100.0

    def test_save_all_domains(self, engine):
        """Test saving multiple domains."""
        from database.persistence import DomainPersistenceService
        from knowledge.domains.code import create_code_domain
        from knowledge.domains.mathematics import create_mathematics_domain
        from knowledge.domains.physics import create_physics_domain

        service = DomainPersistenceService(auto_init=False)
        domains = [create_mathematics_domain(), create_physics_domain(), create_code_domain()]

        saved = service.save_all_domains(domains)
        assert len(saved) == 3

        listed = service.list_domains()
        assert len(listed) == 3

    def test_validate_persisted_domains(self, engine):
        """Test validation of persisted domains."""
        from database.persistence import DomainPersistenceService
        from knowledge.domains.mathematics import create_mathematics_domain

        service = DomainPersistenceService(auto_init=False)
        service.save_domain(create_mathematics_domain())

        report = service.validate_persisted_domains()
        assert report["all_compliant"] is True

    def test_update_existing_domain(self, engine):
        """Test updating an existing domain."""
        from database.persistence import DomainPersistenceService
        from knowledge.domains.mathematics import create_mathematics_domain

        service = DomainPersistenceService(auto_init=False)

        # Save initial
        domain = create_mathematics_domain()
        service.save_domain(domain)

        # Save again (update)
        db_domain = service.save_domain(domain)
        assert db_domain is not None

        # Should still be one domain
        domains = service.list_domains()
        assert len(domains) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
