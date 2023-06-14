from aiogram import Bot
from aiogram.types import Message
from core.keybords.inline import get_inl_kbd_basic


async def get_start(message: Message, bot: Bot):
    await message.answer(f'Вы находитесь в главном меню и здесь вы сможете\n'
                         f'выбрать любое интересующее вас направление, а я смогу\n'
                         f'предоставить <b>всю</b> необходимую информацию о нем!\n\n'
                         f'Контакты владельца бота:\n\n'
                         f'@andrey_abyazov\n\n'
                         f'Выбирайте меню с чего начнем', reply_markup=get_inl_kbd_basic())


