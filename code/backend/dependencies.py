from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from code.backend.database import SessionLocal
from code.backend.schemas import User


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def fake_decode_token(token):
    return User(
        email=token+"@example.com"
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user
