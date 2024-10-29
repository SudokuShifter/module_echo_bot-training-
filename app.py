import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
from config_data.config import Config, load_config

from handlers import other_handlers, user_handlers


async def main() -> None:

    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    async def hello_message():
        await bot.send_message(
            chat_id=504633851,
            text='<ins><i>Пример форматированного текста</i></ins>',
            parse_mode='HTML'
        )


    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    await hello_message()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
