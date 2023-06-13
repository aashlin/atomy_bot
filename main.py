import asyncio
import logging
from aiogram import Dispatcher, Bot, F
from aiogram.filters import Command
from core.utils.commands import set_commands
from core.settings import settings
from core.handlers.basic import get_start


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bot.admin_id, 'Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bot.admin_id, 'Бот остановлен')


async def start():
    logging.basicConfig(level=logging.DEBUG)

    bot = Bot(token=settings.bot.bot_token, parse_mode='HTML')
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start, Command(commands=['start', 'run']))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()



if __name__ == '__main__':
    asyncio.run(start())


