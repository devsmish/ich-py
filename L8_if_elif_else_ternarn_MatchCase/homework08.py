'''1. Сортировка чисел
Напишите программу, которая запрашивает у пользователя три числа и выводит их в порядке
возрастания, разделенные запятой.'''
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")
if num1 <= num2 and num2 <= num3:
    print(num1, num2, num3)
elif num2 <= num1 and num1 <= num3:
    print(num2, num1, num3)
elif num3 <= num1 and num1 <= num2:
    print(num3, num1, num2)
elif num1 <= num2 and num3 <= num2 and num1 <= num3:
    print(num1, num3, num2)
elif num2 <= num1 and num3 <= num1 and num2 <= num3:
    print(num2, num3, num1)
else:
    print(num3, num2, num1)

'''2. Високосный год
Напишите программу, которая запрашивает у пользователя год и проверяет, является ли он
високосным. Год является високосным, если он делится на 4 без остатка, и в то же время не делится
на 100 без остатка. При этом если год делятся на 400 без остатка, он тоже является високосным.
Выведите соответствующее сообщение на экран с помощью функции print.'''
year = int(input("Enter the year: "))
if year % 400 == 0:
    print("Год", year, "является высокосным")
elif year % 4 == 0 and year % 100 != 0:
    print("Год", year, "является высокосным")
else:
    print("Год", year, "НЕ является высокосным")