from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
    await message.answer(f'Вы находитесь в главном меню и здесь вы сможете'
                         f'выбрать любое интересующее вас направление, а я смогу'
                         f'предоставить всю необходимую информацию о нем!')