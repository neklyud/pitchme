from pydantic import (
    BaseModel,
    Field,
)
from typing import (
    List,
    Optional,
)


class FiltersBaseSchema(BaseModel):
    class Config:
        orm_mode = True


class FiltersPatchSchema(FiltersBaseSchema):
    name: Optional[str] = Field(default=None, description="Название фильтра")
    filter_body: Optional[str] = Field(default=None, description="Тело фильтра")


class FiltersPostSchema(FiltersBaseSchema):
    name: str = Field(description="Название события")
    filter_body: str = Field(description="Почта")
    user_id: int = Field(description="Хэш паспорта")


class FiltersSchema(FiltersPostSchema):
    id: int = Field(description="Идентификатор объекта")


class FiltersOutListSchema(BaseModel):
    data: List[FiltersSchema]
