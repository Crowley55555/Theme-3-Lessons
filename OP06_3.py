#Импортируем модуль для генерации случайных чисел.
import random

# Считываем входноqсписок учащихся:**
file = open("names1.txt", encoding="utf-8")
with open("names1.txt", encoding="utf-8") as file:
    names = file.read().splitlines()

#Используем метод for для случайного выбора 5 уникальных имён из списка.
list = ""
for i in range (5):
  list += random.choice(names)
  a = list
# печатаем результат
  print(f"Список учащихся: {a}")