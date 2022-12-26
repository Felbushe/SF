import telebot
from config import keys, TOKEN
from utils import ConvertionExpection, Converter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = f'Привет {message.chat.username}! \n Я бот-конвертер валют.\n- Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\n-Увидеть список всех доступных валют:\n/values\n-Напомнить, что я могу через команду:\n /help'
    bot.reply_to(message, text)

@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\n Чтобы увидеть список всех доступных валют, введите команду:\n/values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
        bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) > 3:
            raise ConvertionExpection('Слишком много параметров.')
        if len(values) < 3:
            raise ConvertionExpection('Не хватает параметров.')

        quote, base, amount = values
        total_base = Converter.convert(quote, base, amount)
    except ConvertionExpection as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount}  {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()