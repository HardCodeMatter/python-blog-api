from fastapi import HTTPException
from sqlalchemy import insert, select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.user import UserCreateSchema
from models.user import User


class UserService:
    @staticmethod
    async def create_user(data: UserCreateSchema, session: AsyncSession):
        try:
            user = User(**data.model_dump())
            
            session.add(user)
            await session.commit()

            return user
        except Exception as e:
            raise HTTPException(status_code=500, detail={
                'status': 'error',
                'detail': e,
            })
        
    @staticmethod
    async def get_user(id: int, session: AsyncSession):
        try:
            stmt = (
                select(User)
                .options(selectinload(User.posts))
                .filter(User.id==id)
            )

            result = await session.execute(stmt)
            await session.commit()

            return result.scalars().one()
        except Exception as e:
            raise HTTPException(status_code=500, detail={
                'status': 'error',
                'detail': e,
            })
