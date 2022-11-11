import logging

import telebot
from telebot import types

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)  # Outputs debug messages to console.

bot = telebot.TeleBot('5277345966:AAGxh5pqqilQsyjAOn7ADNC893m6Er9F12c')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "PIDORAS")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
