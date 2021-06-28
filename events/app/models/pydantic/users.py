from pydantic import (
    BaseModel,
    Field,
)
from typing import (
    List,
    Optional,
)
from datetime import datetime


class UsersBaseSchema(BaseModel):
    class Config:
        orm_mode = True


class UsersPatchSchema(UsersBaseSchema):
    name: Optional[str] = Field(default=None, description="Имя пользователя")
    email: Optional[str] = Field(default=None, description="Почта")
    password_hash: Optional[str] = Field(default=None, description="Хэш паспорта")
    access_token: Optional[str] = Field(default=None, description="Токен")
    expires_at: Optional[str] = Field(default=None, description="Время истечения токенов")


class UsersPostSchema(UsersBaseSchema):
    name: str = Field(description="Название события")
    email: str = Field(description="Почта")
    password_hash: str = Field(description="Хэш паспорта")
    access_token: Optional[str] = Field(default=None, description="Токен")
    expires_at: Optional[datetime] = Field(default=None, description="Время истечения токена")


class UsersSchema(UsersPostSchema):
    id: int = Field(description="Идентификатор объекта")


class UsersOutListSchema(BaseModel):
    data: List[UsersSchema]
