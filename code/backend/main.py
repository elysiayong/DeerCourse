import uvicorn
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

from code.backend import models
from code.backend.database import engine
from code.backend.routers import Users, Courses, Programs, Authorization

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(Authorization.router)
app.include_router(Users.router)
app.include_router(Courses.router)
app.include_router(Programs.router)

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8080, reload=True)
