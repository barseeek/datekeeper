from aiogram import Bot, Dispatcher
from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import Request, APIRouter, Header

from datekeeper.settings import Settings


@inject
async def update_handler(
    request: Request,
    bot: FromDishka[Bot],
    dispatcher: FromDishka[Dispatcher],
    settings: FromDishka[Settings],
    x_telegram_bot_api_secret_token: str = Header(None),
):
    if x_telegram_bot_api_secret_token != settings.webhook.secret:
        return {'message': 'OK'}
    raw_update = await request.json()
    await dispatcher.feed_raw_update(bot, raw_update)
    return {'message': 'OK'}


def setup(settings: Settings) -> APIRouter:
    router: APIRouter = APIRouter()
    router.add_api_route(path=settings.webhook.path, endpoint=update_handler, include_in_schema=False, methods=['POST'])
    return router
