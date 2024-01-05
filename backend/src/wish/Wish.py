from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .services import add_new_wish_to_db, get_user_wishes_from_db, hide_wish_in_db, remove_wish_from_db, unhide_wish_in_db
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

@router.delete('/{id}')
def delete_wishes(db: db_dependency, id: int, user: user_dependency):
    return remove_wish_from_db(db=db, id=id, user_id=user.id)

@router.put('/{id}')
def update_wishes(db: db_dependency, user: user_dependency, wish: schemas.WishCreate):
    pass

@router.put('/{id}/hide', response_model=schemas.Wish)
def hide_wish(db: db_dependency, user: user_dependency, id: int):
    return hide_wish_in_db(db=db, id=id, user_id=user.id)

@router.put('/{id}/unhide', response_model=schemas.Wish)
def unhide_wish(db: db_dependency, user: user_dependency, id: int):
    return unhide_wish_in_db(db=db, id=id, user_id=user.id)
