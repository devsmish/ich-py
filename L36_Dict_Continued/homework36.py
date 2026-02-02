'''1. Реверс словаря
Напишите программу, которая меняет местами ключи и значения в словаре. Если значения повторяются, добавьте их в список.
Данные:
data = {"a": 1, "b": 2, "c": 1, "d": 3}
Пример вывода:
Перевернутый словарь: {1: ['a', 'c'], 2: ['b'], 3: ['d']}'''
data = {"a": 1, "b": 2, "c": 1, "d": 3}
reversed_data = {}
for key, value in data.items():
    if value not in reversed_data:
        reversed_data[value] = []
    reversed_data[value].append(key)
print(reversed_data)

'''2. Счётчик букв в словах
Напишите программу, которая подсчитывает количество каждой буквы в заданных словах и создаёт словарь, где ключи — это 
слова, а значения — это ещё один словарь с подсчётом каждой буквы.
Данные:
words = ["anna", "bennet", "john"]
Пример вывода:
{'anna': {'a': 2, 'n': 2}, 'bennet': {'b': 1, 'e': 2, 'n': 2, 't': 1}, 'john': {'j': 1, 'o': 1, 'h': 1, 'n': 1}}'''
words = ["anna", "bennet", "john"]
name_dict = {}
for word in words:
    char_dict = {}
    for char in word:
        if char not in char_dict:
            char_dict[char] = word.count(char)
    name_dict[word]= char_dict
print(name_dict)

'''3. Распределение студентов по группам
У вас есть словарь, где ключи — имена студентов, а значения — их баллы за экзамен.
Необходимо распределить студентов по группам:
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
students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}
groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]
distribution = {group: {} for group in groups}
for student, grade in students.items():
    if grade >= 85:
        distribution["Отличники"].update({student: grade})
    elif grade >= 70 and grade <= 84:
        distribution["Хорошисты"].update({student: grade})
    elif grade >= 50 and grade <= 69:
        distribution["Троечники"].update({student: grade})
    else:
        distribution["Не сдали"].update({student: grade})
print(distribution)
