from shared.abstractions.db.connection_builder import DBConnectionURLBuilder


class MySQLURLBuilder(DBConnectionURLBuilder):
    def build(self, settings) -> str:
        return f"mysql+pymysql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
