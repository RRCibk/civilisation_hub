"""
Repository Layer
================
Repository pattern implementation for database operations.
Maintains META 50/50 balance validation on all operations.
"""

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, Type
from uuid import UUID

from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

from database.models import (
    Base,
    DomainModel,
    ConceptModel,
    ConceptRelationModel,
    RelationModel,
    DualityModel,
)
from database.session import SessionManager, get_session_manager


T = TypeVar("T", bound=Base)


class Repository(ABC, Generic[T]):
    """
    Abstract base repository with common CRUD operations.
    All operations maintain META 50/50 awareness.
    """

    def __init__(self, session_manager: SessionManager | None = None):
        """
        Initialize repository.

        Args:
            session_manager: Session manager instance. Uses default if None.
        """
        self._session_manager = session_manager or get_session_manager()

    @property
    @abstractmethod
    def model_class(self) -> Type[T]:
        """Return the model class this repository manages."""
        pass

    def create(self, session: Session, **kwargs) -> T:
        """
        Create a new instance.

        Args:
            session: Database session
            **kwargs: Model attributes

        Returns:
            Created model instance
        """
        instance = self.model_class(**kwargs)
        session.add(instance)
        session.flush()
        return instance

    def get_by_id(self, session: Session, id: int) -> T | None:
        """
        Get instance by ID.

        Args:
            session: Database session
            id: Primary key ID

        Returns:
            Model instance or None
        """
        return session.get(self.model_class, id)

    def get_by_uuid(self, session: Session, uuid: str) -> T | None:
        """
        Get instance by UUID.

        Args:
            session: Database session
            uuid: UUID string

        Returns:
            Model instance or None
        """
        stmt = select(self.model_class).where(self.model_class.uuid == uuid)
        return session.execute(stmt).scalar_one_or_none()

    def get_all(self, session: Session, limit: int | None = None) -> list[T]:
        """
        Get all instances.

        Args:
            session: Database session
            limit: Maximum number of results

        Returns:
            List of model instances
        """
        stmt = select(self.model_class)
        if limit:
            stmt = stmt.limit(limit)
        return list(session.execute(stmt).scalars().all())

    def update(self, session: Session, instance: T, **kwargs) -> T:
        """
        Update instance attributes.

        Args:
            session: Database session
            instance: Model instance to update
            **kwargs: Attributes to update

        Returns:
            Updated model instance
        """
        for key, value in kwargs.items():
            if hasattr(instance, key):
                setattr(instance, key, value)
        session.flush()
        return instance

    def delete(self, session: Session, instance: T) -> None:
        """
        Delete instance.

        Args:
            session: Database session
            instance: Model instance to delete
        """
        session.delete(instance)
        session.flush()

    def delete_by_id(self, session: Session, id: int) -> bool:
        """
        Delete instance by ID.

        Args:
            session: Database session
            id: Primary key ID

        Returns:
            True if deleted, False if not found
        """
        instance = self.get_by_id(session, id)
        if instance:
            self.delete(session, instance)
            return True
        return False

    def count(self, session: Session) -> int:
        """
        Count total instances.

        Args:
            session: Database session

        Returns:
            Total count
        """
        from sqlalchemy import func
        stmt = select(func.count()).select_from(self.model_class)
        return session.execute(stmt).scalar() or 0

    def exists(self, session: Session, id: int) -> bool:
        """
        Check if instance exists.

        Args:
            session: Database session
            id: Primary key ID

        Returns:
            True if exists
        """
        return self.get_by_id(session, id) is not None


