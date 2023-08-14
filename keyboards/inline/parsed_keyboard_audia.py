from bs4 import BeautifulSoup
import requests
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import pprint

link = 'https://uamp3.org/'

my_answer = requests.get(link)

soup = BeautifulSoup(my_answer.content, "html.parser")

to_kb_au = {}
for data in soup.find_all(class_ = "cat__item")[4:13]:
    a = data.find('a', class_ = "pajax-link")
    href = a.get('href')
    url = "https://uamp3.org" + href
    
    to_kb_au[href]={"url":url,
                    "name":a.text}
    
audi = InlineKeyboardMarkup()
list_to_kb_au = []
for href, name in to_kb_au.items():
    button = InlineKeyboardButton(text=name['name'], callback_data=href)
    list_to_kb_au.append(button)
    print(list_to_kb_au)
    if len(list_to_kb_au) == 2:   
        audi.add(*list_to_kb_au)
        list_to_kb_au.clear()
    
if list_to_kb_au:
    audi.add(*list_to_kb_au)



 