from typing import Annotated

from fastapi import FastAPI, status, Depends
from sqlalchemy.orm import Session

from . import schemas
from .auth import Auth
from .auth.services import get_current_user
from .wish import Wish
from .wish.services import get_user_unhidden_wishes
from .database import Get_DB

app = FastAPI()
app.include_router(Auth.router)
app.include_router(Wish.router)

db_dependency = Annotated[Session, Depends(Get_DB)]
user_dependency = Annotated[schemas.User, Depends(get_current_user)]

@app.get('/me', status_code = status.HTTP_200_OK, response_model=schemas.User)
def user(user: user_dependency):
    return user

@app.get('/users/{user_id}/wishes')
def read_user_wishes(user_id: int, db: db_dependency):
    return get_user_unhidden_wishes(db, user_id)