from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScope


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        )
    ]