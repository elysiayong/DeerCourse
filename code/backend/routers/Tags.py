from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from backend import schemas, crud
from backend.dependencies import get_db

router = APIRouter(prefix="/tags",
                   tags=['tags'])


@router.get("",
            summary="Get all tags",
            response_model=schemas.Tags)
def get_tags(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_tags(db, skip, limit)


@router.get("/{tag_id}",
            summary="Get a tag by id",
            response_model=schemas.Tag)
def get_tag_by_id(tag_id: int, db: Session = Depends(get_db)):
    tag = crud.get_tag_by_id(db, tag_id)
    if not tag:
        raise HTTPException(404, "Tag not found")
    return tag
