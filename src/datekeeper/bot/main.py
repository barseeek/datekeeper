from aiogram import Bot, Dispatcher
from dishka import AsyncContainer

from datekeeper.bot.routers import greetings
from datekeeper.settings import Settings


async def on_startup(container: AsyncContainer):
    settings = await container.get(Settings)
    bot = await container.get(Bot)
    await bot.set_webhook(f'{settings.webhook.url}{settings.webhook.path}', secret_token=settings.webhook.secret)
    print('Webhook is set')


async def on_shutdown(container: AsyncContainer):
    bot = await container.get(Bot)
    await bot.delete_webhook()
    print('Webhook is unset')


def register_routers(dp: Dispatcher):
    dp.include_routers(
        greetings.router,
    )


def create_bot_and_dp(settings: Settings) -> tuple[Bot, Dispatcher]:
    bot = Bot(token=settings.bot.token)
    dp = Dispatcher()
    register_routers(dp)
    return bot, dp
