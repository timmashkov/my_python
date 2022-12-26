import logging
import random
import telebot


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)  # Outputs debug messages to console.

bot = telebot.TeleBot('5277345966:AAGxh5pqqilQsyjAOn7ADNC893m6Er9F12c')

def my_project():
    def is_valid(number):
        if 1 <= number <= 100:
            return True
        else:
            return False


    number = random.randint(1, 100)
    phrase = 'Добро пожаловать в числовую угадайку'
    print(phrase)
    while True:
        your_number = int(input('Введите число от 1 до 100:'))
        if is_valid(your_number) == True:
            print(int(your_number))
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
        if your_number > number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif your_number < number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
