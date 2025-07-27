from aiogram import Router, types, F,dp
from aiogram.filters import Command

private_router = Router()

@Router.message(commands=['start'])
async def command_start(message: types.Message):
    await message.answer("Hello!")

@private_router(F.text == "Hello")
async def handle_hello(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_name = message.from_user.username
    user_ad_id = message.from_user.id
    await message.answer(""""
name-{first_name}
last_name-{last_name}
username-{user_name}
user_ad_id-{user_ad_id}
""")

