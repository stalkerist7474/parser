import telebot
import os
import requests

from bs4 import BeautifulSoup
#from config import TOKEN
from dotenv import load_dotenv
from pathlib import Path



# получаем токен из env файла
load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv("TOKEN_T")


bot = telebot.TeleBot(TOKEN)


base = 'https://vc.ru/'
html = requests.get(base).content
soup = BeautifulSoup(html, 'lxml')
div = soup.find('div', class_='feed__item l-island-round')

url_news_html = div.find_all('div', class_='content--short')



for a in url_news_html:
    link_news = a.find('a', class_='content-link').get('href')


answer =  link_news
print(answer)



@bot.message_handler(content_types=['text'])
def send_last_news(message):
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)

