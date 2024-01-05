from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .services import add_new_wish_to_db, get_user_wishes_from_db, remove_wish_from_db
from ..auth.services import get_current_user
from ..database import Get_DB
from .. import schemas

router = APIRouter(
    prefix='/wish',
    tags=['wish']
)

db_dependency = Annotated[Session, Depends(Get_DB)]
user_dependency = Annotated[schemas.User, Depends(get_current_user)]

# @router.get('')
# def read_wish():
#     pass

@router.get('', response_model=list[schemas.Wish])
def read_wishes(user: user_dependency, db: db_dependency):
    return get_user_wishes_from_db(db=db, owner_id=user.id)

@router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.Wish)
def create_wishes(db: db_dependency, wish: schemas.WishCreate, user: user_dependency):
    return add_new_wish_to_db(**wish.model_dump(), db=db, owner_id=user.id)

@router.delete('/{id}', dependencies=[Depends(get_current_user)])
def delete_wishes(db: db_dependency, id: int):
    return remove_wish_from_db(db=db, id=id)

@router.put('')
def update_wishes():
    pass

@router.put('')
def toggle_is_hidden():
    pass
