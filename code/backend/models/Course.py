from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import relationship

from code.backend.database import Base

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
