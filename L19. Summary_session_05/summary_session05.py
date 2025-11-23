# Python Fundamentals 2025: Домашнее задание 8
'''1. Проверка кодировки
Напишите программу, которая принимает от пользователя один символ и выводит его код в таблице Unicode и его
принадлежность к диапазону ASCII (True/False).
Пример вывода:
Введите символ: A
Код Unicode: 65
ASCII символ: True'''
char = input("Введите символ: ")
unicode_code = ord(char)
is_ascii = 0 <= unicode_code <= 127
print("Код Unicode:", unicode_code)
print("ASCII символ:", is_ascii)

'''2. Подстрока с заполнением
Напишите программу, которая принимает строку и индексы начала и конца. Программа должна вывести подстроку на указанных 
позициях. Также если конечный индекс выходит за пределы строки, программа заполняет недостающие символы символами _.
Пример вывода:
Введите строку: Программирование  
Введите начальный индекс: 3  
Введите конечный индекс: 20  
Подстрока: граммирование_____'''
# teacher
text = input("Введите строку: ")
start = int(input("Введите начальный индекс: "))
end = int(input("Введите конечный индекс: "))

if end > len(text):
    substring = text[start:] + "_" * (end - len(text))
else:
    substring = text[start:end]

print("Подстрока:", substring)

# Another variant
text = input("Введите строку: ")
start = int(input("Введите начальный индекс: "))
end = int(input("Введите конечный индекс: "))
substring = text[start:end]
missing = max(0, end - len(text))
substring += "_" * missing
print("Подстрока:", substring)

'''3. Подсчёт символа
Напишите программу, которая принимает строку и символ, а затем подсчитывает, сколько раз символ встречается в строке.
Пример вывода:
Введите строку: Hello, world!  
Введите символ: o  
Символ o встречается 2 раз(а).'''
# teacher
text = input("Введите строку: ")
symbol = input("Введите символ: ")
count = 0
index = 0

while index < len(text):
    if text[index] == symbol:
        count += 1
    index += 1

print("Символ", symbol, "встречается", count, "раз(а).")

# analog with for
text = input("Введите строку: ")
symbol = input("Введите символ: ")
count = 0

for s in text:
    if s == symbol:
        count += 1

print("Символ", symbol, "встречается", count, "раз(а).")

'''4. Инвертирование строки без цифр
Напишите программу, которая принимает строку и выводит её в обратном порядке, пропуская все цифры.
Пример вывода:
Введите строку: n52uFs6Inoh67ty8P  
Результат: PythonIsFun'''
# teacher
text = input("Введите строку: ")
reversed_text = ""
index = len(text) - 1

while index >= 0:
    char = text[index]
    if not ('0' <= char <= '9'):  # Проверка, что символ не цифра
        reversed_text += char
    index -= 1

print("Результат:", reversed_text)

# Another variant
text = input("Введите строку: ")
result = ""

i = len(text) - 1
while i >= 0:
    if  text[i] not in "0123456789":
        result += text[i]
    i = i - 1

print("Результат:", result)

# Python Fundamentals 2025: Домашнее задание 9
'''1. Таблица умножения
Напишите программу, которая выводит таблицу умножения для чисел от 1 до n. Где n это число, которое введет пользователь.
Оформите вывод так, чтобы столбцы были ровные (число ровно под числом)'''
# teacher
n = int(input("Введите число: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end='\t')
    print()

# Another variant
n = int(input("Введите число: "))
max_num = n * n
width = len(str(max_num)) + 3

for i in range(1, n + 1):
    for j in range(1, n + 1):
        s = str(i * j)
        print(" " * (width - len(s)) + s, end="")
    print()

'''2. Лестница чисел
Напишите программу, которая принимает число n и выводит "лестницу" из чисел. Каждая строка лестницы содержит числа от 
1 до номера строки.'''
# teacher
n = int(input("Введите число: "))

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()

'''3. Удаление всех повторяющихся символов
Напишите программу, которая принимает строку и удаляет из неё все повторяющиеся символы, сохраняя только первые их вхождения.
Пример вывода:
Введите строку: Python programming  
Результат: Python prgami'''
# teacher
text = input("Введите строку: ")
result = ""

for char in text:
    if char not in result:
        result += char

print("Результат:", result)