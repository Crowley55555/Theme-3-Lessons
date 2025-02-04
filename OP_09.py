import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('7795687126:AAFcz0gtTEy94lUjrntsHiFBk9zEb_3F2kk')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я чат бот который будет напоминать тебе что можно жить лучше!')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()


@bot.message_handler(commands=['fact'])
def fact_message(message):
    list = ["**Каждый день — новый шанс сделать шаг к своей мечте!**",
            "**Трудности — это ступеньки к успеху, не бойся их преодолевать!**",
            "**Ты способен на большее, чем думаешь. Верь в себя!**",
            "**Не откладывай на завтра то, что может изменить твою жизнь сегодня!**",
            "**Каждый маленький шаг приближает тебя к большой цели.**",
            "**Мы не можем изменить прошлое, но мы можем начать сегодня делать лучшим свое завтра**"]
    random_fact = random.choice(list)
    bot.reply_to(message, f'Лови мотивашку {random_fact}')

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