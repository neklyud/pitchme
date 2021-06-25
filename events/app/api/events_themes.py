from fastapi import APIRouter
from events.app.models.pydantic.events_schema import (
    EventsThemesSchema,
    EventsThemesOutListSchema,
    EventsThemesPostSchema,
)
from typing import Optional
from events.app.crud.event import events_themes_crud
from core.models.pydantic.json_api.filters import Filter, FilterList
from core.models.enums.filters import JsonAPIFiltersOperators

router: APIRouter = APIRouter()


class EventsThemesRouter(object):
    @classmethod
    async def get(cls, obj_id: int, related_fields: bool = False) -> EventsThemesSchema:
        try:
            res = await events_themes_crud.select(
                response_model=EventsThemesSchema,
                filters=[Filter(name="id", op=JsonAPIFiltersOperators.eq, val=obj_id)],
            )
        except Exception:
            raise
        return res

    @classmethod
    async def post(cls, event_theme: EventsThemesPostSchema) -> EventsThemesOutListSchema:
        return await events_themes_crud.insert(event_theme)


class EventThemesRouterList(object):

    @classmethod
    async def get(cls, filters: Optional[str] = None, related_fields: bool = False) -> EventsThemesOutListSchema:
        if filters:
            filters = FilterList.parse_raw(filters).filters
        res = await events_themes_crud.select(
            response_model=EventsThemesOutListSchema,
            filters=filters,
        )
        return res
