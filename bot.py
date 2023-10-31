import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import different_types
from handlers.signals import start_bot, stop_bot
from utils.commands import set_commands
from states import auth_state, profile_state, statistics_state, daily_food_state, start_state, exit_state

from bot_settings import config

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()

# Запуск бота
async def main():
    dp.startup.register(start_bot)
    dp.include_routers(
        start_state.router,
        auth_state.router,
        profile_state.router,
        statistics_state.router,
        daily_food_state.router,
        exit_state.router,
        different_types.router,

    )

    dp.shutdown.register(stop_bot)
    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await set_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
