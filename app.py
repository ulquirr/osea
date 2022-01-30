import telebot
import os
from dotenv import load_dotenv
from collectInfo import updateStatsInformation

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.from_user.first_name
    bot.send_message(
        message.chat.id, f"Welcome {name} , type /send_floor and i will send you anatomy and mutant apes floor")


@bot.message_handler(commands=['send_floor'])
def send_floor(message):
    a, b = updateStatsInformation()
    
    bot.send_message(message.chat.id, "Anatomy floor: " + f'{a}' + "🐒\n" + "Mutant floor: " + f'{b}' + " 🧟‍♂️")

bot.infinity_polling()

