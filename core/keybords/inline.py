from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inl_kbd_basic():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Раскажи мне о компании Atomy', callback_data='about')
    keyboard_builder.button(text='Раскажи мне о бизнесе Atomy', callback_data='business')
    keyboard_builder.button(text='О продукции компании', callback_data='products')
    keyboard_builder.button(text='О системе продвижения в бизнесе', callback_data='condition_distributor')
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
    keyboard_builder.button(text='Мастерское вознаграждение', callback_data='qualif_master')
    keyboard_builder.button(text='Условия повышения уровня мастерства', callback_data='condition_master')
    keyboard_builder.button(text='Бонусы и поощрения для мастеров', callback_data='bonuses_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_condition_distributor():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Торговый представитель', callback_data='sales_repr')
    keyboard_builder.button(text='Агент', callback_data='agent')
    keyboard_builder.button(text='Специальный агент', callback_data='specagent')
    keyboard_builder.button(text='Дилер', callback_data='dealer')
    keyboard_builder.button(text='Эксклюзивный представитель', callback_data='exclusive_repr')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_sales_repr():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Агент', callback_data='agent')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_agent():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Специальный агент', callback_data='specagent')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_specagent():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Дилер', callback_data='dealer')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_dealer():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Эксклюзивный представитель', callback_data='exclusive_repr')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_exclusive_repr():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Квалификация мастеров', callback_data='qualif_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_master_qualif():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Мастер продаж', callback_data='sales_master')
    keyboard_builder.button(text='Брилиантовый мастер', callback_data='diamond_master')
    keyboard_builder.button(text='Мастер Шаронской розы', callback_data='sharon_master')
    keyboard_builder.button(text='Стар мастер', callback_data='star_master')
    keyboard_builder.button(text='Роял мастер', callback_data='royal_master')
    keyboard_builder.button(text='Краун мастер', callback_data='kraun_master')
    keyboard_builder.button(text='Империал мастер', callback_data='imper_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_sales_master():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Брилиантовый мастер', callback_data='diamond_master')
    keyboard_builder.button(text='Шаг назад', callback_data='qualif_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_diamond_master():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Мастер Шаронской розы', callback_data='sharon_master')
    keyboard_builder.button(text='Шаг назад', callback_data='qualif_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_sharon_master():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Стар мастер', callback_data='star_master')
    keyboard_builder.button(text='Шаг назад', callback_data='qualif_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_star_master():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Роял мастер', callback_data='royal_master')
    keyboard_builder.button(text='Шаг назад', callback_data='qualif_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_royal_master():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Краун мастер', callback_data='kraun_master')
    keyboard_builder.button(text='Шаг назад', callback_data='qualif_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_kraun_master():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Империал мастер', callback_data='imper_master')
    keyboard_builder.button(text='Шаг назад', callback_data='qualif_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_imper_master():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Условия повышения уровня мастерства', callback_data='condition_master')
    keyboard_builder.button(text='Шаг назад', callback_data='qualif_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_sponsor_reward():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Мастерское вознаграждение', callback_data='qualif_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_products():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Здоровье', callback_data='health')
    keyboard_builder.button(text='Уход за волосами', callback_data='hair')
    keyboard_builder.button(text='Уход за кожей', callback_data='leather')
    keyboard_builder.button(text='Уход за полостью рта', callback_data='mouth')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_products_menu():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Хочу заказть', callback_data='products_order')
    keyboard_builder.button(text='Шаг назад', callback_data='products')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_condition_master():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Бонусы и поощрения для мастеров', callback_data='bonuses_master')
    keyboard_builder.button(text='Шаг назад', callback_data='qualif_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_bonuses_master():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Мастер продаж', callback_data='sales_master_b')
    keyboard_builder.button(text='Брилиантовый мастер', callback_data='diamond_master_b')
    keyboard_builder.button(text='Мастер Шаронской розы', callback_data='sharon_master_b')
    keyboard_builder.button(text='Стар мастер', callback_data='star_master_b')
    keyboard_builder.button(text='Роял мастер', callback_data='royal_master_b')
    keyboard_builder.button(text='Краун мастер', callback_data='kraun_master_b')
    keyboard_builder.button(text='Империал мастер', callback_data='imper_master_b')
    keyboard_builder.button(text='Шаг назад', callback_data='condition_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_sales_master_b():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Брилиантовый мастер', callback_data='diamond_master_b')
    keyboard_builder.button(text='Шаг назад', callback_data='bonuses_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_diamond_master_b():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Мастер Шаронской розы', callback_data='sharon_master_b')
    keyboard_builder.button(text='Шаг назад', callback_data='bonuses_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_sharon_master_b():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Стар мастер', callback_data='star_master_b')
    keyboard_builder.button(text='Шаг назад', callback_data='bonuses_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_star_master_b():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Роял мастер', callback_data='royal_master_b')
    keyboard_builder.button(text='Шаг назад', callback_data='bonuses_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_royal_master_b():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Краун мастер', callback_data='kraun_master_b')
    keyboard_builder.button(text='Шаг назад', callback_data='bonuses_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_kraun_master_b():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Империал мастер', callback_data='imper_master_b')
    keyboard_builder.button(text='Шаг назад', callback_data='bonuses_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()

def get_inl_kbd_imper_master_b():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Как стать партнером Атоми', callback_data='partner')
    keyboard_builder.button(text='Условия повышения уровня мастерства', callback_data='condition_master')
    keyboard_builder.button(text='Шаг назад', callback_data='bonuses_master')
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()


def get_inl_kbd_partner():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Главное меню', callback_data='basic')
    keyboard_builder.adjust(1, True)
    return keyboard_builder.as_markup()