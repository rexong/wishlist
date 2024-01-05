from sqlalchemy.orm import Session

from .. import models
from ..auth.services import get_user_from_db_by_id, USER_NOT_FOUND_EXCEPTION

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
        owner_id=owner_id
    )
    db.add(wishDB)
    db.commit()
    db.refresh(wishDB)
    return wishDB

def get_user_wishes_from_db(
    db: Session,
    owner_id: int
):
    userDB = get_user_from_db_by_id(db=db, id=owner_id)
    if userDB:
        wishes = userDB.items
        return wishes
    else:
        raise USER_NOT_FOUND_EXCEPTION