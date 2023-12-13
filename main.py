from fastapi import FastAPI
from routers import task, user
from db import models
from db.database import engine
from auth import authentication

app = FastAPI()

app.include_router(authentication.router)
app.include_router(task.router)
app.include_router(user.router)


@app.get('/')
def index():
  return {'message': 'Hello world!'}


models.Base.metadata.create_all(engine)
