from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_async_session
from schemas.user import UserCreateSchema
from services.user import UserService


router = APIRouter(
    prefix='/users',
    tags=['User'],
)


@router.post('/')
async def create_user(
    data: UserCreateSchema = None,
    session: AsyncSession = Depends(get_async_session)
):
    response = await UserService().create_user(data, session)
    return response


@router.get('/{id}')
async def get_user(
    id: int = None,
    session: AsyncSession = Depends(get_async_session)
):
    response = await UserService().get_user(id, session)
    return response
