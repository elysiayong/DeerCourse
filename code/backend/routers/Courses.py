from typing import List

from fastapi import Depends, APIRouter, HTTPException, Path, Query
from sqlalchemy.orm import Session

from code.backend import schemas, crud
from code.backend.dependencies import get_db

router = APIRouter(prefix="/courses",
                   tags=['courses']
                   )


@router.get("/",
            summary='Get all courses',
            response_model=List[schemas.Course])
def get_all_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    raise HTTPException(status_code=400, detail="Not implemented")


@router.get("/{course_code}",
            summary='Get a single course',
            response_model=schemas.CourseExtra)
def get_course(course_code: str = Path(..., description="Course code to fetch"),
               include_extra: bool = Query(False,
                                           description="Whether the result should contain pre/corequisites and "
                                                       "exclusions"),
               db: Session = Depends(get_db)):
    raise HTTPException(status_code=400, detail="Not implemented")
