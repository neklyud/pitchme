from pydantic import (
    BaseModel,
    Field,
)
from datetime import datetime
from typing import (
    List,
    Optional,
)


class EventBaseSchema(BaseModel):
    class Config:
        orm_mode = True


class EventPatchSchema(EventBaseSchema):
    name: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None, description="Описание события")
    city: Optional[str] = Field(default=None, description="Город в котором проводится событие")
    start_time: Optional[datetime] = Field(default=None, description="Время начала события")
    end_time: Optional[datetime] = Field(default=None, description="Время окончания события")


class EventPostSchema(EventBaseSchema):
    name: str = Field(description="Название события")
    description: str = Field(default="", description="Описание события")
    city: str = Field(description="Город в котором проводится событие")
    start_time: datetime = Field(default_factory=datetime.utcnow, description="Время начала события")
    end_time: datetime = Field(default_factory=datetime.utcnow, description="Время окончания события")
    related_data: Optional[List] = Field(default=None, description="Связанные темы")


class EventSchema(EventPostSchema):
    id: int = Field(description="Идентификатор объекта")


class EventsOutListSchema(BaseModel):
    data: List[EventSchema]
