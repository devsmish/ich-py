'''1. Генератор Фибоначчи
Создайте генератор, который генерирует
последовательность Фибоначчи бесконечно,
возвращая по одному числу за раз.
Последовательность Фибоначчи — это ряд чисел,
где каждое следующее число равно сумме двух
предыдущих.
Начинается с 0 и 1.
Пример вывода:
0
1
1
2
3
5
8
13
21
34'''
def fibonacci_row(n):
    res_list = [0, 1]
    for i in range(2, n):
        res_list.append(res_list[-1] + res_list[-2])
    yield from res_list

n = int(input("Enter a length Fibonacci row: "))

gen = fibonacci_row(n)

for _ in range(n):
    print(next(gen))

# Correct option
def fibonacci_row(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = int(input("Enter a length Fibonacci row: "))

for num in fibonacci_row(n):
    print(num)

'''2. Генератор уникальных элементов
Создайте генератор, который принимает список элементов и выдаёт только уникальные значения, сохраняя
порядок их появления в исходном списке
Пример вывода:
3
1
2
4
5
6
7
8
'''
import random

rand_list = []
num_count = int(input("Enter a length of random list: "))
num_limit = int(input("Enter a limit of random list: "))
for _ in range(num_count):
    rand_list.append(random.randint(1, num_limit))
print(rand_list)

def unique_elements(arr: list):
    unique_list = []
    for elem in arr:
        if elem not in unique_list:
            unique_list.append(elem)
            yield elem
    print(unique_list)

gen = unique_elements(rand_list)

for num in gen:
    print(num)