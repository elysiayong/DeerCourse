from sqlalchemy import Column, Integer, String

from backend.database import Base


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    text = Column(String)
