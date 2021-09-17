import requests, telebot
from bs4 import BeautifulSoup
url = "https://vodokanal-ykt.ru/uvedomleniya-dlya-abonentov/"
def pars(url):
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
    }
    req = requests.get(url, headers=headers)
    src = req.text

    return src
#print(src)
#with open("index.html", "w") as file:
#    file.write(src)

soup = BeautifulSoup(pars(url), 'lxml')
url_item = soup.findAll("a", class_="_self pt-cv-href-thumbnail pt-cv-thumb-default")
#print(url_item)
j = 0
for i in url_item:
    j+=1
    if j == 10:
        break
    i_text = i.text
    url_news = i.get("href")
    soup_news = BeautifulSoup(pars(url_news), 'lxml')
    text_news = soup_news.find("div", class_="entry-content clear")
    if ('ФАПК “Якутия”') in text_news.text:
        s = text_news.text

bot = telebot.TeleBot('1967252257:AAG7rV1tfkXl2wqtIYl5lK77olUmOwGmwY8')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет" or "привет":
        bot.send_message(message.from_user.id, s)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)