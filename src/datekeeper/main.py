from fastapi import FastAPI

from datekeeper.api.main import create_fastapi_app


def create_app() -> FastAPI:
    app = create_fastapi_app()

    return app
