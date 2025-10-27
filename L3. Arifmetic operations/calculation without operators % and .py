'''Вычисление без операторов % и //
Напишите программу, которая получает два числа от пользователя и вычисляет:
Остаток от деления
Результат целочисленного деления
Решить без использования операторов % и //.
Пример ввода:
Введите первое число: 10
Введите второе число: 3
Пример вывода:
Остаток от деления: 1
Целочисленное деление: 3'''

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

whole = remaind = 0
whole = int(first_number / second_number)
remaind = first_number - second_number * whole

print("Целая часть: ", whole)
print("Остаток: ", remaind)