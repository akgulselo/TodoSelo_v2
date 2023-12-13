from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
  username: str
  email: str
  password: str

class UserDisplay(BaseModel):
  username: str
  email: str
  class Config():
    orm_mode = True

class TaskBase(BaseModel):
    title:str
    description:str
    completed: bool = False
   # status:str

class TaskDisplay(BaseModel):
    title:str
    description:str
    #status:str    
    #images: List[str] = []
