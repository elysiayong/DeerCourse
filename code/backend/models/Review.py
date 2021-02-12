from sqlalchemy import Column, ForeignKey, Integer, String

from code.backend.database import Base


class Review(Base):
    __tablename__ = 'reviews'
    review_id = Column(Integer, unique=True, primary_key=True)
    content = Column(String)
    user = Column(String, ForeignKey("users.email"))
    course = Column(String, ForeignKey("courses.name"))
    user_rating = Column(Integer)
    # uncomment when Tag is implemented
    # tag_id = Column(Integer, ForeignKey("tag.id"))
    # tags = relationship("Tag")
