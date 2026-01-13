"""
Domain Persistence Service
==========================
Service for persisting knowledge domains to database.
Bridges in-memory domain objects with database models.
"""

from typing import Any
from uuid import UUID

from sqlalchemy.orm import Session

from database.models import (
    DomainModel,
    ConceptModel,
    ConceptRelationModel,
    DualityModel,
)
from database.repository import (
    DomainRepository,
    ConceptRepository,
    ConceptRelationRepository,
)
from database.session import SessionManager, get_session_manager
from database.engine import get_engine, create_tables

from knowledge.domains.base import (
    KnowledgeDomain,
    Concept,
    ConceptRelation,
    ConceptType,
    RelationType,
)


class DomainPersistenceService:
    """
    Service for persisting and loading knowledge domains.
    Maintains META 50/50 compliance in persistence operations.
    """

    def __init__(
        self,
        session_manager: SessionManager | None = None,
        auto_init: bool = True
    ):
        """
        Initialize persistence service.

        Args:
            session_manager: Session manager instance
            auto_init: Automatically create tables if they don't exist
        """
        if auto_init:
            engine = get_engine()
            create_tables(engine)

        self._session_manager = session_manager or get_session_manager()
        self._domain_repo = DomainRepository(self._session_manager)
        self._concept_repo = ConceptRepository(self._session_manager)
        self._relation_repo = ConceptRelationRepository(self._session_manager)

    def save_domain(self, domain: KnowledgeDomain) -> DomainModel:
        """
        Save a knowledge domain to database.

        Args:
            domain: KnowledgeDomain to persist

        Returns:
            Persisted DomainModel
        """
        with self._session_manager.session_scope() as session:
            # Check if domain already exists
            existing = self._domain_repo.get_by_name(session, domain.name)
            if existing:
                return self._update_domain(session, existing, domain)

            # Create new domain model
            db_domain = self._create_domain_model(session, domain)

            # Save concepts
            concept_map = self._save_concepts(session, domain, db_domain.id)

            # Save relations
            self._save_relations(session, domain, concept_map)

            return db_domain

    def _create_domain_model(
        self,
        session: Session,
        domain: KnowledgeDomain
    ) -> DomainModel:
        """Create database model from knowledge domain."""
        # Create duality if exists
        duality = None
        if domain.domain.duality:
            d = domain.domain.duality
            duality = DualityModel(
                name=f"{domain.name}_duality",
                positive_name=d.positive.name,
                positive_value=d.positive.value,
                negative_name=d.negative.name,
                negative_value=d.negative.value
            )

        db_domain = DomainModel(
            uuid=str(domain.id),
            name=domain.name,
            domain_type=domain.domain_type.value,
            description=domain.description,
            state=domain.domain.state.value,
            is_active=domain.domain.state.value == "active",
            duality=duality
        )

        session.add(db_domain)
        session.flush()
        return db_domain

    def _save_concepts(
        self,
        session: Session,
        domain: KnowledgeDomain,
        domain_id: int
    ) -> dict[UUID, int]:
        """
        Save all concepts from domain.

        Returns:
            Mapping of concept UUID to database ID
        """
        concept_map: dict[UUID, int] = {}

        for concept in domain._concepts.values():
            db_concept = ConceptModel(
                uuid=str(concept.id),
                name=concept.name,
                concept_type=concept.concept_type.value,
                description=concept.description,
                certainty=concept.certainty,
                uncertainty=concept.uncertainty,
                domain_id=domain_id,
                metadata_json=concept.metadata if concept.metadata else None
            )
            session.add(db_concept)
            session.flush()
            concept_map[concept.id] = db_concept.id

        return concept_map

    def _save_relations(
        self,
        session: Session,
        domain: KnowledgeDomain,
        concept_map: dict[UUID, int]
    ) -> None:
        """Save all concept relations."""
        for relation in domain._relations.values():
            if relation.source_id in concept_map and relation.target_id in concept_map:
                db_relation = ConceptRelationModel(
                    uuid=str(relation.id),
                    source_concept_id=concept_map[relation.source_id],
                    target_concept_id=concept_map[relation.target_id],
                    relation_type=relation.relation_type.value,
                    strength=relation.strength,
                    bidirectional=relation.bidirectional,
                    metadata_json=relation.metadata if relation.metadata else None
                )
                session.add(db_relation)

    def _update_domain(
        self,
        session: Session,
        existing: DomainModel,
        domain: KnowledgeDomain
    ) -> DomainModel:
        """Update existing domain with new data."""
        existing.description = domain.description
        existing.state = domain.domain.state.value
        existing.is_active = domain.domain.state.value == "active"

        # Update duality
        if domain.domain.duality and existing.duality:
            d = domain.domain.duality
            existing.duality.positive_value = d.positive.value
            existing.duality.negative_value = d.negative.value

        # Update concepts - add new ones
        existing_uuids = {c.uuid for c in existing.concepts}
        for concept in domain._concepts.values():
            if str(concept.id) not in existing_uuids:
                db_concept = ConceptModel(
                    uuid=str(concept.id),
                    name=concept.name,
                    concept_type=concept.concept_type.value,
                    description=concept.description,
                    certainty=concept.certainty,
                    uncertainty=concept.uncertainty,
                    domain_id=existing.id,
                    metadata_json=concept.metadata if concept.metadata else None
                )
                session.add(db_concept)

        session.flush()
        return existing

    def load_domain(self, name: str) -> dict[str, Any] | None:
        """
        Load domain data from database.

        Args:
            name: Domain name

        Returns:
            Domain data dictionary or None if not found
        """
        with self._session_manager.read_only_session() as session:
            db_domain = self._domain_repo.get_by_name(session, name)
            if not db_domain:
                return None

            return self._domain_to_dict(db_domain)

    def _domain_to_dict(self, db_domain: DomainModel) -> dict[str, Any]:
        """Convert database domain to dictionary."""
        concepts = [
            {
                "id": c.uuid,
                "name": c.name,
                "type": c.concept_type,
                "description": c.description,
                "certainty": c.certainty,
                "uncertainty": c.uncertainty,
                "is_balanced": c.is_balanced,
                "metadata": c.metadata_json
            }
            for c in db_domain.concepts
        ]

        duality = None
        if db_domain.duality:
            duality = {
                "positive": {
                    "name": db_domain.duality.positive_name,
                    "value": db_domain.duality.positive_value
                },
                "negative": {
                    "name": db_domain.duality.negative_name,
                    "value": db_domain.duality.negative_value
                },
                "is_balanced": db_domain.duality.is_balanced
            }

        return {
            "id": db_domain.uuid,
            "name": db_domain.name,
            "type": db_domain.domain_type,
            "description": db_domain.description,
            "state": db_domain.state,
            "is_active": db_domain.is_active,
            "meta_compliant": db_domain.meta_compliant,
            "duality": duality,
            "concepts": concepts,
            "concept_count": len(concepts)
        }

    def list_domains(self) -> list[dict[str, Any]]:
        """
        List all persisted domains.

        Returns:
            List of domain summary dictionaries
        """
        with self._session_manager.read_only_session() as session:
            domains = self._domain_repo.get_all(session)
            return [
                {
                    "id": d.uuid,
                    "name": d.name,
                    "type": d.domain_type,
                    "concept_count": d.concept_count,
                    "meta_compliant": d.meta_compliant,
                    "is_active": d.is_active
                }
                for d in domains
            ]

    def delete_domain(self, name: str) -> bool:
        """
        Delete a domain from database.

        Args:
            name: Domain name

        Returns:
            True if deleted, False if not found
        """
        with self._session_manager.session_scope() as session:
            domain = self._domain_repo.get_by_name(session, name)
            if domain:
                self._domain_repo.delete(session, domain)
                return True
            return False

    def save_all_domains(self, domains: list[KnowledgeDomain]) -> list[str]:
        """
        Save multiple domains.

        Args:
            domains: List of knowledge domains

        Returns:
            List of saved domain names
        """
        saved = []
        for domain in domains:
            self.save_domain(domain)
            saved.append(domain.name)
        return saved

    def get_persistence_stats(self) -> dict[str, Any]:
        """
        Get database persistence statistics.

        Returns:
            Statistics dictionary
        """
        with self._session_manager.read_only_session() as session:
            domain_count = self._domain_repo.count(session)
            concept_count = self._concept_repo.count(session)

            compliant_domains = self._domain_repo.get_meta_compliant_domains(session)

            return {
                "total_domains": domain_count,
                "total_concepts": concept_count,
                "meta_compliant_domains": len(compliant_domains),
                "compliance_rate": (
                    len(compliant_domains) / domain_count * 100
                    if domain_count > 0 else 100.0
                )
            }

    def validate_persisted_domains(self) -> dict[str, Any]:
        """
        Validate META compliance for all persisted domains.

        Returns:
            Validation report
        """
        with self._session_manager.session_scope() as session:
            return self._domain_repo.validate_all_domains(session)


# Convenience functions

def save_domain(domain: KnowledgeDomain) -> DomainModel:
    """Save a domain to database."""
    service = DomainPersistenceService()
    return service.save_domain(domain)


def load_domain(name: str) -> dict[str, Any] | None:
    """Load a domain from database."""
    service = DomainPersistenceService()
    return service.load_domain(name)


def list_persisted_domains() -> list[dict[str, Any]]:
    """List all persisted domains."""
    service = DomainPersistenceService()
    return service.list_domains()
