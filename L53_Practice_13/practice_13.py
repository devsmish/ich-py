'''Подсчёт частоты слов в файле
Напишите программу, которая подсчитывает, сколько раз каждое слово встречается в файле (не учитывая регистр).
Программа запрашивает имя файла и количество популярных слов для вывода.
Если указанный файл не существует, программа должна вывести ошибку.
Используйте файл text.txt.
Пример ввода:
Введите имя файла: text.txt
Введите количество популярных слов: 3
Популярные слова:
python: 4
is: 3
in: 2'''
from collections import Counter
from typing import Any


def word_counter(file_name, count):
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
        content = content.replace('!', ' ').replace(',', ' ').replace('.', ' ').lower()
        return Counter(content.split()).most_common(count)

try:
    print(word_counter("E:\\REPO\\learning\\python\\ich-py\\L53_Practice_13\\text.txt", 3))
except FileNotFoundError as e:
    print(e)

# Extended version

# from collections import Counter
#
# filename = input("Введите имя файла: ")
#
# def count_words_in_file(filename):
#     with open(filename, "r", encoding="utf-8") as file:
#         text = file.read().lower()
#
# punctuation = '.,!?;:"-'
# for char in punctuation:
#     text = text.replace(char, " ")
#
# return Counter(text.split())
#
# try:
#     word_counts = count_words_in_file(filename)
#     num_words = int(input("Введите количество популярных слов: "))
#     print("\nПопулярные слова:")
#     for word, count in word_counts.most_common(num_words):
#     print(f"{word}: {count}")
# except FileNotFoundError:
#     print("Ошибка: Файл не найден.")
# except ValueError:
#     print("Ошибка: Введите целое число для количества популярных слов.")

'''Удаление пустых строк
Напишите программу, которая удаляет пустые строки из указанного пользователем файла и записывает результат в новый файл.
Имя нового файла формируется автоматически по шаблону <oldname>_cleaned.txt. Если указанный файл не существует, 
программа должна вывести ошибку. Используйте файл tasks.txt.
Пример ввода:
Введите имя файла: tasks.txt
Пример вывода:
Пустые строки удалены, сохранено в
tasks_cleaned.txt.'''
import os
filename = input("Введите имя файла: ")
# Генерация имени нового файла
new_filename = f"{os.path.splitext(filename)[0]}_cleaned.txt"
# # Или изученным способом
# old_name = filename.rsplit('.', 1)
# new_filename = f"{old_name[0]}_cleaned.{old_name[1]}"
try:
    with (open(filename, "r", encoding="utf-8") as infile,
        open(new_filename, "w", encoding="utf-8") as outfile):
        for line in infile:
            if line.strip():
                outfile.writelines(line)
                print(f"Пустые строки удалены, сохранено в {new_filename}.")
except FileNotFoundError:
    print(f"Ошибка: файл '{filename}' не найден.")

'''Анализ продаж по категориям и датам
Напишите программу, которая обрабатывает текстовый файл с данными о продажах.
Используйте файл sales_data.txt.
1. Принимать аргументы командной строки:
python sales_report.py <input_file> <output_directory>
Где:
○ <input_file> — путь к входному файлу с продажами.
○ <output_directory> — папка, куда будут сохранены отчёты.
2. Считать данные из текстового файла, в котором каждая строка содержит информацию в следующем
формате:
имя,дата,сумма,категория,город
Пример входных данных:
Olivia Suarez,2024-08-02,4565,Electronics,Dallas
Jennifer Jacobs,2023-08-19,4963,Automotive,London
Erin Johnson,2024-08-29,1796,Clothing,Miami
3. Сгруппировать данные по годам и месяцам, создавая для каждого года и месяца отдельную папку в
указанной директории.
4. Создать общий отчёт по каждому месяцу (monthly_report.txt), в котором указана суммарная выручка по
каждой категории и общая сумма:
Automotive,109539
Books,133160
Clothing,102001
Electronics,79403
Groceries,104387
Home Appliances,99911
Sports,78782
Full,707183
5. Создать файлы для каждой категории товаров, в которых должны быть указаны все продажи по данной
категории в формате:
дата,имя продавца,сумма
Пример файла Electronics.txt:
2025-02-01,Cynthia Maddox,538
2025-02-01,Kendra Martinez,3799
2025-02-02,Rachel Miller,1097
Все записи в файле должны быть отсортированы по дате.
Пример запуска программы
python sales_report.py data/sales_data.txt reports
Пример созданной структуры
reports/
├── 2024/
│ ├── 12/
│ │ ├── monthly_report.txt
│ │ ├── Automotive.txt
├── 2025/
│ ├── 01/
│ │ ├── monthly_report.txt
│ │ ├── Clothing.txt
│ │ ├── Electronics.txt
│ ├── 02/
│ │ ├── monthly_report.txt
│ │ ├── Groceries.txt
│ │ ├── Sports.txt
Анализ продаж по категориям и датам'''
import sys
import os
from collections import defaultdict

