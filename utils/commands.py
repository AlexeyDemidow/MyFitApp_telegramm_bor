from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начать работу',
        ),
        BotCommand(
            command='site',
            description='Перейти на страницу вею-приложения MyFitApp',
        ),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
