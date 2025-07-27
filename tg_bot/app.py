from aiogram import Bot, Dispatcher, types
import asyncio
from hendlers.hendler import private_router

TOKEN = "8282307419:AAEqxXxisZmZFjyaP_fKBsxo7lHKuaBl_P0"

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(private_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    print("Bot is polling...")

asyncio.run(main())















