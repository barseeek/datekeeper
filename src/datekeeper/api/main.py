from fastapi import FastAPI

from datekeeper.api.routers import webhook
from datekeeper.api.routers import debug
from datekeeper.settings import Settings


def create_fastapi_app(settings: Settings) -> FastAPI:
    app = FastAPI()
    register_routers(app, settings)

    return app


def register_routers(app: FastAPI, settings: Settings):
    app.include_router(debug.router)
    app.include_router(webhook.setup(settings))
