from shared.abstractions.db.connection_builder import DBConnectionURLBuilder


class PostgresURLBuilder(DBConnectionURLBuilder):
    def build(self, settings) -> str:
        return f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
