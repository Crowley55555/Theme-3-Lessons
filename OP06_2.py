#Создайте модуль arithmetic.py, который будет содержать 4 функции: сложение, вычитание, умножение и деление.\n
# Импортируйте модуль в другой файл Python и выполните каждую из функций с произвольными аргументами.

#Решение

while True:
    import arithmetic

    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    print(arithmetic.summa(a, b))
    print(arithmetic.mul(a, b))
    print(arithmetic.de(a, b))
    print(arithmetic.mi(a, b))
