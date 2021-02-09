from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
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

prerequisite_association = Table('Prerequisites', Base.metadata,
    Column('course', String, ForeignKey('courses.name')),
    Column('prerequisite', String, ForeignKey('courses.name'))
)

exclusion_association = Table('Exclusions', Base.metadata,
    Column('course', String, ForeignKey('courses.name')),
    Column('exclusion', String, ForeignKey('courses.name'))
)

corerequisite_association = Table('Corerequisites', Base.metadata,
    Column('course', String, ForeignKey('courses.name')),
    Column('corerequisite', String, ForeignKey('courses.name'))
)
class Course(Base):
    __tablename__ = 'courses'
    name = Column(String, unique=True, primary_key=True)
    description = Column(String)
    prerequisites = relationship("Prerequisite", secondary=prerequisite_association)
    exclusions = relationship("Exclusion", secondary=exclusion_association)
    corerequisites = relationship("Corerequisite", secondary=corerequisite_association)

class Program(Base):
    __tablename__ = 'programs'
    name = Column(String, unique=True, primary_key=True)
    description = Column(String)