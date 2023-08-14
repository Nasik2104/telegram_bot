import random

from bs4 import BeautifulSoup
import requests
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.inline import to_kb


@dp.callback_query_handler(lambda callback_query: True, state="Flow:Film_state", )
async def pars(call: types.CallbackQuery, state=FSMContext):
    callback_querry = call.data
    data = to_kb[callback_querry]
    url = data['url']
    my_answer = requests.get(url)
    soup = BeautifulSoup(my_answer.content, "html.parser")
    films = {}
    names = []
    for text in soup.find_all('a', class_='short-title'):
        href_value = text.get('href')
        data_for_description = requests.get(href_value)
        soup2 = BeautifulSoup(data_for_description.content, 'html.parser')
        description = soup2.find('div', attrs={"itemprop": "description"})
        photo = soup2.find('a', attrs={"data-fancybox": True})
        photo_url = photo['href']
        films[text.text] = {
            "description": description.get_text(strip=True) if description else "",
            'url': href_value,
            'photo': photo_url
        }
        names.append(text.text)
    random_film_name = random.choice(names)
    random_film = films[random_film_name]
    message_text = f"<b>Назва</b> -- {random_film_name}\n\n<b>Опис</b> -- {random_film['description']}\n\n<b>Посилання</b> -- {random_film['url']}"
    await call.message.answer(message_text, parse_mode='html')
    await call.message.answer_photo(random_film['photo'])
    await state.finish()
    
