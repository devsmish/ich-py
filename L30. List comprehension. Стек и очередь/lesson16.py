# numbers = [1, 4, 6, 7, 9]
# # Возведение каждого элемента numbers в квадрат
# # squares = [n ** 2 for n in numbers]
# squares = [numbers.append(numbers[i] ** 2) for i in range(len(numbers))]
# print(squares)
# print(numbers)  # Изначальный список останется без изменений

# numbers = [1, 4, 6, 7, 9]
# # Возведение каждого элемента numbers в квадрат
# squares = [n ** 2 for n in numbers]
# print(squares)
# print(numbers)  # Изначальный список останется без изменений


# numbers = [1, 4, 6, 7, 9]
# # Возведение каждого элемента numbers в квадрат
# squares = []
# for n in numbers:
#     squares.append(n ** 2)
#
# print(squares)
# print(numbers)  # Изначальный список останется без изменений

# # List comprehension
# words = ["hello", "world", "python"]
# uppercase_words = [word.upper() for word in words]
# # uppercase_words = []
# # uppercase_words = [uppercase_words.append(word.upper()) for word in words]
# print(uppercase_words)

# # Эквивалент с циклом for
# words = ["hello", "world", "python"]
# uppercase_words = []
# for word in words:
#     uppercase_words.append(word.upper())
# print(uppercase_words)


# # List comprehension
# even_numbers = [x for x in range(10) if x % 2 == 0]
# print(even_numbers)
#
# # Эквивалент с циклом for
# even_numbers = []
# for x in range(10):
#     if x % 2 == 0:
#         even_numbers.append(x)
# print(even_numbers)


# # List comprehension
# words = ["apple", "banana", "cherry", "date"]
# words_with_a = [word for word in words if 'a' in word]
# print(words_with_a)
#
# # Эквивалент с циклом for
# words = ["apple", "banana", "cherry", "date"]
# words_with_a = []
# for word in words:
#     if 'a' in word:
#         words_with_a.append(word)
# print(words_with_a)
#
# # List comprehension
# numbers = [2, 7, 5, 4, 1, 1, 7, 8]
# modified_list = [x if x % 2 == 0 else -1 for x in numbers]
# print(modified_list)
#
# # Эквивалент с циклом for
# numbers = [2, 7, 5, 4, 1, 1, 7, 8]
# modified_list = []
# for x in numbers:
#     if x % 2 == 0:
#         modified_list.append(x)
#     else:
#         modified_list.append(-1)
# print(modified_list)


# # List comprehension
# words = ["hi", "apple", "banana", "cat", "blueberry", "on"]
# modified_words = [word
#                   if len(word) > 5
#                   else ('medium' if len(word) >= 3 else 'short')
#                   for word in words]
# print(modified_words)
# # Эквивалент с циклом for
# words = ["hi", "apple", "banana", "cat", "blueberry", "on"]
# modified_words = []
# for word in words:
#     if len(word) > 5:
#         modified_words.append(word)
#     else:
#         if len(word) >= 3:
#             modified_words.append('medium')
#         else:
#             modified_words.append('short')
# print(modified_words)
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # List comprehension
# pairs = [(x, y) for x in range(3) for y in "AB"]
# print(pairs)
#
# # Эквивалент с циклом for
# pairs = []
# for x in range(3):
#     for y in "AB":
#         pairs.append((x, y))
#
# print(pairs)


# List comprehension
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened = [num for row in matrix for num in row]
# print(flattened)
#
# # Эквивалент с циклом for
# flattened = []
# for row in matrix:
#     for num in row:
#         flattened.append(num)
# print(flattened)

# # Объединение нескольких итерируемых объектов одинаковой длины
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# cities = ['Hamburg', 'Berlin', 'Munich']
# # combined = list(zip(names, ages, cities))
# combined = zip(names, ages, cities)
# print(combined)
# print(*list(combined))
# print(*list(combined))

# # Объединение нескольких итерируемых объектов разной длины
# list1 = [1, 2, 3]
# list2 = ['a', 'b']
# result = zip(list1, list2)
# print(list(result))

# # Использование в цикле for
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# data = zip(names, ages)
# ages[1] = 0
#
# print(*zip(names, ages))
# for name, age in data:
#     print(f"{name} is {age} years old.")

# stack = []
# # Добавление элементов в стек
# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)
# # Удаление последних элементов из стека
# print(stack.pop())
# print(stack.pop())
# # Текущий стек
# print(stack)

from collections import deque
queue = deque()
# Добавление элементов в очередь
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
# Удаление первых элементов из очереди
print(queue.popleft())
print(queue.popleft())
# Текущая очередь
print(queue)

