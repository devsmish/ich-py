# Пример кодирования/декодирования строки в UTF-8
text = "Привет"
# Кодирование строки в байты с использованием UTF-8
encoded_text = text.encode('utf-8')
print(encoded_text)

decoded_text = encoded_text.decode('utf-8')
print(decoded_text)

'''1. Найди делители.
Напишите программу, которая запрашивает у пользователя число и выводит все его делители.
Пример вывода:
Введите число: 12
Делители числа: 1, 2, 3, 4, 6, 12
'''
num = int(input("Enter a number: "))
divider = 1
while divider <= num:
    if num % divider == 0:
        print("Детитель числа", num, "равен", divider)
        divider += 1
    else:
        divider += 1

'''2. Простые числа.
Напишите программу, которая выводит все простые числа от 2 до N (число вводится пользователем).
Пример вывода:
Введите число: 10
Простые числа: 2, 3, 5, 7'''
num = int(input("Enter a number: "))
digit = 1
while digit <= num:
    divider = 1
    count_div = 0   # сброс для нового числа
    # ищем количество делителей
    while divider <= digit:
        if digit % divider == 0:
            count_div += 1
        divider += 1
    # проверка простоты: у простых ровно 2 делителя
    if count_div == 2:
        print(f"В числе {num} есть простое число {digit}")
    digit += 1

'''Найди подстроку
Напишите программу, которая принимает от пользователя строку и проверяет, содержится ли слово "Python" в этой строке.
Пример вывода:
Введите строку: Я учу Python!
Содержит 'Python': True'''
text = input("Enter a text: ")
print("Содержит 'Python': ", "Python" in text)

# Разбор домашнего задания
# Python Fundamentals 2025: Домашнее задание 7
'''1. Сумма цифр числа
Напишите программу, которая вычисляет сумму цифр введённого числа.
Пример вывода:
Введите число: 12345
Сумма цифр: 15'''
# teacher
num = int(input("Введите число: "))
sum_digits = 0

while num:  # same
# while num != 0:  # same
# while num > 0:
    sum_digits += num % 10
    num //= 10

print("Сумма цифр:", sum_digits)

# Не принимается!
number = input("Введите число: ")

sum_digits = sum(int(digit) for digit in number)

print(f"Сумма цифр: {sum_digits}")

'''2. Палиндром
Напишите программу, которая запрашивает у пользователя целое число и определяет, является ли оно палиндромом. Число 
является палиндромом, если оно читается одинаково слева направо и справа налево.
Пример вывода:
Введите число: 12321
Число 12321 является палиндромом.
Введите число: 1234
Число 1234 не является палиндромом.'''
# teacher
number = int(input("Введите число: "))
original_number = number
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

if original_number == reversed_number:
    print("Число", original_number, "является палиндромом.")
else:
    print("Число", original_number, "не является палиндромом.")

# Не принимается как решение без цикла, но также правильное
number = int(input("Введите число: "))
str_num = str(number)
if str_num == str_num[::-1]:
    print("Число", number, "является палиндромом")
else:
    print("Число", number, "не является палиндромом")

# Another variant
num = int(input("Введите число: "))
num1 = num
result = ""
while num1 > 0:
    result += str(num1 % 10) #переварачиваем число
    num1 = num1 // 10

if result == str(num): #сравниваем числа
    print("Число",num , "является палиндромом")
else:
    print("Число", num, " не является палиндромом")

'''3. Проверь интуицию
Напишите программу, которая генерирует случайное число от 1 до 100 включительно и дает пользователю 10 попыток, чтобы 
угадать это число. Программа должна подсказывать, больше или меньше загаданное число. После завершения игры программа 
оценивает, насколько хорошая интуиция у игрока.
Пример вывода:
Угадайте число от 1 до 100. У вас 10 попыток.
Ваше предположение: 50
Загаданное число меньше вашего
Ваше предположение: 25
Загаданное число больше вашего
Ваше предположение: 30
Поздравляем! Вы угадали число: 30.
Вы угадали число за 3 попытки. Отличный результат!'''
# teacher
import random

secret_number = random.randint(1, 100)
attempts = 10
used_attempts = 0

print("Угадайте число от 1 до 100. У вас", attempts, "попыток.")

while attempts > 0:
    guess = int(input("Ваше предположение: "))
    used_attempts += 1
    attempts -= 1

    if guess < secret_number:
        print("Загаданное число больше вашего.")
    elif guess > secret_number:
        print("Загаданное число меньше вашего.")
    else:
        print("Поздравляем! Вы угадали число:", secret_number, "за", used_attempts, "попыток.")
        # Оценка догадливости
        if used_attempts == 1:
            print("Отличная интуиция! Вы угадали с первой попытки!")
        elif used_attempts <= 3:
            print("Вы настоящий мастер угадывания!")
        elif used_attempts <= 7:
            print("Неплохой результат!")
        break
else:
    print("К сожалению, вы не угадали число. Загаданное число было:", secret_number)
    print("В следующий раз вам обязательно повезёт!")

# Another variant
import random

a = random.randint(1, 100)
print("Угадай число")
proba = 10
guessed = False
while proba > 0:
    b = int(input("Введите число: "))
    proba -= 1
    if b == a:
        print("True")
        guessed = True
        break
    elif b < a:
        print("Моё число больше")
    else:
        print("Моё число меньше")

if guessed:
    used = 10 - proba
    if used <= 3:
        print("Отлично!")
    elif used <= 7:
        print("Неплохо")
    else:
        print("Хорошо")
else:
    print("Попытки закончились.")
    print(a)

# Variant 2
import random

# Генерируем случайное число от 1 до 100
secret_chislo = random.randint(1, 100)

# Инициализация переменных для цикла
popitki_count = 0  # Счётчик попыток
ugadal = False  # Флаг угадывания

print("Угадайте число от 1 до 100. У вас 10 попыток.")

# Цикл
while ugadal == False and popitki_count < 10:
    popitki_count = popitki_count + 1  #  счётчик попыток
    guess = int(input("Ваше предположение (попытка " + str(popitki_count) + " из 10): "))

    if guess == secret_chislo:
        ugadal = True  # Устанавливаем флаг

    elif guess < secret_chislo:
        print("Загаданное число больше вашего")

    else:  # guess > secret_chislo
        print("Загаданное число меньше вашего")

# проверки
if ugadal == True:

    # 1. Вывод победы
    print("Поздравляем! Вы угадали число: " + str(secret_chislo) + ".")
    print("Вы угадали число за " + str(popitki_count) + " попыток.")

    # 2. Оценка интуиции (используем числа 1, 4, 7)
    if popitki_count == 1:
        assessment = "Отличная интуиция! Вы угадали с первой попытки!"
    elif popitki_count <= 4:
        assessment = "Отличный результат!"
    elif popitki_count <= 7:
        assessment = "Хороший результат!"
    else:
        assessment = "Можно и лучше, но вы справились."
    print(assessment)
else:

    # Вывод проигрыша (цикл завершился по количеству попыток)
    print("Попытки закончились. Вы не угадали.")
    print("Загаданное число было: " + str(secret_chislo) + ".")