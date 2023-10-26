from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from handlers.auth_handler import authorisation
from handlers.profile_handler import profile
from keyboards.main_keyboard import get_keyboard
from keyboards.start_keyboard import start_keyboard
from utils.callbacks import MainCallback
from utils.states import BotStates

router = Router()


@router.callback_query(MainCallback.filter(F.mcb == "auth"))
async def auth_username(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        'Введите логин.'
    )
    await state.set_state(BotStates.auth_username)


@router.message(BotStates.auth_username)
async def auth_password(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer(
        text='Введите пароль.'
    )
    await state.set_state(BotStates.auth_password)


@router.message(BotStates.auth_password)
async def auth(message: Message, state: FSMContext):
    await state.update_data({'password': message.text})
    data = await state.get_data()
    token = await authorisation(username=data["username"], password=data['password'])
    if 'auth_token' not in token:
        await message.answer(
            f"Невозможно войти с предоставленными учетными данными.",
        )
        await message.answer(
            f"Выберите нужную команду в меню",
            reply_markup=await start_keyboard()
        )
    else:
        profile_data = await profile(auth_token=list(token.values())[0])
        await message.answer(
            f"Привет, {list(profile_data.get('results')[0].values())[1]}, выберите что отобразить:",
            reply_markup=await get_keyboard()
        )
        await state.set_state(BotStates.auth)



