from aiogram.fsm.state import StatesGroup, State

class InfoState(StatesGroup):
    age = State()
    gender = State()
    birthday = State()
    phone_number = State()
