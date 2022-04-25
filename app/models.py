from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.dialects.sqlite import TEXT

from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(TEXT, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String)
    email = Column(String)

    def __repr__(self) -> str:
        return f'ModelUser({self.name})'
