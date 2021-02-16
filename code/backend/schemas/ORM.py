from pydantic import BaseModel


class ORMBaseSchema(BaseModel):
    class Config:
        orm_mode = True
