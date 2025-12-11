# a = [1, 2, 3]
# b = a
# print(id(a))  # Идентификатор объекта a
# print(id(b))  # Тот же идентификатор
#
# c = [1, 2, 3]
# print(id(c))  # Другой идентификатор, так как это другой объект
#
# a.append(1)
# print(id(a))

# text1 = "hello"
# text2 = text1  # text2 ссылается на тот же объект
# text1 + " Python"  # Создаётся новый объект
# print(text1)
#
# text2 += " world"  # Создаётся новый объект "hello world"
# print(text1)
# print(text2)

# # Пример списка с вложенными элементами
# list_elements = [[1, 2, 3], [4, 5], 6, [7, [8, [9], 10]]]
# # Доступ к элементам первого уровня осуществляется через один уровень индекса.
# print(list_elements[0])  # Вывод: [1, 2, 3] (первый вложенный список)
# print(list_elements[1])  # Вывод: [4, 5] (второй вложенный список)
# print(list_elements[2])  # Вывод: 6 (отдельный элемент)
# print(list_elements[3])  # Вывод: [7, [8, [9], 10]] (вложенный список с дополнительной
# # вложенностью)
# print("hello"[0])
# # Пример списка с вложенными элементами
# list_elements = [[1, 2, 3], [4, 5], 6, [7, [8, [9], 10]]]
# print(list_elements[0][1])  # 2
# # print([1, 2, 3][1])  # 2
# print(list_elements[0][1:])  # 2
#
# # Пример списка с вложенными элементами
# list_elements = [[1, 2, 3], [4, 5], 6, [7, [8, [9], 10]]]
#
# # Получение числа 10
# print(list_elements[3][1][2])  # Доступ к элементу третьего уровня вложенности
# # Получение числа 9
# print(list_elements[3][1][1][0])  # Доступ к элементу четвертого уровня вложенности
# print(list_elements[3][1][1])  # Доступ к элементу четвертого уровня вложенности

# Пример списка с вложенными элементами
# list_elements = [[1, 2, 3], [4, 5], 6, [7, [8, [9], 10]]]
#
# # Сохраняем первый вложенный список во временную переменную
# first_nested_list = list_elements[0]
# # Доступ ко второму элементу через временную переменную
# second_element = first_nested_list[1]
# # В результате будет получен тот же результат, что и при обращении по нескольким индексам
# print(first_nested_list[2])
# print(second_element)

# # Пример коллекции
# list_elements = [[1, 2], [3, 4], [5, 6]]

# Заменим число 2
# list_elements[0][1] = "two"
# print(list_elements)
# # Заменим список [5, 6]
# list_elements[2] = "new"
# print(list_elements)
#
# # Так так элемент является строкой, к нему можно применять строковые методы
# list_elements[0][1] = list_elements[0][1].upper() # Преобразуем строку в верхний регистр
# print(list_elements)
# print(list_elements[0][1][1:])

# list_elements = [[1, 2], [3, 4], [5, 6]]
#
# # Изменим первый элемент вложенного списка, добавив новое значение
# list_elements[0].append('new value')  # Добавляем новый элемент в первый вложенный список
# print(list_elements)

#
# list_elements = [[1, 2], [3, 4], [5, 6]]
# # for sublist in list_elements:
# #     print(sublist)
#
# # Внешний цикл перебирает каждый вложенный список
# for sublist in list_elements:
#     # Внутренний цикл проходит по каждому элементу внутри этих списков
#     for item in sublist:
#         print(item, end=" ")
#     print()

# list_elements = [[1, 2], [3, 4], [5, 6]]
# # Увеличение каждого элемента в коллекциях на 1
# for i, sublist in enumerate(list_elements):
#     for j, item in enumerate(sublist):
#         list_elements[i][j] = item + 1
# print(list_elements)

# list_elements = ["hello", "python", "java"]
# for i, sublist in enumerate(list_elements):
#     for j, item in enumerate(sublist):
#         print(item)
#     print()
# print(list_elements)

# # Удаление элемента по индексу
# numbers = [10, 20, 30, 40]
# del numbers[2]
# print(numbers)  # [10, 20, 40]
#
# # Удаление первого элемента
# fruits = ["apple", "banana", "cherry"]
# del fruits[0]
# print(fruits)  # ['banana', 'cherry']
#
# # Удаление среза
# numbers = [10, 20, 30, 40, 50]
# del numbers[1:3]
# print(numbers)  # [10, 40, 50]


# # Удаление всех элементов (аналог `clear`)
# numbers = [10, 20, 30, 40]
# del numbers[:]
# print(numbers)  # []

# # Удаление переменной
# old_numbers = [1, 2, 3]
# new_numbers = old_numbers
# del old_numbers
# print(new_numbers)  # [1, 2, 3]
# # print(old_numbers)
# # print(dsfs)


# original_list = [1, 2, 3]
# copied_list = original_list  # Это не создаёт новую копию
# copied_list[0] = 99
# print(copied_list)
# print(original_list)


# original_list = [1, 2, 3]
# copied_list = original_list.copy()
# # copied_list = original_list[:]
# # copied_list = list(original_list)
# copied_list[0] = 99
# print(original_list)  # [1, 2, 3]
# print(copied_list)  # [99, 2, 3]

# original_list = [[1, 2], [3, 4]]
# shallow_copy = original_list.copy()
# print(id(original_list))
# print(id(shallow_copy))
# print(id(original_list[0]))
# print(id(shallow_copy[0]))
# shallow_copy[0][0] = 99
# shallow_copy[1] = [0]
# print(original_list)  # [[99, 2], [3, 4]]
# print(shallow_copy)  # [[99, 2], [3, 4]]

# original_list = [[1, 2], [3, 4]]
# shallow_copy = []
# for el in original_list:
#     shallow_copy.append(el)
# print(shallow_copy)
# print(id(original_list))
# print(id(shallow_copy))
# print(id(original_list[0]))
# print(id(shallow_copy[0]))
#
# shallow_copy[1] = [0]
# shallow_copy[0][0] = 99
# print(original_list)  # [[99, 2], [3, 4]]
# print(shallow_copy)  # [[99, 2], [3, 4]]

import copy

original_list = [[1, 2], [3, 4]]
deep_copy = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(original_list)
deep_copy[0][0] = 99
print(original_list)  # [[1, 2], [3, 4]]
print(deep_copy)  # [[99, 2], [3, 4]]






