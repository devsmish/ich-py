'''1. Округление вверх и вниз
Напишите программу, которая:
● принимает число с плавающей запятой
● выводит результат округления вверх и вниз
Пример вывода:
Введите число: 4.3
Округление вверх: 5
Округление вниз: 4'''
import math
nummer = float(input("Enter any number: "))
print("Округление вверх:", math.ceil(nummer))
print("Округление вниз:", math.floor(nummer))

'''2. Сумма чисел
Напишите программу, которая принимает число от пользователя и выводит сумму с чисел от 1 до самого числа.
Пример вывода:
Введите число: 5
Сумма чисел от 1 до 5 = 15'''
nummer = int(input("Enter a number: "))
result = 0
i = 0
while i <= nummer:
    result += i
    i += 1
print("Сумма чисел от 1 до", nummer, "=", result)

# Another variant
x = int(input("Введите число: "))

total = 0
while x > 0:
    total += x
    x -= 1

print(total)

'''3. Счётчик факториала
Напишите программу, которая рассчитывает факториал заданного числа
(произведение всех целых чисел от 1 до самого числа) двумя способами.
Выведите оба результата и сравните равны ли они.
Пример вывода:
Введите число: 5
Факториал числа 5 первым способом: 120
Факториал числа 5 вторым способом: 120
Результаты равны? True'''
import math
nummer = int(input("Enter a number: "))
fakt1 = 1
fakt2 = 1
copy_num = nummer
while copy_num > 0:
    fakt1 = fakt1 * copy_num
    copy_num -= 1
print("Факториал числа", nummer, "первым способом:", fakt1)
fakt2 = math.factorial(copy_num)
print("Факториал числа", nummer, "вторым способом:", fakt2)
if fakt1 == fakt2:
    print("Результаты равны? True")
else:
    print("Результаты равны? False")

'''4. Симулятор кассы. Напишите программу, которая принимает от пользователя цены товаров. Пользователь вводит цены по 
одному (ввод завершается при вводе нуля). Программа должна: Рассчитать и вывести общую сумму покупки, округленную до 
целого числа. Определить, какую сумму покупатель должен заплатить, если у него есть только купюры номиналом 100 евро.
Рассчитать и вывести сдачу, которую нужно дать покупателю.
Пример вывода: 
Введите цену товара: 45.50
Введите цену товара: 29.99
Введите цену товара: 22.49
Введите цену товара: 0
Сумма покупки: 98 евро
Покупатель передал: 100 евро
Сдача: 2 евро'''
price = None
result = 0
while price !=0:
    price = float(input("Enter a price: "))
    result += price
print("Сумма покупки:", round(result), "евро")
number_of_bills = -1
while result > 0:
    number_of_bills += 1
    result -= 100
print("Покупатель передал:", (number_of_bills) * 100, "евро")

print("Сдача:", round(number_of_bills * 100 - result), "евро")

# Another variant
summ = 0

while True:
    temp_val = float(input('Введите цену товара: '))

    if temp_val == 0:
        break

    summ += temp_val

sell_sull = round(summ)
summ = sell_sull

print(f'Сумма покупки: {sell_sull} евро')

count_of_money = 0

while sell_sull > 0:
    sell_sull -= 100
    count_of_money += 1

print(f'Покупатель передал: {count_of_money*100} евро')
print(f'Сдача: {count_of_money*100 - summ} евро')

# Variant 2
from math import ceil

summ = 0

while True:
    temp_val = float(input('Введите цену товара: '))

    if temp_val == 0:
        break

    summ += temp_val

sell_summ = round(summ)

print(f'Сумма покупки: {sell_summ} евро')

payment = ceil(sell_summ / 100) * 100
print(f'Покупатель передал: {payment} евро')
print(f'Сдача: {payment - sell_summ} евро')

'''5. Учет доходов и расходов
Напишите программу, которая принимает на вход положительные и отрицательные значения и останавливается получив ноль. 
Программа должна рассчитать сумму доходов (положительные) и расходов (отрицательные), а также итоговый баланс.
Пример вывода:
Введите доход, расход или '0' для получения итога: 15000
Введите доход, расход или '0' для получения итога: -5000
Введите доход, расход или '0' для получения итога: -3000
Введите доход, расход или '0' для получения итога: 0
Доходы: 15000
Расходы: 8000
Итоговый баланс: 7000'''
income = 0
expense = 0
result = 0
while True:
    nummer = float(input("Введите доход, расход или '0' для получения итога: "))
    if nummer > 0:
        income += nummer
    elif nummer < 0:
        expense += nummer
    else:
        break
