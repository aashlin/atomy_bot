from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inl_kbd_basic():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Раскажи мне о компании Atomy', callback_data='about')
    keyboard_builder.button(text='Раскажи мне о бизнесе Atomy', callback_data='business')
    keyboard_builder.button(text='О продукции компании', callback_data='products')
    keyboard_builder.button(text='О системе продвижения в бизнесе', callback_data='system')
    keyboard_builder.button(text='Заказать такого бота себе', callback_data='buy_bot')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()

def get_inl_kbd_about():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='? Почему именно Атоми ?', callback_data='why_atomy')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_why_atomy():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Расскажи мне о бизнесе Атоми', callback_data='business')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_business():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='? За что и сколько платит компания ?', callback_data='pay_company')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_pay_company():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Посмотреть видео', callback_data='video')
    keyboard_builder.button(text='Давай ты мне расскажешь', callback_data='tell')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_video():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Мне все понятно. Хочу стать партнером', callback_data='partner')
    keyboard_builder.button(text='Шаг назад', callback_data='pay_company')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()



def get_inl_kbd_tell():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Классификация и условия дистрибьютерства ', callback_data='condition_distributor')
    keyboard_builder.button(text='Спонсорское вознаграждение', callback_data='sponsor_reward')
    keyboard_builder.button(text='Мастерское вознаграждение', callback_data='master_reward')
    keyboard_builder.button(text='Условия повышения уровня мастерства', callback_data='condition_master')
    keyboard_builder.button(text='Бонусы и поощрения для мастеров', callback_data='bonuses_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()