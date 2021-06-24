from typing import List
from fastapi import APIRouter
from events.app.models.pydantic.events import (
    EventSchema,
    EventsOutListSchema,
    EventBaseSchema,
)
from core.models.pydantic.json_api.filters import Filter
from typing import Optional
import logging
from events.app.models.alchemy.events import Event
from events.app.crud.event import EventsCrud

router: APIRouter = APIRouter()


class EventsRouter(object):
    @classmethod
    async def get(cls, related_fields: bool = False) -> EventsOutListSchema:
        logging.info("Get")
        res = await EventsCrud().select()
        return res

    @classmethod
    async def patch(cls, event: EventBaseSchema) -> EventsOutListSchema:
        pass

    @classmethod
    async def post(cls, event: EventBaseSchema) -> EventsOutListSchema:
        await EventsCrud().insert(event)
        return EventsOutListSchema()


class EventRouterList(object):
    @classmethod
    async def get(cls, filters: Optional[List[Filter]] = None, related_fields: bool = False) -> EventsOutListSchema:
        pass
