"""
Database Models
===============
SQLAlchemy models for persisting domains, concepts, and relations.
All models maintain META 50/50 balance validation.
"""

from datetime import datetime
from typing import Any, Optional
from uuid import uuid4

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    JSON,
    String,
    Text,
    event,
)
from sqlalchemy.dialects.sqlite import JSON as SQLiteJSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Base class for all database models."""
    pass


class DualityModel(Base):
    """
    Model for domain dualities.
    Ensures META 50/50 balance on save.
    """
    __tablename__ = "dualities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(String(36), unique=True, default=lambda: str(uuid4()))
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    positive_name: Mapped[str] = mapped_column(String(255), nullable=False)
    positive_value: Mapped[float] = mapped_column(Float, default=50.0)
    negative_name: Mapped[str] = mapped_column(String(255), nullable=False)
    negative_value: Mapped[float] = mapped_column(Float, default=50.0)
    is_balanced: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship
    domain_id: Mapped[Optional[int]] = mapped_column(ForeignKey("domains.id"), nullable=True)
    domain: Mapped[Optional["DomainModel"]] = relationship("DomainModel", back_populates="duality")

    def __repr__(self) -> str:
        return f"DualityModel(name={self.name}, {self.positive_name}/{self.negative_name})"

    def validate_balance(self) -> bool:
        """Validate META 50/50 balance."""
        total = self.positive_value + self.negative_value
        if total == 0:
            return True
        pos_ratio = self.positive_value / total * 100
        neg_ratio = self.negative_value / total * 100
        self.is_balanced = abs(pos_ratio - 50.0) < 0.01 and abs(neg_ratio - 50.0) < 0.01
        return self.is_balanced

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "uuid": self.uuid,
            "name": self.name,
            "positive": {"name": self.positive_name, "value": self.positive_value},
            "negative": {"name": self.negative_name, "value": self.negative_value},
            "is_balanced": self.is_balanced,
        }


class DomainModel(Base):
    """
    Model for knowledge domains.
    Each domain has a duality maintaining META 50/50.
    """
    __tablename__ = "domains"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(String(36), unique=True, default=lambda: str(uuid4()))
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    domain_type: Mapped[str] = mapped_column(String(50), default="fundamental")
    description: Mapped[str] = mapped_column(Text, nullable=True)
    state: Mapped[str] = mapped_column(String(50), default="inactive")
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    meta_compliant: Mapped[bool] = mapped_column(Boolean, default=True)
    metadata_json: Mapped[Optional[str]] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    duality: Mapped[Optional["DualityModel"]] = relationship(
        "DualityModel",
        back_populates="domain",
        uselist=False,
        cascade="all, delete-orphan"
    )
    concepts: Mapped[list["ConceptModel"]] = relationship(
        "ConceptModel",
        back_populates="domain",
        cascade="all, delete-orphan"
    )
    source_relations: Mapped[list["RelationModel"]] = relationship(
        "RelationModel",
        foreign_keys="RelationModel.source_domain_id",
        back_populates="source_domain",
        cascade="all, delete-orphan"
    )
    target_relations: Mapped[list["RelationModel"]] = relationship(
        "RelationModel",
        foreign_keys="RelationModel.target_domain_id",
        back_populates="target_domain",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"DomainModel(name={self.name}, type={self.domain_type})"

    @property
    def concept_count(self) -> int:
        return len(self.concepts)

    def validate_meta_compliance(self) -> bool:
        """Validate domain maintains META 50/50."""
        if self.duality is None:
            self.meta_compliant = False
            return False
        self.meta_compliant = self.duality.validate_balance()
        return self.meta_compliant

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "uuid": self.uuid,
            "name": self.name,
            "domain_type": self.domain_type,
            "description": self.description,
            "state": self.state,
            "is_active": self.is_active,
            "meta_compliant": self.meta_compliant,
            "concept_count": self.concept_count,
            "duality": self.duality.to_dict() if self.duality else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }


class ConceptModel(Base):
    """
    Model for concepts within a domain.
    Concepts maintain certainty/uncertainty balance.
    """
    __tablename__ = "concepts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(String(36), unique=True, default=lambda: str(uuid4()))
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    concept_type: Mapped[str] = mapped_column(String(50), default="definition")
    description: Mapped[str] = mapped_column(Text, nullable=True)
    certainty: Mapped[float] = mapped_column(Float, default=50.0)
    uncertainty: Mapped[float] = mapped_column(Float, default=50.0)
    is_balanced: Mapped[bool] = mapped_column(Boolean, default=True)
    metadata_json: Mapped[Optional[str]] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Foreign key
    domain_id: Mapped[int] = mapped_column(ForeignKey("domains.id"), nullable=False)
    domain: Mapped["DomainModel"] = relationship("DomainModel", back_populates="concepts")

    # Relationships for concept relations
    source_relations: Mapped[list["ConceptRelationModel"]] = relationship(
        "ConceptRelationModel",
        foreign_keys="ConceptRelationModel.source_concept_id",
        back_populates="source_concept",
        cascade="all, delete-orphan"
    )
    target_relations: Mapped[list["ConceptRelationModel"]] = relationship(
        "ConceptRelationModel",
        foreign_keys="ConceptRelationModel.target_concept_id",
        back_populates="target_concept",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"ConceptModel(name={self.name}, type={self.concept_type})"

    def validate_balance(self) -> bool:
        """Validate certainty/uncertainty balance."""
        total = self.certainty + self.uncertainty
        if total > 0:
            self.certainty = self.certainty / total * 100
            self.uncertainty = self.uncertainty / total * 100
        self.is_balanced = abs(self.certainty - 50.0) < 0.01
        return self.is_balanced

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "uuid": self.uuid,
            "name": self.name,
            "concept_type": self.concept_type,
            "description": self.description,
            "certainty": self.certainty,
            "uncertainty": self.uncertainty,
            "is_balanced": self.is_balanced,
            "domain_id": self.domain_id,
            "metadata": self.metadata_json,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class ConceptRelationModel(Base):
    """
    Model for relations between concepts.
    """
    __tablename__ = "concept_relations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(String(36), unique=True, default=lambda: str(uuid4()))
    relation_type: Mapped[str] = mapped_column(String(50), default="derives_from")
    strength: Mapped[float] = mapped_column(Float, default=50.0)
    bidirectional: Mapped[bool] = mapped_column(Boolean, default=False)
    metadata_json: Mapped[Optional[str]] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Foreign keys
    source_concept_id: Mapped[int] = mapped_column(ForeignKey("concepts.id"), nullable=False)
    target_concept_id: Mapped[int] = mapped_column(ForeignKey("concepts.id"), nullable=False)

    # Relationships
    source_concept: Mapped["ConceptModel"] = relationship(
        "ConceptModel",
        foreign_keys=[source_concept_id],
        back_populates="source_relations"
    )
    target_concept: Mapped["ConceptModel"] = relationship(
        "ConceptModel",
        foreign_keys=[target_concept_id],
        back_populates="target_relations"
    )

    def __repr__(self) -> str:
        return f"ConceptRelationModel(type={self.relation_type}, strength={self.strength})"

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "uuid": self.uuid,
            "relation_type": self.relation_type,
            "strength": self.strength,
            "bidirectional": self.bidirectional,
            "source_concept_id": self.source_concept_id,
            "target_concept_id": self.target_concept_id,
        }


class RelationModel(Base):
    """
    Model for relations between domains.
    Maintains balanced give/receive influence.
    """
    __tablename__ = "domain_relations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(String(36), unique=True, default=lambda: str(uuid4()))
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    relation_type: Mapped[str] = mapped_column(String(50), default="bidirectional")
    influence_give: Mapped[float] = mapped_column(Float, default=50.0)
    influence_receive: Mapped[float] = mapped_column(Float, default=50.0)
    is_balanced: Mapped[bool] = mapped_column(Boolean, default=True)
    metadata_json: Mapped[Optional[str]] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Foreign keys
    source_domain_id: Mapped[int] = mapped_column(ForeignKey("domains.id"), nullable=False)
    target_domain_id: Mapped[int] = mapped_column(ForeignKey("domains.id"), nullable=False)

    # Relationships
    source_domain: Mapped["DomainModel"] = relationship(
        "DomainModel",
        foreign_keys=[source_domain_id],
        back_populates="source_relations"
    )
    target_domain: Mapped["DomainModel"] = relationship(
        "DomainModel",
        foreign_keys=[target_domain_id],
        back_populates="target_relations"
    )

    def __repr__(self) -> str:
        return f"RelationModel(name={self.name}, type={self.relation_type})"

    def validate_balance(self) -> bool:
        """Validate give/receive balance."""
        total = self.influence_give + self.influence_receive
        if total == 0:
            self.is_balanced = True
            return True
        give_ratio = self.influence_give / total * 100
        self.is_balanced = abs(give_ratio - 50.0) < 0.01
        return self.is_balanced

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "uuid": self.uuid,
            "name": self.name,
            "relation_type": self.relation_type,
            "influence_give": self.influence_give,
            "influence_receive": self.influence_receive,
            "is_balanced": self.is_balanced,
            "source_domain_id": self.source_domain_id,
            "target_domain_id": self.target_domain_id,
        }


# Event listeners for automatic validation
@event.listens_for(DualityModel, "before_insert")
@event.listens_for(DualityModel, "before_update")
def validate_duality_balance(mapper, connection, target):
    """Validate duality balance before save."""
    target.validate_balance()


@event.listens_for(DomainModel, "before_insert")
@event.listens_for(DomainModel, "before_update")
def validate_domain_compliance(mapper, connection, target):
    """Validate domain META compliance before save."""
    if target.duality:
        target.validate_meta_compliance()


@event.listens_for(RelationModel, "before_insert")
@event.listens_for(RelationModel, "before_update")
def validate_relation_balance(mapper, connection, target):
    """Validate relation balance before save."""
    target.validate_balance()
