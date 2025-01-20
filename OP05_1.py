#Использовать конструкцию try-except
try:
    a = float(input("Введите число: "))
    b = float(input("Введите число: "))
    c = a / b
    print(c)
#Обрабатываeм исключение:
except ZeroDivisionError:
    c = None
except ValueError:
    c = ("Failed")
    print(c)