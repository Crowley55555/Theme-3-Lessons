#Задание 3: Обработка исключений прошлых программ
#Возьми одну из программ, которую мы писали на прошлых уроках, продумай, какие ошибки в программе могут появляться(можно прям специально пробовать ее ломать) и дополни код конструкцией try-except для обработки выявленных исключений.

while True:
    try:
      def bank(a, years):
        # Процентная ставка
        interest_rate = 0.10

        # Итоговая сумма
        total_amount = a

        # Цикл по количеству лет
        for year in range(years):
          total_amount += total_amount * interest_rate

        return total_amount


      # Пример использования функции:
      if __name__ == "__main__":
        a = float(input("Введите сумму вклада (в рублях): "))
        years = int(input("Введите срок вклада (в годах): "))

        result = bank(a, years)
        print(f"Сумма на счету через {years} лет составит: {result:.2f} рублей")

    except KeyboardInterrupt:
      print("  Попытка закрытия программы")
    except TypeError:
      print("Неверное значение")
    except ValueError:
      print("Ошибка ввода")