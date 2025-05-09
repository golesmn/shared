from typing import Optional
import uuid
from dataclasses import asdict, dataclass
from datetime import datetime


@dataclass
class Event:
    event_id: Optional[str]
    event_type: str
    timestamp: Optional[datetime]

    def __post_init__(self):
        if not self.event_id:
            self.event_id = str(uuid.uuid4())
        if not self.timestamp:
            self.timestamp = datetime.now()

    def asdict(self):
        return {k: str(v) for k, v in asdict(self).items()}
