import json
import logging

from access_management.repositories.user_repository import UserRepository
from kafka import KafkaProducer
from flask import request

from access_management.application.services.user_service import UserService
from access_management.domain.aggregates.user import User
from shared.abstractions.events.event import Event
from shared.infrastructure.db.db import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

KAKFA_TOPICS_MAP = {
    "UserCreated" : "request-topic"
}

class KafkaEventDispatcher:
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
