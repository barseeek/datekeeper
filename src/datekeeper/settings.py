from os import environ

from pydantic import BaseModel, Field


class BotSettings(BaseModel):
    token: str = Field(..., alias='BOT_TOKEN')


class WebHookSettings(BaseModel):
    url: str = Field(..., alias='WEBHOOK_URL')
    secret: str = Field(..., alias='WEBHOOK_SECRET')
    path: str = Field('/update', alias='WEBHOOK_PATH')


class Settings(BaseModel):
    bot: BotSettings = Field(default_factory=lambda: BotSettings(**environ))
    webhook: WebHookSettings = Field(default_factory=lambda: WebHookSettings(**environ))
