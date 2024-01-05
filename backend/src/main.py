from fastapi import FastAPI, status, Depends, HTTPException
from typing import Annotated
from sqlalchemy.orm import Session

from . import models, schemas, auth
from .database import engine, Get_DB

app = FastAPI()
app.include_router(auth.router)

models.Base.metadata.create_all(bind=engine)

db_dependency = Annotated[Session, Depends(Get_DB)]
user_dependency = Annotated[dict, Depends(auth.get_current_user)]

@app.get('/', status_code = status.HTTP_200_OK)
def user(user: user_dependency, db: db_dependency):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication Failed")
    return {"User": user}