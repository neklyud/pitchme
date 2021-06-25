from core.utils.databases.alchemy import BaseCrud, Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    Sequence,
)
from datetime import datetime
from events.app.models.pydantic.events import (
    EventSchema,
)
from events.app.helpers import alchemy
import logging
from sqlalchemy.future import select
from sqlalchemy import insert


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, Sequence('event_id_seq'), primary_key=True)
    name = Column(String)
    description = Column(Text)
    city = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow())
    end_time = Column(DateTime, default=datetime.utcnow())

    def __repr__(self):
        return "<Event id={id}>".format(id=self.id)

    # def __dict__(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "description": self.description,
    #         "city": self.city,
    #         "start_time": self.start_time,
    #         "end_time": self.end_time,
    #     }
