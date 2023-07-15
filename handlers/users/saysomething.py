from .cutats import text
from loader import dp

import random

from aiogram import types


@dp.message_handler(commands=['saysomething'])
async def saysomething(message: types.Message):
    message.answer(random.choice(text))