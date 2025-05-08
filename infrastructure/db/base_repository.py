from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    def save(self, entity: T) -> None:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[T]:
        pass
