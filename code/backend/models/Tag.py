from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from backend.database import Base
from backend.models.Review import review_tags


class Tag(Base):
    __tablename__ = 'tags'
    tag_id = Column(Integer, primary_key=True)
    text = Column(String, unique=True)
    reviews = relationship("Review",
                           secondary=review_tags,
                           back_populates="tags")
