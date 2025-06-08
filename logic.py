import telebot
from config import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот по экологии. Напиши команду /hello, /bye, /statistic, /country_status или /advices  ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['statistic'])
def send_password(message):
    statistic = "https://tochno.st/problems/ecology"
    bot.reply_to(message, f"Вот статистика по экологии на сегодняшний день: {statistic}")

@bot.message_handler(commands=['ecology_status'])
def send_emodji(message):
    country_status = "https://nonews.co/directory/lists/countries/ecology"
    bot.reply_to(message, f"Вот таблица статуса каждой страны в мире': {country_status}")

@bot.message_handler(commands=['advices'])
def send_coin(message):
    advices = "https://rusarctica.ru/blog/idei-i-layfkhaki/kak-spasti-prirodu-8-shagov-kotorye-mozhet-sdelat-kazhdyy/"
    bot.reply_to(message, f"Вот список советов на улучщение экологии мира: {advices}")

bot.polling()
