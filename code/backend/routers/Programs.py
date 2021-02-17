from typing import List

from fastapi import Depends, APIRouter, HTTPException, Path
from sqlalchemy.orm import Session

from code.backend import schemas, crud
from code.backend.dependencies import get_db

router = APIRouter(prefix="/programs",
                   tags=['programs']
                   )


@router.get("/",
            summary='Get all programs',
            response_model=List[schemas.Program])
def create_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    raise HTTPException(status_code=400, detail="Not implemented")


@router.get("/{program_code}",
            summary='Get a single program',
            response_model=schemas.Program)
def create_user(program_code: str = Path(..., description="Program code to fetch"), db: Session = Depends(get_db)):
    raise HTTPException(status_code=400, detail="Not implemented")


@router.get("/{program_code}/courses",
            summary='Get all courses for a program',
            response_model=List[schemas.Course],
            tags=['courses'])
def create_user(program_code: str = Path(..., description="Program code to fetch courses for"), db: Session = Depends(get_db)):
    raise HTTPException(status_code=400, detail="Not implemented")
