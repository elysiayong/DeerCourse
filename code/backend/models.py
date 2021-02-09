from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = 'users'
    email = Column(String, unique=True, primary_key=True)
    password_hash = Column(String)
    # Uncomment when flairs are implemented
    # flair_id = Column(Integer, ForeignKey("flairs.id"))
    # flair = relationship("Flair", uselist=False)

class Review(Base):
    __tablename__ = 'reviews'
    review_id = Column(Integer, unique=True, primary_key=True)
    content = Column(String)
    user = Column(String, ForeignKey("users.email"))
    # course = Column(String, ForeignKey("course.name"))
    user_rating = Column(Integer)
    # uncomment when Tag is implemented
    # tag_id = Column(Integer, ForeignKey("tag.id"))
    # tags = relationship("Tag")
