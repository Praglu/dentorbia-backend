import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_VERSION: str = os.getenv('API_VERSION', '/api/v1')
    DATABASE_URL: str = os.getenv('DATABASE_URL')
    USERNAME: str = os.getenv('USERNAME', 'foo')
    PASSWORD: str = os.getenv('PASSWORD', 'bar')
    

settings = Settings()
