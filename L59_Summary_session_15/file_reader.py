'''
Дополнительно: если файл tasks.txt отсутствует, программа делает 5 попыток с паузой 3 секунды перед завершением.
'''
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

# input()