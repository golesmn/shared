from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from shared.infrastructure.settings import db_settings


def get_db_connection_url() -> str:
    password = db_settings.DB_PASSWORD
    user = db_settings.DB_USER
    host = db_settings.DB_HOST
    db_name = db_settings.DB_NAME
    port = db_settings.DB_POT

    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


DATABASE_URL = get_db_connection_url()


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
