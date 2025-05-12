from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from shared.infrastructure.settings import db_settings
from shared.utils.db.get_connection_url import get_db_connection_url

DATABASE_URL = get_db_connection_url()


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
