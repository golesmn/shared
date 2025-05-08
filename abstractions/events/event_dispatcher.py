from abc import ABC, abstractmethod

from .event import Event


class EventDispatcher:
    handlers = {}

    @classmethod
    def register(cls, event_type, handler):
        cls.handlers.setdefault(event_type, []).append(handler)

    @classmethod
    def dispatch(cls, event):
        for handler in cls.handlers.get(type(event), []):
            handler(event)
