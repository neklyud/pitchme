from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.pydantic.json_api.filters import Filter
from typing import Optional


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


class BaseCrud(object):
    async def select(self, response_model, filters: Optional[Filter] = None):
        raise Exception

    async def insert(self, new_item):
        raise Exception

    async def update(self, response_model, updating_data, filters: Optional[Filter] = None):
        raise Exception

    async def delete(self):
        ...

    def to_schema(self, model, schema):
        return schema.from_orm(model)
