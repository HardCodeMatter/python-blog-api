from pydantic import BaseModel, Field, ConfigDict


class UserSchema(BaseModel):
    id: int
    username: str

    model_config = ConfigDict(
        from_attributes=True
    )



class UserCreateSchema(BaseModel):
    username: str = Field(max_length=30)

    model_config = ConfigDict(
        from_attributes=True
    )
