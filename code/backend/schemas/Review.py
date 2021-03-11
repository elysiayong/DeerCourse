from typing import List, Optional

from pydantic import create_model

from .Course import Course
from .ORM import ORMBaseSchema
from .User import User
from .Tag import Tag


class Review(ORMBaseSchema):
    review_id: int
    content: str
    course: Course
    user_rating: int
    tags: List[Tag]

class ReviewCreate(ORMBaseSchema):
    content: str
    course_code: str
    user_rating: int
    tag_ids: List[int] = []

"""
ReviewUpdate schema is created dynamically from all fields (except from course_code) present in ReviewCreate,
but with all fields optional. Any change in ReviewCreate will be reflected in ReviewUpdate
"""
update_fields = {}
for field in ReviewCreate.__fields__.values():
    if field.name != "course_code":
        update_fields[field.name] = (Optional[field.outer_type_], None)


ReviewUpdate = create_model(
    "ReviewUpdate",
    **update_fields
)
