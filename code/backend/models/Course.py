from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import relationship

from backend.database import Base

# Course's co/prerequisites/exclusions are represented via a self-referential many-to-many
# It's complicated, explanation below
# https://blog.ramosly.com/sqlalchemy-orm-setting-up-self-referential-many-to-many-relationships-866c97d9308b


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


class Course(Base):
    __tablename__ = 'courses'
    code = Column(String, unique=True, primary_key=True)
    name = Column(String)
    description = Column(String)
    prerequisites = Column(String)
    corequisites = Column(String)
    exclusions = Column(String)
    program_code = Column(String, ForeignKey('programs.code'))
    program = relationship('Program', back_populates='courses')

    def __repr__(self):
        return f"<Course: {self.name}>"