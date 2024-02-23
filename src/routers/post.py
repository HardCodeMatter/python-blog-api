from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.database import get_async_session
from schemas.post import PostCreateSchema, PostSchema
from services.post import PostService


router = APIRouter(
    prefix='/posts',
    tags=['Post'],
)


@router.post('/', response_model=PostCreateSchema)
async def create_post(
    data: PostCreateSchema,
    session: AsyncSession = Depends(get_async_session)
):
    return await PostService.create_post(data, session)


@router.get('/{id}', response_model=PostSchema)
async def get_post(
    id: int,
    session: AsyncSession = Depends(get_async_session)
):
    return await PostService.get_post(id, session)
