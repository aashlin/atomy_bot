import asyncio
import logging
from aiogram import Dispatcher, Bot, F
from aiogram.filters import Command
from core.utils.commands import set_commands
from core.settings import settings
from core.handlers.basic import get_start
from core.handlers.callback import get_about, get_basic, get_why_atomy, get_business, get_pay_company, \
    get_video, get_tell


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
    dp.callback_query.register(get_about, F.data == 'about')
    dp.callback_query.register(get_basic, F.data == 'basic')
    dp.callback_query.register(get_why_atomy, F.data == 'why_atomy')
    dp.callback_query.register(get_business, F.data == 'business')
    dp.callback_query.register(get_pay_company, F.data == 'pay_company')
    dp.callback_query.register(get_video, F.data == 'video')
    dp.callback_query.register(get_tell, F.data == 'tell')
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()



if __name__ == '__main__':
    asyncio.run(start())


