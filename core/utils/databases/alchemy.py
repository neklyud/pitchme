from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.pydantic.json_api.filters import Filter
from typing import Optional
from sqlalchemy import (
    select,
    update,
    delete,
    insert,
)
from typing import List

from core.utils.filters.filter_converter import filter_converter

class AlchemyHelper(object):
    def __init__(self, config):
        self._config = config
        self._engine = create_async_engine(self._config.SQLALCHEMY_DATABASE_URI, echo=True)
        self._session = sessionmaker(bind=self.engine, class_=AsyncSession)

    @property
    def session(self):
        return self._session

    @property
    def engine(self):
        return self._engine


Base = declarative_base()


class Crud(object):
    def __init__(self, model, session_maker: AlchemyHelper, response_schema, response_list_schema):
        self.model = model
        self.session = session_maker.session
        self.response_schema = response_schema
        self.response_list_schema = response_list_schema

    async def select(self, response_model, filters: Optional[List[Filter]] = None):
        async with self.session() as session:
            selection = select(self.model)
            if filters:
                selection = filter_converter(filters, selection)
            result = await session.execute(selection)
            data = []
            for row in result.scalars():
                data.append(self.to_schema(row, self.response_schema))
        if response_model is self.response_schema and data:
            return data[0]
        if response_model is self.response_list_schema:
            return self.response_list_schema(data=data)
        raise Exception("Object not found")

    async def insert(self, new_item):
        new_event = None
        async with self.session() as session:
            insert_query = insert(self.model).returning(
                *self.model.__table__.columns
            ).values(**new_item.dict(exclude_unset=True))
            res = await session.execute(insert_query)
            for i_scalar in res.fetchall():
                new_event = self.response_schema.from_orm(i_scalar)
            await session.commit()
        return new_event

    async def update(self, response_model, updating_data, filters: Optional[List[Filter]] = None):
        async with self.session() as session:
            query = update(self.model)
            if filters:
                query = filter_converter(filters, query)
            query = query.values(**updating_data.dict(exclude_unset=True))
            query = query.execution_options(synchronize_session=None)
            query = query.returning(*self.model.__table__.columns)
            result = await session.execute(query)
            data = []
            for i_res in result.fetchall():
                print(i_res)
                data.append(self.response_schema.from_orm(i_res))
            await session.commit()
        if response_model is self.response_schema and data:
            return data[0]
        if response_model is self.response_list_schema:
            return self.response_list_schema(data=data)
        raise Exception("Object not updated")

    async def delete(self, filters: Optional[List[Filter]] = None):
        async with self.session() as session:
            query = delete(self.model)
            if filters:
                query = filter_converter(filters, query)
            query = query.execution_options(synchronize_session=None)
            await session.execute(query)
        return True

    def to_schema(self, model, schema):
        return schema.from_orm(model)
