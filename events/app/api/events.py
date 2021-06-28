from fastapi import APIRouter
from events.app.models.pydantic.events import (
    EventSchema,
    EventsOutListSchema,
    EventPatchSchema,
    EventPostSchema,
)
from typing import Optional, List
from events.app.crud.event import event_crud
from core.models.pydantic.json_api.filters import Filter, FilterList
from core.models.enums.filters import JsonAPIFiltersOperators
from events.app.models.alchemy.event_theme import EventsThemes
from events.app.models.alchemy.theme import Theme
from events.app.models.alchemy.events import Event
from sqlalchemy import join
router: APIRouter = APIRouter()


class EventsRouter(object):
    @classmethod
    async def get(cls, obj_id: int, related_fields: bool = False) -> EventSchema:
        j = None
        if related_fields:
            j = join(Event, EventsThemes, Event.id == EventsThemes.event_id)
            j = j.join(Theme, EventsThemes.theme_id == Theme.id)
        try:
            res = await event_crud.select(
                response_model=EventSchema,
                filters=[
                    Filter(name="event.id", op=JsonAPIFiltersOperators.eq, val=obj_id),
                ],
                tables_for_join=[EventsThemes, Theme],
                join=j,
            )
        except Exception:
            raise
        return res

    @classmethod
    async def patch(cls, obj_id, event: EventPatchSchema) -> EventSchema:
        res = await event_crud.update(
            response_model=EventSchema,
            updating_data=event,
            filters=[Filter(name="id", op=JsonAPIFiltersOperators.eq, val=obj_id)]
        )
        return res

    @classmethod
    async def post(cls, event: EventPostSchema) -> EventsOutListSchema:
        return await event_crud.insert(event)


class EventRouterList(object):

    @classmethod
    async def get(cls, filters: Optional[str] = None, related_fields: bool = False) -> EventsOutListSchema:
        j = None
        filters_list: Optional[List[Filter]] = None
        if related_fields:
            j = join(Event, EventsThemes, Event.id == EventsThemes.event_id)
            j = j.join(Theme, EventsThemes.theme_id == Theme.id)
        if filters:
            filters_list = FilterList.parse_raw(filters).filters
        res = await event_crud.select(
            response_model=EventsOutListSchema,
            filters=filters_list,
            tables_for_join=[EventsThemes, Theme],
            join=j,
        )
        return res
