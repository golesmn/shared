from shared.infrastructure.db.db import SessionLocal
from shared.infrastructure.db.uow import UnitOfWork
from shared.infrastructure.messaging.kafka_producer import KafkaEventDispatcher


def create_service(repo_cls, service_cls, dispatcher: KafkaEventDispatcher):
    """
    Generic factory that returns (service, unit_of_work)
    based on provided repository and service classes.
    """
    uow = UnitOfWork(SessionLocal, dispatcher=dispatcher)
    repo = repo_cls(session=uow.session)
    service = service_cls(repo)
    return service, uow
