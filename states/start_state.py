from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.start_keyboard import start_keyboard
from utils import messages
from utils.states import BotStates

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        messages.GREETINGS
    )
    await message.answer(
        'Выберите нужную команду в меню',
        reply_markup=await start_keyboard()
    )
    await state.set_state(BotStates.start)


@router.message(Command("site"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        messages.SITE
    )
    await message.answer(
        'Выберите нужную команду в меню',
        reply_markup=await start_keyboard()
    )
    await state.set_state(BotStates.start)
