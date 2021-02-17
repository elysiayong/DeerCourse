from datetime import timedelta

from fastapi import Depends, APIRouter, HTTPException, Form, status

from code.backend import crud, schemas
from code.backend.dependencies import get_db
from code.backend.options import ACCESS_TOKEN_EXPIRE_MINUTES
from code.backend.schemas.Token import Token

router = APIRouter(prefix="/auth",
                   tags=['auth']
                   )


@router.post('',
             response_model=Token,
             summary="Get user token")
def auth(username: str = Form(...), password: str = Form(...), db=Depends(get_db)):
    """
    Get an authentication token for user with email ***username*** and password ***password***\n
    That token can be used with later calls that require authentication\n
    Note that the request is not a JSON body, but is an HTML form data, as per OAuth2 standards
    """
    user = crud.authenticate_user(db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
