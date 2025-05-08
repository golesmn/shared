from abc import ABC, abstractmethod

from .event import Event


class EventDispatcher(ABC):
    
    @abstractmethod
    def dispatch(self, event: Event):
        pass

