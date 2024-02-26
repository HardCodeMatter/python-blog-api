from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.post import PostCreateSchema
from models.post import Post

from utils.firestore import firestore_client


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
        post = result.scalars().first()
        
        if post:
            try:
                firebase_content = await firestore_client.get_document_by_id('content', post.content)

                if firebase_content:
                    post.content = firebase_content
            except Exception as e:
                print(f'Error fetching content from Firestore Database: {e}')

        await session.commit()

        return post
