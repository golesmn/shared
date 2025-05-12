import json
import logging
from functools import lru_cache
from typing import Any

from kafka import KafkaProducer

from shared.abstractions.events.event import Event
from shared.abstractions.events.event_dispatcher import EventDispatcher
from shared.utils.enable_hashable_dict import hash_dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)




class KafkaEventDispatcher(EventDispatcher):
    def __init__(self, bootstrap_servers: str, kafka_topic_map: dict[str, Any]):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        self._kafka_topic_map = kafka_topic_map

    def _get_kafka_topic(self, event: Event):
        topic = self._kafka_topic_map[event.__class__.__name__]
        return topic

    def dispatch(self, event: Event):
        topic = self._get_kafka_topic(event=event)
        payload = self._serialize_event(event)
        self.producer.send(topic=topic, value=payload)
        self.producer.flush()

    def _serialize_event(self, event: Event) -> str:
        return event.asdict()

@hash_dict
@lru_cache
def get_dispatcher(kafka_topic_map: dict[str, Any]):
    return KafkaEventDispatcher(
        bootstrap_servers="my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092",
        kafka_topic_map=kafka_topic_map,
    )
