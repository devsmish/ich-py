'''1. Список квадратов.
Создайте список, содержащий квадраты всех чётных чисел из диапазона от 1 до заданного пользователем числа включительно.
Пример вывода:
Введите конец диапазона: 20
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]'''
from itertools import count

diap = int(input("Введите конец диапазона: "))
quadr_list = [i ** 2 for i in range(2, diap + 1, 2)]
print(quadr_list)

'''2. Фильтрация по символу
Создайте новый список, исключив все строки, содержащие введённый пользователем символ.
Данные:
words = ["apple", "cherry", "kiwi", "banana", "orange"]
Пример вывода:
Исключить символ: r
['apple', 'kiwi', 'banana']'''
words = ["apple", "cherry", "kiwi", "banana", "orange"]
char = input("Исключить символ: ")
exceptions_list = []
if len(char) > 1:
    print("Вы ввели больше одного символа!")
for word in words:
    if char not in word:
        exceptions_list.append(word)
print(exceptions_list)

'''3. База данных обитателей джунглей
Данные:
animals = ["тигр", "слон", "обезьяна", "змея"]
weights = [250, 4000, 15, 5]
Пример вывода:
['Тигр весит 250 кг', 'Слон весит 4000 кг', 'Обезьяна весит 15 кг', 'Змея весит 5 кг']
Самое лёгкое животное: змея'''
animals = ["тигр", "слон", "обезьяна", "змея"]
weights = [250, 4000, 15, 5]
paare = zip(animals, weights)
min_weight = min(weights)
light_animal = ''
for animal, weight in paare:
    print(f"{animal.capitalize()} весит {weight} кг")
    if min_weight == weight:
        light_animal = animal
print("Самое лёгкое животное:", light_animal.capitalize())

# Another variant
print([f"{animal.capitalize()} весит {weight} кг" for animal, weight in zip(animals, weights)])
min_weights = min(weights)
min_animals = weights.index(min_weights)
snake = animals[min_animals]
print (f"Самое лёгкое животное: {snake.capitalize()}")

'''4. Группы слов
Группируйте слова по длине в обратном порядке, отсортированные по алфавиту внутри группы.
Данные:
words = ["apple", "banana", "kiwi", "cherry", "pear", "grape", "melon"]
Пример вывода:
Группы слов: [['banana', 'cherry'], ['apple', 'grape', 'melon'], ['kiwi', 'pear']]'''
words = ["apple", "banana", "kiwi", "cherry", "pear", "grape", "melon"]

# Получаем уникальные длины слов
lengths_word = set()
for word in words:
    lengths_word.add(len(word))

# Сортируем длины по убыванию
sorted_lengths = sorted(lengths_word, reverse=True)

# Формируем группы
sorted_list = []
for length in sorted_lengths:
    temp_list = []
    for word in words:
        if len(word) == length:
            temp_list.append(word)
    sorted_list.append(sorted(temp_list))

print("Группы слов:", sorted_list)

'''5. Распаковка матрицы
Создайте список, содержащий все элементы двумерной матрицы в одном измерении.
Данные:
matrix = [[1, 2], [3, 4], [5, 6]]
Пример вывода:
[1, 2, 3, 4, 5, 6]'''
matrix = [[1, 2], [3, 4], [5, 6]]
res_matrix = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        res_matrix.append(matrix[i][j])
print(res_matrix)

# Variant with list comprehension
matrix = [[1, 2], [3, 4], [5, 6]]
res_matrix = [elem for row in matrix for elem in row]
print(res_matrix)

'''6. Координатная сетка
Создайте список всех возможных координат на квадратной сетке размером n x n.
Пример вывода:
Введите размер координатной сетки: 3
Координаты: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]'''
coordinate_grid = int(input("Введите размер координатной сетки: "))
coordinates = [(i, j) for i in range(coordinate_grid) for j in range(coordinate_grid)]
print(coordinates)

'''7. Сравнение матриц
Проверьте, совпадают ли диагональные элементы двух квадратных матриц одинакового размера.
Данные:
matrix1 = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
matrix2 = [
 [1, 0, 3],
 [0, 5, 0],
 [7, 0, 9]
]
Пример вывода:
Совпадают ли главные диагонали: True
Совпадают ли побочные диагонали: True'''
matrix1 = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
matrix2 = [
 [1, 0, 3],
 [0, 5, 0],
 [7, 0, 9]
]
n = len(matrix1)
count = 0
for i in range(len(matrix1)):
    if matrix1[i][i] == matrix2[i][i]:
        count += 1
if count == n:
    print("Совпадают ли главные диагонали: True")
else:
    print("Совпадают ли главные диагонали: False")
count = 0
for i in range(len(matrix1)):
    if matrix1[i][-1 - i] == matrix2[i][-1 - i]:
        count += 1
if count == n:
    print("Совпадают ли побочные диагонали: True")
