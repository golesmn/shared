from abc import ABC
from typing import List

from shared.abstractions.events.event import Event


class AggregateRoot(ABC):
    _events: List[Event] = []

    def add_event(self, event: Event):
        self._events.append(event)

    def pull_events(self) -> List[Event]:
        events, self._events = self._events, []
        return events
