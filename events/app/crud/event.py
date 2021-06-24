from core.utils.databases.alchemy import (
    BaseCrud,
)
from events.app.models.alchemy.events import Event
from events.app.helpers import (
    alchemy,
    AlchemyHelper,
)
from sqlalchemy.future import select
from sqlalchemy import insert
import logging
from events.app.models.pydantic.events import (
    EventSchema,
    EventsOutListSchema,
)


class EventsCrud(BaseCrud):
    alchemy_base: AlchemyHelper = alchemy

    async def insert(self, new_item):
        session_maker = alchemy.session
        async with session_maker() as session:
            new_event = await session.execute(insert(Event).values(**new_item.attributes.dict()))
            logging.info(new_event.id)

    async def select(self):
        session_maker = alchemy.session
        async with session_maker() as session:
            result = await session.execute(select(Event))
            data = []
            for row in result.scalars():
                data.append(self.to_schema(row, EventSchema))
        return EventsOutListSchema(data=data)

    async def update(self):
        pass

    async def delete(self):
        pass
