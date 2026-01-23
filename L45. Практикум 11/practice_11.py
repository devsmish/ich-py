'''Задание 1.1
Фильтрация четных с функцией
Напишите функцию-предикат, которая проверяет четный ли переданный элемент. Также напишите функцию, которая принимает
функцию-предикат и список чисел. Она должна возвращать новый список, содержащий только элементы, для которых предикат
возвращает True.
Данные:
nums = [1, 2, 3, 4, 5, 6]
Пример вывода:
[2, 4, 6]'''
from typing import Callable

def is_even(num: int) -> bool:
    return num % 2 == 0

def list_even(predicat: Callable[[int], bool], nums: list[int]) -> list[int]:
    return [num for num in nums if predicat(num)]

nums = [1, 2, 3, 4, 5, 6]

print(list_even(is_even, nums))

'''1.2 Фильтрация четных с filter
Выполните те же условия, что в задаче "Фильтрация списка с функцией", но решите с помощью filter и lambda.
Данные:
nums = [1, 2, 3, 4, 5, 6]
Пример вывода:
[2, 4, 6]'''
nums = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda num: num % 2 == 0, nums)
print(list(even_numbers))

'''2.1 Фильтрация списка строк
Отфильтруйте в новый список только слова, длина которых больше трех символов. Реализуйте в виде функции.
Данные:
words = ["hi", "Hello", "a", "python", "Ok"]
Пример вывода:
['Hello', 'python']'''
words = ["hi", "Hello", "a", "python", "Ok"]

def sort_len_words(words: list[str]) -> list[str]:
    sorted_list = [word for word in words if len(word) > 3]
    return sorted(sorted_list, key=len)

print(sort_len_words(words))

'''2.2 Фильтрация списка строк по длине
Доработайте функцию так, чтобы можно было передавать значение минимальной длины слов, которые нужно оставить.
words = ["hi", "Hello", "a", "python", "Ok"]
min_len = 2
Пример вывода:
['hi', 'Hello', 'python', 'Ok']'''
words = ["hi", "Hello", "a", "python", "Ok"]
min_len = int(input("Enter a number: "))

def sort_len_words(min_len: int, words: list[str]) -> list[str]:
    sorted_list = [word for word in words if len(word) > min_len]
    return sorted(sorted_list, key=len)

print(sort_len_words(min_len, words))


'''2.3 Фильтрация списка строк по критерию
Доработайте функцию так, чтобы можно было передавать критерии отбора слов, которые нужно оставить.
Например:
● слова, начинаются с заглавной буквы
● слова из одного символа
● слова начинаются и заканчиваются одной буквой, независимо от регистра
words = ["hi", "Hello", "a", "python", "Ok", "Radar"]
Пример вывода:
['Hello', 'Ok', 'Radar']
['a']
['a', 'Radar']'''
words = ["hi", "Hello", "a", "python", "Ok", "Radar"]

choice = input("Выберите критерий отбора из (1, 2, 3): ")

def begin_with_caps_a_z(words: list[str]) -> list[str]:
    sorted_list = [word for word in words if word[0].isupper()]
    return sorted_list

def one_char(words: list[str]) -> list[str]:
    sorted_list = [word for word in words if len(word) == 1]
    return sorted_list

def start_end_same_letter(words: list[str]) -> list[str]:
    sorted_list = [word for word in words if word[0].lower() == word[-1].lower()]
    return sorted_list

filter_types = {"1": begin_with_caps_a_z,
                "2": one_char,
                "3": start_end_same_letter}

# # Из словаря получена функция и скобки с аргументами запускают её
print(filter_types[choice](words))

'''3. Агрегирование списка
Вычислите произведение всех элементов списка с помощью функции высшего порядка.
Данные:
numbers = [1, 2, 3, 4, 5]
Пример вывода:
120'''
from functools import reduce
numbers = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x * y, numbers))

# Another variant
numbers = [1, 2, 3, 4, 5]
from functools import reduce
from typing import Iterable
def count_get_multiple(numbers: Iterable[int]) -> int:
    return reduce(lambda x, y: x * y, numbers)
print(count_get_multiple(numbers))

'''4. Сортировка списка по длине
Отсортируйте список слов по длине, используя параметр.
Данные:
words = ["apple", "banana", "kiwi", "grape"]
print(sort_by_length(words))
Пример вывода:
['kiwi', 'grape', 'apple', 'banana']'''
words = ["apple", "banana", "kiwi", "grape"]
def sort_by_length(words: list[str]) -> list[str]:
    return sorted(words, key=len)
print(sort_by_length(words))

