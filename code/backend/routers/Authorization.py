from typing import List

from fastapi import Depends, APIRouter, HTTPException, Form
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel

from code.backend import schemas, crud
from code.backend.dependencies import get_db, get_current_user

router = APIRouter(prefix="/auth",
                   tags=['auth']
                   )


class TokenData(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post('/',
             response_model=TokenData,
             summary="Get user token")
def auth(username: str = Form(...), password: str = Form(...), db=Depends(get_db)):
    """
    Get an authentication token for user with email ***username*** and password ***password***\n
    That token can be used with later calls that require authentication\n
    Note that the request is not a JSON body, but is an HTML form data, as per OAuth2 standards
    """
    user = crud.get_user_by_email(db, username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not crud.verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": "name", "token_type": "bearer"}
