import telebot
import bot_config
import subprocess


API_key=bot_config.API_key
bot = telebot.TeleBot(API_key);

default_message = """/del - очистить текущие данные
/reset - перезагрузить Персону
"""
global name
global desc
global filename
global pass="1254"
name = ""
desc = ""
filename = ""

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    
    if len(str(message.text))>3:
        if str(message.text).lower() == "/del":
            global filename
            filename = ""
            bot.send_message(message.from_user.id, "Данные сброшены")
        elif str(message.text).lower() == "/reset":
            subprocess.run(["python", "./zdata.py"])
            bot.send_message(message.from_user.id, "Персона перезагружена")
        else:
            global filename
            bot.send_message(message.from_user.id, default_message + '/n'+ filename)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    global filename
    filename = "image.jpg"
    with open(filename, 'wb') as new_file:
        new_file.write(downloaded_file)
    
    bot.send_message(message.chat.id, "Фото загружено")
 

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)