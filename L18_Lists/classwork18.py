'''1. Список чисел
Напишите программу, которая сохраняет в списке все числа от 0 до n (введённого пользователем), которые
делятся на 3. Выведите эти числа на экран.
Пример вывода:
Введите число: 15'''
from pickletools import long1

n = int(input("Enter a number: "))
num_list = []
for i in range(n + 1):
    if i % 3 == 0:
        num_list = num_list + [i]
print(num_list)

'''2. Список имен
Напишите программу, которая обрабатывает список строк, состоящий из имен. Нужно вывести только те имена, длина 
которых больше средней длины имен в списке. Пример данных для обработки:
names = ["John", "Bob", "Alice", "Anna", "Mark"]
Пример вывода:
Список имён: ['John', 'Bob', 'Alice', 'Anna', 'Mark']
Средняя длина имён: 4.0
Имена длиннее средней длины:
Alice'''
names = ["John", "Bob", "Alice", "Anna", "Mark"]
avg_longnames = 0
longnames = ''
count_names = 0
for name in names:
    avg_longnames = avg_longnames + len(name)
    count_names += 1
    if (len(name) > len(longnames)):
        longnames = name
print("Средняя длина имён:", avg_longnames/count_names)
print("Имена длиннее средней длины:", longnames)