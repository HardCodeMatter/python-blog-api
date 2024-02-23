from pydantic import BaseModel, ConfigDict

from .user import UserSchema


class PostSchema(BaseModel):
    id: int
    title: str
    content: str

    user: 'UserSchema'

    model_config = ConfigDict(
        from_attributes=True
    )


class PostCreateSchema(BaseModel):
    title: str
    content: str

    user_id: int

    model_config = ConfigDict(
        from_attributes=True
    )