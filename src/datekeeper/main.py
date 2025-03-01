from functools import partial

from aiogram import Dispatcher, Bot
from dishka import make_async_container, AsyncContainer
from dishka.integrations.aiogram import setup_dishka as setup_dishka_aiogram
from dishka.integrations.fastapi import setup_dishka as setup_dishka_fastapi

from dotenv import load_dotenv
from fastapi import FastAPI

from datekeeper.bot.main import create_bot_and_dp, on_startup, on_shutdown
from datekeeper.api.main import create_fastapi_app
from datekeeper.infrastructure.di import AppProvider
from datekeeper.settings import Settings


def create_app() -> FastAPI:
    load_dotenv()

    settings: Settings = Settings()
    bot, dp = create_bot_and_dp(settings)
    app: FastAPI = create_fastapi_app(settings)
    container: AsyncContainer = make_async_container(
        AppProvider(), context={Settings: settings, Bot: bot, Dispatcher: dp}
    )
    setup_dishka_aiogram(container=container, router=dp, auto_inject=True)
    setup_dishka_fastapi(container=container, app=app)

    app.add_event_handler('startup', partial(on_startup, container))
    app.add_event_handler('shutdown', partial(on_shutdown, container))

    return app
