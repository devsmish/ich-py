# # добавление числа
# numbers = [1, 2, 3]
# numbers2 = numbers
# numbers.append(4)
# numbers2.append(5)
# print(numbers)
# print(numbers2)

# # добавление строки
# fruits = ["apple", "banana"]
# fruits.append("cherry")
# print(fruits.append("cherry"))
# print(fruits)

# fruits = ["apple", "banana"].append("cherry")
# print(fruits)

# # добавление другой коллекции в список
# nested_list = [1, 2, 3]
# nested_list.append([4, 5])
# print(nested_list)
#
#
# # добавление нескольких элементов
# nested_list = [1, 2, 3]
# nested_list.append(4, 5)  # вызовет
# # TypeError, так как ожидается один элемент


# # расширение списка другой коллекцией
# numbers = [1, 2, 3]
# numbers.extend([4, 5, 6])
# print(numbers)
# for i in [7, 8, 9]:
#     numbers.append(i)
# print(numbers)

# # расширение списком строк
# fruits = ["apple", "banana"]
# fruits.extend(["cherry"])
# fruits.extend("cherry")
# print(fruits)

# # расширение списка строкой (символы строки добавляются по отдельности)
# fruits = ["apple", "banana"]
# fruits.extend("cherry")
# print(fruits)
# # расширение списка другим итеририруемым объектом (например, range)
# numbers = [0]
# numbers.extend(range(1, 5))
# print(numbers)

# # расширение списка несколькими элементами
# numbers = [1, 2, 3]
# numbers.extend(4, 5)  # вызовет TypeError, так как ожидается один элемент

# # расширение списка неитерируемым объектом
# numbers = [1, 2, 3]
# numbers.extend([])
# # numbers.extend([4])
# # numbers.extend(4)  # вызовет TypeError, так как int не является итерируемым объектом
# print(numbers)

# # вставка элемента в начало
# fruits = ["apple", "banana"]
# fruits.insert(0, "blueberry")
# print(fruits)
#
# # вставка элемента между другими
# numbers = [1, 2, 3]
# numbers.insert(1, 4)
# print(numbers)

# # вставка в конец списка с индексом, превышающего длину списка
# animals = ["cat", "dog"]
# animals.insert(10, "rabbit")
# print(animals)

# # вставка другой коллекции
# nested_list = [1, 2, 3]
# nested_list.insert(2, [4, 5])
# print(nested_list)

# # использование отрицательного индекса для вставки
# letters = ['a', 'b', 'c']
# letters.insert(-1, 'x')
# print(letters)

# # вставка элемента без указания индекса
# numbers = [1, 2, 3]
# numbers.insert(5)
# # вызовет TypeError, так как ожидается два аргумента: индекс и элемент


# # удаление первого вхождения элемента
# fruits = ["apple", "banana", "cherry", "banana"]
# fruits.remove("banana")
# print(fruits)
#
# # повторное удаление первого вхождения элемента
# print(fruits.remove("banana"))
# print(fruits)
#
# # попытка удалить несуществующий элемент ()
# numbers = [1, 2, 3, 4, 5]
# # numbers.remove(10)  # вызовет ValueError


# # удаление и возврат последнего элемента
# numbers = [10, 20, 30, 40]
# last_item = numbers.pop()  # возвращенный элемент можно присвоить переменной
# print(last_item)
# last_item = numbers.pop()  # возвращенный элемент можно присвоить переменной
# print(last_item)
# print(numbers)

# # удаление и возврат элемента по индексу
# numbers = [10, 20, 30, 40]
# second_item = numbers.pop(1)
# print(numbers)
# print(second_item)
#
# # # попытка удалить элемент по несуществующему индексу
# # numbers.pop(10)  # вызовет ValueError

# nums = [10, 20, 30, 40]
# # очистка всего списка
# fruits = ["apple", "banana", "cherry", nums]
# nums.clear()
# # nums[6]
# nums = 1
# print(fruits)
# fruits2 = fruits
# fruits2.clear()
# print(fruits)
# print(fruits2)
# print(nums)



# # # поиск первого вхождения элемента "banana"
# # fruits = ["apple", "banana", "cherry", "banana", "cherry"]
# # banana_index = fruits.index("banana")
# # print(banana_index)
# # поиск первого вхождения "banana", начиная с индекса 2
# fruits = ["apple", "banana", "cherry", "banana", "cherry"]
# banana_index = fruits.index("banana", 2)
# print(banana_index)
# # поиск "cherry" в диапазоне индексов от 1 до 4 (не включая 4)
# fruits = ["cherry", "banana", "cherry", "banana", "cherry"]
# banana_index = fruits.index("cherry", 3, 4)
# print(banana_index)
# # # поиск индекса элемента, которого нет в списке
# # fruits = ["apple", "banana", "cherry", "banana"]
# # index = fruits.index("orange")  # вызовет ValueError

