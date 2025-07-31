from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from random import choice
from kbrds.reply import help_kb
private_router = Router()

@private_router.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer("Hello! напиши /help чтоб узнать что я умію",
                        reply_markup=help_kb.as_markup(resize_keboard=True))

@private_router.message(Command("help"))
async def command_help(message: types.Message):
    await message.answer("""
/start - старт
/help - команди
/info - інформація про користувача
/anekdot - анекдот
""")
    

@private_router.message(F.text == "info")
async def handle_hello(message: types.Message) -> None:
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_name = message.from_user.username
    user_id = message.from_user.id
    await message.answer(f""""
name-{first_name}
last_name-{last_name}
username-{user_name}
user_ad_id-{user_id}
""")
    
@private_router.message(F.text == "anekdot")
async def anekdot(message: types.Message):
    anekdots_list = [
        "— Що робити, якщо напав ведмідь? — Не знаю, а що? — Не нападати!",
        "— Лікарю, в мене пам’ять як у рибки! — І з чим ви до мене прийшли? — А з чим?",
        "Пішов Іван дощем... бо без парасольки.",
        "— Тату, а що таке сарказм? — Це коли ти питаєш, чи можна погратись на маминому ноуті... а я кажу: «Авжеж, синку, ламай, тільки глибше!»",
        "На уроці біології: — Петренко, назви частини тіла. — Голова, тулуб, ноги, руки, смартфон.",
        "Урок географії: — Вова, де знаходиться Америка? — В зошиті, третя сторінка знизу.",
        "Песик навчився відкривати двері лапою. Тепер він вважає себе кішкою.",
        "— Чому ти такий веселий? — Я зранку на ваги став... а вони зламались!",
        "Кіт спить 16 годин на добу. Може, він теж програміст?",
        "Прийшла весна. Пора худнути. Але прийшло й морозиво…"
    ]
    random_anekdot = choice(anekdots_list)
    await message.answer(random_anekdot)

