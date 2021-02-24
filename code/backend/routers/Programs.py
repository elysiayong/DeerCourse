from typing import List

from fastapi import Depends, APIRouter, HTTPException, Path
from sqlalchemy.orm import Session

from backend import schemas, crud
from backend.dependencies import get_db

router = APIRouter(prefix="/programs",
                   tags=['programs']
                   )


@router.post("/{program_code}",
            summary='Create a program',
            response_model=schemas.Program,
             deprecated=True)
def create_program(program: schemas.Program, db: Session = Depends(get_db)):
    db_program = crud.get_program_by_code(db, code=program.code)
    if db_program:
        raise HTTPException(status_code=400, detail="Program already exists")
    return crud.create_program(db=db, program=program)

@router.get("/",
            summary='Get all programs',
            response_model=List[schemas.Program])
def get_all_programs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    programs = crud.get_program(db, skip=skip, limit=limit)
    return programs


@router.get("/{program_code}",
            summary='Get a single program by program code',
            response_model=schemas.Program)
def get_program_by_code(program_code: str = Path(..., description="Program code to fetch"), db: Session = Depends(get_db)):
    program = crud.get_program_by_code(db, program_code)
    if not program:
        raise HTTPException(status_code=404, detail="Program does not exist")
    return program


@router.get("/{program_code}/courses",
            summary='Get all courses for a program',
            response_model=List[schemas.Course],
            tags=['courses'])
def get_courses_by_program_code(program_code: str = Path(..., description="Program code to fetch courses for"),
                db: Session = Depends(get_db)):
    program = crud.get_program_by_code(db, program_code)
    if not program:
        raise HTTPException(status_code=404, detail="Program does not exist")
    courses = crud.get_courses_by_program_code(db, program_code)
    return courses
