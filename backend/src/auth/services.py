from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import ExpiredSignatureError, jwt, JWTError
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from ..database import Get_DB
from .. import models, schemas

SECRET_KEY = '36eefdd0b0fa8a635fee6cf33466fa2a79e4c0a278e942d5eb455646782d03d7'
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

AUTHENTICATION_EXCEPTION = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could Not Validate User")
USER_NOT_FOUND_EXCEPTION = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")

def hash_password(password):
    return bcrypt_context.hash(password)

def authenticate_user(email: str, password: str, db: Session) -> models.User:
    userDB = get_user_from_db_by_email(email, db)
    if not userDB:
        raise AUTHENTICATION_EXCEPTION 
    if not bcrypt_context.verify(password, userDB.hashed_password): 
        raise AUTHENTICATION_EXCEPTION
    return userDB

def create_access_token(email: str, user_id: int, expires_delta: timedelta = timedelta(minutes=20)):
    encode = {'sub': email, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

def get_user_from_db_by_id(id: int, db:Session) -> models.User | None:
    return db.query(models.User).filter(models.User.id == id).first()

def get_user_from_db_by_email(email: str, db: Session) -> models.User | None:
    return db.query(models.User).filter(models.User.email == email).first()

def add_new_user_to_db(email: str, password: str, db: Session):
    userDB = get_user_from_db_by_email(email, db)
    if userDB:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Email already exists")
    _hash_password = hash_password(password)
    userDB = models.User(
        email=email,
        hashed_password=_hash_password
    )
    db.add(userDB)
    db.commit()
    db.refresh(userDB)
    return userDB

def delete_user_from_db(email: str, db: Session) -> models.User:
    userDB = get_user_from_db_by_email(email, db)
    if not userDB:
        raise USER_NOT_FOUND_EXCEPTION
    db.delete(userDB)
    db.commit()
    return userDB

def decode_access_token(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        user_id: int = payload.get('id')
        if email is None or user_id is None:
            raise AUTHENTICATION_EXCEPTION
        user = schemas.User(
            email=email,
            id=user_id
        )
        return user
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Access Token Expires")
    except JWTError:
       raise AUTHENTICATION_EXCEPTION
    
def get_current_user(user: Annotated[schemas.User, Depends(decode_access_token)], db: Annotated[Session, Depends(Get_DB)]):
    userDB = get_user_from_db_by_email(user.email, db)
    if not userDB:
        raise USER_NOT_FOUND_EXCEPTION
    return userDB