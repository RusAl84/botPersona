import telebot
import bot_config
import subprocess


API_key=bot_config.API_key
bot = telebot.TeleBot(API_key);

default_message = """/del - очистить текущие данные
/reset - перезагрузить Персону

"""


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if len(str(message.text))>3:
        if str(message.text).lower() == "привет":
            bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        elif str(message.text).lower() == "/reset":
            subprocess.run(["./zdata.py", ""])
            bot.send_message(message.from_user.id, "Персона перезагружена")
        else:
            bot.send_message(message.from_user.id, default_message)

bot.polling(none_stop=True, interval=0)