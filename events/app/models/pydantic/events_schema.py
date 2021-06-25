from pydantic import (
    BaseModel,
    Field,
)
from typing import (
    List,
    Optional,
)


class EventsThemesBaseSchema(BaseModel):
    class Config:
        orm_mode = True


class EventsThemesPatchSchema(EventsThemesBaseSchema):
    event_id: Optional[int] = Field(default=None)
    theme_id: Optional[int] = Field(default=None)


class EventsThemesPostSchema(EventsThemesBaseSchema):
    event_id: int = Field(description="Ид события")
    theme_id: int = Field(description="Ид темы")


class EventsThemesSchema(EventsThemesPostSchema):
    id: int = Field(description="Идентификатор объекта")
    related_data: Optional[List] = Field(default=None, description="Связанные темы")


class EventsThemesOutListSchema(BaseModel):
    data: List[EventsThemesSchema]
