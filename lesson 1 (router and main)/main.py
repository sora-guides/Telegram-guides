import sys
import asyncio
import logging
from decouple import config

from aiogram import Dispatcher, Bot
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.additional_handler import router as add_route
from handlers.user_handler import router as user_route


async def main() -> None:
    dispatcher = Dispatcher()
    bot = Bot(
        token=config("TOKEN"),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    
    dispatcher.include_routers(
        add_route,
        user_route
    )
    # Есть два варианта подключить роутер. Перечислить все роутеры в include_routers
    # Либо в __init__ файле собрать все роутеры и в главной функции запихнуть
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout) 
    asyncio.run(main())
    # Логгеры в aiogram уже написаны, можно не делать свои