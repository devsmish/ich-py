'''Фильтр чисел
Создайте генератор, который принимает список чисел и выдаёт только числа, кратные 5.
Данные:
numbers = [12, 15, 33, 40, 55, 62, 75, 83, 90]
Пример вывода:
15
40
55
75
90'''
numbers = [12, 15, 33, 40, 55, 62, 75, 83, 90]

def gen(numbers):
    for i in numbers:
        if i % 5 == 0:
            yield i

for i in gen(numbers):
    print(i)

'''Создайте генератор, который принимает число n и генерирует квадраты чисел от 1 до n включительно
Данные:
n = 10
Пример вывода:
1
4
9
16
25
36
49
64
81
100'''
n = 10

def square_num(n):
    for num in range(1, n + 1):
        yield num ** 2

gen = square_num(10)

for square in gen:
    print(square)

'''Генератор, аналогичный range()
Создайте генератор, который повторяет функциональность range(),
принимая start, stop, step и возвращая последовательность чисел.
Данные:
start = 2
stop = 10
step = 2
Пример вывода:
2
4
6
8'''

def range_analogy(start, stop, step):
    cur_pos = start
    while cur_pos < stop:
        yield cur_pos
        cur_pos += step

start = 2
stop = 10
step = 2

for i in range_analogy(start, stop, step):
    print(i)

# Another variant
def my_range(stop, start=2, step=1):
    current = start
    while (step > 0 and current < stop) or (step < 0 and current > stop):
        yield current
        current += step

start = 2
stop = 10
step = 2

for number in my_range(stop=stop, step=step):
    # for number in my_range(start, stop, step):
    print(number)

'''2. Генератор случайных дат
Создайте генератор, который генерирует случайные даты в пределах одного года.
Генератор должен принимать год в качестве аргумента и выдавать следующую случайную дату при каждом вызове, учитывая 
количество дней в месяце, а также високосные годы.
Пример вывода:
2025-02-14
2025-06-28
2025-09-09'''
import random

year = int(input("Enter year: "))

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def date_generator(year: int):
    day_in_month = {
        1: 31,
        2: 29 if is_leap_year(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31}

    while True:
        ran_month = random.randint(1, 12)
        ran_day = random.randint(1, day_in_month[ran_month])
        yield f"{year}-{ran_month:02d}-{ran_day:02d}"

ran_date = date_generator(year)
for i in range(7):
    print(next(ran_date))

'''3. Генератор случайных имён
Создайте генератор, который выдаёт случайные имена и фамилии.
Выведите 5 имён.
Для получения случайного значения из списка можно использовать choice() из модуля random.
Данные:
first_names = ["Alice", "Bob", "Charlie", "David", "Emma"]
last_names = ["Smith", "Johnson", "Brown", "Williams", "Jones"]
Пример вывода:
Alice Johnson
David Brown
'''
from random import choice

def random_names(first_names: list, last_names: list):
    while True:
        full_name = f"{choice(first_names)} {choice(last_names)}"
        yield full_name

first_names = ["Alice", "Bob", "Charlie", "David", "Emma"]
last_names = ["Smith", "Johnson", "Brown", "Williams", "Jones"]

gen = random_names(first_names, last_names)

for _ in range(5):
    print(next(gen))

'''4. Генератор тестовых данных
Создайте генератор, который повторяет функциональность range(),
принимая start, stop, step и возвращая последовательность чисел.
Данные:
name_gen = random_names()
date_gen = random_dates(2025)
Пример вывода:
('Emma Brown', '2025-02-14')
('Bob Williams', '2025-06-28')
('Charlie Johnson', '2025-09-09')
'''
import random

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def random_dates(year: int):
    day_in_month = {
        1: 31,
        2: 29 if is_leap_year(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31}
    while True:
        ran_month = random.randint(1, 12)
        ran_day = random.randint(1, day_in_month[ran_month])
        yield f"{year}-{ran_month:02d}-{ran_day:02d}"

def random_names(first_names: list, last_names: list):
    while True:
        full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
        yield full_name

def data_test(name_gen, date_gen):
    while True:
        yield (next(name_gen), next(date_gen))

year = int(input("Enter year: "))
first_names = ["Alice", "Bob", "Charlie", "David", "Emma"]
last_names = ["Smith", "Johnson", "Brown", "Williams", "Jones"]

name_gen = random_names(first_names, last_names)
date_gen = random_dates(year)
datas_gen = data_test(name_gen, date_gen)

for _ in range(5):
    print(next(datas_gen))

'''5. Система распределения задач
Программа будет состоять из двух частей, работающих независимо:
Добавление задач – пользователь вводит новые задачи, и они записываются в файл.
Распределение задач – другая программа читает задачи из файла и назначает их сотрудникам по очереди.
Запустите обе программы одновременно.
5.1 Добавление задач
Эта программа запрашивает задачи у пользователя и записывает их в файл tasks.txt. Она работает в бесконечном цикле, пока 
пользователь не введёт exit.
Данные:
Файл tasks.txt – каждая строка содержит одно задание.
Пример файла:
Подготовить отчёт
Провести собрание
Проверить документацию
Разработать новый модуль
Настроить сервер
Пример вывода:
Введите задачу: Подготовить отчёт 
Введите задачу: Провести собрание 
Введите задачу: Проверить документацию 
Введите задачу: Разработать новый модуль 
Введите задачу: Настроить сервер 
Введите задачу: exit'''
# task_writer.py
def write_to_file(filename='tasks.txt'):
    while True:
        with open(filename, 'a', encoding='utf-8') as file:
            task = input('Введите задачу, "exit" to exit: ').strip()

            if task == 'exit':
                break

            if task:
                file.write(task + '\n')

                print('Задача успешно записана!')

write_to_file('tasks.txt')

'''5.2 Распределение задач
Эта программа читает файл tasks.txt и назначает задачи сотрудникам по очереди.
Она использует генератор для постепенного чтения новых задач и назначения сотрудникам.
Дополнительно: если файл tasks.txt отсутствует, программа делает 5 попыток с паузой 3 секунды перед завершением.
Данные:
employees = ["Alice", "Bob", "Charlie"]
Пример вывода:
Alice выполняет: Подготовить отчёт
Bob выполняет: Провести собрание
Charlie выполняет: Проверить документацию
Alice выполняет: Разработать новый модуль
Bob выполняет: Настроить сервер'''
# file_reader.py
from itertools import cycle
import time

def task_generator(employees, filename='tasks.txt'):
    employees_cycle = cycle(employees)

    for retry in range(5):
        try:
            with open(filename, 'r', encoding = 'utf-8') as file:
                while True:
                    task = file.readline().strip()

                    if task:
                        employees = next(employees_cycle)

                        yield employees, task

                    else:
                        print('Задания закончились, ожидаем 3 секунды.')

                        time.sleep(3)

        except FileNotFoundError:
            print('Файл не найден, ожидаем 3 секунды.', 'Попыток затрачено:', retry)

            time.sleep(3)

    else:
        print("Файл не был обнаружен, завершение выполнения.")

employees = ["Alice", "Bob", "Charlie"]

gen_ = task_generator(employees)

for emp, task in gen_:
    print(emp, 'выполняет:', task)