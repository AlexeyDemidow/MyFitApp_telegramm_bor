from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram import F

from handlers.auth_handler import authorisation
from handlers.statistics_handler import statistics, water_statistics
from handlers.profile_handler import profile
from keyboards.main_keyboard import get_keyboard
from utils.callbacks import MainCallback
from utils.states import BotStates

router = Router()


@router.callback_query(MainCallback.filter(F.mcb == "statistics"))
async def statistics_callback_view(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    token = await authorisation(username=data["username"], password=data["password"])
    profile_data = await profile(auth_token=list(token.values())[0])
    daily_statistics = await statistics(auth_token=list(token.values())[0])
    water = await water_statistics(auth_token=list(token.values())[0])
    await call.message.answer(
        f'Статистика за сегодня:\n'
        f"Всего съедено продуктов - {daily_statistics.get('all_products')} шт\n"
        f"Дневная норма калорий - {daily_statistics.get('norm_calories')} Ккал\n"
        f"Калорий употреблено - {daily_statistics.get('calories_counter')} Ккал\n"
        f"Калорий осталось - {daily_statistics.get('remaining_calories_counter')} Ккал\n"
        f"Всего белков - {daily_statistics.get('protein_counter')} г\n"
        f"Всего жиров - {daily_statistics.get('fats_counter')} г\n"
        f"Всего углеводов - {daily_statistics.get('carb_counter')} г\n"
        f"Выпито стаканов воды - {water.get('all_glasses')}\n",
    )
    await call.message.answer(
        f"Привет, {list(profile_data.get('results')[0].values())[1]}, выберите что отобразить:",
        reply_markup=await get_keyboard()
    )
    await state.set_state(BotStates.auth)