class DomainRepository(Repository[DomainModel]):
    """Repository for domain operations."""

    @property
    def model_class(self) -> Type[DomainModel]:
        return DomainModel

    def get_by_name(self, session: Session, name: str) -> DomainModel | None:
        """
        Get domain by name.

        Args:
            session: Database session
            name: Domain name

        Returns:
            DomainModel or None
        """
        stmt = select(DomainModel).where(DomainModel.name == name)
        return session.execute(stmt).scalar_one_or_none()

    def create_with_duality(
        self,
        session: Session,
        name: str,
        domain_type: str = "fundamental",
        description: str = "",
        positive_name: str = "positive",
        positive_value: float = 50.0,
        negative_name: str = "negative",
        negative_value: float = 50.0
    ) -> DomainModel:
        """
        Create domain with duality.

        Args:
            session: Database session
            name: Domain name
            domain_type: Type of domain
            description: Domain description
            positive_name: Positive pole name
            positive_value: Positive pole value (should be 50)
            negative_name: Negative pole name
            negative_value: Negative pole value (should be 50)

        Returns:
            Created DomainModel with duality
        """
        # Create duality
        duality = DualityModel(
            name=f"{name}_duality",
            positive_name=positive_name,
            positive_value=positive_value,
            negative_name=negative_name,
            negative_value=negative_value
        )

        # Create domain
        domain = DomainModel(
            name=name,
            domain_type=domain_type,
            description=description,
            duality=duality
        )

        session.add(domain)
        session.flush()
        return domain

    def get_active_domains(self, session: Session) -> list[DomainModel]:
        """Get all active domains."""
        stmt = select(DomainModel).where(DomainModel.is_active == True)
        return list(session.execute(stmt).scalars().all())

    def get_meta_compliant_domains(self, session: Session) -> list[DomainModel]:
        """Get all META compliant domains."""
        stmt = select(DomainModel).where(DomainModel.meta_compliant == True)
        return list(session.execute(stmt).scalars().all())

    def get_by_type(self, session: Session, domain_type: str) -> list[DomainModel]:
        """Get domains by type."""
        stmt = select(DomainModel).where(DomainModel.domain_type == domain_type)
        return list(session.execute(stmt).scalars().all())

    def activate_domain(self, session: Session, domain: DomainModel) -> DomainModel:
        """Activate a domain."""
        domain.is_active = True
        domain.state = "active"
        session.flush()
        return domain

    def deactivate_domain(self, session: Session, domain: DomainModel) -> DomainModel:
        """Deactivate a domain."""
        domain.is_active = False
        domain.state = "inactive"
        session.flush()
        return domain

    def validate_all_domains(self, session: Session) -> dict[str, Any]:
        """
        Validate META compliance for all domains.

        Returns:
            Validation report
        """
        domains = self.get_all(session)
        valid = []
        invalid = []

        for domain in domains:
            if domain.validate_meta_compliance():
                valid.append(domain.name)
            else:
                invalid.append(domain.name)

        return {
            "total": len(domains),
            "valid": len(valid),
            "invalid": len(invalid),
            "valid_domains": valid,
            "invalid_domains": invalid,
            "all_compliant": len(invalid) == 0
        }


class ConceptRepository(Repository[ConceptModel]):
    """Repository for concept operations."""

    @property
    def model_class(self) -> Type[ConceptModel]:
        return ConceptModel

    def get_by_name(
        self,
        session: Session,
        name: str,
        domain_id: int | None = None
    ) -> ConceptModel | None:
        """
        Get concept by name, optionally filtered by domain.

        Args:
            session: Database session
            name: Concept name
            domain_id: Optional domain ID filter

        Returns:
            ConceptModel or None
        """
        stmt = select(ConceptModel).where(ConceptModel.name == name)
        if domain_id:
            stmt = stmt.where(ConceptModel.domain_id == domain_id)
        return session.execute(stmt).scalar_one_or_none()

    def get_by_domain(self, session: Session, domain_id: int) -> list[ConceptModel]:
        """Get all concepts for a domain."""
        stmt = select(ConceptModel).where(ConceptModel.domain_id == domain_id)
        return list(session.execute(stmt).scalars().all())

    def get_by_type(
        self,
        session: Session,
        concept_type: str,
        domain_id: int | None = None
    ) -> list[ConceptModel]:
        """Get concepts by type."""
        stmt = select(ConceptModel).where(ConceptModel.concept_type == concept_type)
        if domain_id:
            stmt = stmt.where(ConceptModel.domain_id == domain_id)
        return list(session.execute(stmt).scalars().all())

    def get_balanced_concepts(self, session: Session) -> list[ConceptModel]:
        """Get all balanced concepts (certainty = 50)."""
        stmt = select(ConceptModel).where(ConceptModel.is_balanced == True)
        return list(session.execute(stmt).scalars().all())

    def create_concept(
        self,
        session: Session,
        domain_id: int,
        name: str,
        concept_type: str = "definition",
        description: str = "",
        certainty: float = 50.0,
        metadata: dict | None = None
    ) -> ConceptModel:
        """
        Create a new concept.

        Args:
            session: Database session
            domain_id: Parent domain ID
            name: Concept name
            concept_type: Type of concept
            description: Concept description
            certainty: Certainty level (default 50 for balance)
            metadata: Additional metadata

        Returns:
            Created ConceptModel
        """
        concept = ConceptModel(
            domain_id=domain_id,
            name=name,
            concept_type=concept_type,
            description=description,
            certainty=certainty,
            uncertainty=100 - certainty,
            metadata_json=metadata
        )
        session.add(concept)
        session.flush()
        return concept

    def count_by_domain(self, session: Session, domain_id: int) -> int:
        """Count concepts in a domain."""
        from sqlalchemy import func
        stmt = select(func.count()).select_from(ConceptModel).where(
            ConceptModel.domain_id == domain_id
        )
        return session.execute(stmt).scalar() or 0


