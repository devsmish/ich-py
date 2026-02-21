'''Реализуйте программу, которая должна:
Прочитать данные из JSON-файла.
Для каждого ученика и предмета вычислить среднюю оценку за каждый учебный квартал:
1 квартал: январь–март
2 квартал: апрель–май (лето пропускается)
3 квартал: сентябрь–декабрь
Записать результаты в новый JSON-файл, сгруппированные по ученикам, предметам и кварталам.
Пример вывода
quarterly_report.json
{
    "Bob": {
        "Science": {
            "Q1": 86.0
        },
        "Literature": {
            "Q1": 94.0,
            "Q2": 68.0,
            "Q3": 81.0
        },
        "History": {
            "Q1": 73.67
        }
    }'''
import json
from collections import defaultdict
from datetime import datetime

def get_quartal(date_str):
    month = datetime.strptime(date_str, "%d-%m-%Y").month
    if month in [9,10,11]:
        return "Q1"
    elif month in [12,1,2]:
        return "Q2"
    elif month in [3,4,5]:
        return "Q3"

# print(get_quarter("10-11-2026"))

with open("E:\\REPO\\learning\\python\\ich-py\\L61_Practice_15\\grades.json", "r", encoding='utf-8') as inputfile:
    data = json.load(inputfile)
    print(data)

grouped_data = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

for d in data:
    name = d["name"]
    grade = d["grade"]
    subject = d["subject"]
    date = d["date"]
    quartal = get_quartal(date)
    if quartal:
        grouped_data[name][subject][quartal].append(grade)
print(grouped_data)

report = {}
for name, subjects in grouped_data.items():
    report[name] = {}
    for subject, quartals in subjects.items():
        report[name][subject] = {}
        for quartal, grades in quartals.items():
            report[name][subject][quartal] = round(sum(grades) / len(grades))
print(report)

with open("E:\\REPO\\learning\\python\\ich-py\\L61_Practice_15\\quarterly_report.json","w", encoding="utf-8") as outfile:
    json.dump(report, outfile, indent=4)

'''2. Поиск немецких мобильных номеров
Реализуйте программу, которая:
● Находит в тексте все немецкие мобильные номера, записанные в одном из следующих форматов:
○ начинаются с +49 или 0049,
○ далее префикс мобильного оператора, начинающийся на 15, 16 или 17,
○ далее — от 7 до 9 цифр (в номере могут быть пробелы, дефисы или табуляции между блоками).
● Очищает найденные номера от пробелов, дефисов, табов.
● Преобразует номер в единый формат, начинающийся с +49.
● Проверяет, что в результате (после очистки):
○ префикс после +49 должен начинаться с 15, 16 или 17.
○ и содержит 1012 цифр после кода страны (то есть общий формат: +49XXXXXXXXXX — от 13 до 15
символов).
● Возвращает список валидных номеров.
Данные
файл german_numbers.txt'''
import re


def check_phone_number():
    with open("E:\\REPO\\learning\\python\\ich-py\\L61_Practice_15\\german_numbers.txt",
        "r", encoding="utf-8") as inputfile:
        data = inputfile.read()
        pattern = r"(?:\+49|0049)[\s\-\\t]*(15|16|17)(?:[\s\-\\t]*\d){7,9}"
        matches = re.findall(pattern, data)
        raw_matches = re.finditer(pattern, data)
        valid_numbers = []
        for match in raw_matches:
            number = match.group()
            # удалить пробелы, дефисы, табы
            clean = re.sub(r"[\s\-\\t]", "", number)
            # заменить 0049 на +49
            if clean.startswith("0049"):
                clean = "+49" + clean[4:]
            # проверка длины
            digits_after = clean[3:]
            if (digits_after.startswith(("15", "16", "17")) and 10 <= len(digits_after) <= 12):
                valid_numbers.append(clean)

        return valid_numbers

gen = check_phone_number()
for item in gen:
    print(item)

'''3. Извлечение email-адресов
Реализуйте программу, которая:
● Находит в тексте все email-адреса, соответствующие следующим критериям:
○ Перед @ допускаются буквы, цифры, точки (.) и подчёркивания (_), но не начинается и не
заканчивается точкой.
○ После @ следует:
■ Домен второго уровня: буквы, цифры, дефисы, точки.
■ Затем домен верхнего уровня (например, .com, .org, .net, .pl), от 2 до 3 букв.
○ Email не может содержать пробелы.
Данные:
text = """
Valid:
- support@mail.com
- info@company.org
- personal_email123@edu.university.net
- user.name@sub.domain.com
- contact_us123@my-site.org
- hello.world@some.place.travel
- admin@server.local
- support@company-name.de
- user@data.edu.pl
Invalid:
- user@domain,com
- name@domaincom
- name@domain.c
- user@domain.toolongtldddddd
- no@space .com
- bad@@mail.com
- missing@dotcom
"""
Пример вывода:
'''
import re

text = """
Valid:
- support@mail.com
- info@company.org
- personal_email123@edu.university.net
- user.name@sub.domain.com
- contact_us123@my-site.org
- hello.world@some.place.travel
- admin@server.local
- support@company-name.de
- user@data.edu.pl
Invalid:
- user@domain,com
- name@domaincom
- name@domain.c
- user@domain.toolongtldddddd
- no@space .com
- bad@@mail.com
- missing@dotcom
"""

pattern = r"\b[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)*@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,5}\b"
emails = re.findall(pattern, text)

for email in emails:
    print(email)

'''4. Извлечение номеров банковских карт
Реализуйте программу, которая должна найти все номера карт, записанные как 16 цифр, разделённые пробелами,
дефисами или без разделителей.
Данные:
text = """
Valid examples:
1234 5678 9012 3456
4321-8765-2109-6543
1234567812345678
1234-5678 9012-3456
Invalid examples:
123456781234567
1234/5678/9012/3456
1234 5678 9012
1234-5678-ABCD-3456
1234--5678--9012--3456
1234 56789 012 3456
"""
Пример вывода:
Валидные номера:
1234 5678 9012 3456
4321-8765-2109-6543
1234567812345678
1234-5678 9012-3456
'''
import re

text = """
Valid examples:
1234 5678 9012 3456
4321-8765-2109-6543
1234567812345678
1234-5678 9012-3456
Invalid examples:
123456781234567
1234/5678/9012/3456
1234 5678 9012
1234-5678-ABCD-3456
1234--5678--9012--3456
1234 56789 012 3456
"""
pattern = r"\b(?:\d{4}[- ]?){3}\d{4}\b"
accounts = re.findall(pattern, text)

print("Валидные номера:\n")
for account in accounts:
    print(account)