from pydantic import (
    BaseModel,
    Field,
)
from typing import (
    List,
    Optional,
)


class ThemeBaseSchema(BaseModel):
    class Config:
        orm_mode = True


class ThemePatchSchema(ThemeBaseSchema):
    name: Optional[str] = Field(default=None)


class ThemePostSchema(ThemeBaseSchema):
    name: str = Field(description="Название события")


class ThemeSchema(ThemePostSchema):
    id: int = Field(description="Идентификатор объекта")
    related_data: Optional[List] = Field(default=None, description="Связанные темы")


class ThemeOutListSchema(BaseModel):
    data: List[ThemeSchema]
