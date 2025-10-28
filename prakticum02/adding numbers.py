'''Напишите программу, которая считывает число "n" и вычисляет выражение "n + nn + nnn", где "nn" — это
число "n", записанное дважды, а "nnn" — трижды.
Пример вывода:
Введите число: 5
Значение выражения: 615'''
num = int(input("Enter a integer number (from 0 to 9): "))
num1 = str(num)
num2 = str(num1 + num1)
num3 = str(num1 + num2)
print("Значение выражения:", str(int(num1)+int(num2)+int(num3)))