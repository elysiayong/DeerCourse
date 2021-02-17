from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from code.backend.database import Base


class User(Base):
    __tablename__ = 'users'
    email = Column(String, unique=True, primary_key=True)
    password_hash = Column(String)
    flair_id = Column(Integer, ForeignKey("flairs.id"))
    flair = relationship("Flair")
