import telebot
import time

from telebot import types

bot = telebot.TeleBot('1652220208:AAFm0QJZ_KrzfAlny_X7HXcaa7_b7ERNb2o') #АPI bot'a который выдал Бот Фазер
bot.send_message(1561011865, 'Привет')

# @bot.message_handler(commands=['start'])
# def welcome(message):
#     bot.send_message(message.chat.id, 'Привет')

# def score(total):
#     with open('score.txt', 'r') as f:
#         score = int(f.read(1))

#         if total > 5:
#             score = score + 1

#         with open('score.txt', 'w') as f1:
#             if score > 2 and total < 6:
#                 f1.write(str(0))
#                 return ('Тотал 6')

#             if total <= 5:
#                 f1.write(str(0))
#                 return None
#             f1.write(str(score))

#     return None

# @bot.message_handler(content_types=['text'])
# def privateChat(message):
#     if message.chat.type == 'private':
#         total = int(message.text)
#         scorepoint = score(total)

#         if scorepoint != None:
#             bot.send_message(message.chat.id, scorepoint)

if __name__ == '__main__':
        print('start')
        while True:
            try:
                bot.polling(none_stop=True)
            except:
                pass
        print('stop')
