from core.utils.databases.alchemy import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    Sequence,
)
from datetime import datetime


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
