import os
from dotenv import load_dotenv
from telebot import types, TeleBot

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = TeleBot(BOT_TOKEN)
# print(bot.get_me())
@bot.message_handler(commands=['start'])