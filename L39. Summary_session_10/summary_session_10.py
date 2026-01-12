# Python Fundamentals 2025: Домашнее задание 18
'''1. Не уникальные числа
Напишите программу, которая находит все числа, встречающиеся более одного раза в списке, и выводит их в порядке убывания.
Данные:
numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
Пример вывода:
Числа, встречающиеся более одного раза: [8, 7, 4, 3]'''
# teacher
numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]

repeated_numbers = {n for n in numbers if numbers.count(n) > 1}
sorted_repeated_numbers = sorted(repeated_numbers, reverse=True)
print("Числа, встречающиеся более одного раза:", sorted_repeated_numbers)

# Another variant
numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]

# 1. считаем количество вхождений только повторяющихся
attempts = {n: numbers.count(n) for n in numbers if numbers.count(n) > 1}

# 2. формируем список
items = list(attempts.items())

# 3. сортировка
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] < items[j][1] or (
            items[i][1] == items[j][1] and items[i][0] < items[j][0]
        ):
            items[i], items[j] = items[j], items[i]

# 4. берём только числа
result = list(dict(items).keys())

print(result)

'''2. Проверка подмножества
Напишите программу, которая проверяет, является ли один словарь подмножеством другого (т.е. все его пары "ключ-значение" 
содержатся в другом словаре).
Данные:
dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}
Пример вывода:
Первый словарь является подмножеством второго.'''
# teacher
dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 4, "c": 3}

is_subset = True

for key in dict1:
    if key not in dict2 or dict1[key] != dict2[key]:
        is_subset = False
        break

if is_subset:
    print("Первый словарь является подмножеством второго.")
else:
    print("Первый словарь не является подмножеством второго.")

# Another variant
dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}

set1 = frozenset(dict1.items())
set2 = frozenset(dict2.items())

if set1.issubset(set2):
    print("The first dictionary is a subset of the second.")
else:
    print("The first dictionary is not a subset of the second.")

# Variant2
dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}

set1 = frozenset(dict1.items())
set2 = frozenset(dict2.items())

if set1.issubset(set2) or set2.issubset(set1):
    print("One of dictionaries is a subset of another.")
else:
    print("One of dictionaries is not subset of another.")

# Variant3
dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "c": 3, "b": 2}
if dict1.items() <= dict2.items():
    print("Первый словарь является подмножеством второго.")
else:
    print("Первый словарь не является подмножеством второго.")

# Python Fundamentals 2025: Домашнее задание 19
'''1. Реверс словаря
Напишите программу, которая меняет местами ключи и значения в словаре. Если значения повторяются, добавьте их в список.
Данные:
data = {"a": 1, "b": 2, "c": 1, "d": 3}
Пример вывода:
Перевернутый словарь: {1: ['a', 'c'], 2: ['b'], 3: ['d']}'''
# teacher
data = {"a": 1, "b": 2, "c": 1, "d": 3}

reversed_dict = {}

for key, value in data.items():
    if value not in reversed_dict:
        reversed_dict[value] = [key]
    else:
        reversed_dict[value].append(key)

print("Перевернутый словарь:", reversed_dict)

# Another variant
data = {"a": 1, "b": 2, "c": 1, "d": 3}

reversed_dict = {}

for key, value in data.items():
    reversed_dict.setdefault(value, []).append(key)

print("Перевернутый словарь:", reversed_dict)

'''2. Счётчик букв в словах
Напишите программу, которая подсчитывает количество каждой буквы в заданных словах и создаёт словарь, где ключи — это 
слова, а значения — это ещё один словарь с подсчётом каждой буквы.
Данные:
words = ["anna", "bennet", "john"]
Пример вывода:
{'anna': {'a': 2, 'n': 2}, 'bennet': {'b': 1, 'e': 2, 'n': 2, 't': 1}, 'john': {'j': 1, 'o': 1, 'h': 1, 'n': 1}}'''
# teacher
words = ["anna", "bennet", "john"]
new_dict = {}
for word in words:
    new_dict[word] = {char: word.count(char) for char in set(word)}
print(new_dict)

# Another variant
words = ["anna", "bennet", "john"]

letter_count = {}

for word in words:
    letter_count[word] = {}
    for letter in word:
        letter_count[word][letter] = letter_count[word].get(letter, 0) + 1

print(letter_count)

'''3. Распределение студентов по группам
У вас есть словарь, где ключи — имена студентов, а значения — их баллы за экзамен. Необходимо распределить студентов по группам:
"Отличники": баллы >= 85
"Хорошисты": баллы от 70 до 84
"Троечники": баллы от 50 до 69
"Не сдали": баллы < 50
Создайте словарь с ключами-группами и словарями со студентами в качестве значений.
Данные:
students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}
groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]
Пример вывода:
Распределение по группам:
{'Отличники': {'Аня': 92, 'Дима': 88}, 'Хорошисты': {'Боря': 76}, 'Троечники': {'Ваня': 65, 'Ева': 54}, 'Не сдали': {'Галя': 48}}'''
# teacher
students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}
groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]

student_groups = {group: {} for group in groups}

for name, score in students.items():
    if score >= 85:
        group_name = "Отличники"
    elif 70 <= score < 85:
        group_name = "Хорошисты"
    elif 50 <= score < 70:
        group_name = "Троечники"
    else:
        group_name = "Не сдали"
    student_groups[group_name][name] = score

print("Распределение по группам:")
print(student_groups)