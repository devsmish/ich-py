'''1. Таблица умножения
Напишите программу, которая выводит таблицу умножения для чисел от 1 до n. Где n это число, которое введет пользователь.
Оформите вывод так, чтобы столбцы были ровные (число ровно под числом)
Пример вывода:
Введите число: 5'''
mult = int(input("Enter a number: "))
for i in range(1, mult+1):
    result = ''
    for j in range(1, mult+1):
        result = result + str(i * j) + ' ' * (len(str(mult * mult)) - len(str(i * j)) + 1)
    print(result)

'''2. Лестница чисел
Напишите программу, которая принимает число n и выводит "лестницу" из чисел. Каждая строка лестницы содержит числа от 1 
до номера строки.
Пример вывода:
Введите число: 5'''
nummer = int(input("Enter a number: "))
for i in range(1, nummer + 1):
    res = ''
    for j in range(1, i + 1):
        res = res + str(j) + ' '
    print(res)

'''3. Удаление всех повторяющихся символов
Напишите программу, которая принимает строку и удаляет из неё все повторяющиеся символы, сохраняя только первые их 
вхождения.
Пример вывода:
Введите строку: Python programming  
Результат: Python prgami'''
text = input("Enter a text: ")
res = ''
copy_text = text
for letter in text:
    if letter not in res:
        res += letter
print(res)