from fastapi import HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.user import UserCreateSchema
from models.user import User


class UserService:
    @staticmethod
    async def create_user(data: UserCreateSchema, session: AsyncSession):
        try:
            stmt = insert(User).values(**data.__dict__)
            
            await session.execute(stmt)
            await session.commit()
        except Exception as e:
            raise HTTPException(status_code=500, detail={
                'status': 'error',
                'detail': e,
            })
        
    @staticmethod
    async def get_user(id: int, session: AsyncSession):
        try:
            stmt = select(User).filter(User.id==id)

            result = await session.execute(stmt)
            await session.commit()

            return result.scalars().one()
        except Exception as e:
            raise HTTPException(status_code=500, detail={
                'status': 'error',
                'detail': e,
            })
