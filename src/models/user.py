from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base

from .post import Post


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, index=True)

    posts: Mapped[list[Post]] = relationship(back_populates='user')
