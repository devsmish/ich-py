'''Анализ курсов студентов
Реализовать программу, которая должна:
Прочитать файл student_courses.json, содержащий:
имя,
дату рождения (birth_date) в формате дд.мм.гггг,
дату поступления (enrollment_date) в том же формате,
список курсов.
Вычислить:
Общее количество студентов.
Средний возраст на момент поступления.
Количество студентов на каждом курсе.
Сохранить отчёт в JSON-файл student_courses_report.json.
Данные:[
  {"name": "Diana Williams", "birth_date": "12.06.1983", "enrollment_date": "29.04.2023", "courses": ["Physics", "Chemistry"]},
  {"name": "Tina Miller", "birth_date": "06.07.2004", "enrollment_date": "18.04.2020", "courses": ["Biology", "Business"]},
  {"name": "Kevin Miller", "birth_date": "20.12.2004", "enrollment_date": "16.12.2020", "courses": ["Linguistics", "Math", "History"]},
  {"name": "Fiona Brown", "birth_date": "05.07.1999", "enrollment_date": "02.09.2022", "courses": ["Art", "Philosophy"]},
  {"name": "Charlie Davis", "birth_date": "17.07.1998", "enrollment_date": "17.05.2023", "courses": ["Chemistry", "Physics", "Business"]},
  {"name": "Diana Jones", "birth_date": "24.12.1980", "enrollment_date": "26.11.2021", "courses": ["Economics", "Linguistics"]},
  {"name": "Alice Johnson", "birth_date": "22.09.1981", "enrollment_date": "23.12.2020", "courses": ["Chemistry", "Economics", "Math"]},
  {"name": "Ian Lopez", "birth_date": "23.11.2001", "enrollment_date": "07.05.2020", "courses": ["Philosophy", "Art", "Physics"]},
  {"name": "Kevin Davis", "birth_date": "30.01.1997", "enrollment_date": "20.03.2021", "courses": ["Math", "Economics"]},
  ...]
Пример вывода (student_courses_report.json):{
    "total_students": 100,
    "average_enrollment_age": 27.9,
    "students_per_course": {
        "Art": 21,
        "Biology": 18,
        "Business": 28,
        "Chemistry": 16,
        "Economics": 23,
        "History": 9,
        "Linguistics": 23,
        "Math": 23,
        "Philosophy": 19,
        "Physics": 19
    }
}'''
import json
from datetime import datetime


def analyze_courses():
    with open('E:\\REPO\\learning\\python\\ich-py\\L58_JSON-files_and_DATETIME_modul\\student_courses.json', 'r', encoding="utf-8") as json_file:
        data = json.load(json_file)
        student_count = 0
        sum_age = 0
        dict_courses = {}
        for item in data:
            student_count += 1
            birth = datetime.strptime(item["birth_date"], "%d.%m.%Y")
            enroll = datetime.strptime(item["enrollment_date"], "%d.%m.%Y")
            difference = enroll.year - birth.year
            if (enroll.month, enroll.day) < (birth.month, birth.day):
                sum_age += difference - 1
            else:
                sum_age += difference
            for kurs in item["courses"]:
                if kurs not in dict_courses:
                    dict_courses[kurs] = 1
                else:
                    dict_courses[kurs] += 1
    data_write = {
        "total_students": student_count,
        "average_enrollment_age": round(sum_age / student_count, 1),
        "students_per_course": dict_courses
    }

    with open('E:\\REPO\\learning\\python\\ich-py\\L58_JSON-files_and_DATETIME_modul\\student_courses_report.json', 'w', encoding="utf-8") as json_file:
        json.dump(data_write, json_file, ensure_ascii=False, indent=4)

analyze_courses()

with open('E:\\REPO\\learning\\python\\ich-py\\L58_JSON-files_and_DATETIME_modul\\student_courses_report.json', 'r', encoding="utf-8") as json_file:
    data = json.load(json_file)
    print(data)