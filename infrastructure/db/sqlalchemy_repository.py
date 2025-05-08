from typing import Generic, Optional, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

from .base_repository import BaseRepository

T = TypeVar("T")


class SQLAlchemyRepository(BaseRepository[T], Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    def save(self, entity: T) -> None:
        self.session.add(entity)
        # self.session.commit()

    def get_by_id(self, entity_id: int) -> Optional[T]:
        return self.session.query(self.model).get(entity_id)

    def delete(self, entity: T) -> None:
        self.session.delete(entity)
        # self.session.commit()

    def update(self, entity: T) -> None:
        self.session.commit()

    def all(self) -> list[T]:
        return self.session.query(self.model).all()
