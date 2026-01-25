'''Функция deepcopy
Реализуйте аналог deepcopy() с помощью рекурсии. Не забудьте проверить, чтобы изменения в копии не затронули оригинал.
Данные:
original_data = [
 [1, 2, 3], # Вложенный список
 (4, [5, 6], {7, 8}), # Кортеж с вложенными структурами
 {"a": 9, "b": [10, 11]}, # Словарь со списком
 "Hello", # Строка
 [12, (13, 14)], # Список с кортежем
 15.5, # Число с плавающей точкой
 5 # Целое число
]'''
def deep_copy(data):
    if isinstance(data, list):
        return [deep_copy(item) for item in data]
    elif isinstance(data, dict):
        return {key: deep_copy(value) for key, value in data.items()}
    elif isinstance(data, set):
        return {deep_copy(item) for item in data}
    elif isinstance(data, tuple):
        return tuple([deep_copy(item) for item in data])
    else:
        return data
original_data = [
 [1, 2, 3], # Вложенный список
 (4, [5, 6], {7, 8}), # Кортеж с вложенными структурами
 {"a": 9, "b": [10, 11]}, # Словарь со списком
 "Hello", # Строка
 [12, (13, 14)], # Список с кортежем
 15.5, # Число с плавающей точкой
 5 # Целое число
]
copied_data = deep_copy(original_data)

# Проверяем, что копия независима от оригинала
original_data[1][1][0] = 0
print(f"Исходный: {original_data}")
print(f"Копия: {copied_data}")

'''Обратный вывод строки
Напишите рекурсивную функцию, которая выводит строку в обратном порядке.
Данные:
text = "hello"'''
def reverse_string(s):
    if not s:
        return ""
    return s[-1] + reverse_string(s[:-1])
text = "hello"
print(reverse_string(text))

'''Подсчёт определённых слов
Напишите рекурсивную функцию, которая подсчитывает количество вхождений определённого слова во вложенной 
структуре (список списков строк).
Данные:
nested_sentences = [
 ["Python is great", "I love Python"],
 ["Python is powerful", ["Python is everywhere", "Learn Python"]],
 "Coding in Python is fun"]
word = "Python"'''
def count_word(nested_sentences, word):
    if isinstance(nested_sentences, str):
        return nested_sentences.split().count(word)
    if isinstance(nested_sentences, list):
        return sum(count_word(sublist, word) for sublist in nested_sentences)
    return 0
nested_sentences = [
 ["Python is great", "I love Python"],
 ["Python is powerful", ["Python is everywhere", "Learn Python"]],
 "Coding in Python is fun"]
word = "Python"

print("Количество вхождений:", count_word(nested_sentences, word))