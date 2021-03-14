from datetime import timedelta, datetime
from typing import Optional, List

from sqlalchemy.orm import Session
from backend import models, schemas
from passlib.context import CryptContext
from jose import JWTError, jwt

from backend.options import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user_by_email(db: Session, email: str) -> models.User:
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_email(db, username)
    if not user:
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(email=user.email, password_hash=hash_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_course_by_code(db: Session, code: str) -> models.Course:
    return db.query(models.Course).filter(models.Course.code == code).first()


def get_courses(db: Session, skip: int = 0, limit: int = 100) -> List[models.Course]:
    return db.query(models.Course).offset(skip).limit(limit).all()


def get_courses_match(db: Session, search: schemas.CourseSearch, limit: int = 20) -> List[models.Course]:
    search_dict = search.dict(exclude_unset=True)
    model = models.Course

    fuzzy = "%{}%".format(search_dict.pop("code"))
    query = db.query(model).filter(model.code.like(fuzzy))

    for col in search_dict:
        query = query.filter(getattr(model, col) == search_dict[col])

    return query.limit(limit).all()


def create_course(db: Session, course: schemas.CourseCreate) -> models.Course:
    course_dict = course.dict()
    program_codes = course_dict.pop("program_codes")
    programs = []
    for code in program_codes:
        programs.append(get_program_by_code(db, code))

    db_course = models.Course(**course_dict, programs=programs)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def update_course(db: Session, course: schemas.CourseUpdate, course_code: str) -> models.Course:
    course_dict = course.dict(exclude={"program_codes"}, exclude_unset=True)

    course_query = db.query(models.Course).filter(models.Course.code == course_code)
    if len(course_dict) > 0:
        course_query.update(course_dict)
    updated_course: models.Course = course_query.first()

    if course.program_codes is not None:
        programs = []
        for code in course.program_codes:
            programs.append(get_program_by_code(db, code))
        updated_course.programs = programs

    db.commit()
    return get_course_by_code(db, course_code)


def create_program(db: Session, program: schemas.Program) -> models.Program:
    db_program = models.Program(**program.dict())
    db.add(db_program)
    db.commit()
    db.refresh(db_program)
    return db_program


def update_program(db: Session, program: schemas.ProgramUpdate, program_code: str) -> models.Program:
    program_dict = program.dict(exclude_unset=True)

    program_query = db.query(models.Program).filter(models.Program.code == program_code)
    if len(program_dict) > 0:
        program_query.update(program_dict)
    db.commit()
    return get_program_by_code(db, program_code)


def get_program(db: Session, skip: int = 0, limit: int = 100) -> List[models.Program]:
    return db.query(models.Program).offset(skip).limit(limit).all()


def get_program_by_code(db: Session, code: str) -> models.Program:
    return db.query(models.Program).filter(models.Program.code == code).first()


def get_courses_by_program_code(db: Session, code: str) -> List[models.Program]:
    return get_program_by_code(db, code).courses


def delete_course(db: Session, course: schemas.Course) -> None:
    db.delete(course)
    db.commit()
    return None

def delete_courses(db: Session) -> List[models.Course]:
    courses_list = db.query(models.Course).all()
    for course in courses_list:
        db.delete(course)
    db.commit()
    return courses_list

def delete_program(db: Session, program: schemas.Program) -> None:
    db.delete(program)
    db.commit()
    return None

  
def delete_programs(db: Session) -> List[models.Program]:
    programs_list = db.query(models.Program).all()
    for program in programs_list:
        db.delete(program)
    db.commit()
    return programs_list
  
    
def get_reviews_by_code(db: Session, course_code: str) -> List[models.Review]:
    return db.query(models.Review).filter(models.Review.course_code == course_code).all()

def get_reviews_by_me(db: Session, user: schemas.User) -> List[models.Review]:
    return db.query(models.Review).filter(models.Review.user_email == user.email).all()

def get_review_by_id(db: Session, review_id: int) -> models.Review:
    return db.query(models.Review).filter(models.Review.review_id == review_id).first()

def create_review(db: Session, review: schemas.ReviewCreate, user: schemas.User) -> models.Review:
    review_dict = review.dict()
    email = user.email
    code = review_dict.pop("course_code")
    tag_ids = review_dict.pop("tag_ids")
    tags = []
    for tag_id in tag_ids:
        tags.append(get_tag_by_id(db, tag_id))
    course = get_course_by_code(db, code)
    db_review = models.Review(**review_dict, user=user, course=course, user_email=email,
                                course_code=code, tags=tags)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def update_review(db: Session, review: schemas.ReviewUpdate, review_id: int,
                    user: schemas.User) -> models.Review:
    review_dict = review.dict(exclude={"tag_ids"}, exclude_unset=True)
    review_query = db.query(models.Review).filter(models.Review.review_id == review_id)
    
    if len(review_dict) > 0:
        review_query.update(review_dict)
    updated_review: models.Review = review_query.first()

    if review.tag_ids is not None:
        tags = []
        for tag_id in review.tag_ids:
            tags.append(get_tag_by_id(db, tag_id))
        updated_review.tags = tags

    db.commit()
    return get_review_by_id(db, review_id)

def delete_review(db: Session, review: schemas.Review) -> None:
    db.delete(review)
    db.commit()
    return None

def get_tag_by_id(db: Session, tag_id: int) -> models.Tag:
    return db.query(models.Tag).filter(models.Tag.tag_id == tag_id).first()


def get_all_tags(db: Session, skip: int = 0, limit: int = 100) -> List[models.Tag]:
    return db.query(models.Tag).offset(skip).limit(limit).all()


def create_tag(db: Session, tag_data: schemas.TagCreate) -> models.Tag:
    tag = models.Tag(**tag_data.dict())
    db.add(tag)
    db.commit()
    return tag

def get_tag_by_text(db: Session, text: schemas.Tag) -> models.Tag:
    return db.query(models.Tag).filter(models.Tag.text == text).first()


def delete_tag(db: Session, tag_id: int) -> models.Tag:
    tag = get_tag_by_id(db, tag_id)
    db.delete(tag)
    return tag


def modify_tag(db: Session, tag_data: schemas.TagCreate, tag_id: int) -> models.Tag:
    tag = get_tag_by_id(db, tag_id)
    for k, v in tag_data.dict(exclude_unset=True).items():
        setattr(tag, k, v)
    db.commit()
    return tag
