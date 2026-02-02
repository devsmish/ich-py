'''1. Перевёрнутая лестница
Напишите программу, которая рисует перевёрнутую лестницу из звёздочек заданной высоты.
Пример вывода:
Введите высоту лестницы: 5
*****
****
***
**
*'''
star_count = int(input("Введите высоту лестницы: "))
for i in range(star_count):
    print("*" * (star_count - i))
    i += 1

# Another variant
height = int(input('Введите высоту лестницы: '))

# while height > 0:
#     print('*' * height)
#     height -= 1

for i in range(height, 0, -1):
    print('*' * i)

'''2. Проверка текста на ASCII
Напишите программу, которая принимает строку от пользователя и проверяет, являются ли все символы
строки ASCII - символами (диапазон кодов от 0 до 127 включительно).
Пример вывода:
Введите текст: Python
Все символы ASCII: True
Введите текст: Привет
Все символы ASCII: False'''
text = input("Введите текст: ")
in_ascii = True
for i in range(len(text)-1):
    if 0 <= ord(text[i]) <= 127:
        i += 1
        in_ascii = True
    else:
        in_ascii = False
print("Все символы ASCII:", in_ascii)

# Another variant
text = input("Введите текст: ")
in_ascii = True
for char in text:
    if char >= "$":
        in_ascii = False
        break

print("Все символы ASCII:", in_ascii)
text = input("Введите текст: ")
in_ascii = True
for char in text:
    if ord(char) > 127:
        in_ascii = False
        break

print("Все символы ASCII:", in_ascii)

'''3. Вывод строки с интервалами
Напишите программу, которая принимает строку от пользователя и выводит её символы через пробел на
одной строке. Обратите внимание, что в конце не должно быть лишнего пробела.
Пример вывода:
Введите строку: Python
P y t h o n'''
text = input("Enter any text: ")
print(text, end=" ")

# Another variant
text = input("Enter a text: ")
for char in text[:-1]:
    print(char, end="-")
print(text[-1])

'''4. Проверка скобок
Задание: Напишите программу, которая проверяет правильность расстановки круглых скобок в строке.
Пример вывода:
Введите строку: (a+b)*(c-d)
Скобки расставлены правильно? True
Введите строку: (a+b)(*((c-d)
Скобки расставлены правильно? False'''
string = "(a+b)*(c-d)"
balance = 0
for s in string:
    if s == "(":
        balance += 1
    elif s == ")":
        balance -=1
        if balance < 0:
            break
print("Скобки расставлены правильно?", balance == 0)

'''5. Поиск минимального символа
Напишите программу, которая принимает строку от пользователя и выводит символ с минимальным кодом.
Пример вывода:
Введите строку: Hello!
Минимальный символ: !'''
text = input("Enter any text: ")
min_simbol = 127
for char in text:
    if ord(char) <= min_simbol:
        min_simbol = ord(char)
    else:
        min_simbol = ord(char)
print("Минимальный символ:", chr(min_simbol))

'''6. Четные и нечетные цифры
Напишите программу, которая принимает одно число и формирует из его цифр два новых числа: одно из
четных цифр, другое из нечетных. Если в числе нет четных или нечетных цифр, программа должна выводить 0
вместо числа.
Пример вывода:
Введите число: 238947203429
Число из четных цифр: 2842042
Число из нечетных цифр: 39739
Введите число: 482262
Число из четных цифр: 482262
Число из нечетных цифр: 0'''
nummer = input("Enter any number: ")
even  = ''
odd = ''
for char in nummer:
    if int(char) % 2 == 0:
        even = even + char
    else:
        odd = odd + char
if even == '':
    even = '0'
if odd == '':
    odd = '0'
print("Число из четных цифр:", even)
print("Число из нечетных цифр:", odd)

'''7. Строка из диапазона Unicode
Напишите программу, которая принимает два числа (начало и конец диапазона Unicode) и выводит строку,
состоящую из всех символов этого диапазона.
Пример вывода:
Введите начальный код: 65
Введите конечный код: 70
Символы: ABCDEF'''
start = int(input("Старт: "))
end = int(input("Конец: "))
res = ""
for code in range(start, end + 1):
    res += chr(code)
print("Символы:", res)

'''8. Длина слов
Напишите программу, которая принимает строку, разделяет её на слова по пробелам и выводит каждое слово
с его длиной.
Пример вывода:
Введите строку: Программирование это весело
Слово: Программирование, Длина: 16
Слово: это, Длина: 3
Слово: весело, Длина: 6'''
text = input("Enter any text: ")
ind = len(text)
j = 0
for i in range(ind):
    word = ''
    if text[i] == " ":
        word += text[j:i]
        j = i + 1
        print("Слово:", word, "Длина:", len(word))
    elif i == (ind - 1) and text[-1] != ' ':
        word += text[j:ind]
        print("Слово:", word, "Длина:", len(word))

