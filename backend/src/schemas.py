from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

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

class WishEdit(WishBase):
    title: str | None = None
    is_hidden: bool | None = None

class Wish(WishBase):
    id: int
    owner_id: int

class User(UserBase):
    id: int
    wishes: list[Wish] = []