class RelationRepository(Repository[RelationModel]):
    """Repository for domain relation operations."""

    @property
    def model_class(self) -> Type[RelationModel]:
        return RelationModel

    def get_by_domains(
        self,
        session: Session,
        source_id: int,
        target_id: int
    ) -> RelationModel | None:
        """Get relation between two domains."""
        stmt = select(RelationModel).where(
            RelationModel.source_domain_id == source_id,
            RelationModel.target_domain_id == target_id
        )
        return session.execute(stmt).scalar_one_or_none()

    def get_relations_for_domain(
        self,
        session: Session,
        domain_id: int
    ) -> list[RelationModel]:
        """Get all relations involving a domain."""
        stmt = select(RelationModel).where(
            (RelationModel.source_domain_id == domain_id) |
            (RelationModel.target_domain_id == domain_id)
        )
        return list(session.execute(stmt).scalars().all())

    def create_balanced_relation(
        self,
        session: Session,
        source_domain_id: int,
        target_domain_id: int,
        name: str,
        total_influence: float = 100.0,
        relation_type: str = "bidirectional"
    ) -> RelationModel:
        """
        Create a balanced relation (50/50 give/receive).

        Args:
            session: Database session
            source_domain_id: Source domain ID
            target_domain_id: Target domain ID
            name: Relation name
            total_influence: Total influence (split 50/50)
            relation_type: Type of relation

        Returns:
            Created RelationModel
        """
        half = total_influence / 2
        relation = RelationModel(
            source_domain_id=source_domain_id,
            target_domain_id=target_domain_id,
            name=name,
            relation_type=relation_type,
            influence_give=half,
            influence_receive=half
        )
        session.add(relation)
        session.flush()
        return relation

    def get_balanced_relations(self, session: Session) -> list[RelationModel]:
        """Get all balanced relations."""
        stmt = select(RelationModel).where(RelationModel.is_balanced == True)
        return list(session.execute(stmt).scalars().all())


class ConceptRelationRepository(Repository[ConceptRelationModel]):
    """Repository for concept relation operations."""

    @property
    def model_class(self) -> Type[ConceptRelationModel]:
        return ConceptRelationModel

    def get_relations_for_concept(
        self,
        session: Session,
        concept_id: int
    ) -> list[ConceptRelationModel]:
        """Get all relations involving a concept."""
        stmt = select(ConceptRelationModel).where(
            (ConceptRelationModel.source_concept_id == concept_id) |
            (ConceptRelationModel.target_concept_id == concept_id)
        )
        return list(session.execute(stmt).scalars().all())

    def create_relation(
        self,
        session: Session,
        source_concept_id: int,
        target_concept_id: int,
        relation_type: str = "derives_from",
        strength: float = 50.0,
        bidirectional: bool = False
    ) -> ConceptRelationModel:
        """
        Create a concept relation.

        Args:
            session: Database session
            source_concept_id: Source concept ID
            target_concept_id: Target concept ID
            relation_type: Type of relation
            strength: Relation strength
            bidirectional: Whether relation is bidirectional

        Returns:
            Created ConceptRelationModel
        """
        relation = ConceptRelationModel(
            source_concept_id=source_concept_id,
            target_concept_id=target_concept_id,
            relation_type=relation_type,
            strength=strength,
            bidirectional=bidirectional
        )
        session.add(relation)
        session.flush()
        return relation


# Factory functions for repositories
def get_domain_repository(
    session_manager: SessionManager | None = None
) -> DomainRepository:
    """Get domain repository instance."""
    return DomainRepository(session_manager)


def get_concept_repository(
    session_manager: SessionManager | None = None
) -> ConceptRepository:
    """Get concept repository instance."""
    return ConceptRepository(session_manager)


def get_relation_repository(
    session_manager: SessionManager | None = None
) -> RelationRepository:
    """Get relation repository instance."""
    return RelationRepository(session_manager)
