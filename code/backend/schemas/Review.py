from .Course import Course
from .ORM import ORMBaseSchema
from .User import User


class Review(ORMBaseSchema):
    review_id: int
    content: str
    user: User
    course: Course
    user_rating: int

    # tags: List[Tag]
