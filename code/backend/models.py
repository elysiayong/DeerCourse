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
    course = Column(String, ForeignKey("courses.name"))
    user_rating = Column(Integer)
    # uncomment when Tag is implemented
    # tag_id = Column(Integer, ForeignKey("tag.id"))
    # tags = relationship("Tag")


# Association tables for many-to-many
prerequisite_association = Table('prerequisites', Base.metadata,
                                 Column('course_name', String, ForeignKey('courses.name')),
                                 Column('prerequisite_name', String, ForeignKey('courses.name'))
                                 )

exclusion_association = Table('exclusions', Base.metadata,
                              Column('course_name', String, ForeignKey('courses.name')),
                              Column('exclusion_name', String, ForeignKey('courses.name'))
                              )

corequisite_association = Table('corequisites', Base.metadata,
                                Column('course_name', String, ForeignKey('courses.name')),
                                Column('corequisite_name', String, ForeignKey('courses.name'))
                                )


# Complicated self-referential many-to-many below:
# https://blog.ramosly.com/sqlalchemy-orm-setting-up-self-referential-many-to-many-relationships-866c97d9308b
class Course(Base):
    __tablename__ = 'courses'
    name = Column(String, unique=True, primary_key=True)
    description = Column(String)
    prerequisites = relationship("Course",
                                 secondary=prerequisite_association,
                                 primaryjoin=prerequisite_association.c.course_name == name,
                                 secondaryjoin=prerequisite_association.c.prerequisite_name == name)
    corequisites = relationship("Course",
                                secondary=corequisite_association,
                                primaryjoin=corequisite_association.c.course_name == name,
                                secondaryjoin=corequisite_association.c.corequisite_name == name)
    exclusions = relationship("Course",
                              secondary=exclusion_association,
                              primaryjoin=exclusion_association.c.course_name == name,
                              secondaryjoin=exclusion_association.c.exclusion_name == name)
    program_name = Column(String, ForeignKey('programs.name'))
    program = relationship('Program', back_populates='courses')

    def __repr__(self):
        return f"<Course: {self.name}>"


class Program(Base):
    __tablename__ = 'programs'
    name = Column(String, unique=True, primary_key=True)
    description = Column(String)
    courses = relationship('Course', back_populates='program')
