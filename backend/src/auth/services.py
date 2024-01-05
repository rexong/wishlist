from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import ExpiredSignatureError, jwt, JWTError
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from .. import models

SECRET_KEY = '36eefdd0b0fa8a635fee6cf33466fa2a79e4c0a278e942d5eb455646782d03d7'
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

AUTHENTICATION_EXCEPTION = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")

def hash_password(password):
    return bcrypt_context.hash(password)

def authenticate_user(username: str, password: str, db: Session):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise AUTHENTICATION_EXCEPTION 
    if not bcrypt_context.verify(password, user.hashed_password): 
        raise AUTHENTICATION_EXCEPTION
    return user

def create_access_token(username: str, user_id: int, expires_delta: timedelta = timedelta(minutes=20)):
    encode = {'sub': username, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

def add_new_user_to_db(username: str, password: str, db: Session):
    userDB = db.query(models.User).filter(models.User.username == username).first()
    if userDB:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Username already exists")
    _hash_password = hash_password(password)
    userDB = models.User(
        username=username,
        hashed_password=_hash_password
    )
    db.add(userDB)
    db.commit()
    db.refresh(userDB)
    return userDB

def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise AUTHENTICATION_EXCEPTION
        return {"username": username, "id": user_id}
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Access Token Expires")
    except JWTError:
       raise AUTHENTICATION_EXCEPTION