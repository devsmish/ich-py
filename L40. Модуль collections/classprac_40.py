'''1. Частотный анализ слов
Напишите программу, которая подсчитывает количество вхождений каждого слова в тексте.
Программа должна игнорировать регистр слов и символы . и ,.
Данные:
text = "This is a test. This test is only a test."
Пример вывода:
{'this': 2, 'is': 2, 'a': 2, 'test': 3, 'only': 1}'''
from collections import Counter
text = "This is a test. This test is only a test."
# Приводим текст к нижнему регистру и разделяем на слова
words = text.lower().replace(".", "").replace(",", "").split()
# Подсчитываем частоту слов
word_count = Counter(words)
print(dict(word_count))

'''2. Список студентов по факультетам
Напишите программу, которая принимает список студентов и их факультетов (кортежи) и
группирует студентов по факультетам в словарь.
Данные:
students = [
 ("Иван", "Физика"),
 ("Мария", "Математика"),
 ("Пётр", "Физика"),
 ("Анна", "Математика"),
 ("Олег", "Информатика"),
 ("Наталья", "Физика"),
]
Пример вывода:
Факультеты и студенты:
Физика: ['Иван', 'Пётр', 'Наталья']
Математика: ['Мария', 'Анна']
Информатика: ['Олег'] '''
from collections import defaultdict

def group_students_by_faculty(students):
    faculty_dict = defaultdict(list)
    for name, faculty in students:
        faculty_dict[faculty].append(name)
    return dict(faculty_dict)

students = [
 ("Иван", "Физика"),
 ("Мария", "Математика"),
 ("Пётр", "Физика"),
 ("Анна", "Математика"),
 ("Олег", "Информатика"),
 ("Наталья", "Физика"),
]

result = group_students_by_faculty(students)
print("Факультеты и студенты:")
for faculty, names in result.items():
    print(f"{faculty}: {names}")