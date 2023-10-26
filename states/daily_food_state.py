from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram import F

from handlers.auth_handler import authorisation
from handlers.daily_food_handler import daily_food
from handlers.profile_handler import profile
from keyboards.main_keyboard import get_keyboard
from utils.callbacks import MainCallback
from utils.states import BotStates

router = Router()


@router.callback_query(MainCallback.filter(F.mcb == "daily_food"))
async def daily_food_callback_view(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    token = await authorisation(username=data["username"], password=data["password"])
    profile_data = await profile(auth_token=list(token.values())[0])
    food = await daily_food(auth_token=list(token.values())[0])
    cats = ['breakfast', 'lunch', 'dinner', 'snacks']
    cats_ru = ['Завтрак', 'Обед', 'Ужин', 'Перекусы']
    if not food.get('results'):
        await call.message.answer(f"Сегодня нет записанных приемов пищи\n")
    else:
        await call.message.answer(f"Продукты употребленные сегодня:\n")
        for i in food.get('results'):
            for j in range(len(cats)):
                if i.get("category") == cats[j]:
                    await call.message.answer(f"{cats_ru[j]}:\n")
                    await call.message.answer(
                        f'{i.get("fooditem_name")}\n'
                        f'Масса - {i.get("quantity")} г\n'
                        f'Белки - {i.get("fooditem_protein")} г\n'
                        f'Жиры - {i.get("fooditem_fats")} г\n'
                        f'Углеводы - {i.get("fooditem_carbohydrate")} г\n'
                        f'Калории - {i.get("fooditem_calorie")} Ккал\n'
                    )
    await call.message.answer(
        f"Привет, {list(profile_data.get('results')[0].values())[1]}, выберите что отобразить:",
        reply_markup=await get_keyboard()
    )
    await state.set_state(BotStates.auth)
