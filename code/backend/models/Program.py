from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from code.backend.database import Base


class Program(Base):
    __tablename__ = 'programs'
    name = Column(String, unique=True, primary_key=True)
    description = Column(String)
    courses = relationship('Course', back_populates='program')
