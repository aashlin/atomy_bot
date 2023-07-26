import asyncio
import logging
from aiogram import Dispatcher, Bot, F
from aiogram.filters import Command
from core.utils.commands import set_commands
from core.settings import settings
from core.handlers.basic import get_start
from core.handlers.callback import get_about, get_basic, get_why_atomy, get_business, get_pay_company, \
    get_video, get_tell, get_condition_distributor, get_agent, get_sales_repr, get_specagent, get_exclusive_repr, \
    get_dealer, get_qualif_master, get_sales_master, get_diamond_master, get_star_master, get_sharon_master, \
    get_kraun_master, get_imper_master, get_royal_master, get_sponsor_reward, get_products, get_hair, get_health, \
    get_leather, get_mouth


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
    dp.callback_query.register(get_condition_distributor, F.data == 'condition_distributor')
    dp.callback_query.register(get_agent, F.data == 'agent')
    dp.callback_query.register(get_sales_repr, F.data == 'sales_repr')
    dp.callback_query.register(get_specagent, F.data == 'specagent')
    dp.callback_query.register(get_dealer, F.data == 'dealer')
    dp.callback_query.register(get_exclusive_repr, F.data == 'exclusive_repr')
    dp.callback_query.register(get_qualif_master, F.data == 'qualif_master')
    dp.callback_query.register(get_sales_master, F.data == 'sales_master')
    dp.callback_query.register(get_diamond_master, F.data == 'diamond_master')
    dp.callback_query.register(get_sharon_master, F.data == 'sharon_master')
    dp.callback_query.register(get_star_master, F.data == 'star_master')
    dp.callback_query.register(get_royal_master, F.data == 'royal_master')
    dp.callback_query.register(get_kraun_master, F.data == 'kraun_master')
    dp.callback_query.register(get_imper_master, F.data == 'imper_master')
    dp.callback_query.register(get_sponsor_reward, F.data == 'sponsor_reward')
    dp.callback_query.register(get_products, F.data == 'products')
    dp.callback_query.register(get_health, F.data == 'health')
    dp.callback_query.register(get_hair, F.data == 'hair')
    dp.callback_query.register(get_leather, F.data == 'leather')
    dp.callback_query.register(get_mouth, F.data == 'mouth')
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()



if __name__ == '__main__':
    asyncio.run(start())


