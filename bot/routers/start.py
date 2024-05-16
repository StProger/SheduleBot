from aiogram import Router, F, types
from aiogram.filters import StateFilter
from aiogram.filters.command import CommandStart
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext

from bot.settings import settings

router = Router()


@router.message(CommandStart(), StateFilter("*"))
async def start(message: types.Message):
    builder = InlineKeyboardBuilder()
    stations = settings.stations_id
    for index, key in enumerate(stations.keys()):

        if index % 2 == 0:
            builder.row(
                InlineKeyboardButton(
                    text=key, callback_data=f"from_{stations[key]}"
                )
            )
        else:

            builder.button(
                text=key, callback_data=f"from_{stations[key]}"
            )

    await message.answer("Выберите станцию отправления",
                         reply_markup=builder.as_markup())



