from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.inline import film
from keyboards.inline import audi
from keyboards.default import need
from states.flow import Flow

@dp.message_handler(commands="film_and_audio")
async def film_and_audio(message: types.Message):
    await message.answer("Вибирайте", reply_markup=need)

@dp.message_handler(text = 'Хочу фільм')
async def film_and_audio(message: types.Message, state: FSMContext):
    await message.answer("Виберіть жанр:", reply_markup=film)
    await Flow.Film_state.set()

@dp.message_handler(text = 'Хочу музику')
async def film_and_audio(message: types.Message):
    await message.answer("Виберіть жанр:", reply_markup=audi)
    