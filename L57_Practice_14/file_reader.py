'''
5.2 Распределение задач
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
Bob выполняет: Настроить сервер
'''
from itertools import cycle
import time

def task_generator(employees, filename='tasks.txt'):
    employees_cycle = cycle(employees)

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
        pass

employees = ["Alice", "Bob", "Charlie"]

gen_ = task_generator(employees)

for _ in range(8):
    emp, task = gen_.__next__()
    print(emp, 'выполняет:', task)