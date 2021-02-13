import uvicorn
from fastapi import FastAPI

from code.backend import models
from code.backend.database import engine
from code.backend.routers import Users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(Users.router)

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8080, reload=True)
