import telebot

TOKEN = 'yourtoken'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('hello.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("my code")
    item2 = types.KeyboardButton("dm me")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Hi from , {0.first_name}!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    
    @bot.message_handler(content_types=['text'])
    def text(message):
        if message.chat.type == 'private':
            if message.text == 'my code':
                bot.send_message(message.chat.id, 'https://github.com/royalehoneybadger')
            elif message.text == 'dm me':
                bot.send_message(message.chat.id, 'https://t.me/440781040')
            else:
                bot.send_message(message.chat.id, 'I dont kow how to respond')


bot.polling(none_stop=True)