'''9. Текст палиндром
Напишите программу, которая принимает строку и проверяет, является ли она палиндромом, игнорируя всё
кроме букв русского и английского алфавита.
Пример вывода:
Введите строку: А роза упала на лапу Азора
Палиндром? True'''
text = input("Введите строку: ")
correct_text = ''

for char in text:
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or 'а' <= char <= 'я' or 'А' <= char <= 'Я':
        if 'A' <= char <= 'Z' or 'А' <= char <= 'Я':
            char = chr(ord(char) + 32)
        correct_text += char
print(f"Палиндром? {correct_text == correct_text[::-1]}")

# Another variant
text = input("Enter a string: ")
new_text = ""

for symbol in text:
    if symbol >= "a" and symbol <= "z":
        new_text += symbol
    elif symbol >= "A" and symbol <= "Z":
        new_text += symbol
    elif symbol >= "А" and symbol <= "Я":
        new_text += symbol
    elif symbol >= "а" and symbol <= "я":
        new_text += symbol
    else:
        continue

tmp_new_text = new_text[::-1]

if (tmp_new_text == new_text):
    print(f"Да это палиндром!\n {text}")
else:
    print(f"Это не палиндром!\n {text}")

'''10. Все буквы алфавита
Напишите программу, которая проверяет, содержит ли введённая строка все буквы английского алфавита (без
учёта регистра).
Пример вывода:
Введите строку: The quick brown fox jumps over the lazy dog
Содержит все буквы алфавита? True'''
text = input("Enter any text: ")
count_letter = 0
for i in range(65, 91):
    simbol = chr(i)
    if simbol.lower() in text or simbol.upper() in text:
        count_letter += 1
    else:
        continue
if count_letter == 26:
    print("Содержит все буквы алфавита? True")
else:
    print("Содержит все буквы алфавита? False")

'''11. Сравнение строк на уникальность
Напишите программу, которая принимает две строки и сравнивает в какой из них больше уникальных
символов.
Пример вывода:
Введите первую строку: Python
Введите вторую строку: JavaJava
Больше уникальных символов в строке: Python'''
text1 = input("Enter any text: ")
text2 = input("Enter any text: ")
uniq_let1 = 0
uniq_let2 = 0
for i in range(65, 91):
    simbol = chr(i)
    if simbol.lower() in text1 or simbol.upper() in text1:
        uniq_let1 += 1
    if simbol.lower() in text2 or simbol.upper() in text2:
        uniq_let2 += 1
if uniq_let1 > uniq_let2:
    print("Больше уникальных символов в строке:", text1)
elif uniq_let2 > uniq_let1:
    print("Больше уникальных символов в строке:", text2)
else:
    print("В строках одинаковое количество уникальных символов!")

'''12. Счётчик символов
Напишите программу, которая принимает строку и подсчитывает количество английских букв, цифр и
остальных символов в строке.
Пример вывода:
Введите строку: Python 3.12!
Букв: 6
Цифр: 3
Остальных символов: 3'''
text = input("Введите строку: ")
count_letter = count_digit = count_other = 0
for char in text:
    if "0" <= char <= "9":
        count_digit += 1
    elif "A" <= char <= "Z" or "a" <= char <= "z":
        count_letter += 1
    else:
        count_other += 1
print("Букв:", count_letter)
print("Цифр:", count_digit)
print("Остальных символов:", count_other)

'''13. Одинаковый сдвиг
Напишите программу, которая проверяет, имеют ли две строки одинаковые сдвиги между парами символов в
разных словах на одинаковых позициях. Например 'acc' имеет сдвиги 2, 0, и 'egg' имеет такие же
Пример вывода:
Введите первую строку: acc
Введите вторую строку: egg
Одинаковый сдвиг? True'''
first_text = input("Введите первую строку: ")
second_text = input("Введите вторую строку: ")
len1 = len(first_text)
len2 = len(second_text)
if len1 < len2:
    limit = len1
else:
    limit = len2
res = True
for i in range(limit - 1):
    shift1 = ord(first_text[i + 1]) - ord(first_text[i])
    shift2 = ord(second_text[i + 1]) - ord(second_text[i])
    if shift1 != shift2:
        res = False
        break
print("Одинаковый сдвиг?", res)