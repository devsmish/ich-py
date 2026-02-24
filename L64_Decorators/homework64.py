'''1. Среднее время выполнения
Создайте декоратор measure_time, который измеряет и выводит среднее время
выполнения функции за 5 вызовов.
Функция может быть любой: например, сортировка списка, чтение из файла или
расчёты.
Пример применения:
@measure_time
def compute():
 total = 0
 for i in range(10_000_000):
 total += i
 return total
 Пример вывода:
Среднее время выполнения для 5 вызовов:
0.21 секунд
Результат: 49999995000000'''
import time
def measure_time(func):
    def wrapper(*args, **kwargs):
        total_time = result = 0
        for i in range(5):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            total_time += (end - start)
        avg = total_time / 5
        print(f"Среднее время выполнения для 5 вызовов: {round(avg, 2)} секунд")
        print(f"Результат: {result}")
        return result
    return wrapper

@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

compute()

'''2. Среднее время выполнения с количеством вызовов
Доработайте декоратор measure_time, чтобы он принимал параметр repeats —
количество вызовов функции.
Декоратор должен выполнять функцию указанное число раз и выводить среднее
время выполнения.
Пример вывода:
Среднее время выполнения для 10 вызовов:
0.21 секунд
Результат: 49999995000000
Пример применения:
@measure_time(10)
def compute():
 total = 0
 for i in range(10_000_000):
 total += i
 return total
Пример вывода:
Среднее время выполнения для 10 вызовов:
0.21 секунд
Результат: 49999995000000
'''
import time
def measure_time(repeat):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = result = 0
            for i in range(repeat):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                total_time += (end - start)
            avg = total_time / repeat
            print(f"Среднее время выполнения для {repeat} вызовов: {round(avg, 2)} секунд")
            print(f"Результат: {result}")
            return result
        return wrapper
    return decorator

repeat = int(input("Enter the number of counts: "))

@measure_time(repeat)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

compute()