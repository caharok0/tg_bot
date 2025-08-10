from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

help_kb = ReplyKeyboardBuilder()
help_kb.add(
    KeyboardButton(text="info"),
    KeyboardButton(text="anekdot"),
    KeyboardButton(text="заповнити анкету")
)

help_kb.adjust(2, 1)

