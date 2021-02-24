from typing import List

from fastapi import Depends, APIRouter, HTTPException, Path, Query
from sqlalchemy.orm import Session

from backend import schemas, crud
from backend.dependencies import get_db

router = APIRouter(prefix="/courses",
                   tags=['courses']
                   )

@router.post("/{course_code}",
            summary='Create a course',
            response_model=schemas.CourseCreate,
             deprecated=True)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.get_course_by_code(db, code=course.code)
    if db_course:
        raise HTTPException(status_code=400, detail="Course already exists")
    return crud.create_course(db=db, course=course)

@router.get("/",
            summary='Get all courses',
            response_model=List[schemas.Course])
def get_all_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses


@router.get("/{course_code}",
            summary='Get a single course',
            response_model=schemas.CourseExtra)
def get_course(course_code: str = Path(..., description="Course code to fetch"),
               include_extra: bool = Query(False,
                                           description="Whether the result should contain pre/corequisites and "
                                                       "exclusions"),
               db: Session = Depends(get_db)):
    course: schemas.CourseExtra = crud.get_course_by_code(db, code=course_code)
    if not course:
        raise HTTPException(status_code=404, detail="Course does not exist")
    if include_extra:
        return course
    # https://pydantic-docs.helpmanual.io/usage/exporting_models/
    return course.dict(exclude={'prerequisites', 'corequisites', 'exclusions'})
