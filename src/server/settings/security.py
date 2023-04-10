import secrets

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from typing import Annotated

from server.settings.config import settings

router = APIRouter(
    tags=['login']
)


oauth_scheme = OAuth2PasswordBearer(tokenUrl='token')


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_hashed_password(password):
    return pwd_context.hash(password)


@router.post('/token')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    username = form_data.username
    password = form_data.password
    is_correct_username = secrets.compare_digest(username, settings.USERNAME)
    if not is_correct_username:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Incorrect username or password'
            )
    is_correct_password = secrets.compare_digest(password, settings.PASSWORD)
    if not is_correct_password:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Incorrect username or password'
            )

    return {'access_token': settings.USERNAME, 'token_type': 'Bearer'}
