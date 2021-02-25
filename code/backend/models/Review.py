from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.database import Base


class Review(Base):
    __tablename__ = 'reviews'
    review_id = Column(Integer, unique=True, primary_key=True)
    content = Column(String)
    user = Column(String, ForeignKey("users.email"))
    course = Column(String, ForeignKey("courses.name"))
    user_rating = Column(Integer)
    tag_id = Column(Integer, ForeignKey("tags.id"))
    tag = relationship("Tag")
