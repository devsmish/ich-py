'''Умножение чисел
Напишите программу, которая получает два числа от пользователя, умножает одно число на второе
и выводит результат и оба числа через дефис. Не сохраняете результат умножения в переменной.
Пример вывода:
Введите первое число: 4
Введите второе число: 5
Результат: 20-4-5'''

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print(first_number*second_number, first_number, second_number, sep="-")