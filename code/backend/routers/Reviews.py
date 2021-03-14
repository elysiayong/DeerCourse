from typing import List

from fastapi import Depends, APIRouter, HTTPException, Path, Query
from sqlalchemy.orm import Session

from backend import schemas, crud
from backend.dependencies import get_db, get_current_user

router = APIRouter(prefix="/reviews",
                   tags=['reviews']
                   )

@router.get("/for/{course_code}",
            summary='Get reviews for a course',
            response_model=List[schemas.Review])
def get_reviews_by_course_code(course_code: str = Path(..., description="Course code to fetch"),
               db: Session = Depends(get_db)):
    course = crud.get_course_by_code(db, course_code)
    if not course:
        raise HTTPException(status_code=404, detail="Course does not exist")
    reviews = crud.get_reviews_by_code(db, course_code)
    return reviews

@router.get("/me",
            summary='Get reviews for the current user',
            response_model=List[schemas.Review])
def get_reviews_by_me(user=Depends(get_current_user), db: Session = Depends(get_db)):
    reviews = crud.get_reviews_by_me(db, user)
    return reviews

@router.get("/{review_id}",
            summary='Get the review corresponding to the review id',
            response_model=schemas.Review)
def get_review_by_id(review_id: int = Path(..., description="Review id to fetch"),
                db: Session = Depends(get_db)):
    review = crud.get_review_by_id(db, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review does not exist")
    return review

@router.put("",
            summary='Create a review',
            response_model=schemas.Review)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db),
                    user=Depends(get_current_user)):
    course = crud.get_course_by_code(db, review.course_code)
    if not course:
        raise HTTPException(status_code=404, detail="Course does not exist")
    for tag_id in review.tag_ids:
        if not crud.get_tag_by_id(db, tag_id):
            raise HTTPException(status_code=404, detail="Tag id does not exist")
    return crud.create_review(db=db, review=review, user=user)

@router.post("/{review_id}",
            summary='Update a review',
            response_model=schemas.Review)
def update_review(review: schemas.ReviewUpdate, review_id: int, 
                    db: Session = Depends(get_db), user=Depends(get_current_user)):
    old_review = crud.get_review_by_id(db, review_id)
    if not old_review:
        raise HTTPException(404, "Review not found")
    if old_review.user_email != user.email:
        raise HTTPException(403, "Cannot access another user's review")
    if review.tag_ids is not None:
        for tag_id in review.tag_ids:
            if not crud.get_tag_by_id(db, tag_id):
                raise HTTPException(status_code=404, detail="Tag id does not exist")
    return crud.update_review(db=db, review=review, review_id = review_id, user=user)

@router.delete("/{review_id}",
                summary="Delete a review",
                response_model=schemas.Review)
def delete_review(review_id: int, db: Session = Depends(get_db), 
                    user=Depends(get_current_user)):
    review = crud.get_review_by_id(db, review_id)
    if not review:
        raise HTTPException(404, "Review not found")
    if review.user_email != user.email:
        raise HTTPException(403, "Cannot access another user's review")
    response = schemas.Review.from_orm(review)
    crud.delete_review(db=db, review=review)
    return response

