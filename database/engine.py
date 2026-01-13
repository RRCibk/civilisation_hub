"""
Database Engine
===============
SQLAlchemy engine configuration and management.
"""

from pathlib import Path
from typing import Any

from sqlalchemy import create_engine, Engine, event
from sqlalchemy.pool import StaticPool

from database.models import Base


class DatabaseEngine:
    """
    Database engine manager.
    Supports SQLite (file and in-memory) with optional PostgreSQL support.
    """

    def __init__(
        self,
        database_url: str | None = None,
        echo: bool = False,
        in_memory: bool = False
    ):
        """
        Initialize database engine.

        Args:
            database_url: Database connection URL. If None, uses SQLite.
            echo: Whether to log SQL statements.
            in_memory: Use in-memory SQLite (for testing).
        """
        if database_url:
            self._url = database_url
        elif in_memory:
            self._url = "sqlite:///:memory:"
        else:
            # Default to file-based SQLite
            db_path = Path("data/civilisation_hub.db")
            db_path.parent.mkdir(parents=True, exist_ok=True)
            self._url = f"sqlite:///{db_path}"

        self._echo = echo
        self._in_memory = in_memory
        self._engine: Engine | None = None

    @property
    def url(self) -> str:
        """Get database URL."""
        return self._url

    @property
    def engine(self) -> Engine:
        """Get or create SQLAlchemy engine."""
        if self._engine is None:
            self._engine = self._create_engine()
        return self._engine

    def _create_engine(self) -> Engine:
        """Create SQLAlchemy engine with appropriate settings."""
        if self._in_memory or "sqlite" in self._url:
            # SQLite-specific settings
            engine = create_engine(
                self._url,
                echo=self._echo,
                connect_args={"check_same_thread": False},
                poolclass=StaticPool if self._in_memory else None,
            )

            # Enable foreign key support for SQLite
            @event.listens_for(engine, "connect")
            def set_sqlite_pragma(dbapi_connection, connection_record):
                cursor = dbapi_connection.cursor()
                cursor.execute("PRAGMA foreign_keys=ON")
                cursor.close()

            return engine
        else:
            # PostgreSQL or other databases
            return create_engine(
                self._url,
                echo=self._echo,
                pool_pre_ping=True,
            )

    def create_all_tables(self) -> None:
        """Create all tables defined in models."""
        Base.metadata.create_all(self.engine)

    def drop_all_tables(self) -> None:
        """Drop all tables."""
        Base.metadata.drop_all(self.engine)

    def reset_database(self) -> None:
        """Drop and recreate all tables."""
        self.drop_all_tables()
        self.create_all_tables()

    def dispose(self) -> None:
        """Dispose of the engine connection pool."""
        if self._engine:
            self._engine.dispose()
            self._engine = None

    def get_table_names(self) -> list[str]:
        """Get list of table names in database."""
        from sqlalchemy import inspect
        inspector = inspect(self.engine)
        return inspector.get_table_names()

    def get_table_info(self, table_name: str) -> dict[str, Any]:
        """Get information about a specific table."""
        from sqlalchemy import inspect
        inspector = inspect(self.engine)

        columns = []
        for col in inspector.get_columns(table_name):
            columns.append({
                "name": col["name"],
                "type": str(col["type"]),
                "nullable": col["nullable"],
            })

        return {
            "name": table_name,
            "columns": columns,
            "primary_keys": inspector.get_pk_constraint(table_name),
            "foreign_keys": inspector.get_foreign_keys(table_name),
        }

    def __repr__(self) -> str:
        return f"DatabaseEngine(url={self._url})"


# Default engine instance
_default_engine: DatabaseEngine | None = None


def get_engine(
    database_url: str | None = None,
    echo: bool = False,
    in_memory: bool = False,
    reset: bool = False
) -> DatabaseEngine:
    """
    Get or create the default database engine.

    Args:
        database_url: Database connection URL
        echo: Whether to log SQL
        in_memory: Use in-memory database
        reset: Reset the existing engine

    Returns:
        DatabaseEngine instance
    """
    global _default_engine

    if reset and _default_engine:
        _default_engine.dispose()
        _default_engine = None

    if _default_engine is None:
        _default_engine = DatabaseEngine(
            database_url=database_url,
            echo=echo,
            in_memory=in_memory
        )

    return _default_engine


def create_tables(engine: DatabaseEngine | None = None) -> None:
    """Create all database tables."""
    if engine is None:
        engine = get_engine()
    engine.create_all_tables()


def drop_tables(engine: DatabaseEngine | None = None) -> None:
    """Drop all database tables."""
    if engine is None:
        engine = get_engine()
    engine.drop_all_tables()


def reset_engine() -> None:
    """Reset the default engine."""
    global _default_engine
    if _default_engine:
        _default_engine.dispose()
    _default_engine = None