result = round((income + expense), 2)
print("Доходы:", income)
print("Расходы:", abs(expense))
print("Итоговый баланс:", result)

# Another variant
inc = 0
exp = 0
while True:
    number = int(input("Введите доход, расход или '0' для получения итога:"))
    if number > 0:
        inc += number
    elif number < 0:
        exp += abs(number)
    else:
        break
print(f"Доходы {inc}")
print(f"Расходы {exp}")
print(f"Итоговый баланс {inc - exp}")

'''6. Последовательности Фибоначчи
Напишите программу, которая выводит первые n чисел последовательности Фибоначчи. Число n вводится пользователем.
Пример вывода:
Введите количество чисел: 7
0 1 1 2 3 5 8'''
counter = int(input("Enter a number: "))
Fibonacci1 = 0
Fibonacci2 = 1
count = 0
while count < counter:
    print(Fibonacci1, sep=" ")
    Fibonacci1, Fibonacci2 = Fibonacci2, Fibonacci1 + Fibonacci2
    count += 1


'''7. Число Армстронга
Напишите программу, которая запрашивает у пользователя целое число и проверяет, является ли оно числом Армстронга. Число 
Армстронга — это число, которое равно сумме своих цифр, которые были возведены в степень, равную количеству цифр в числе.
Например 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27
Пример вывода:
Введите число: 153
Число 153 является числом Армстронга.
Введите число: 123
Число 123 не является числом Армстронга.'''
number = int(input("Enter a number: "))
length_of_number = 0
tmp_number = number

while tmp_number > 0:
   tmp_number = tmp_number // 10
   length_of_number += 1

total = 0
tmp_number = number
while tmp_number > 0:
    total += (tmp_number % 10) ** length_of_number
    tmp_number = tmp_number // 10

print("Res:", total)
print("True or False:", number == total)

'''8. Угадай за 5 попыток
Напишите программу, которая генерирует случайное число от 1 до 10 и просит пользователя угадать его за 5
попыток. Если пользователь не угадывает за 5 попыток, программа выводит загаданное число.
Пример вывода:
Попробуйте угадать число от 1 до 10: 10
Неверно! У вас осталось 4 попытки.
Попробуйте угадать число от 1 до 10: 3
Неверно! У вас осталось 3 попытки.
Попробуйте угадать число от 1 до 10: 7
Поздравляем! Вы угадали число.'''
import random
random_num = random.randint(1, 10)
num_attempts = 0
print("Угадайте число от 1 до 10. У вас 5 попыток.")
while num_attempts < 5:
    num_answer = int(input("Попробуйте угадать число от 1 до 10: "))
    if num_answer == random_num:
        print("Поздравляем! Вы угадали число.", random_num)
        break
    else:
        print(f"Неверно! У вас осталось {4 - num_attempts} попытки.")
    num_attempts += 1
    if num_attempts >=  5:
        print(f"Вы не отгадали число {random_num} за отведенные 5 попыток!")
        break

'''9. Определение простого числа
Напишите программу, которая запрашивать число у пользователя и определяет, является ли заданное число простым.
Число является простым, если оно:
● Больше 1.
● Имеет только два делителя: единицу и само себя.
Пример вывода:
Введите число: 29
Число 29 является простым.
Введите число: 15
Число 15 не является простым.'''
number = int(input("Enter a positive integer number: "))
divisors_count = 0
divisors = 1
while divisors <= number:
    if number % divisors == 0:
        divisors_count += 1
    else:
        divisors_count += 0
    divisors +=1
if number > 1 and divisors_count == 2:
    print(f"Число {number} является простым.")
elif number == 0:
    print("Вы ввели 0")
else:
    print(f"Число {number} не является простым.")

'''10. Упорядоченность цифр
Напишите программу, которая получает натуральное число и определяет, являются ли его цифры упорядоченными по возрастанию.
Пример вывода:
Введите число: 1347
Цифры упорядочены по возрастанию.
Введите число: 1523
Цифры не упорядочены по возрастанию.'''
num = int(input("Enter a positive integer number: "))
next_num = 0
temp_num = num % 10
while num > 0:
    next_num = num % 10
    if next_num <= temp_num:
        temp_num = next_num
        num = num // 10
    else:
        print("Цифры не упорядочены по возрастанию.")
        break
else:
    print("Цифры упорядочены по возрастанию.")