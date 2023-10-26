from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram import F

from handlers.auth_handler import authorisation
from handlers.profile_handler import profile
from keyboards.main_keyboard import get_keyboard
from utils.callbacks import MainCallback
from utils.states import BotStates

router = Router()


@router.callback_query(MainCallback.filter(F.mcb == "profile"))
async def profile_callback_view(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    token = await authorisation(username=data["username"], password=data["password"])
    profile_data = await profile(auth_token=list(token.values())[0])
    await call.message.answer(
        f'Профиль:\n'
        f"Псевдоним: {list(profile_data.get('results')[0].values())[1]}\n"
        f"email: {list(profile_data.get('results')[0].values())[2]}\n"
        f"Пол: {list(profile_data.get('results')[0].values())[3]}\n"
        f"Год рождения: {list(profile_data.get('results')[0].values())[4]}\n"
        f"Рост: {list(profile_data.get('results')[0].values())[5]}\n"
        f"Вес: {list(profile_data.get('results')[0].values())[6]}\n"
        f"Уровень активности: {list(profile_data.get('results')[0].values())[7]}\n",
    )
    await call.message.answer(
        f"Привет, {list(profile_data.get('results')[0].values())[1]}, выберите что отобразить:",
        reply_markup=await get_keyboard()
    )
    await state.set_state(BotStates.auth)
