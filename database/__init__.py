"""
Database Module
===============
Database persistence for Civilisation Hub domains and concepts.
Maintains META 50/50 equilibrium validation on all persisted data.
"""

from database.models import (
    Base,
    DomainModel,
    ConceptModel,
    RelationModel,
    DualityModel,
)
from database.engine import (
    DatabaseEngine,
    get_engine,
    create_tables,
    drop_tables,
)
from database.repository import (
    Repository,
    DomainRepository,
    ConceptRepository,
    RelationRepository,
)
from database.session import (
    SessionManager,
    get_session,
    session_scope,
)
from database.persistence import (
    DomainPersistenceService,
    save_domain,
    load_domain,
    list_persisted_domains,
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
