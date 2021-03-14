from typing import List

from fastapi import Depends, APIRouter, HTTPException, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from backend import schemas, crud
from backend.dependencies import get_db

router = APIRouter(prefix="/admin",
                   tags=['admin']
                   )


# end points for creating programs
@router.put("/programs",
            summary='Create a program',
            response_model=schemas.Program,
            responses={
                409: {
                    "description": "Program you're trying to insert already exists\n"
                                   "Returns the program already stored in the database",
                    "model": schemas.Program
                }
            })
def create_program(program: schemas.Program, db: Session = Depends(get_db)):
    db_program = crud.get_program_by_code(db, code=program.code)
    if db_program:
        raise HTTPException(status_code=409, detail="Program already exists")
    return crud.create_program(db=db, program=program)


@router.post("/programs/{program_code}",
             summary="Update a program",
             response_model=schemas.Program)
def update_program(course: schemas.ProgramUpdate, program_code: str, db: Session = Depends(get_db)):
    if not crud.get_program_by_code(db, program_code):
        raise HTTPException(404, "Course not found")
    return crud.update_program(db, course, program_code)


# end points for creating courses 
@router.put("/courses",
            summary='Create a course',
            response_model=schemas.Course,
            responses={
                409: {
                    "description": "Course you're trying to insert already exists\n"
                                   "Returns the course already stored in the database",
                    "model": schemas.Course
                }
            })
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = crud.get_course_by_code(db, code=course.code)
    if db_course:
        return JSONResponse(status_code=409,
                            content=jsonable_encoder(schemas.Course.from_orm(db_course)))

    for code in course.program_codes:
        program = crud.get_program_by_code(db, code)
        if not program:
            raise HTTPException(status_code=400, detail="Provided program code does not exist",)
    return crud.create_course(db=db, course=course)


@router.post("/courses/{course_code}",
             summary="Update a course",
             response_model=schemas.Course)
def update_course(course: schemas.CourseUpdate, course_code: str, db: Session = Depends(get_db)):
    if not crud.get_course_by_code(db, course_code):
        raise HTTPException(404, "Course not found !!!")
    for code in course.program_codes or []:
        program = crud.get_program_by_code(db, code)
        if not program:
            raise HTTPException(status_code=400, detail="Provided program code does not exist",)
    return crud.update_course(db, course, course_code)


# delete course by code
@router.delete("/courses/{course_code}",
                summary="Delete a course",
                response_model=schemas.Course)
def delete_course(course_code: str, db: Session = Depends(get_db)):
    
    course = crud.get_course_by_code(db, course_code)
    if not course: # course not found in db
        raise HTTPException(status_code = 404, detail = "Course not found")
    # delete course from courses table and program_association table 
    crud.delete_course(db = db, course = course)
    return course


@router.put("/tag",
            summary="Create a tag",
            response_model=schemas.Tag,
            responses={
                409: {
                    "description": "Tag you're trying to insert already exists\n"
                                   "Returns the tag already stored in the database",
                    "model": schemas.Tag
                }
            })
def create_tag(tag_data: schemas.TagCreate, db: Session = Depends(get_db)):
    db_tag = crud.get_tag_by_text(db, tag_data.text)
    if db_tag:
        return JSONResponse(status_code=409,
                            content=jsonable_encoder(schemas.Tag.from_orm(db_tag)))
    return crud.create_tag(db, tag_data)


@router.post("/tag/{tag_id}",
             summary="Update a tag",
             response_model=schemas.Tag)
def update_tag(tag_data: schemas.TagCreate, tag_id: int, db: Session = Depends(get_db)):
    if not crud.get_tag_by_id(db, tag_id):
        raise HTTPException(404, "Tag not found")
    return crud.modify_tag(db, tag_data, tag_id)


@router.delete("/tag/{tag_id}",
               summary="Delete a tag",
               response_model=schemas.Tag)
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    if not crud.get_tag_by_id(db, tag_id):
        raise HTTPException(404, "Tag not found")
    return crud.delete_tag(db, tag_id)

# delete all courses
@router.delete("/courses",
                summary="Delete all courses",
                response_model=schemas.Courses)
def delete_all_courses(db: Session = Depends(get_db)):
    return crud.delete_courses(db)
    

# delete program by code
@router.delete("/programs/{program_code}",
                summary="Delete a program",
                response_model=schemas.Program)
def delete_program(program_code: str, db: Session = Depends(get_db)):
    
    program = crud.get_program_by_code(db, program_code)
    if not program: # program not found in db
        raise HTTPException(status_code = 404, detail = "Program not found")
    # delete program from program table and program_association table 
    crud.delete_program(db = db, program = program)
    return program

# delete all programs 
@router.delete("/programs",
                summary="Delete all programs",
                response_model=schemas.Programs)
def delete_all_programs(db: Session = Depends(get_db)):
    return crud.delete_programs(db)
    
