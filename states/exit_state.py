from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from handlers.auth_handler import authorisation
from handlers.exit_handler import bot_exit
from keyboards.start_keyboard import start_keyboard
from utils.callbacks import MainCallback


router = Router()


@router.callback_query(MainCallback.filter(F.mcb == "exit"))
async def exit_callback_view(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    token = await authorisation(username=data["username"], password=data["password"])
    escape = await bot_exit(auth_token=list(token.values())[0])
    await callback.message.answer(
        f'{escape}\n',
    )
    await callback.message.answer(
        'Выберите нужную команду в меню.',
        reply_markup=await start_keyboard()
    )
    await state.clear()
