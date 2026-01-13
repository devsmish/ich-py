'''Повторения букв
Реализуйте функцию, которая принимает текст и возвращает словарь с подсчётом количества каждой буквы,
игнорируя регистр.
Данные:
text = "Programming is fun!"
Пример вывода:
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}'''
from collections import Counter
text = "Programming is fun!"
str_text = text.lower().replace(" ", "").replace("!", "")

def repeat_character(str_text):
    cnt_chars = Counter(str_text)
    return cnt_chars

print(repeat_character(str_text))

# Universal variant
from collections import Counter

def repeat_character(text):
    text = text.lower()
    cnt_chars = Counter(ch for ch in text if ch.isalpha())
    return cnt_chars

text = "Programming is fun!"
print(repeat_character(text))

'''Группировка студентов по классам
Создайте структуру для группировки студентов по классам.
Добавьте студентов в соответствующие группы.
Данные:
students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3",
"Daisy")]
Пример вывода:
{'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}'''
from collections import defaultdict

def group_classes(students):
    class_dict = defaultdict(list)
    for student in students:
        class_dict[student[0]].append(student[1])
    return class_dict

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

print(dict(group_classes(students)))

# через dict
def group_classes(students):
    result = {}
    for class_name, student_name in students:
        result.setdefault(class_name, []).append(student_name)
    return result