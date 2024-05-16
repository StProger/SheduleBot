from aiogram import Dispatcher

from bot.routers import start
from bot.routers.user import select_s


def register_all_routers(dp: Dispatcher):
    dp.include_router(start.router)
    dp.include_router(select_s.router)
