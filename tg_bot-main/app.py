from aiogram import Bot, Dispatcher
import asyncio
from handlers.private_handlers import private_router
from handlers.group_handler import group_router

TOKEN = "8371246441:AAGEP0b7kS38ZsuVBbtMES-yg-3cnt5Lye0"

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(private_router)
dp.include_router(group_router)  # Assuming group_router is defined in handlers/group_handler.py

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    print("Bot is polling...")

asyncio.run(main())















