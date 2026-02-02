# Python Fundamentals 2025: Домашнее задание 20
'''### 1. Простое число
Напишите функцию, которая проверяет, является ли число n простым (делится только на 1 и само себя) и возвращает булевый
результат. Данные:
n = 17
Пример вывода:
Число 17 является простым'''
# teacher
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = 17
print(f"Число {n} {'является' if is_prime(n) else 'не является'} простым")

# Another variant
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True

n = 17
print(f"Число {n} {'является' if is_prime(n) else 'не является'} простым")

'''2. Фильтрация чисел по чётности
Напишите функцию, которая принимает filter_type ("even" или "odd") и произвольное количество чисел, возвращая только те, 
которые соответствуют фильтру.
Пример вызова:
print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))
Пример вывода:
[2, 4, 6]
[15, 25]
Некорректный фильтр'''
# teacher
def filter_numbers(filter_type, *args):
    if filter_type == "even":
        return [num for num in args if num % 2 == 0]
    elif filter_type == "odd":
        return [num for num in args if num % 2 != 0]
    return "Некорректный фильтр"

print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))

'''3. Объединение словарей
Напишите функцию, которая принимает любое количество словарей и объединяет их в один. Если ключи повторяются, 
используется значение из последнего словаря.
Данные:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}
Пример вызова:
print(merge_dicts(dict1, dict2, dict3))
Пример вывода:
{'a': 1, 'b': 3, 'c': 4, 'd': 5}'''
# teacher
def merge_dicts(*dicts):
    merged = {}
    for d in dicts:
        merged.update(d)
    return merged

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}

print(merge_dicts(dict1, dict2, dict3))

# Python Fundamentals 2025: Домашнее задание 21
'''1. Повторения букв
Реализуйте функцию, которая принимает текст и возвращает словарь с подсчётом количества каждой буквы, игнорируя регистр.
Данные:
text = "Programming is fun!"
Пример вывода:
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}'''
# teacher
from collections import Counter

def count_letters(text):
    return dict(Counter([char for char in text.lower() if char.isalpha()]))

text = "Programming is fun!"
result = count_letters(text)
print(result)

'''2. Группировка студентов по классам
Создайте структуру для группировки студентов по классам. Добавьте студентов в соответствующие группы.
Данные:
students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
Пример вывода:
{'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}'''
# teacher
from collections import defaultdict

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

# Группируем студентов по классам
class_groups = defaultdict(list)
for class_name, student in students:
    class_groups[class_name].append(student)

print(dict(class_groups))

# Another variant
from collections import defaultdict

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

def group_by_key(data):
    # Группируем студентов по классам
    class_groups = defaultdict(list)
    for class_name, student in data:
        class_groups[class_name].append(student)
    return dict(class_groups)

print(group_by_key(students))