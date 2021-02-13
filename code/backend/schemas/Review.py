from .Course import Course
from .ORM import ORMBaseModel
from .User import User


class Review(ORMBaseModel):
    review_id: int
    content: str
    user: User
    course: Course
    user_rating: int

    # tags: List[Tag]
