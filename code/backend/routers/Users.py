from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from code.backend import schemas, crud
from code.backend.dependencies import get_db, get_current_user

router = APIRouter(prefix="/users",
                   tags=['users']
                   )


@router.post("/",
             summary='Create a user',
             response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/",
            summary='Fetch all users',
            response_model=List[schemas.User],
            response_model_exclude_none=True)
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/me",
            summary='Fetch current user',
            response_model=schemas.User,
            response_model_exclude_none=True)
def get_me(user=Depends(get_current_user)):
    return user
