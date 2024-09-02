from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app import controllers, models, security

app = FastAPI()


app.include_router(security.router)

for extension in (models, controllers):
    extension.init_app(app)
