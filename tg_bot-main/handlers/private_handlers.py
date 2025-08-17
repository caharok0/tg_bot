
from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from random import choice
from kbrds.reply import help_kb
from storage.data import InfoState
from aiogram.fsm.context import FSMContext
from filters.chat_types import ChatTypes

private_router = Router()
private_router.message.filter(ChatTypes(["private"]))

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

@private_router.message(F.text == "заповнити анкету")
async def fill_age(message: types.Message, state: FSMContext):
    await message.answer("скільки тобі років")
    await state.set_state(InfoState.age)

@private_router.message(InfoState.age)
async def fill_gender(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Хлопець|Дівчина")
    await state.set_state(InfoState.gender)

@private_router.message(InfoState.gender)
async def fill_city(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await message.answer("З якого ти міста")
    await state.set_state(InfoState.phone_number)

@private_router.message(InfoState.phone_number)
async def fill_city(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await message.answer("номер телефону")
    await state.set_state(InfoState.birthday)

@private_router.message(InfoState.birthday)
async def fill_city(message: types.Message, state: FSMContext):
    await state.update_data(birthday=message.text)
    data = await state.get_data()
    print(data)
    await message.answer(f"""
дякую за заповнення анкети
вік {data["age"]}
стать {data["gender"]}
номер телефону {data["phone_number"]}
день народження {data["birthday"]}
""")
    await state.clear()
