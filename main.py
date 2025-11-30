import telebot
import random
import schedule
import time
import threading
from config import token
from facts import FACTS
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(token)

subscribed_users = set()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я Telegram бот. Я помогу решить проблему глобального потепления!")

@bot.message_handler(commands=['news'])
def send_news(message):
    bot.reply_to(message, "Вот ссылка на самые новые новость в мире глобального потепления: https://ria.ru/keyword_globalnoe_poteplenie/")

@bot.message_handler(commands=['facts'])
def send_facts(message):
    bot.reply_to(message, random.choice(FACTS))

@bot.message_handler(commands=['subscribe'])
def subscribe_daily(message):
    user_id = message.chat.id
    if user_id not in subscribed_users:
        subscribed_users.add(user_id)
        bot.reply_to(message, "✅ Вы подписались на ежедневную рассылку! Рассылка происходит раз в 24 часа.")
    else:
        bot.reply_to(message, "❌ Вы уже подписаны на рассылку!")

@bot.message_handler(commands=['unsubscribe'])
def unsubscribe(message):
    user_id = message.chat.id
    if user_id in subscribed_users:
        subscribed_users.remove(user_id)
        bot.reply_to(message, "🔕 Вы отписались от рассылки.")
    else:
        bot.reply_to(message, "ℹ️ Вы не были подписаны на рассылку.")

def news():
    print("Вот ссылка на самые новые новость в мире глобального потепления: https://ria.ru/keyword_globalnoe_poteplenie/")

user_id = message.chat.id
if user_id in subscribed_users:
    schedule.every().day.at("12:00").do(news)
