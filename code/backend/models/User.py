from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from backend.database import Base


class User(Base):
    __tablename__ = 'users'
    email = Column(String, unique=True, primary_key=True)
    password_hash = Column(String)
    flair_id = Column(Integer, ForeignKey("flairs.flair_id"))
    flair = relationship("Flair")
    reviews = relationship("Review", back_populates="user")
