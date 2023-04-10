from fastapi import FastAPI

from server.db.database import engine
from server.settings.config import settings
from server.settings.security import router as security_router
from server.users import models
from server.users.views import router as views_router


app = FastAPI(
    title='Dentorbia Backend'
)


@app.on_event('startup')
def on_startup():
    models.Base.metadata.create_all(bind=engine)


app.include_router(views_router, prefix=settings.API_VERSION)
app.include_router(security_router, prefix=settings.API_VERSION)
