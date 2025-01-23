#Напишите скрипт, который запрашивает у пользователя текст, а затем записывает этот
#текст в файл user_data.txt.
user_input = input("Введите текст: ")
with open("user_data.txt", "w", encoding="utf-8") as f:
    f.write(user_input)
    result = (user_input)
    print(f"Текст {result} добавлен в файл user_data")