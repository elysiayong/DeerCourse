from typing import List

from fastapi import Depends, APIRouter, HTTPException, Path
from sqlalchemy.orm import Session

from backend import schemas, crud
from backend.dependencies import get_db

router = APIRouter(prefix="/admin",
                   tags=['admin']
                   )

# end points for creating programs
@router.post("/programs/{program_code}",
            summary='Create a program',
            response_model=schemas.Program)
def create_program(program: schemas.Program, db: Session = Depends(get_db)):
    db_program = crud.get_program_by_code(db, code=program.code)
    if db_program:
        raise HTTPException(status_code=400, detail="Program already exists")
    return crud.create_program(db=db, program=program)

# end points for creating courses 
@router.post("/courses/{course_code}",
            summary='Create a course',
            response_model=schemas.CourseCreate)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.get_course_by_code(db, code=course.code)
    if db_course:
        raise HTTPException(status_code=400, detail="Course already exists")
    return crud.create_course(db=db, course=course)