import random

from bs4 import BeautifulSoup
import requests
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from keyboards.inline import to_kb_au

@dp.callback_query_handler(lambda callback_query: True,)
async def pars(call: types.CallbackQuery, ):
    print('dtd')
    callback_querry =call.data
    print(callback_querry)
    data = to_kb_au[callback_querry]
    print(data)
    url = data['url']
    print(url)
    my_answer = requests.get(url)
    soup = BeautifulSoup(my_answer.content, "html.parser")

    names = []
    audios = {}
    for data in soup.find_all('div', class_="plitem__title no__wrap track-item__title"):
        a = data.find("a", class_="pajax-link")
        href = a.get('href')
        author = a.text
        span = data.find(class_="no__wrap")
        name = span.text 
        print(href)
        print(author)
        print(name)
        
        audios[name] = {"url":"https://uamp3.org" + href,
                        "author":author.replace("-",""),
                        "name":name}
        names.append(name)
        
    random_audi_name = random.choice(names)
    random_audio = audios[random_audi_name]
    print(random_audio)
    await call.message.answer(f"<b>Назва --</b> {random_audio['name']}\n<b>Автор</b> -- {random_audio['author']}\n<b>Посилання</b> -- {random_audio['url']}")
    
    
