from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_async_session
from schemas.user import UserSchema, UserCreateSchema, UserWithPostSchema
from services.user import UserService


router = APIRouter(
    prefix='/users',
    tags=['User'],
)


@router.post('/', response_model=UserSchema)
async def create_user(
    data: UserCreateSchema,
    session: AsyncSession = Depends(get_async_session)
):
    return await UserService().create_user(data, session)


@router.get('/{id}', response_model=UserWithPostSchema)
async def get_user(
    id: int = None,
    session: AsyncSession = Depends(get_async_session)
):
    response = await UserService().get_user(id, session)
    return response
