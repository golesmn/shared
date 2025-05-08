import json
import logging

from kafka import KafkaProducer

from shared.abstractions.events.event import Event
from shared.abstractions.events.event_dispatcher import EventDispatcher

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

KAKFA_TOPICS_MAP = {"UserCreated": "request-topic"}


class KafkaEventDispatcher(EventDispatcher):
    def __init__(self, bootstrap_servers: str):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )

    def dispatch(self, event: Event):
        topic = self._get_topic_for_event(event)
        payload = self._serialize_event(event)
        self.producer.send(topic=topic, value=payload, key="access_management".encode())
        self.producer.flush()

    def _get_topic_for_event(self, event: Event) -> str:
        return KAKFA_TOPICS_MAP[event.__class__.__name__]

    def _serialize_event(self, event: Event) -> str:
        return event.asdict()
