'''1. Квадрат чисел в строке
Напишите программу, которая обрабатывает строку и заменяет все вхождения чисел в строке на их квадрат, оставляя другие
части строки неизменными. Данные:
text = "I have 2 apples and 4 bananas"
Пример вывода:
I have 4 apples and 16 bananas'''
text = "I have 2 apples and 4 bananas"
word_list = text.split()
new_string = ""
for i in range(len(word_list)):
    if word_list[i].isdigit():
        word_list[i] = str(int(word_list[i]) ** 2)
    new_string += word_list[i] + ' '
print(new_string)

# Another variant
text = "I have 2 apples and 4 bananas"
new_list = text.split()
for i in range(len(new_list)):
    if new_list[i].isdigit():
        new_list[i] = str(int(new_list[i]) ** 2)

print(' '.join(new_list))

'''1.1 Вариант решения, если числа еще в кавычках'''
text = "I have '2' apples and '14' bananas"

new_list = text.split()
for i in range(len(new_list)):
    tmp = new_list[i].strip('\'"')
    if tmp.isdigit():
        new_list[i] = "'" + str(int(tmp) ** 2) + "'"
# "4"
print(' '.join(new_list))

'''2. Корректные имена
Напишите программу, которая обрабатывает список строк, состоящий из имён, и выводит только корректные имена. Корректные 
это те, которые начинаются с заглавной буквы и состоят только из букв.
Данные:
names = ["Alice", "bob", "Charlie", "dave", "Eva", "Frank123"]
Пример вывода:
Имена с заглавной буквы и без цифр:
 Alice
 Charlie
 Eva
'''
names = ["Alice", "bob", "Charlie", "dave", "Eva", "Frank123"]
for item in names:
    if item.isalpha() and item.istitle():
        print(item)

'''Задание 1
Сложение чисел
Напишите программу, которая принимает строку с числами через пробел и выводит сумму всех чисел.
Пример вывода:
Введите список чисел через пробел: 1 2 3 4 5 
Сумма чисел: 15'''
text = input("Enter any nummer srp by space: ")
num_list = text.split()
result= 0
for i in range(len(num_list)):
    result += int(num_list[i])
print(result)

'''2. Обратный список
Задача: Напишите программу, которая принимает строку с числами через пробел и
выводит его в обратном порядке. Обратите внимание, что в списке должны быть
именно числа, а не строки.
Пример вывода: Введите список чисел через пробел: 1 2 3 4 5
Обратный список: [5, 4, 3, 2, 1]'''
nummers = input("Enter any nummer sep by space: ")
list_nummers = nummers.split()
for i in range(len(list_nummers)):
    list_nummers[i] = int(list_nummers[i])
print("Обратный список:", list_nummers[::-1])

'''3. Сумма чётных и нечётных чисел
Задача: Напишите программу, которая подсчитывает сумму чётных и нечётных
чисел в списке по отдельности.
Данные: numbers = [-1, 8, 2, 0, -3, -9, -1, 10, 7, -4]
Пример вывода: Изначальный список: [-1, 8, 2, 0, -3, -9, -1, 10, 7, -4] Сумма чётных: 16
Сумма нечётных: -7'''
numbers = [-1, 8, 2, 0, -3, -9, -1, 10, 7, -4]
even = odd = 0
for num in numbers:
    if num % 2 == 0:
        even += num
    else:
        odd += num
print("Сумма чётных:", even)
print("Сумма нечётных:", odd)

'''4. Задание
Максимальное число
Напишите программу, которая выводит наибольшее число в списке, не используя встроенную функцию max(), а также его индекс в списке.
numbers = [3, 12, 8, 22, 9, 25, 6, 23, 8, 7]
Пример вывода:
Список чисел: [3, 12, 8, 22, 9, 25, 6, 23, 8, 7]
Наибольшее число: 25
Индекс числа: 5'''
numbers = [3, 12, 8, 22, 9, 25, 6, 23, 8, 7]
max_num = 0
index = 0
for i in range(len(numbers)):
    if numbers[i] > max_num:
        max_num = numbers[i]
        index = i
print("Наибольшее число:", max_num)
print("Индекс числа:", index)

'''Задание 5
Перестановка соседних элементов
Напишите программу, которая меняет местами соседние элементы списка. 
Пример списка: numbers = [1, 2, 3, 4, 5]
Пример вывода:
Изначальный список: [1, 2, 3, 4, 5]
Список после перестановки: [2, 1, 4, 3, 5]'''
numbers = [1, 2, 3, 4, 5]
for i in range(0, len(numbers) - 1, 2):
    if i < len(numbers):
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    else:
        break
print(numbers)

