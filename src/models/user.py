from datetime import datetime
from sqlalchemy import String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base

from .post import Post


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(30), unique=True, index=True)
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow)

    posts: Mapped[list['Post']] = relationship(back_populates='user')
