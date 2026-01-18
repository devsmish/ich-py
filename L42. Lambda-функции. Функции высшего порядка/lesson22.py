# def square(x):
#     return x * x
#
# def cube(x):
#     return x * x * x
#
# def apply_function(func, value):
#     return func(value)  # Вызываем переданную функцию внутри другой функции
#
# result_square = apply_function(square, 5)  # Передаём функцию square без вызова (скобок)
# result_cube = apply_function(cube, 5)  # Передаём функцию cube без вызова (скобок)
# print(result_square)
# print(result_cube)
#
# # result = apply_function(square(5), 5)  # Ошибка!

# def add(x, y):
#     return x + y
#
# def multiply(x, y):
#     return x * y
#
# # Функции можно хранить в списках, словарях и передавать их динамически
# operations = {
#     "+": add,
#     "*": multiply
# }
# choice = input("Выберите операцию (+, *): ")
# # Из словаря получена функция и скобки с аргументами запускают её
# print(operations[choice](10, 5))

# def process_data(func, data):
#     return func(data)
#
# # Можно передавать не только пользовательские функции, но и встроенные
# result = process_data(abs, -10)
# print(result)

# ------------------------------------------------------


# # Функция принимает число x и возвращает его квадрат
# square = lambda x: x ** 2
# print(square(4))
# print(square(5))
#
# # Аналог с def
# def square(x):
#     return x ** 2
# print(square(4))
# print(square(5))


# # Функция принимает два аргумента и возвращает их сумму
# add = lambda x, y: x + y
# print(add(3, 5))
# print(add(8, 9))
#
# # Аналог с def
# def add(x, y):
#     return x + y
# print(add(3, 5))
# print(add(8, 9))

# def apply_func(func, numbers):
#     return [func(num) for num in numbers]
#
# result = apply_func(lambda x: x + 10, [5, 8, 3])
# print(result)
#
# print(apply_func(lambda x: x ** 2, [2, 3, 4]))
# print(apply_func(lambda x: x ** 4, [2, 3, 4]))

# def add(x, y):
#     return x + y
#
# print((lambda func, a, b: func(a, b))(add, 3, 4))

#
# numbers = [1, 2, 3, 4]
#
# # Каждый элемент списка возводится в квадрат
# squared = map(lambda x: x ** 2, numbers)
# print(squared)
# for i in squared:
#     print(i)
#
# print(list(squared))  # [1, 4, 9, 16]
# print(list(squared))  # [1, 4, 9, 16]



# numbers = [1, 2, 3, 4]
#
# # Каждый элемент списка возводится в квадрат
# squared = list(map(lambda x: x ** 2, numbers))
# print(squared)
# print(*squared)

# a = [1, 2, 3]
# b = [4, 5, 6]
# # Каждая пара элементов списков суммируется
# result = map(lambda x, y: x + y, a, b)
# print(list(result))  # [5, 7, 9]

#
# group_numbers = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
# # К каждому кортежу применяется функция sum
# result = map(sum, group_numbers)
# print(list(result))  # [6, 15, 24]


# result = map(int, input().split())
# # print(list(result))
# print(sum(result))



# numbers = [1, 2, 4, 5, 7, 9, 10, 11]
# # Из списка выбираются только чётные числа
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))  # [2, 4, 10]
# print(numbers)


# data = [0, 1, False, True, '', 'Python', [], [1, 2, 3]]
# # Из списка выбираются только те элементы, которые оцениваются как True
# even_numbers = filter(None, data)
# print(even_numbers)
# print(list(even_numbers))


# from functools import reduce
#
# numbers = [1, 2, 3, 4]
# # Умножение всех элементов списка последовательно
# result = reduce(lambda x, y: x * y, numbers)
# print(result)  # 24
#
#
# numbers = [1, 2, 3, 4]
# # Умножение всех элементов списка, начиная с 10
# result = reduce(lambda x, y: x * y, numbers, 10)
# print(result)  # 240


# data = [0, None, False, 1]
# print(any(data))  # True, так как есть хотя бы одно истинное значение (1)
#
# data = [0, None, False]
# print(any(data))  # False, так как все элементы ложные
#
# data = []
# print(any(data))  # False, так как объект пустой



# data = [1, 2, 3]
# print(all(data))  # True, так как все элементы истинные
#
# data = [1, 0, 3]
# print(all(data))  # False, так как 0 — ложное значение
#
# data = []
# print(all(data))  # True, так как объект пустой
# print(bool(data))


# # Проверка, что хотя бы один объект соответствует условию
# conditions = [x > 10 for x in [5, 20, 8]]
# print(conditions)
# print(any(conditions))  # True
#
# # Проверка, что все объекты соответствуют условию
# conditions = [x > 0 for x in [-5, 20, 8]]
# print(conditions)
# print(all(conditions))


# words = ['mango', 'grape', 'pineapple', 'apple', 'strawberry',
#          'banana', 'kiwi', 'blueberry']
# # Сортировка по длине слов
# print(sorted(words))
# print(sorted(words, key=len))
#
# def last_char_len(s):
#     return s[-1], len(s)
#
# def last_char_lexic(s):
#     return s[-1], s
#
# # Сортировка по последнему символу и длине слова
# print(sorted(words, key=last_char_len))
# # Сортировка по последнему символу и лексикографически
# print(sorted(words, key=last_char_lexic))

#
# words = ['mango', 'grape', 'Ananas', 'apple', 'Strawberry',
#          'Banana', 'pineapple', 'kiwi', 'blueberry']
# # Сортировка по первому символу (игнорируя регистр) и по последнему символу
# result = sorted(words, key=lambda x: (x[0].lower(), x[-1]))
# print(result)

# students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
# # Сортировка списка кортежей по возрасту # (второй элемент)
# sorted_students = sorted(students, key=lambda x: x[1])
# print(sorted_students)

# cities = [('New York', 8419600), ('Los Angeles', 3980400), ('Chicago', 2716000)]
# smallest_city = min(cities, key=lambda x: x[1])
# print(smallest_city)

cities = [('New York', 419600), # 419600
          ('Los Angeles', 3980400), # 3980400
          ('Chicago', 2716000)] # 2716000
smallest_city = min(cities, key=lambda x: x[1])
print(smallest_city)