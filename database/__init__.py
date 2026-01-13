"""
Database Module
===============
Database persistence for Civilisation Hub domains and concepts.
Maintains META 50/50 equilibrium validation on all persisted data.
"""

from database.engine import (
    DatabaseEngine,
    create_tables,
    drop_tables,
    get_engine,
)
from database.models import (
    Base,
    ConceptModel,
    DomainModel,
    DualityModel,
    RelationModel,
)
from database.persistence import (
    DomainPersistenceService,
    list_persisted_domains,
    load_domain,
    save_domain,
)
from database.repository import (
    ConceptRepository,
    DomainRepository,
    RelationRepository,
    Repository,
)
from database.session import (
    SessionManager,
    get_session,
    session_scope,
)

__all__ = [
    "Base",
    "DomainModel",
    "ConceptModel",
    "RelationModel",
    "DualityModel",
    "DatabaseEngine",
    "get_engine",
    "create_tables",
    "drop_tables",
    "Repository",
    "DomainRepository",
    "ConceptRepository",
    "RelationRepository",
    "SessionManager",
    "get_session",
    "session_scope",
    "DomainPersistenceService",
    "save_domain",
    "load_domain",
    "list_persisted_domains",
]
