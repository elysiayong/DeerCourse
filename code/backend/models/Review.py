from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from backend.database import Base

review_tags = Table('review_tags', Base.metadata,
                    Column('review', Integer, ForeignKey('reviews.review_id')),
                    Column('tag', Integer, ForeignKey('tags.tag_id')))


class Review(Base):
    __tablename__ = 'reviews'
    review_id = Column(Integer, unique=True, primary_key=True)
    content = Column(String)
    user_email = Column(String, ForeignKey("users.email"))
    user = relationship("User", back_populates="reviews")
    course_code = Column(String, ForeignKey("courses.code"), nullable=False)
    course = relationship("Course", back_populates="reviews")
    user_rating = Column(Integer)
    tags = relationship("Tag",
                        secondary=review_tags,
                        back_populates="reviews")