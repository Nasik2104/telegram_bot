from aiogram import types
from aiogram.dispatcher import FSMContext
from .cutats import text
from loader import dp

import random

@dp.message_handler(commands=['saysomething'])
async def saysomething(message: types.Message):
    await message.answer(random.choice(text))

@dp.message_handler(text = 'Доброго ранку')
async def morning(message: types.Message):
    await message.answer('Доброго ранку, чим будеш снідати?')
    await message.answer_sticker("CAACAgIAAxkBAAOsZLLcqtFfzR_jr35VBZNR_AyVDTEAAsMOAAJccAlKrXuplxYXNaYvBA")

# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Эхо без состояния."
                         f"Сообщение:\n"
                         f"{message.text}")


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")
