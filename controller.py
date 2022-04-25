from sqlalchemy.future import select
from sqlalchemy.orm import Session

from app import schemas
from app.models import User as ModelUser


async def get_users(db: Session, skip: int = 0, limit: int = 100):
    result = await db.execute(select(ModelUser).order_by(
        ModelUser.email).offset(skip).limit(limit))
    return result.scalars().all()


async def get_user_by_id(db: Session, user_id: str):
    result = await db.execute(select(ModelUser).filter(
        ModelUser.id == user_id))
    return result.scalars().first()
    # return db.query(ModelUser).filter(ModelUser.id == user_id).first()


async def get_user_by_email(db: Session, user_email: str):
    result = await db.execute(select(ModelUser).filter(
        ModelUser.email == user_email))
    return result.scalars().first()
    # return db.query(ModelUser).filter(ModelUser.email == user_email).first()


async def create_user(db: Session, user: schemas.UserIn) -> ModelUser:
    new_user = ModelUser(**user.dict())
    db.add(new_user)
    await db.commit()
    # db.commit()
    # db.refresh(new_user)
    return new_user
