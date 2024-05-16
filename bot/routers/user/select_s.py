from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.settings import settings
from bot.utils.yndex_shedule import get_shedule

from datetime import datetime

router = Router()


@router.callback_query(F.data.startswith('from'))
async def get_to(callback: types.CallbackQuery, state: FSMContext):

    await state.update_data(from_=callback.data.split("_")[-1])

    builder = InlineKeyboardBuilder()
    stations = settings.stations_id
    for index, key in enumerate(stations.keys()):

        if index % 2 == 0:
            builder.row(
                InlineKeyboardButton(
                    text=key, callback_data=f"to_{stations[key]}"
                )
            )
        else:

            builder.button(
                text=key, callback_data=f"to_{stations[key]}"
            )
    await callback.message.delete()
    await callback.message.answer(text="Выберите станцию прибытия",
                                  reply_markup=builder.as_markup())


@router.callback_query(F.data.startswith("to_"))
async def get_shedules(callback: types.CallbackQuery, state: FSMContext):

    state_data = await state.get_data()

    if state_data["from_"] == callback.data.split("_")[-1]:

        await callback.answer("Нельзя выбирать ту же станцию.", show_alert=True)
    else:
        text = ""
        data = await get_shedule(from_=state_data["from_"], to_=callback.data.split("_")[-1])

        if data is None:
            await callback.answer("Произошла ошибка.")
        else:
            choose_station = settings.stations_id_reverse[callback.data.split("_")[-1]]
            for index, shedule in enumerate(data):

                if index == 10:
                    break

                title: str = shedule["thread"]["title"]
                print(title.split("-", maxsplit=1))
                departure_time = shedule["departure"]
                arrival_time = shedule["arrival"]

                duration = shedule["duration"] // 60
                price = None
                if shedule["tickets_info"]:

                    price = shedule["tickets_info"]["places"][0]["price"]["whole"]

                text += (f"{title.split("—", maxsplit=1)[0]} - {choose_station}\n"
                         f"{datetime.fromisoformat(departure_time).strftime('%H:%M')} - {datetime.fromisoformat(arrival_time).strftime('%H:%M')}\n"
                         f"Время в пути: {int(duration)} минут.")

                if price:
                    text += f" Цена: {price} RUB\n\n"
                else:
                    text += "\n\n"

        await callback.message.answer(
            text=text
        )