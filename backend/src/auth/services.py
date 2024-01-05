from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import ExpiredSignatureError, jwt, JWTError
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from .. import models, schemas

SECRET_KEY = '36eefdd0b0fa8a635fee6cf33466fa2a79e4c0a278e942d5eb455646782d03d7'
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

AUTHENTICATION_EXCEPTION = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user.")

def hash_password(password):
    return bcrypt_context.hash(password)

def authenticate_user(email: str, password: str, db: Session):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise AUTHENTICATION_EXCEPTION 
    if not bcrypt_context.verify(password, user.hashed_password): 
        raise AUTHENTICATION_EXCEPTION
    return user

def create_access_token(email: str, user_id: int, expires_delta: timedelta = timedelta(minutes=20)):
    encode = {'sub': email, 'id': user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

def add_new_user_to_db(email: str, password: str, db: Session):
    userDB = db.query(models.User).filter(models.User.email == email).first()
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

def delete_user_from_db(email: str, db: Session):
    userDB = db.query(models.User).filter(models.User.email == email).first()
    if not userDB:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not Found")
    db.delete(userDB)
    db.commit()
    return userDB

def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
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