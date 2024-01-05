from fastapi import FastAPI, status, Depends
from typing import Annotated

from . import schemas
from .auth import Auth
from .auth.services import get_current_user
from .wish import Wish

app = FastAPI()
app.include_router(Auth.router)
app.include_router(Wish.router)

user_dependency = Annotated[schemas.User, Depends(get_current_user)]

@app.get('/me', status_code = status.HTTP_200_OK, response_model=schemas.User)
def user(user: user_dependency):
    return user