import telebot
import datetime
import time
import threading
import random
from telebot import types
import json
import os

bot = telebot.TeleBot('7795687126:AAFcz0gtTEy94lUjrntsHiFBk9zEb_3F2kk')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я чат бот который будет напоминать тебе что можно жить лучше!')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    fact_button = types.KeyboardButton("Получить мотивашку")
    markup.add(fact_button)

    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.message_handler(commands=['fact'])
def fact_message(message):
    with open("motivaxa.txt", encoding="utf-8") as file:
        list = [line.strip() for line in file if line.strip()]
        random_fact = random.choice(list)
        bot.reply_to(message, f'Лови мотивашку {random_fact}')
        send_messages.add(random_fact)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Получить мотивашку":
        fact_message(message)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите действие из меню.")
send_messages = set()

def send_reminders(chat_id):
    first_rem = "20:27"
    second_rem = "20:28"
    end_rem = "20:29"

    with open("motivaxa.txt", encoding="utf-8") as file:
        list1 = [line.strip() for line in file if line.strip()]

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == first_rem:
            random_fact1 = random.choice(list1)
            while random_fact1 in send_messages:
                random_fact = random.choice(list1)
            bot.send_message(chat_id, text=f"Вот твоя мотивашка - {random_fact1}")
            send_messages.add(random_fact1)
            time.sleep(61)
            continue
        if now == second_rem:
            random_fact1 = random.choice(list1)
            while random_fact1 in send_messages:
                random_fact = random.choice(list1)
            bot.send_message(chat_id, text=f"Вот твоя мотивашка - {random_fact1}")
            send_messages.add(random_fact1)
            time.sleep(61)
            continue
        if now == end_rem:
            random_fact1 = random.choice(list1)
            while random_fact1 in send_messages:
                random_fact = random.choice(list1)
            bot.send_message(chat_id, text=f"Вот твоя мотивашка - {random_fact1}")
            send_messages.add(random_fact1)
            time.sleep(61)
            continue
        time.sleep(1)

bot.polling(none_stop=True)
