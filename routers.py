from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import controller
from app.database import get_session
from app.schemas import User, UserIn

router = APIRouter()


@router.get('/users', response_model=list[User])
async def list_all_users(skip: int = 0, limit: int = 100,
                         db: Session = Depends(get_session)):
    '''
    List all users.
    '''
    return await controller.get_users(db=db, skip=skip, limit=limit)


@router.post('/user', response_model=User)
async def create_user(new_user: UserIn, db: Session = Depends(get_session)):
    '''
    Create new user.
    '''
    user = await controller.get_user_by_email(db, new_user.email)
    if user:
        raise HTTPException(
            status_code=400, detail='Email already registered.')
    return await controller.create_user(db, new_user)


@router.get('/user/email/{email}', response_model=User)
async def find_user_by_email(email, db: Session = Depends(get_session)):
    '''
    Find user by email.
    '''
    return await controller.get_user_by_email(db, email)


@router.get('/user/id/{id}', response_model=User)
async def find_user_by_id(id, db: Session = Depends(get_session)):
    '''
    Find user by id.
    '''
    return await controller.get_user_by_id(db, id)
