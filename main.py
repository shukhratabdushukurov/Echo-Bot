import os
from dotenv import load_dotenv
from telebot import types, TeleBot

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = TeleBot(BOT_TOKEN, parse_mode='HTML')
# print(bot.get_me())
@bot.message_handler(commands=['start', 'info', 'about'])
def handle_commands(message:types.Message):
    username = message.chat.username
    chat_id = message.chat.id
    # print(message)
    if message.text == '/start':
        bot.send_message(chat_id, f'Hello <b><i>{username}</i></b>')
    elif message.text == '/info':
        bot.send_message(chat_id, 'info')
    elif message.text == '/about':
        bot.send_message(chat_id, 'about')

@bot.message_handler(func=lambda message: message.text == 'книги')
def handle_books(message: types.Message):
    bot.send_message(message.chat.id, 'Это Ваш список книг')

@bot.message_handler(content_types=['text'])
def handle_text(message: types.Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, message.text)

@bot.message_handler(content_types=['voice'])
def handle_voice(message: types.Message):
    print(message.voice)
    chat_id = message.chat.id
    bot.send_voice(chat_id, message.voice.file_id)

@bot.message_handler(content_types=['audio'])
def handle_audio(message: types.Message):
    print(message.audio)
    chat_id = message.chat.id
    bot.send_audio(chat_id, message.audio.file_id)

@bot.message_handler(content_types=['document'])
def handle_document(message: types.Message):
    print(message.document)
    chat_id = message.chat.id
    bot.send_document(chat_id, message.document.file_id)

bot.infinity_polling()