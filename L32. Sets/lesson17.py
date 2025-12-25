# # Создание множества с помощью фигурных скобок
# unique_numbers = {1, 2, 3, 4, 5}
# print(unique_numbers)
# print(type(unique_numbers))
# # Создание пустого множества с использованием функции set()
# empty_set = set()
# print(empty_set)
# print(type(empty_set))
# # Ошибка: {} создаёт пустой словарь, а не множество
# empty = {}
# print(type(empty))


# # Хеш-код для строки
# print(hash("hello"))
# print(hash("hello"))  # Хеш-код одинаковый для одного значения
# print(hash('1'))
#
# # Хеш-код для числа
# print(hash(42))
# print(hash(1))
# print(hash(1.0))

# # Хеш-код для bool
# print(hash(True))
#
# # Хеш-код для кортежа
# my_tuple = (1, 2, 3)
# print(hash(my_tuple))


# my_set = {'20', '10', '30', '40'}
#
#
# # Каждый элемент проходит через хеш-функцию
# print(hash(20))  # Вывод хеш-кода для элемента 20
# print(hash(10))  # Вывод хеш-кода для элемента 10
# print(hash(30))  # Вывод хеш-кода для элемента 30
# print(hash(40))  # Вывод хеш-кода для элемента 40
#
#
# print(my_set)
# print(my_set)
# print(my_set)


# # Преобразование списка
# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique_numbers = set(numbers)
# print(unique_numbers)
# # Преобразование строки
# text = "hello"
# unique_chars = set(text)
# print(unique_chars)
# # Преобразование объекта range
# numbers = set(range(10))
# print(numbers)


# my_list = [1, 2, 3]
# my_set = {my_list}
# print(my_set)
#
# my_set = {1, 2, "3"}
# print("3" in my_set)
# print(hash("3") in my_set)
# # print(["3"] in my_set)


# # Метод add()
# my_set = {1, 2, 3}
# my_set.add(4)
# my_set.add(3)
# print(my_set)
#
# # Метод remove()
# my_set = {1, 2, 3}
# my_set.remove(2)
# print(my_set)
# # my_set.remove(2)  # Попытка повторного удаления вызовет ошибку KeyError
#
# # Метод discard()
# my_set = {1, 2, 3}
# my_set.discard(2)
# my_set.discard(4)  # Ошибки не будет
# print(my_set)

# # Метод pop()
# my_set = {"1", "2"}
# print(my_set)  # Оставшиеся элементы
# removed_element = my_set.pop()
# print(removed_element)
# print(my_set)  # Оставшиеся элементы
# print(my_set.pop())
# print(my_set)  # Оставшиеся элементы
# # print(my_set.pop())  # Вызовет ошибку KeyError, так как элементов больше нет.
#
# # Метод clear()
# my_set = {1, 2, 3}
# my_set.clear()
# print(my_set)

# # Метод copy()
# original_set = {1, 2, 3}
# copied_set = original_set.copy()
#
# # Проверим, что это отдельный объект
# copied_set.add(4)
# print(copied_set)
# print(original_set)

# my_set = {3, 1, 4, 2}
# print(sorted(my_set))


# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
#
# result1 = set1.union(set2)  # Неизменяющий метод
# result2 = set1 | set2  # Использование оператора
# print(result1)
# print(result2)
# print(set1)
#
# set1.update(set2)  # Изменяющий метод
# print(set1)

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# result1 = set1.intersection(set2)  # Неизменяющий метод
# result2 = set1 & set2  # Использование оператора
# print(result1)
# print(result2)
# print(set1)
#
# set1.intersection_update(set2)  # Изменяющий метод
# print(set1)

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# result1 = set1.difference(set2)  # Неизменяющий метод
# result2 = set1 - set2  # Использование оператора
# print(result1)
# print(result2)
# print(set1)
#
# set1.difference_update(set2)  # Изменяющий метод
# print(set1)

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# result1 = set1.symmetric_difference(set2)  # Неизменяющий метод
# result2 = set1 ^ set2  # Использование оператора
# print(result1)
# print(result2)
# print(set1)
#
# set1.symmetric_difference_update(set2)  # Изменяющий метод
# print(set1)

# set1 = {1, 3}
# set2 = {1, 2}
# set3 = {1, 2, 3, 4}
# print(set1 <= set2)
# print(set2 <= set1)
# print(set2 < set1)
# print(set1.issubset(set3))


# set1 = {1, 2, 3, 5}
# set2 = {2, 1}
# set3 = {1, 2, 3, 4}
# print(set1 >= set2)
# print(set2 >= set1)
# print(set1 > set3)
# print(set1.issuperset(set3))

# set1 = {1, 2, 3}
# set2 = {3, 2, 1}
# print(set1 == set2)
#
#
# set1 = {1, 2, 3}
# set2 = {3, 2, 1}
# print(set1 != set2)


# set1 = {1, 2}
# set2 = {3, 4}
# set3 = {2, 3}
# print(set1.isdisjoint(set2))
# print(set1.isdisjoint(set3))


my_set = {'10', '20', '30', '40', '50'}

for item in my_set:
    print(item)
