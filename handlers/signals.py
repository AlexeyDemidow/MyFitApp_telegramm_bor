from aiogram import Router, F, Bot

import bot_settings

router = Router()

async def start_bot(bot: Bot):
    await bot.send_message(bot_settings.config.admin_id, text='Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(bot_settings.config.admin_id, text='Бот остановлен')
