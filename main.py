from aiogram import Dispatcher, Bot

from bot.settings import settings
from bot.routers import register_all_routers

import asyncio, logging


async def main():

    bot = Bot(token=settings.BOT_TOKEN)

    dp = Dispatcher()

    register_all_routers(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
