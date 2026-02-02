'''Деление без ошибок
Напишите функцию, которая выполняет деление двух чисел, введенных пользователем, и обрабатывает возможные ошибки.
Пример вывода:
Введите делимое: 345
Введите делитель: 5a
Ошибка: Введено некорректное число.'''
def dividing_numbers(n: float, m: float) -> float:
    try:
        return n / m
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль")
        return None

while True:
    dividend = input("Введите делимое: ")
    divisor = input("Введите делитель: ")
    try:
        dividend = float(dividend)
        divisor = float(divisor)
        print('Вы ввели числа:', dividend, "и", divisor )
        result = dividing_numbers(dividend, divisor)
        if result is not None:
            print("Результат их деления:", result)
        break
    except ValueError:
        print("Ошибка: Введено некорректное число.")

'''Логирование ошибок
Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log в соответствии с форматом ниже.
Пример вывода:
2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.'''
import logging

logging.basicConfig(
    filename="errors.log",
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s",
    level=logging.INFO
)

logging.info("Программа запущена")


def dividing_numbers(n: float, m: float) -> float | None:
    try:
        result = n / m
        logging.info(f"Успешное деление: {n} / {m} = {result}")
        return result
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль")
        logging.error(f"Попытка деления на ноль: {n} / {m}")
        return None


while True:
    dividend = input("Введите делимое: ")
    divisor = input("Введите делитель: ")

    try:
        dividend = float(dividend)
        divisor = float(divisor)

        print("Вы ввели числа:", dividend, "и", divisor)

        result = dividing_numbers(dividend, divisor)
        if result is not None:
            print("Результат их деления:", result)

        break

    except ValueError:
        print("Ошибка: Введено некорректное число.")
        logging.error(f"Некорректный ввод: '{dividend}', '{divisor}'")