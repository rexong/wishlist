from sqlalchemy.orm import Session

from .. import models

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
