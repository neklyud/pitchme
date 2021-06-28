from fastapi import APIRouter
from events.app.models.pydantic.theme import (
    ThemeSchema,
    ThemeOutListSchema,
    ThemePatchSchema,
    ThemePostSchema,
)
from typing import Optional, List
from events.app.crud.event import theme_crud
from core.models.pydantic.json_api.filters import Filter, FilterList
from core.models.enums.filters import JsonAPIFiltersOperators

router: APIRouter = APIRouter()


class ThemeRouter(object):
    @classmethod
    async def get(cls, obj_id: int, related_fields: bool = False) -> ThemeSchema:
        try:
            res = await theme_crud.select(
                response_model=ThemeSchema,
                filters=[Filter(name="id", op=JsonAPIFiltersOperators.eq, val=obj_id)],
            )
        except Exception:
            raise
        return res

    @classmethod
    async def patch(cls, obj_id, event: ThemePatchSchema) -> ThemeSchema:
        res = await theme_crud.update(
            response_model=ThemeSchema,
            updating_data=event,
            filters=[Filter(name="id", op=JsonAPIFiltersOperators.eq, val=obj_id)]
        )
        return res

    @classmethod
    async def post(cls, theme: ThemePostSchema) -> ThemeOutListSchema:
        return await theme_crud.insert(theme)


class ThemeRouterList(object):

    @classmethod
    async def get(cls, filters: Optional[str] = None, related_fields: bool = False) -> ThemeOutListSchema:
        filters_list: Optional[List[Filter]] = None
        if filters:
            filters_list = FilterList.parse_raw(filters).filters
        res = await theme_crud.select(
            response_model=ThemeOutListSchema,
            filters=filters_list,
        )
        return res
