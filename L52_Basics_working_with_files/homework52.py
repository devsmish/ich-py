'''1. Фильтрация по ключевому слову
Напишите программу, которая ищет в файле все строки, содержащие указанное пользователем слово, и
сохраняет их в новый файл.
● Имя нового файла формируется как <keyword>_<original_filename>.
● Если файл не существует, программа должна вывести ошибку.
● Если совпадения не найдены, новый файл не создаётся.
Используйте файл system_log.txt.
Пример ввода:
Введите имя файла для поиска: system_log.txt
Введите ключевое слово: error
Пример вывода:
Строки, содержащие 'error',
сохранены в error_system_log.txt.'''
import os

filename = input("Enter your file name: ")
keyword = input("Enter your keyword: ")
full_path = os.path.join(os.getcwd(), filename)

def find_keywords(full_path: str, keyword: str) -> list [str]:
    lines = []
    with open(full_path, 'r', encoding="utf-8") as open_file:
        for line in open_file:
            if keyword.lower() in line.lower():
                lines.append(line)
    return lines

try:
    matched_lines = find_keywords(full_path, keyword)
    if not matched_lines:
        print(f"Нет строк, содержащих ключевое слово: {keyword}")
    else:
        new_filename = f"{keyword}_{filename}"
        new_path = os.path.join(os.getcwd(), new_filename)
        with open(new_path, 'w', encoding='utf-8') as new_file:
            new_file.writelines(matched_lines)
        print(f"Строки, содержащие '{keyword}', сохранены в {new_filename}")
except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")

'''2. Поиск и удаление дубликатов
Напишите программу, которая удаляет дублирующиеся строки из файла и сохраняет результат в новый файл.
● Имя нового файла формируется как unique_<original_filename>.
● Если файл не существует, программа должна вывести ошибку.
● Исходный порядок строк должен сохраниться.
● Если в файле нет дубликатов, создаётся точная копия файла.
Используйте файл movies_to_watch.txt.
Пример ввода:
Введите имя файла: movies_to_watch.txt
Пример вывода:
Дубликаты удалены. Уникальные
строки сохранены в
unique_movies_to_watch.txt.'''
import os
filename = input("Введите имя файла: ")
full_path = os.path.join(os.getcwd(), filename)

new_filename = f"unique_{filename}"
new_path = os.path.join(os.getcwd(), new_filename)

set_lines = set()
has_duplicates = False

try:
    with (open(full_path, "r", encoding="utf-8") as infile,
        open(new_path, "w", encoding="utf-8") as outfile):
        for line in infile:
            if line not in set_lines:
                outfile.write(line)
                set_lines.add(line)
            else:
                has_duplicates = True
    if has_duplicates:
        print(f"Дубликаты удалены. Уникальные строки сохранены в {new_filename}")
    else:
        print(f"В файле не было дубликатов. Создана копия {new_filename}")
    if not set_lines:
        print(f"Исходный файл {filename} пустой")
except FileNotFoundError:
    print(f"Ошибка: файл '{filename}' не найден.")
