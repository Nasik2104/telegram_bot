from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

need = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Хочу фільм", ),
            KeyboardButton("Хочу музику",)
        ]
    ],
    resize_keyboard=True
)
