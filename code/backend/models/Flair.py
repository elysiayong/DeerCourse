from sqlalchemy import Column, Integer, String

from backend.database import Base


class Flair(Base):
    __tablename__ = 'flairs'
    flair_id = Column(Integer, primary_key=True)
    text = Column(String)
