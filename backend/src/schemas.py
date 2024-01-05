from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

class Token(BaseModel):
    access_token: str
    token_type: str

class WishBase(BaseModel):
    title: str
    description: str | None = None
    link: str | None = None
    is_hidden: bool = False

class WishCreate(WishBase):
    pass 

class Wish(WishBase):
    id: int