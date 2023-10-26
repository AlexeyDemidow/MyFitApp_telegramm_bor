from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.callbacks import MainCallback


async def start_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(
        text='Вход',
        callback_data=MainCallback(mcb='auth').pack(),
    )
    kb.button(
        text='Перейти на сайт веб-приложения',
        url='http://myfitapp.site/',
    )
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
