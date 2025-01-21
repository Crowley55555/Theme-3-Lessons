while True:
    try:
        num = int(input("Введите целое число: "))
        num = int(num)
        print("Введенное число:", num)

    except ValueError:
        print("Невозможно преобразовать введенное значение в целое числo")
    except TypeError:
        print("Введенный символ не является числом")
    except KeyboardInterrupt:
        print("Попытка закрытия программы")