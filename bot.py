import telebot
from time import sleep
bot = telebot.TeleBot("5287776172:AAFEwlece-h_cTSJjYAgURPMGF0cPO5aIno")

@bot.message_handler(content_types=['text'])
def start(message):
	if message.text == '/reg':
		bot.send_message(message.from_user.id, "Как тебя зовут?");
		bot.register_nest_step_handler(message, get_name);
	else:
		bot.send_message(message.from_user.id, "Напиши /reg");
    
