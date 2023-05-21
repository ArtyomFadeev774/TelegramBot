import os
from dotenv import load_dotenv
import telebot
from telebot import types
from valute import *
from hello import *


load_dotenv()
token = os.getenv('TOKEN')

bot = telebot.TeleBot(token)

def create_keyboard():
    keyboard = types.ReplyKeyboardMarkup()
    buttons = create_buttons()
    for button in buttons:
        btn = types.KeyboardButton(button)
        keyboard.add(btn)
    return keyboard

@bot.message_handler(commands=['start', 'go'])
def start(message):
    #print(message)
    bot.send_message(message.from_user.id, 'Привет', reply_markup=create_keyboard())
    bot.send_message(message.from_user.id, hello, reply_markup=create_keyboard())

@bot.message_handler(content_types=['text'])
def go(message):
    try:
        res = get_data(message.text)
        bot.send_message(message.from_user.id, res)
    except: 
        bot.send_message(message.from_user.id, message.text)



print('Бот Работает!')
bot.polling(non_stop=True, interval=0)