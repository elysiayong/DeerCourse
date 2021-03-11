from typing import List, Set, Optional
from enum import Enum

from pydantic import create_model

from .ORM import ORMBaseSchema
from .Program import Program


class CourseLevel(Enum):
    """
    String, acceptable values: '000', '100', '200', '300', '400'
    """
    intro = "000"
    one_hundred = "100"
    two_hundred = "200"
    three_hundred = "300"
    four_hundred = "400"

class CourseDuration(Enum):
    """
    String, acceptable values: 'H', 'Y'
    """
    half_year = "H"
    full_year = "Y"


class CourseBase(ORMBaseSchema):
    code: str
    name: str
    level: CourseLevel
    duration: CourseDuration
    description: str
    prerequisites: Optional[str]
    exclusions: Optional[str]
    corequisites: Optional[str]


class CourseSearch(ORMBaseSchema):
    code: str
    level: Optional[CourseLevel]
    duration: Optional[CourseDuration]


class Course(CourseBase):
    programs: List[Program]


class CourseCreate(CourseBase):
    program_codes: Set[str] = []


class Courses(ORMBaseSchema):
    """
    List of Course objects
    """
    __root__: List[Course]


"""
CourseUpdate schema is created dynamically from all fields (except from code) present in CourseCreate,
but with all fields optional. Any change in CourseCreate will be reflected in CourseUpdate
"""
update_fields = {}
for field in CourseCreate.__fields__.values():
    if field.name != "code":
        update_fields[field.name] = (Optional[field.outer_type_], None)


CourseUpdate = create_model(
    "CourseUpdate",
    **update_fields
)
