'''Список файлов и папок
Напишите программу, которая принимает путь к директории через аргумент командной строки и выводит:
● Отдельно список папок
● Отдельно список файлов
Пример запуска:
python script.py /home/user/documents
Пример вывода:
Содержимое директории '/home/user/documents':
Папки:
- folder1
- folder2
Файлы:
- file1.txt
- file2.txt
- notes.docx'''
import sys
import os

if len(sys.argv) != 2:
     print("Использование: python script.py <директория>")
     sys.exit(1)

directory = sys.argv[1]

if not os.path.isdir(directory):
    print(f"Директория '{directory}' не существует.")
    sys.exit(1)

file_list = []
dir_list = []
for item in os.listdir(directory):
    if os.path.isdir(os.path.join(directory, item)):
        dir_list.append(item)
    else:
        file_list.append(item)

print(f"Содержимое директории '{directory}':")
print("Папки:")
for item in dir_list:
    print(f" - {item}")
print("Файлы:")
for item in file_list:
    print(f" - {item}")

# Для запуска python E:\\REPO\\learning\\python\\ich-py\\L50_Working_with_filesystem\\homework50.py E:\\REPO\\learning\\python\\ich-py

'''Поиск и удаление файлов с указанным расширением
Напишите программу, которая
● Принимает путь к директории и расширение файлов через аргумент командной строки.
● Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
● Спрашивает у пользователя, хочет ли он удалить найденные файлы.
● Если пользователь подтверждает, удаляет их.
Пример запуска
python script.py /home/user/PycharmProjects/project1 .log
Пример вывода:
Найдены файлы с расширением '.log':
- logs/error.log
- logs/system.log
- logs/backup/old.log
- logs/backup/debug.log
Вы хотите удалить эти файлы? (y/n): y
Удаление завершено.'''
import sys
import os

if len(sys.argv) != 3:
    print("Использование: python script.py /home/user/PycharmProjects/ <расширение>")
    sys.exit(1)

directory = sys.argv[1]
if not os.path.isdir(directory):
    print(f"Директория '{directory}' не существует.")
    sys.exit(1)

extension = sys.argv[2]
file_list = []
for root, dirs, files in os.walk(directory):
    for name in files:
        if name.endswith(extension):
            full_path = os.path.join(root, name)
            file_list.append(full_path)

if not file_list:
    print(f"В директории '{directory}' файлов с расширением '{extension}' не найдено.")
    sys.exit(0)
else:
    print(f"В директории '{directory}' найдены файлы с расширением '{extension}': ")
    for item in file_list:
        print(f" - {item}")

user_answer = input("Вы хотите удалить эти файлы? (y/n): ")

if user_answer == "y":
    for file_name in file_list:
        os.remove(file_name)
        print(f"Файл {file_name} удален")
    print("Удаление завершено.")
else:
    print("Удаление отменено.")

# Для запуска python E:\\REPO\\learning\\python\\ich-py\\L50_Working_with_filesystem\\homework50.py E:\\REPO\\learning\\
# python\\ich-py\\L50_Working_with_filesystem\\test_dir .txt