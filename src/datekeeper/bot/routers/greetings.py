from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router(name='greetings')


@router.message(CommandStart())
async def hello(message: Message):
    await message.answer(f'Hello, {message.from_user.full_name}!')
