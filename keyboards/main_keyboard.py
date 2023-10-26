from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.callbacks import MainCallback


async def get_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(
        text='Профиль',
        callback_data=MainCallback(mcb='profile').pack(),
    )
    kb.button(
        text='Статистика',
        callback_data=MainCallback(mcb='statistics').pack(),
    )
    kb.button(
        text='Съедено за день',
        callback_data=MainCallback(mcb='daily_food').pack(),
    )
    kb.button(
        text='Выйти',
        callback_data=MainCallback(mcb='exit').pack(),
    )
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
