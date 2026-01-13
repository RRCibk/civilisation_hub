"""
Session Management
==================
SQLAlchemy session management with context managers.
"""

from contextlib import contextmanager
from typing import Generator

from sqlalchemy.orm import Session, sessionmaker

from database.engine import DatabaseEngine, get_engine


class SessionManager:
    """
    Manages database sessions.
    Provides context managers for safe session handling.
    """

    def __init__(self, engine: DatabaseEngine | None = None):
        """
        Initialize session manager.

        Args:
            engine: Database engine instance. Uses default if None.
        """
        self._engine = engine or get_engine()
        self._session_factory = sessionmaker(
            bind=self._engine.engine,
            expire_on_commit=False
        )

    @property
    def engine(self) -> DatabaseEngine:
        """Get the database engine."""
        return self._engine

    def create_session(self) -> Session:
        """Create a new session."""
        return self._session_factory()

    @contextmanager
    def session_scope(self) -> Generator[Session, None, None]:
        """
        Provide a transactional scope around a series of operations.

        Usage:
            with session_manager.session_scope() as session:
                session.add(model)
                # auto-commits on success, rolls back on exception
        """
        session = self.create_session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    @contextmanager
    def read_only_session(self) -> Generator[Session, None, None]:
        """
        Provide a read-only session scope.
        Does not commit changes.
        """
        session = self.create_session()
        try:
            yield session
        finally:
            session.close()


# Default session manager
_default_session_manager: SessionManager | None = None


def get_session_manager(engine: DatabaseEngine | None = None) -> SessionManager:
    """
    Get or create the default session manager.

    Args:
        engine: Database engine to use

    Returns:
        SessionManager instance
    """
    global _default_session_manager

    if _default_session_manager is None:
        _default_session_manager = SessionManager(engine)

    return _default_session_manager


def get_session() -> Session:
    """Get a new database session."""
    return get_session_manager().create_session()


@contextmanager
def session_scope() -> Generator[Session, None, None]:
    """
    Context manager for database session with auto-commit/rollback.

    Usage:
        with session_scope() as session:
            domain = DomainModel(name="Test")
            session.add(domain)
    """
    manager = get_session_manager()
    with manager.session_scope() as session:
        yield session


def reset_session_manager() -> None:
    """Reset the default session manager."""
    global _default_session_manager
    _default_session_manager = None
