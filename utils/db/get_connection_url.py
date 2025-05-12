from shared.infrastructure.db.connection.mysql_connection_builder import MySQLURLBuilder
from shared.infrastructure.db.connection.postgres_connection_builder import (
    PostgresURLBuilder,
)
from shared.infrastructure.settings import db_settings

ENGINE_STRATEGIES = {
    "postgresql": PostgresURLBuilder(),
    "mysql": MySQLURLBuilder(),
}


def get_db_connection_url() -> str:
    engine = db_settings.DB_ENGINE.lowe()
    builder = ENGINE_STRATEGIES.get(engine)
    if not builder:
        raise ValueError(f"Unsupported DB_ENGINE: {engine}")
    return builder.build(db_settings)
