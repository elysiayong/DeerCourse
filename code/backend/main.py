import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import sys
import os

# Easier to run as a module this way
script_path = os.path.split(sys.path[0])
if script_path[-1] == 'backend':
    sys.path[0] = script_path[0]

from backend import models
from backend.database import engine
from backend.routers import Users, Courses, Programs, Authorization, Admin, Reviews, Tags
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DeerCourse BE",
    description="Backend for UTM course review website"
)

origins = [
    "http://localhost:3000",
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Authorization.router)
app.include_router(Users.router)
app.include_router(Courses.router)
app.include_router(Programs.router)
app.include_router(Reviews.router)
app.include_router(Tags.router)

# Goes last
app.include_router(Admin.router)


@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8080, reload=True)
