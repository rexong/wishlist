from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import schemas
from ..database import Get_DB
from .services import (add_new_user_to_db, authenticate_user,
                       create_access_token, delete_user_from_db,
                       get_current_user)

router = APIRouter(prefix="/auth", tags=["auth"])

db_dependency = Annotated[Session, Depends(Get_DB)]
user_dependency = Annotated[schemas.User, Depends(get_current_user)]


@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(db: db_dependency, user: schemas.UserCreate):
    return add_new_user_to_db(user.email, user.password, db)


@router.delete("/users", response_model=schemas.User)
def delete_user(db: db_dependency, user: user_dependency):
    return delete_user_from_db(user.email, db)


@router.post("/token", response_model=schemas.Token)
def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    user = authenticate_user(form_data.username, form_data.password, db)
    token = create_access_token(email=str(user.email), user_id=int(user.id))

    return {"access_token": token, "token_type": "bearer"}