else:
    print("Совпадают ли побочные диагонали: False")

# Another variant
matrix1 = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
matrix2 = [
 [1, 0, 3],
 [0, 5, 0],
 [7, 0, 9]
]
same_main = same_said = True
for i in range(len(matrix1)):
    if matrix1[i][i] != matrix2[i][i]:
        same_main = False
print("Совпадают ли главные диагонали:", same_main)

for i in range(len(matrix1)):
    if matrix1[i][-1 - i] != matrix2[i][-1 - i]:
        same_said = False
print("Совпадают ли побочные диагонали:", same_said)

'''8. Подсчёт уникальных слов
Напишите программу, которая принимает строку текста, разделённого пробелами, и определяет количество уникальных слов.
Данные:
text = "Apple orange apple banana Orange"
Пример вывода:
Количество уникальных: 3'''
text = "Apple orange apple banana Orange"
text_list = text.lower().split()
text_set = set(text_list)
print("Количество уникальных:",len(text_list))
print(text_set)

# Another variant
text = "Apple orange apple banana Orange".lower().split(' ')
print('Количество уникальных:', len(set(text)))

'''9. Одинаковые значения
Проверка, состоят ли два списка чисел из одинаковых цифр (независимо от порядка).
Данные:
list1 = [1, 2, 3, 4, 4]
list2 = [4, 3, 2, 1, 1]
Пример вывода:
True'''
list1 = [1, 2, 3, 4, 4]
list2 = [4, 3, 2, 1, 1]
print(set(list1) == set(list2))

'''10. Охота за сокровищами
Определение различий и пересечений между двумя наборами драгоценностей.
Данные:
chest1 = {"золото", "серебро", "рубины", "алмазы"}
chest2 = {"серебро", "рубины", "изумруды", "сапфиры"}
Пример вывода:
Только в первом сундуке: {'золото', 'алмазы'}
Общее в обоих сундуках: {'серебро', 'рубины'}
Все уникальные драгоценности: {'золото', 'серебро', 'рубины', 'алмазы', 'изумруды', 'сапфиры'}'''
chest1 = {"золото", "серебро", "рубины", "алмазы"}
chest2 = {"серебро", "рубины", "изумруды", "сапфиры"}
print("Только в первом сундуке:", chest1 - chest2)
print("Общее в обоих сундуках:", chest1 & chest2)
print("Все уникальные драгоценности:", chest1 | chest2)

'''11. Уникальные в множестве
Создание списка с элементами, которые есть только в одном из двух множеств. Решить без использования операторов множеств.
Данные:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
Пример вывода:
[1, 2, 4, 5]'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}
list1 = list(set1)
list2 = list(set2)
res_list = []
for i in range(3):
    if list1[i] not in res_list and list1[i] not in list2:
        res_list.append(list1[i])
    if list2[i] not in res_list and list2[i] not in list1:
        res_list.append(list2[i])
print(res_list)

# Another variant
set1 = {1, 2, 3}
set2 = {3, 4, 5}
res = list((set1 - set2) | (set2 - set1))
print(res)
res = list((set1 | set2) - (set2 & set1))
print(res)

res = []
for item in set1:
    if item not in set2:
        res.append(item)

for item in set2:
   if item not in set1:
       res.append(item)
print(res)

'''12. Уникальные по порядку
Формирование списка уникальных чисел в порядке их появления.
Данные:
numbers = [4, 1, 7, 6, 2, 6, 8, 1, 5, 4]
Пример вывода:
Уникальные: [4, 1, 7, 6, 2, 8, 5]'''
numbers = [4, 1, 7, 6, 2, 6, 8, 1, 5, 4]
set_num = set(numbers)
ordered_list = []
for item in numbers:
    if item in set_num:
        ordered_list.append(item)
        set_num.discard(item)
print("Уникальные:", ordered_list)

# Another variant
numbers = [4, 1, 7, 6, 2, 6, 8, 1, 5, 4]
unique_list= []
unique = set()
# print (set(numbers) )
for number in numbers:
    if number not in unique:
        unique.add(number)
        unique_list.append(number)
print(unique_list)

'''13. Очередь заказов
Реализуйте очередь для обработки заказов, пока пользователь не введёт "exit".
Пример вывода:
Введите заказ или "exit" для завершения: Pizza
Введите заказ или "exit" для завершения: Burger
Введите заказ или "exit" для завершения: Pasta
Введите заказ или "exit" для завершения: exit
Первый заказ: Pizza
Осталось 2 заказов:
- Burger
- Pasta'''
from collections import deque
queue = deque()
while True:
    order = input("Enter your order or (exit): ")
    if order == "exit":
        break
    queue.append(order)
print("Первый заказ:", queue[0])
print(f"Осталось {len(queue) - 1} заказов:")
for order in list(queue)[1:]:
    print("-", order)
