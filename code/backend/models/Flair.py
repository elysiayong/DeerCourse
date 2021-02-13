from sqlalchemy import Column, Integer, String

from code.backend.database import Base


class Flair(Base):
    __tablename__ = 'flairs'
    id = Column(Integer, primary_key=True)
    text = Column(String)
