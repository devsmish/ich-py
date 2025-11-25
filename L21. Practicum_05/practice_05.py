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

'''Задание
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

# Задание 7
'''Кодирование строки
Напишите программу, которая принимает строку и кодирует её с помощью следующего правила: каждая последовательность 
одинаковых символов заменяется на символ и количество его повторений. Например, строка aaaabbc превращается в a4b2c1.
Пример вывода:
Введите строку: aaaabbc 
Закодированная строка: a4b2c1'''
text = input("Enter any text: ")
res_str = ''
letter = ''
count_let = 0
for i in range(len(text)):
    letter = text[i]
    if i + 1 < len(text) and text[i] == text[i + 1]:
        count_let += 1
    else:
        count_let = 1
res_str += letter + str(count_let)
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

# Задание 10
'''10. Развернуть слова
Напишите программу, которая разворачивает каждое слово в строке, сохраняя их порядок.
Пример вывода:
Введите строку: Python is fun 
Результат: nohtyP si nuf'''