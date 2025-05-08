# uow.py
from shared.abstractions.events.event_dispatcher import EventDispatcher
from shared.abstractions.primitives.aggregate import AggregateRoot
from shared.infrastructure.messaging.kafka_producer import KafkaEventDispatcher


class UnitOfWork:
    def __init__(self, session_factory, kafka_dispatcher: KafkaEventDispatcher):
        self.session = session_factory()
        self._aggregates = set()
        self._kafka_dispatcher = kafka_dispatcher

    def register(self, aggregate: AggregateRoot):
        self._aggregates.add(aggregate)

    def commit(self):
        self.session.commit()
        self._dispatch_events()

    def rollback(self):
        self.session.rollback()

    def _dispatch_events(self):
        for aggregate in self._aggregates:
            for event in aggregate.pull_events():
                self._kafka_dispatcher.dispatch(event)
        self._aggregates.clear()