# Another variant
list1 = [1, 2, 3, 4, 5]
for i in range(0, len(list1)-1,2):
    list1[i], list1[i+1] = list1[i+1], list1[i]
print(f"Список после перестановки:{list1}")

'''6. Числа и слова
Задача: Напишите программу, которая обрабатывает строку, содержащую слова и
целые числа, разделённые пробелами. Программа должна преобразовать строку в
список, где числа преобразуются в тип int, а остальные элементы остаются
строками и начинаются с заглавной буквы.
Данные: text = "apple 42 banana 3 100 orange"
Пример вывода: Изначальная строка: apple 42 banana 3 100 orange Результат:
['Apple', 42, 'Banana', 3, 100, 'Orange']'''
text = "apple 42 banana 3 100 orange"
text_list = text.split()
for i in range(len(text_list)):
    if text_list[i].isdigit():
        text_list[i] = int(text_list[i])
    else:
        text_list[i] = text_list[i].title()
print(text_list)

# Задание 7
'''Кодирование строки
Напишите программу, которая принимает строку и кодирует её с помощью следующего правила: каждая последовательность 
одинаковых символов заменяется на символ и количество его повторений. Например, строка aaaabbc превращается в a4b2c1.
Пример вывода:
Введите строку: aaaabbc 
Закодированная строка: a4b2c1'''
text = input("Enter any text: ")
res_str = ''
count_let = 1

for i in range(len(text)):
    if i + 1 < len(text) and text[i] == text[i + 1]:
        count_let += 1
    else:
        res_str += text[i] + str(count_let)
        count_let = 1

print(res_str)

# Another variant
s = input("введите строку")

result =""
count = 1
letter = s[0]
for i in range(1, len(s)):
    if letter == s[i]:
        count += 1
    else:
        result += letter + str(count)
        letter = s[i]
        count = 1
result += letter + str(count)
print(result)

'''8. Проверка формата email
Задача: Напишите программу, которая проверяет, начинается ли строка с буквы,
содержит ли в себе символ @, и заканчивается ли на .com или .de.
Пример вывода: Введите email: user@example.com Корректный формат? True'''
email = input("Enter any email: ")
if email[0].isalpha() and email.count('@') == 1 and (email.endswith('.de') or email.endswith('.com')):
    print("Корректный формат? True")
else:
    print("Некорректный формат? False")

'''9. Количество символов
Задача: Напишите программу, которая подсчитывает количество букв, цифр и
пробелов в строке. Также выведите количество остальных символов.
Пример вывода: Введите строку: Python 3.12 is awesome!
Буквы: 15 Цифры: 3 Пробелы: 3 Остальные символы: 2
'''
text = input("Введите строку: ")
count_letter = count_digit = count_space = count_other = 0
for char in text:
    if "0" <= char <= "9":
        count_digit += 1
    elif "A" <= char <= "Z" or "a" <= char <= "z":
        count_letter += 1
    elif char == " ":
        count_space += 1
    else:
        count_other += 1
print("Букв:", count_letter)
print("Цифр:", count_digit)
print("Пробелы:", count_space)
print("Остальных символов:", count_other)

# Задание 10
'''10. Развернуть слова
Напишите программу, которая разворачивает каждое слово в строке, сохраняя их порядок.
Пример вывода:
Введите строку: Python is fun 
Результат: nohtyP si nuf'''
text = input("Enter any text: ")
word_list = text.split()
new_text = ''
for item in word_list:
        new_text += item[::-1] + ' '
print(new_text)

'''11. По одному пробелу
Задача: Напишите программу, которая удаляет в строке лишние пробелы, оставляя
только по одному пробелу между словами.
Данные: text = " Hello, World! How are you? "
Пример вывода: Строка: ' Hello, World! How are you? ' Результат: 'Hello, World! How
are you?'''
text = input("Enter any text: ")
correkt_text = ''
tmp_list = text.split()
for i in range(len(tmp_list)):
    if i == 0:
        correkt_text += tmp_list[i].lstrip() + ' '
    elif i == len(tmp_list) - 1:
        correkt_text += tmp_list[i].rstrip() + ' '
    else:
        correkt_text += tmp_list[i] + ' '
print(correkt_text)

'''12. Все позиции подстроки
Задача: Напишите программу, которая ищет подстроку в строке и выводит все
индексы начала вхождения подстроки.
Пример вывода: Строка: Banana bAnana baNAna Подстрока: ban Позиция: 0 Позиция:
7 Позиция: 14'''
text = input("Enter any text: ")
little_str = input("Enter any text: ")
position = 0
tmp_text = ''
i = 0
while i < len(text):
    position = text.find(little_str)
    i = position + 1
    print("Позиция:", position)

