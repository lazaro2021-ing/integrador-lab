from pydantic import BaseModel
from typing import ForwardRef, List, Optional

class ClassificationTypeD(BaseModel):
    id:Optional[int]
    type:str
    charge:Optional[float]
    class Config:
        orm_mode = True



class ClassificationD(BaseModel):
    id:Optional[int]
    charge:Optional[float]
    clasification:ClassificationTypeD=None
    class Config:
        orm_mode = True