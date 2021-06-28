from fastapi import APIRouter
from events.app.models.pydantic.users import (
    UsersSchema,
    UsersOutListSchema,
    UsersPatchSchema,
    UsersPostSchema,
)
from typing import Optional, List
from events.app.crud.event import users_crud
from core.models.pydantic.json_api.filters import Filter, FilterList
from core.models.enums.filters import JsonAPIFiltersOperators

router: APIRouter = APIRouter()


class UsersRouter(object):
    @classmethod
    async def get(cls, obj_id: int, related_fields: bool = False) -> UsersSchema:
        try:
            res = await users_crud.select(
                response_model=UsersSchema,
                filters=[Filter(name="id", op=JsonAPIFiltersOperators.eq, val=obj_id)],
            )
        except Exception:
            raise
        return res

    @classmethod
    async def patch(cls, obj_id, users: UsersPatchSchema) -> UsersSchema:
        res = await users_crud.update(
            response_model=UsersSchema,
            updating_data=users,
            filters=[Filter(name="id", op=JsonAPIFiltersOperators.eq, val=obj_id)]
        )
        return res

    @classmethod
    async def post(cls, users: UsersPostSchema) -> UsersOutListSchema:
        return await users_crud.insert(users)


class UsersRouterList(object):

    @classmethod
    async def get(cls, filters: Optional[str] = None, related_fields: bool = False) -> UsersOutListSchema:
        filters_list: Optional[List[Filter]] = None
        if filters:
            filters_list = FilterList.parse_raw(filters).filters
        res = await users_crud.select(
            response_model=UsersOutListSchema,
            filters=filters_list,
        )
        return res
