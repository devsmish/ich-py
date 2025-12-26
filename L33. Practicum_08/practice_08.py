'''1. Список квадратов
Создайте список, содержащий квадраты всех чётных чисел из диапазона от 1 до заданного пользователем числа включительно.
Пример вывода:
Введите конец диапазона: 20
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]'''
diap = int(input("Введите конец диапазона: "))
quadr_list = [i ** 2 for i in range(2, diap + 1), 2]
print(quadr_list)

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