'''5. Очередь с ограничением времени
Реализуйте функцию, которая принимает очередь задач с указанием времени их выполнения и лимит.
Если суммарное время превышает заданный лимит, программа должна удалять из очереди задачи с
минимальным временем выполнения, пока лимит не будет соблюдён или не останется выполнимых за остаток
времени задач.
Данные:
tasks = {"task1": 5, "task2": 3, "task3": 7, "task4": 2}
time_limit = 10
Пример вывода:
Задачи с лимитом по времени:
{'task3': 7, 'task2': 3}
'''
def select_tasks(tasks: dict, time_limit: int) -> dict:
    result = {}
    remaining_time = time_limit

    # сортируем по времени выполнения по убыванию
    for task, time in sorted(tasks.items(), key=lambda x: x[1], reverse=True):
        if time <= remaining_time:
            result[task] = time
            remaining_time -= time

    return result

tasks = {"task1": 5, "task2": 3, "task3": 7, "task4": 2}
time_limit = 10

print("Задачи с лимитом по времени:")
print(select_tasks(tasks, time_limit))

'''6. Анализ оценок студентов
Дан список студентов с их оценками по разным предметам.
Напишите программу, которая:
● Вычисляет среднюю оценку для каждого студента.
● Возвращает словарь студентов с их средней оценкой, отсортированный по убыванию оценок.
Данные:
students = [
 {"name": "Alice", "grades": [90, 85, 88]},
 {"name": "Bob", "grades": [78, 81, 75]},
 {"name": "Charlie", "grades": [95, 92, 90]},
 {"name": "Diana", "grades": [88, 84, 82]}
]
Пример вывода:
{'Charlie': 92.33, 'Alice': 87.67, 'Diana': 84.67, 'Bob': 78.0}'''

def sort_students(students: list[dict[str, list[int]]]) -> dict[str, float]:
    stud_avg_grades = {item["name"]: round((sum(item["grades"]) / len(item["grades"])), 2) for item in students}
    return sorted(stud_avg_grades.items(), key=lambda item: item[1], reverse=True)

students = [
 {"name": "Alice", "grades": [90, 85, 88]},
 {"name": "Bob", "grades": [78, 81, 75]},
 {"name": "Charlie", "grades": [95, 92, 90]},
 {"name": "Diana", "grades": [88, 84, 82]}
]

print(sort_students(students))

'''7. Поиск максимального элемента
Отсортируйте слова в списке исходя из суммы порядковых номеров всех символов в слове.
К примеру "kiwi" = ord("k") + ord("i") + ord("w") + ord("i") = 107 + 105 + 119 + 105 = 436.
Попробуйте решить в одну строку с помощью lambda и функций высшего порядка.
Данные:
words = ["banana", "kiwi", "grapefruit", "apple"]
Пример вывода:
['kiwi', 'apple', 'banana', 'grapefruit']'''
def sort_words(words: list[str]) -> list[str]:
    return sorted(words, key=lambda word: sum(ord(x) for x in word))

words = ["banana", "kiwi", "grapefruit", "apple"]

print(sort_words(words))

'''8. Очередь с LRU-кэшированием
Реализуйте функцию, которая поддерживает механизм LRU-кэша для очереди задач. Функция должна принимать:
● Текущую очередь задач.
● Новые задачи для добавления.
● Максимальный размер очереди.
Если лимит очереди превышен, удаляйте задачи, которые не использовались дольше всех.'''

'''9. Цепочка шифрования строки
Реализуйте функции:
1. Преобразуйте все буквы в предложении в верхний регистр.
2. Зашифруйте строку, сдвинув символы на 5 элементов вправо.
3. Переверните строку.
Реализуйте функцию шифрования, которая последовательно применит каждую из списка переданных функций
к переданной строке.
Данные:
sentence = "Functional programming is powerful"
functions = [to_uppercase, shift_encrypt, reverse_string]
Пример вывода:
QZKWJ\TU%XN%LSNRRFWLTWU%QFSTNYHSZK'''

'''10. Аннотация структур данных
Напишите функцию, которая принимает список строк и возвращает словарь, где ключи — строки, а значения — длина этих
строк. Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.
Данные:
words = ["apple", "banana", "cherry"]
Пример вывода:
{'apple': 5, 'banana': 6, 'cherry': 6}'''
from functools import reduce


def dict_by_length(words_data: list[str]) -> dict[str, int]:
    return {word: len(word) for word in words_data}
words = ["apple", "banana", "cherry"]
print(dict_by_length(words))

'''11. Генерация отчёта
Напишите функцию, которая принимает имя пользователя и необязательный список его достижений. Если список пуст,
возвращается сообщение "Нет достижений". Если список не пуст, возвращается строка с перечислением достижений. Добавьте
документацию и аннотации типов для всех параметров и возвращаемого значения.
Данные:
name = "Alice"
achievements = ["Won chess tournament", "Completed marathon", "Published a book"]
Пример вывода:
Alice: Won chess tournament, Completed marathon, Published a book'''
def user_report(name: str, achievs_data: list[str] | None = None) -> str:
    if achievs_data:
        return f"{name}: {', '.join(achievs_data)}."
    return "Нет достижений!"
user_name = "Alice"
achievements = ["Won chess tournament", "Completed marathon", "Published a book"]
print(user_report(user_name, achievements))
print(user_report(user_name))