from fastapi import FastAPI, status, Depends, HTTPException
from typing import Annotated
from sqlalchemy.orm import Session

from . import models, schemas
from .auth import Auth
from .auth.services import (
   USER_NOT_FOUND_EXCEPTION,
   get_current_user,
   get_user_from_db_by_email 
)
from .database import engine, Get_DB

app = FastAPI()
app.include_router(Auth.router)

models.Base.metadata.create_all(bind=engine)

db_dependency = Annotated[Session, Depends(Get_DB)]
user_dependency = Annotated[schemas.User, Depends(get_current_user)]

@app.get('/me', status_code = status.HTTP_200_OK, response_model=schemas.User)
def user(user: user_dependency, db: db_dependency):
    userDB = get_user_from_db_by_email(user.email, db)
    if not userDB:
        raise USER_NOT_FOUND_EXCEPTION
    return user