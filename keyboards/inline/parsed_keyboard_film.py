from bs4 import BeautifulSoup
import requests
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import pprint

link = "https://kinoukr.com/"

my_answer = requests.get(link)

soup = BeautifulSoup(my_answer.content, "html.parser")
data = soup.find('ul', class_="rzmenu__list fx-row")
names = data.find_all('a')

to_kb = {}
for link in names:
    href_value = link.get('href')
    url = "https://kinoukr.com/" + href_value

    to_kb[href_value]={"url":url,
                       "name":link.text}

film = InlineKeyboardMarkup(
)
list_to_kb = []
for href, name in to_kb.items():
    button = InlineKeyboardButton(text=name['name'], callback_data=href)
    list_to_kb.append(button)
    print(list_to_kb)
    if len(list_to_kb) == 2:   
        film.add(*list_to_kb)
        list_to_kb.clear()
    
if list_to_kb:
    film.add(*list_to_kb)