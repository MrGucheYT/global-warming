import telebot
import random
import schedule
import time
import threading
from config import token
from facts import FACTS
from tips import TIPS

bot = telebot.TeleBot(token)

subscribed_users = set()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я Telegram бот. Я помогу решить проблему глобального потепления!")

@bot.message_handler(commands=['news'])
def send_news(message):
    bot.reply_to(message, "Вот ссылка на самые свежие новости в мире глобального потепления: https://ria.ru/keyword_globalnoe_poteplenie/")

@bot.message_handler(commands=['facts'])
def send_facts(message):
    bot.reply_to(message, random.choice(FACTS))

@bot.message_handler(commands=['tips'])
def send_tips(message):
    bot.reply_to(message, random.choice(TIPS))

@bot.message_handler(commands=['subscribe'])
def subscribe_daily(message):
    user_id = message.chat.id
    if user_id not in subscribed_users:
        subscribed_users.add(user_id)
        bot.reply_to(message, "✅ Вы подписались на ежедневную рассылку! Рассылка происходит раз в 24 часа.")
        news(message)
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

@bot.message_handler(commands=['help'])  
def handle_help(message):  
    help_text = (  
        "/start - Начать работу с ботом\n"  
        "/help - Получить список команд\n"  
        "/tips - Отправляет рандомный способ решения проблемы глобального потепления\n"
        "/facts - Отправляет рандомный факт о глобальном потеплении\n"
        "/news - Даёт ссылку на все свежие новости о глобальном потеплении\n"
        "/subscribe - При отправке команды, вы подписываетесь на рассылку новостной ссылки каждый день\n"
        "/unsubscribe - При отправке команды, вы отписываетесь от рассылки\n"
    )    
    bot.send_message(message.chat.id, help_text)  

def news(message):
    bot.send_message(message.chat.id, "Вот ссылка на самые свежие новости в мире глобального потепления: https://ria.ru/keyword_globalnoe_poteplenie/")
    user_id = message.chat.id
    if user_id in subscribed_users:
        schedule.every().day.at("12:00").do(news)
        while True:
            schedule.run_pending()
            time.sleep(1)

bot.polling()