# # подсчёт вхождений элемента
# fruits = ["apple", "banana", "cherry", "banana"]
# banana_count = fruits.count("banana")
# print(banana_count)
#
# # подсчёт элементов, которых нет в списке
# orange_count = fruits.count("orange")
# print(orange_count)

# # Сортировка по возрастанию (по умолчанию)
# numbers = [4, 1, 7, 2, 9]
# print(numbers.sort())
# # numbers.sort()
# print(numbers)
# # Сортировка по убыванию с параметром reverse=True
# numbers = [4, 1, 7, 2, 9]
# numbers.sort(reverse=True)
# print(numbers)
# Сортировка строк по алфавиту
# fruits = ["banana", "apple", 1, " ", "cherry", "4"]
# fruits.sort()  # По умолчанию лексикографическое сравнение
# print(fruits)
#
# # Использование встроенной функции len()**`len()`** для сортировки строк по их длине, а не
# # лексикографически.
# fruits = ["banana", "apple", "cherry", "blueberry"]
# fruits.sort(key=len)
# print(fruits)

# # Использование встроенной функции max() для сортировки кортежей по максимальному элементу.
# tuples = [(3, 6), (1, 7, 9), (12, 5), (1, 3, 7)]
# #            6        9         12         7
# tuples.sort(key=max)
# print(tuples)
# tuples.sort(key=max, reverse=True)
# print(tuples)

# numbers = [4, 1, 7, 2, 9]
# numbers.reverse()
# print(numbers)
# fruits = ["apple", "banana", "cherry"]
# fruits.reverse()
# print(fruits)

# # Сортировка списка чисел
# numbers = [3, 1, 4, 1, 5]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(numbers)

# # Сортировка строки
# letters = "bca"
# sorted_letters = sorted(letters)
# # Вернет отсортированные символы по отдельности
# print(sorted_letters)
# print(letters)
#
# # Сортировка кортежа по длине строк в порядке убывания
# words = ("apple", "banana", "kiwi")
# sorted_words = sorted(words, key=len, reverse=True)
# print(sorted_words)
# print(words)


# # Разворот списка
# numbers = [3, 1, 4, 1, 5]
# reversed_numbers = reversed(numbers)  # возвращает не list, а list_reverseiterator
# print(type(reversed_numbers))
# print(reversed_numbers)
# list_reversed_numbers = list(reversed_numbers)
# # чтобы увидеть элементы, нужно преобразовать в list
# print(list_reversed_numbers)
# for el in reversed_numbers:
#     print(el)

# for _ in range(2):
#     # reversed_numbers[_]  # not subscriptable
#     print(reversed_numbers.__next__())
# print()
#
# list_reversed_numbers = list(reversed_numbers)
# # чтобы увидеть элементы, нужно преобразовать в list
# print(list_reversed_numbers)


# # Разворот строки
# word = "hello"
# reversed_letters = reversed(word)
# print(reversed_letters)
# reversed_word = ''.join(reversed_letters)
# print(reversed_word)



# # Поиск минимального/максимального значения в списке
# numbers = [4, 1, 7, 2, 9]
# print(min(numbers))
# print(max(numbers))
#
# # Поиск минимального/максимального значения среди отдельных аргументов
# print(min(3, 5, 2, 8))
# print(max(3, 5, 2, 8))

# # Поиск минимального/максимального символа
# chars = "Python"
# print(min(chars))
# print(max(chars))

# Использование параметра key для поиска по длине строк
# words = ["banana", "apple", "kiwi", "grape"]
# print(min(words))
# print(min(words, key=len))
# print(max(words, key=len))

# min_word = words[0]
# # lexical
# for el in words:
#     if el < min_word:
#         min_word = el
# print(min_word)
#
# min_word = words[0]
# # len
# for el in words:
#     if len(el) < len(min_word):
#         min_word = el
# print(min_word)


# Сумма чисел в списке
numbers = [4, 1, 7, 2, 9]
total_sum = sum(numbers)
print(total_sum)

# Сумма чисел в списке с начальным значением
total_sum_with_start = sum(numbers, 1000)
print(total_sum_with_start)

# Сумма чисел в кортеже
numbers_tuple = (1, 2, 3)
total_sum_tuple = sum(numbers_tuple)
print(total_sum_tuple)


