from fastapi import FastAPI

from datekeeper.api.routers import debug


def create_fastapi_app() -> FastAPI:
    app = FastAPI()
    register_routers(app)

    return app


def register_routers(app: FastAPI) -> None:
    app.include_router(debug.router)
