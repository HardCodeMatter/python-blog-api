from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

from .post import PostWithoutUserSchema


class UserSchema(BaseModel):
    id: int
    username: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserCreateSchema(BaseModel):
    username: str = Field(max_length=30)

    model_config = ConfigDict(
        from_attributes=True
    )


class UserWithPostSchema(BaseModel):
    id: int
    username: str
    created_at: datetime
    updated_at: datetime

    posts: list["PostWithoutUserSchema"] | None = []

    model_config = ConfigDict(from_attributes=True)
