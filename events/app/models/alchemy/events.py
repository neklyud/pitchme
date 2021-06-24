from core.utils.databases.alchemy import BaseCrud, Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
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

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    city = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow())
    end_time = Column(DateTime, default=datetime.utcnow())

    def __repr__(self):
        return "<Event id={id}>".format(id=self.id)

    # @classmethod
    # async def insert_item(cls, new_item: EventsInJSONAPISchema):
    #     session_maker = alchemy.session
    #     async with session_maker() as session:
    #         new_event = await session.execute(insert(Event).values(**new_item.attributes.dict()))
    #         logging.info(new_event.id)
    #
    # @classmethod
    # async def select_items(cls):
    #     session_maker = alchemy.session
    #     async with session_maker() as session:
    #         result = await session.execute(select(Event))
    #     data = []
    #     for i_res in result.fetchall():
    #         i_res.to_json_api(EventSchema)
    #         print(i_res)
    #     return EventsOutListJSONAPISchema(data=data)

