from aiogram import Router, types, F
from filters.chat_types import ChatTypes

group_router = Router()
group_router.message.filter(ChatTypes(["group", "supergroup"]))

warned_users = {}

restricted_words = {"бовдур", "дурень", "тупий", "ідіот"}

@group_router.message()
async def ban_detector(message: types.Message):
    if restricted_words.intersection(message.text.lower().split(" ")):
        user_id = message.from_user.id
        if user_id in warned_users:
            warned_users[user_id] = warned_users[user_id] + 1
        else:
            warned_users[user_id] = 1
        print(warned_users)
        await message.answer(f"{message.from_user.first_name} {message.from_user.last_name}, ваше повідомлення містить заборонені слова.")
        await message.delete()
        