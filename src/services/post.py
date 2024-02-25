from fastapi import HTTPException, status
from sqlalchemy import insert, select
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User

from schemas.post import PostCreateSchema
from models.post import Post


class PostService:
    @staticmethod
    async def create_post(data: PostCreateSchema, session: AsyncSession):
        try:
            post = Post(**data.model_dump())

            session.add(post)
            await session.commit()

            return post
        except Exception as e:
            raise HTTPException(status_code=500, detail={
                'status': 'error',
                'detail': e,
            })
        
    @staticmethod
    async def get_post(id: int, session: AsyncSession):
        stmt = (
            select(Post)
            .options(joinedload(Post.user))
            .filter(Post.id==id)
        )

        result = await session.execute(stmt)
        await session.commit()

        return result.scalars().first()
