from shared.infrastructure.db.db import SessionLocal
from shared.infrastructure.db.uow import UnitOfWork
from shared.infrastructure.messaging.kafka_producer import get_dispatcher


def create_service(repo_cls, service_cls):
    """
    Generic factory that returns (service, unit_of_work)
    based on provided repository and service classes.
    """
    dispatcher = get_dispatcher()
    uow = UnitOfWork(SessionLocal, dispatcher=dispatcher)
    repo = repo_cls(session=uow.session)
    service = service_cls(repo)
    return service, uow
