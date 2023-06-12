import asyncio
import logging
from aiogram import Dispatcher, Bot, F
from core.utils.commands import set_commands
from core.settings import settings


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bot.admin_id, 'Бот запущен')

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bot.admin_id, 'Бот остановлен')
    