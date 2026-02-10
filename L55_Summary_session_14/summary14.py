# Напишите программу, которая запрашивает у пользователя имя файла с оценками учеников, подсчитывает средний балл
# каждого ученика и выводит результат на экран. Если указанный файл не существует, программа должна вывести ошибку.
# Используйте файл grades.txt.
# Пример вывода:
# Alice: 86.0
# Bob: 87.0
# Charlie: 84.8
from collections import defaultdict

with open(
        "E:\\REPO\\learning\\python\\ich-py\\L55_Summary_session_14\\grades.txt",
        "r",
        encoding="utf-8"
) as grades_file:
    student_grades = defaultdict(list)
    for line in grades_file:
        name, grade, *_ = line.strip().split(", ")
        student_grades[name].append(int(grade))

for name, grades in student_grades.items():
    print(f"{name}: {round(sum(grades) / len(grades), 2)}")
# Alice: 86.0
# Bob: 87.0
# Charlie: 84.8


