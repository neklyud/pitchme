from fastapi import APIRouter
from events.app.models.pydantic.events import (
    EventSchema,
    EventsOutListSchema,
    EventPatchSchema,
    EventPostSchema,
)
from typing import Optional
from events.app.crud.event import EventsCrud
from core.models.pydantic.json_api.filters import Filter, FilterList
from core.models.enums.filters import JsonAPIFiltersOperators

router: APIRouter = APIRouter()


class EventsRouter(object):
    crud: EventsCrud = EventsCrud()

    @classmethod
    async def get(cls, obj_id: int, related_fields: bool = False) -> EventSchema:
        try:
            res = await cls.crud.select(
                response_model=EventSchema,
                filters=[Filter(name="id", op=JsonAPIFiltersOperators.eq, val=obj_id)],
            )
        except Exception:
            raise
        return res

    @classmethod
    async def patch(cls, obj_id, event: EventPatchSchema) -> EventSchema:
        res = await cls.crud.update(
            response_model=EventSchema,
            updating_data=event,
            filters=[Filter(name="id", op=JsonAPIFiltersOperators.eq, val=obj_id)]
        )
        return res

    @classmethod
    async def post(cls, event: EventPostSchema) -> EventsOutListSchema:
        return await cls.crud.insert(event)


class EventRouterList(object):
    crud: EventsCrud = EventsCrud()

    @classmethod
    async def get(cls, filters: Optional[str] = None, related_fields: bool = False) -> EventsOutListSchema:
        if filters:
            filters = FilterList.parse_raw(filters)
        res = await cls.crud.select(
            response_model=EventsOutListSchema,
            filters=filters.filters,
        )
        return res
