from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..auth.services import USER_NOT_FOUND_EXCEPTION, get_user_from_db_by_id

WISH_NOT_FOUND_EXCEPTION = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="Wish Not Found"
)
WISH_OPERATION_FORBIDDEN_EXCEPTION = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN, detail="No Permission to Edit this Wish"
)


def add_new_wish_to_db(
    title: str,
    db: Session,
    owner_id: int,
    description: str | None = None,
    link: str | None = None,
    is_hidden: bool = False,
):
    wishDB = models.Wish(
        title=title,
        description=description,
        link=link,
        is_hidden=is_hidden,
        owner_id=owner_id,
    )
    db.add(wishDB)
    db.commit()
    db.refresh(wishDB)
    return wishDB


def get_user_wishes_from_db(db: Session, owner_id: int):
    userDB = get_user_from_db_by_id(db=db, id=owner_id)
    if not userDB:
        raise USER_NOT_FOUND_EXCEPTION
    wishes = userDB.wishes
    return wishes


def get_user_unhidden_wishes(db: Session, owner_id: int):
    return (
        db.query(models.Wish)
        .filter(models.Wish.owner_id == owner_id, models.Wish.is_hidden == False)
        .all()
    )


def get_wish_from_db_by_id(db: Session, id: int) -> schemas.Wish | None:
    return db.query(models.Wish).filter(models.Wish.id == id).first()


def remove_wish_from_db(db: Session, id: int, user_id: int):
    wishDB = get_wish_from_db_by_id(db, id)
    if not wishDB:
        raise WISH_NOT_FOUND_EXCEPTION
    if wishDB.owner_id != user_id:
        raise WISH_OPERATION_FORBIDDEN_EXCEPTION
    db.delete(wishDB)
    db.commit()
    return wishDB


def hide_wish_in_db(db: Session, id: int, user_id: int):
    wishDB = get_wish_from_db_by_id(db, id)
    if not wishDB:
        raise WISH_NOT_FOUND_EXCEPTION
    if wishDB.owner_id != user_id:
        raise WISH_OPERATION_FORBIDDEN_EXCEPTION
    if wishDB.is_hidden == True:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Wish is already Hidden"
        )
    wishDB.is_hidden = True
    db.commit()
    return wishDB


def unhide_wish_in_db(db: Session, id: int, user_id: int):
    wishDB = get_wish_from_db_by_id(db, id)
    if not wishDB:
        raise WISH_NOT_FOUND_EXCEPTION
    if wishDB.owner_id != user_id:
        raise WISH_OPERATION_FORBIDDEN_EXCEPTION
    if wishDB.is_hidden == False:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Wish is already Unhidden"
        )
    wishDB.is_hidden = False
    db.commit()
    return wishDB


def edit_wish_in_db(
    db: Session,
    id: int,
    user_id: int,
    title: str | None = None,
    description: str | None = None,
    link: str | None = None,
    is_hidden: bool | None = None,
):
    wishDB = get_wish_from_db_by_id(db, id)
    if not wishDB:
        raise WISH_NOT_FOUND_EXCEPTION
    if wishDB.owner_id != user_id:
        raise WISH_OPERATION_FORBIDDEN_EXCEPTION
    if title:
        wishDB.title = title
    if description:
        wishDB.description = description
    if link:
        wishDB.link = link
    if is_hidden != None:
        wishDB.is_hidden = is_hidden
    db.commit()
    return wishDB
