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

    name: str = Field(description="Название события")
    description: str = Field(default="", description="Описание события")
    city: str = Field(description="Город в котором проводится событие")
    start_time: datetime = Field(default_factory=datetime.utcnow, description="Время начала события")
    finish_time: datetime = Field(default_factory=datetime.utcnow, description="Время окончания события")
    related_data: List = Field(default=[], description="Связанные темы")


class EventSchema(EventBaseSchema):
    id: int = Field(description="Идентификатор объекта")

class EventsOutListSchema(BaseModel):
    data: List[EventSchema]
