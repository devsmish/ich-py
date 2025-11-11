# # a = 1 + 3
# n = 17
#
# result = None
# if n % 2 == 0:
#     result = "Четное"
# else:
#     result = "Нечетное"
#
#
# result = "Четное" if n % 2 == 0 else "Нечетное"
#
# print("Четное" if n % 2 == 0 else "Нечетное")
#
# # 17 -> not 1 -> not True -> False
# print("Четное" if not n % 2 else "Нечетное")
# print("Нечетное" if n % 2 else "Четное")
#

# a = 2.5
import math
# print(classic_round)


# Напишите программу, которая получает от пользователя цену
# на товар и количество
# товара. Программа должна рассчитать итоговую сумму
# заказа со скидкой, исходя из
# количества товара. Цену нужно округлить до сотых.
# Условия скидки:
# ● Если количество товара от 10 до 19 — скидка 5%.
# ● Если количество товара от 20 до 49 — скидка 10%.
# ● Если количество товара от 50 до 99 — скидка 15%.
# ● Если количество товара 100 и более — скидка 20%.
# Пример вывода:
# Введите цену товара: 100
# Введите количество товара: 25
# Сумма заказа с учётом скидки: 2250.00

price = int(input("Price: "))
quantity = int(input("Quantity: "))
if 10 <= quantity <= 19:
    discount = 5
elif 20 <= quantity <= 49:
    discount = 10
elif 50 <= quantity <= 99:
    discount = 15
else:
    discount = 20

print(price * quantity * (1 - discount / 100))

# Python Fundamentals 2025: Домашнее задание 5
# Решение домашних задач с оптимизацией
'''1. Сортировка чисел
Напишите программу, которая запрашивает у пользователя три числа и выводит их в порядке возрастания, разделенные запятой.
Пример вывода:
Введите первое число: 5
Введите второе число: 2
Введите третье число: 7
Числа в порядке возрастания: 2, 5, 7'''
# teacher
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

if num1 > num2:
    num1, num2 = num2, num1
if num1 > num3:
    num1, num3 = num3, num1
if num2 > num3:
    num2, num3 = num3, num2

print("Числа в порядке возрастания:", num1, num2, num3)
# 3 1 2
# 1 3 2
# 1 3 2
# 1 2 3

# Another variant
num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_3 = int(input("Введите третье число: "))

bigger = 0
smaller = 0
average = 0

if num_1 > num_2 and num_1 > num_3:

    bigger = num_1

elif num_2 > num_1 and num_2 > num_3:

    bigger = num_2

elif num_3 > num_1 and num_3 > num_2:

    bigger = num_3

if (num_1 > num_2 and num_1 < num_3) or (num_1 < num_2 and num_1 > num_3):

    average = num_1

elif (num_2 > num_1 and num_2 < num_3) or (num_2 < num_1 and num_2 > num_3):

    average = num_2

elif (num_3 > num_1 and num_3 < num_2) or (num_3 < num_1 and num_3 > num_2):

    average = num_3

if (num_1 < num_2 and num_1 < num_3):

    smaller = num_1

elif (num_2 < num_1 and num_2 < num_3):

    smaller = num_2

elif (num_3 < num_1 and num_3 < num_2):

    smaller = num_3

print("Числа в порядке возрастания: ", smaller, average, bigger)

# variant 2
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
c = int(input("Введите третье число:"))
if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    print(a, c, b)
elif b <= c <= a:
    print(b, c, a)
elif b <= a <= с:
    print(b, a, c)
elif c <= a <= b:
    print(c, a, b)
elif c <= b <= a:
    print(c, b, a)

# variant3
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))


if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
else:
    if num1 <= num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)

'''2. Високосный год
Напишите программу, которая запрашивает у пользователя год и проверяет, является ли он високосным. Год является високосным, 
если он делится на 4 без остатка, и в то же время не делится на 100 без остатка. При этом если год делятся на 400 без 
остатка, он тоже является високосным. Выведите соответствующее сообщение на экран с помощью функции print.
Пример вывода:
Введите год: 2024
Год является високосным.
Введите год: 2000
Год является високосным.
Введите год: 1900
Год не является високосным.'''
# teacher
year = int(input("Введите год: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Год является високосным.")
else:
    print("Год не является високосным.")

# Another variant
year = int(input("Введите год: "))

if year % 4 == 0 and year % 100 != 0 :
    print("Год является високосным.")
elif year % 400 == 0 :
    print("Год является високосным.")
else:
    print("Год не является високосным.")

# Variant2
y = int(input("Enter year: "))
if y % 400 == 0:
    print("Leap Year")
elif y % 100 == 0:
    print("Not Leap Year")
elif y % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")

# Python Fundamentals 2025: Домашнее задание 6
'''1. Математическое округление
Напишите программу, которая принимает число с плавающей точкой и округляет его до целого числа в соответствии с правилами 
школьной математики, а не банковского округления. Программа должна корректно работать как с положительными, так и с 
отрицательными числами.
Пример вывода:
Введите вещественное число: 2.5
Округленное значение: 3
Введите вещественное число: -2.5
Округленное значение: -3'''
# teacher
num = float(input("Введите вещественное число: "))

if num > 0:
    rounded_num = int(num + 0.5)
else:
    rounded_num = int(num - 0.5)

print("Округленное значение:", rounded_num)
# 2.1 + 0.5 -> 2.6 - > 2
# 2.5 + 0.5 -> 3 - > 3
# 2.9 + 0.5 -> 3.4 - > 3
# 0 + 0.5 -> 0.5 - > 0
# -0.2 - 0.5 -> -0.7 - > 0

# teacher
# Решение с использованием модуля math
import math

num = float(input("Введите вещественное число: "))
rounded_num = math.floor(num + 0.5) if num > 0 else math.ceil(num - 0.5)
print("Округленное значение:", rounded_num)

# Another variant
num = float(input("Введите вещественное число: "))
whole = int(num)
fraction = num - whole

if fraction >= 0.5:
    whole = whole + 1
elif fraction <= -0.5:
    whole = whole - 1

print("Округленное значение:", whole)

# Variant 2
import math
x = float(input("Enter the value of x: "))
y = x-int(x)
if y >= 0.5 or (-0.5 < y <= 0):
    print(math.ceil(x))
else:
    print(math.floor(x))

'''Гипотенуза треугольника
Напишите программу, которая запрашивает у пользователя длины двух катетов прямоугольного треугольника и вычисляет длину 
гипотенузы. Гипотенуза равна квадратному корню из суммы квадратов катетов.
Пример вывода:
Введите длину первого катета: 3
Введите длину второго катета: 4
Длина гипотенузы: 5.0'''
# teacher
import math

a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))
hypotenuse = round(math.sqrt(a**2 + b**2), 4)
print("Длина гипотенузы:", hypotenuse)

# Another variant

a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))

hypotenuse = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
print("Длина гипотенузы:", hypotenuse)

# Variant 2
from math import sqrt, hypot

a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))
# c = sqrt(a**2 + b**2)
c = hypot(a, b)
print("Длина гипотенузы: ", c)