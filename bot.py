import telebot
from telebot import types

bot = telebot.TeleBot('7248912389:AAHlCUX8-pjS6T9nwhA47t3Q_lL1c_I5XjA')


@bot.message_handler(commands=['start'])
def start_message(massage):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(massage.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "👋 Поздороваться":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Как пользоваться поискавиком ?')
        btn2 = types.KeyboardButton('Что такое поисковик ?')
        btn3 = types.KeyboardButton('Зачем нужен поисковик ?')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Задайте интересующий вас вопрос ?', reply_markup=markup)

    elif message.text == 'Как пользоваться поискавиком ?':
        bot.send_message(message.from_user.id, 'Загугли')

    elif message.text == 'Что такое поисковик ?':
        bot.send_message(message.from_user.id, 'Это поисковик')

    elif message.text == 'Зачем нужен поисковик ?':
        bot.send_message(message.from_user.id, 'Для создания запросов')


bot.polling(none_stop=True, interval=0)
