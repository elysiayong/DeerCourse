from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from backend.database import Base
from backend.models.Course import program_association


class Program(Base):
    __tablename__ = 'programs'
    code = Column(String, unique=True, primary_key=True)
    name = Column(String)
    courses = relationship('Course',
                           secondary=program_association,
                           back_populates='programs')