# 1. Чтение и парсинг входного файла
def get_data_dicts(filename) -> list[dict[str, Any]]:
    """
    Читает файл с продажами и преобразует каждую строку в словарь.
    Формат строки: имя, дата, сумма, категория, город
    """
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            name, date, amount, category, city = line.strip().split(",")
            # Разбиваем дату на компоненты
            year, month, day = date.split("-")
            # Добавляем словари в список
            data.append({
                "name": name,
                "date": date,
                "amount": int(amount),
                "category": category,
                "city": city,
                "year": year,
                "month": month,
                "day": day
            })
    return data

# 2. Группировка данных
def process_data(data) -> tuple[defaultdict[Any, defaultdict[Any, int]], defaultdict[Any, defaultdict[Any, list]]]:
    """
    Создаёт две структуры:
    1) Суммарная выручка по категориям для каждого (год, месяц)
    2) Все продажи по категориям для каждого (год, месяц)
    """
    # {(year, month): {category: total_amount}}
    by_year_month = defaultdict(lambda: defaultdict(int))
    # {(year, month): {category: [(date, name, amount), ...]}}
    by_year_month_category = defaultdict(lambda: defaultdict(list))
    for sale in data:
        key = (sale["year"], sale["month"])
        category = sale["category"]
        amount = sale["amount"]
        # Суммы для monthly_report.txt
        by_year_month[key][category] += amount
        # Детальные продажи для файлов категорий
        by_year_month_category[key][category].append(
            (sale["date"], sale["name"], amount)
        )
    return by_year_month, by_year_month_category

# 3. Создание monthly_report.txt
def write_monthly_reports(by_year_month, output_dir):
    """
    Для каждого года и месяца создаёт monthly_report.txt
    с суммой по категориям и общей суммой (Full)
    """
    for (year, month), categories in by_year_month.items():
        # Создание папок reports/<year>/<month>/
        month_path = os.path.join(output_dir, year, month)
        os.makedirs(month_path, exist_ok=True)
        report_path = os.path.join(month_path, "monthly_report.txt")
        total_sum = 0
        with open(report_path, "w", encoding="utf-8") as f:
            for category, amount in categories.items():
                f.write(f"{category},{amount}\n")
                total_sum += amount
            # Общая сумма за месяц
            f.write(f"Общая сумма: {total_sum}\n")

# ---------- 4. Создание файлов по категориям ----------
def write_category_files(by_year_month_category, output_dir):
    for (year, month), categories in by_year_month_category.items():
        month_path = os.path.join(output_dir, year, month)
        os.makedirs(month_path, exist_ok=True)
        for category, sales in categories.items():
            category_path = os.path.join(month_path, f"{category}.txt")
            sales.sort(key=lambda x: x[0])
            with open(category_path, "w", encoding="utf-8") as f:
                for date, name, amount in sales:
                    f.write(f"{date},{name},{amount}\n")

if len(sys.argv) != 3:
        print("Correct usage: python sales_report.py <input_file> <output_directory>")
        sys.exit(1)

filename = sys.argv[1]
output_dir_name = sys.argv[2]

# Текущая рабочая директория
base_dir = os.getcwd()

# Все отчёты будут создаваться здесь
output_dir = os.path.join(base_dir, output_dir_name)

data = get_data_dicts(filename)
by_year_month, by_year_month_category = process_data(data)

write_monthly_reports(by_year_month, output_dir)
write_category_files(by_year_month_category, output_dir)

print(f"Отчёты созданы в директории: {output_dir}")

# print(process_data(filename))
# print(*get_data_dicts(filename), sep="\n")

# Старт скрипта из консоли
# python E:\\REPO\\learning\\python\\ich-py\\L53_Practice_13\\practice_13.py E:\\REPO\\learning\\python\\ich-py\\
# L53_Practice_13\\sales_data.txt E:\\REPO\\learning\\python\\ich-py\\L53_Practice_13\\monthly_report.txt