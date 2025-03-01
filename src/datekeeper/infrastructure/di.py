from aiogram import Bot, Dispatcher
from dishka import Provider, Scope, from_context

from datekeeper.settings import Settings


class AppProvider(Provider):
    scope = Scope.APP

    settings = from_context(provides=Settings, scope=Scope.APP)
    bot = from_context(provides=Bot, scope=Scope.APP)
    dp = from_context(provides=Dispatcher, scope=Scope.APP)
