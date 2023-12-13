from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from db.database import Base
from sqlalchemy import Column
from datetime import datetime
from pydantic import BaseModel
from typing import List

class DbUser(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String)
  email = Column(String)
  password = Column(String)
  items = relationship('DbTask', back_populates='user')

class DbTask(Base):
  __tablename__='tasks'
  id=Column(Integer, primary_key=True, index=True)
  title=Column(String)
  description=Column(String)
  status=Column(String)
  #user_id = Column(Integer, ForeignKey('users.id'))
  user = relationship("DbUser", back_populates='items')
  #due_date: datetime
  #images: List[str] = []

# You can define a separate model for uploading images if needed.
#class ImageUpload(BaseModel):
 #   image_url: str

