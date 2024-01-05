from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import schemas, models
from ..database import Get_DB
from .services import add_new_user_to_db, authenticate_user, create_access_token

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

db_dependency = Annotated[Session, Depends(Get_DB)]

@router.post('/users', status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(db: db_dependency, user: schemas.UserCreate):
    return add_new_user_to_db(user.username, user.password, db)


@router.post('/token', response_model=schemas.Token)
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")
    token = create_access_token(user.username, user.id)

    return {'access_token': token, 'token_type': 'bearer'}