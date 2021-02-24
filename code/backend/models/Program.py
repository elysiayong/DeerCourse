from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from backend.database import Base


class Program(Base):
    __tablename__ = 'programs'
    code = Column(String, unique=True, primary_key=True)
    name = Column(String)
    description = Column(String)
    courses = relationship('Course', back_populates='program')
