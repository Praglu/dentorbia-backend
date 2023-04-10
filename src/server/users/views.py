from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from server.db.database import get_db
from server.settings.security import oauth_scheme
from server.users import crud, schemas


router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post('/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        HTTPException(status_code=400, detail='Email already reqistered')
    return crud.create_user(db=db, user=user)


@router.get('/', response_model=list[schemas.User])
def read_users(
        # token: Annotated[str, Depends(oauth_scheme)],
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db),
        ):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

