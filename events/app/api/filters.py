from fastapi import APIRouter
from events.app.models.pydantic.filters import (
    FiltersSchema,
    FiltersOutListSchema,
    FiltersPatchSchema,
    FiltersPostSchema,
)
from typing import Optional
from events.app.crud.event import filter_crud
from core.models.pydantic.json_api.filters import Filter, FilterList
from core.models.enums.filters import JsonAPIFiltersOperators

router: APIRouter = APIRouter()


class FiltersRouter(object):
    @classmethod
    async def get(cls, obj_id: int, related_fields: bool = False) -> FiltersSchema:
        try:
            res = await filter_crud.select(
                response_model=FiltersSchema,
                filters=[Filter(name="id", op=JsonAPIFiltersOperators.eq, val=obj_id)],
            )
        except Exception:
            raise
        return res

    @classmethod
    async def patch(cls, obj_id, filter: FiltersPatchSchema) -> FiltersSchema:
        res = await filter_crud.update(
            response_model=FiltersSchema,
            updating_data=filter,
            filters=[Filter(name="id", op=JsonAPIFiltersOperators.eq, val=obj_id)]
        )
        return res

    @classmethod
    async def post(cls, filter: FiltersPostSchema) -> FiltersOutListSchema:
        return await filter_crud.insert(filter)


class FiltersRouterList(object):

    @classmethod
    async def get(cls, filters: Optional[str] = None, related_fields: bool = False) -> FiltersOutListSchema:
        if filters:
            filters = FilterList.parse_raw(filters).filters
        res = await filter_crud.select(
            response_model=FiltersOutListSchema,
            filters=filters,
        )
        return res
