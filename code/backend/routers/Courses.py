from typing import List

from fastapi import Depends, APIRouter, HTTPException, Path, Query
from sqlalchemy.orm import Session

from backend import schemas, crud
from backend.dependencies import get_db, get_current_user

router = APIRouter(prefix="/courses",
                   tags=['courses']
                   )


@router.get("",
            summary='Get all courses',
            response_model=schemas.Courses)
def get_all_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses


@router.get("/{course_code}",
            summary='Get a single course',
            response_model=schemas.Course)
def get_course(course_code: str = Path(..., description="Course code to fetch"),
               db: Session = Depends(get_db)):
    course: schemas.Course = crud.get_course_by_code(db, code=course_code)
    if not course:
        raise HTTPException(status_code=404, detail="Course does not exist")
    return course


@router.post("/search",
            summary='Get all courses approximate to matching strings and filters',
            response_model=schemas.Courses
            )
def get_courses_matching(search: schemas.CourseSearch, limit: int = 20, db: Session = Depends(get_db)):
    courses = crud.get_courses_match(db, search=search, limit=limit)
    if not courses:
        raise HTTPException(status_code=404, detail="Courses do not exist")
    return courses
