from aiogram.fsm.state import State, StatesGroup


class BotStates(StatesGroup):
    start = State()
    auth_username = State()
    auth_password = State()
    auth = State()

