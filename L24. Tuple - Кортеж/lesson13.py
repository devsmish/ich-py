# text = "Some text {}, {}"
# # text2 = f"Some text {5 + 9}, {input()}"
#
# print(text.format(5 + 9, input()))
# print(text.format(5 + 9, input()))

# my_tuple = (1, 2, 3, "apple", True)
# print(my_tuple)
# print(type(my_tuple))

# print(1, 2, 3, "apple", True)
# print((1, 2, 3, "apple", True))
# print([1, 2, '3', "apple", True])

# empty_tuple = ()
# print(empty_tuple)  # Вывод: ()
# print(type(empty_tuple))  # Вывод: ()

# single_element_tuple = (5,)
# print(single_element_tuple)
# print(type(single_element_tuple))

# empty_tuple = tuple()
# print(empty_tuple)  # Вывод: ()
# print(type(empty_tuple))  # Вывод: ()

# print(divmod(13, 5))
# print(type(divmod(13, 5)))

# my_tuple = (10, 20, 30, 40)
# print(my_tuple[1])
# print((10, 20, 30, 40)[1])
# print(my_tuple[-1])

# my_tuple = (10, 20, 30)
# Попытка изменить элемент вызовет ошибку
# my_tuple[1] = 40
# TypeError: 'tuple' object does not
# support item assignment
#
# tuple1 = (1, 2)
# tuple2 = (3, 4)
# print(tuple1 + tuple2)  # Конкатенация кортежей
#
# my_tuple = (1, 2)
# print(my_tuple * 3)  # Повторение кортежей
#
# my_tuple = (10, 20, 30)
# print(20 in my_tuple)  # Проверка на наличие элемента
#
# my_tuple = (1, 2, 3, 4, 5)
# print(len(my_tuple))  # Длина кортежа
#
# # Сравнение кортежей происходит аналогично спискам, то есть поэлементно
# tuple1 = (1, 2, 3, 4)
# tuple2 = (1, 2, 4)
# print(tuple1 == tuple2)  # Сравнение кортежей
# print(tuple1 < tuple2)  # Сравнение кортежей

# my_list = [1, 2, 3]
# # my_tuple = tuple(my_list)
# my_tuple = tuple("text")
# my_tuple2 = ("text",)
# print(my_tuple)
# print(my_tuple2)
# print(type(my_tuple))

# my_tuple = (1, 2, 3)
# my_list = list(my_tuple)
# print(my_list)
# print(type(my_list))
# my_list[1] = 0
# print(my_list)

# my_list = [3]
# my_list = 3
# my_tuple = tuple(my_list)
# print(my_tuple)
# print(type(my_tuple))

# print("python"[5])
# print([1, 2, 3, 4, 5, 6, 7][5])
# print([1, 2, 3, 4, 5, 6, 7], [5])

# my_tuple = (10, 20, 30, 40)
# for item in my_tuple:
#     print(item)

# Упаковка нескольких значений в кортеж
# packed_tuple = 1, 2, 3
# packed_tuple = 1,
# packed_tuple = [1, 2, 3], 1 + 5, "dsfs".upper()
# print(packed_tuple)
# print(type(packed_tuple))
# # list(1,)
# print(list(packed_tuple))

# # result = divmod(13, 5)
# # print(result)
# result = "12"
# # print(result[0])
# # print(result[1])
# # int_div = result[0]
# # rest_div = result[1]
# int_div, rest_div = result
# print(int_div, rest_div)


# # Кортеж с тремя элементами
# packed_tuple = (1, 2, 3)
# # Распаковка значений кортежа в переменные
# a, b, c = packed_tuple
# print(a, b, c)

# numbers = [1, 2, 3, 4, 5, 6]
# # Вывод коллекции
# print(numbers)
# print(numbers[0], numbers[1], numbers[2],
#       numbers[3], numbers[4], sep=" - ")
# # Вывод элементов по отдельности
# print(*numbers, sep=" - ")


# # numbers = [1, 2, 3, 4, 5]
# numbers = (1, 2, 3, 4, 5)
# # Распаковка первого элемента в a,
# # последнего в b, остальные элементы в other
# a, *other, b = numbers
# # a, *other, b = 1, (2, 3, 4), 5
# print(a)
# print(b)
# print(other)

# pairs = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
# for element in pairs:
#     print(element)
#     print(f"Число: {element[0]}, Фрукт: {element[1]}")

# number, fruit = pairs[0]
# print(number, fruit)
# Распаковка элементов кортежа в переменные
# for number, fruit in pairs:
#     print(f"Число: {number}, Фрукт: {fruit}")

# pairs = [(1, 'apple'),
#          (2, 'banana', 34.76),
#          (3, 'cherry', 324.556, 14)]
#
# for number, fruit, *_ in pairs:
#     print(_)
#     print(f"Число: {number}, Фрукт: {fruit}")
# print(pairs)

# fruits = ["apple", "banana", "cherry"]
# enumerated_fruits = enumerate(fruits)
# # Чтобы увидеть содержимое, преобразуем # объект enumerate в список
# print(enumerated_fruits)
# print(list(enumerated_fruits))

fruits = ["apple", "banana", "cherry"]

# for element in enumerate(fruits):
#     print(element)

# for index, fruit in enumerate(fruits):
#     print(f"{index}: {fruit}")

# for index in range(len(fruits)):
#     print(f"{index}: {fruits[index]}")

# languages = ("Python", "Java", "C++")
# for index, language in enumerate(languages, start=1):
#     print(f"{index}: {language}")

# numbers = [10, 20, 30, 40]
#
# for index, value in enumerate(numbers):
#    numbers[index] = value * 10
#
# print(numbers)
#
# numbers = [10, 20, 15, 30, 25, 35]
#
# # Проходим по списку, кроме последнего элемента
# for index, value in enumerate(numbers[:-1], start=1):
#     if value > numbers[index]:
#         print(f"{value} больше, чем {numbers[index]}")
#     else:
#         print(f"{value} меньше или равно {numbers[index]}")

# text = "Python"
#
# for index, letter in enumerate(text):
#     print(f"{index}: {letter}")
#
# my_tuple = (1, 2, 3)
# # a, b, *c = my_tuple[::-1]
# b, a, *c = my_tuple
# print(a, b)
#
# for el in my_tuple[::-1]:
#     print(el)
#
# print(my_tuple[::-1])

# languages = ("Python", "Java", "C++")
# for index, language in list(enumerate(languages))[::-1]:
#     print(f"{index}: {language}")

# my_tuple = (1, 2, 3, 2, 4, 2)
# count_of_twos = my_tuple.count(2)
# print(count_of_twos)

# my_tuple = (10, 20, 30, 20, 40, 20)
# index_of_first_twenty = my_tuple.index(20)
# print(index_of_first_twenty)
#
# my_tuple = (10, 20, 30, 20, 40, 20)
# index_of_first_twenty = my_tuple[2:].index(20) + 2
# print(index_of_first_twenty)
# index_of_first_twenty = my_tuple.index(20, 2)
# print(index_of_first_twenty)

lst = [1, 2, 3]
tpl = 1, 2, 3
lst + [4,]
tpl + (4,)
print(lst)
print(tpl)
# lst[0] = "new"
# print(lst)

tpl2 = tpl
tpl = tpl + (4,)
print(tpl)
print(tpl2)

lst2 = lst
# lst = lst + [4,]
lst[0] = "new"
print(lst)
print(lst2)
