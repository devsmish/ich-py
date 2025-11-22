# fruits = ["apple", "banana", "cherry"]  # Список со строками
# print(fruits)
# numbers = [1, 2, 3]  # Список с числами
# print(numbers)


# numbers = [1, '2', 3, False, "cherry", [6, 7]]  # Список с числами
#
# matrix = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
# print(matrix)

# empty_list = []
# print(empty_list)
#
# my_list = list()
# print(my_list)


# my_list = ["apple", "banana", "cherry", "date"]
# # Доступ к первому элементу
# print(my_list[0])
# # Доступ к последнему элементу с положительным индексом
# print(my_list[3])
# # Доступ к последнему элементу с отрицательным индексом
# print(my_list[-1])
# # Доступ к первому элементу с отрицательным индексом
# print(my_list[-4])

# my_list = [0, 1, 2, 3, 4, 5, 6]
# # Срез с 1-го по 4-й элемент (не включительно)
# print(my_list[1:4])
# # Срез каждого второго элемента
# print(my_list[::2])
# # Срез каждого второго элемента в обратном порядке
# print(my_list[::-2])
# # Срез от 4-го элемента до начала
# print(my_list[4::-1])
# # Срез с 3-го элемента до конца
# print(my_list[3:])
# # Копия списка с помощью среза
# print(my_list[:])
#
# print(my_list[::-1])

# my_list = ["apple", "banana", "cherry"]
#
# # Изменим второй элемент (с индексом 1)
# my_list[1] = "blueberry"
# print(my_list)

# my_list = [10, 20, 30, 40, 50]
# # same_list = my_list
# # print(same_list)
# copy_list = my_list[:]
# print(copy_list)
#
# # Заменим второй и третий элементы
# my_list[1:3] = [200, 300]
# print(my_list)
# # print(same_list)
# print(copy_list)
#
# # finish = "-"
# # print(3,5,6, end=finish)


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# combined_list = list1 + list2
# print(combined_list)
#
# repeated_list = [0] * 5
# print(repeated_list)
# my_list = [1, 2, 3]
# repeated_list = my_list * 3
# print(repeated_list)

# my_list = [1, 2, 3, 4, 5]
# print(3 in my_list)
# print(6 in my_list)
# print([3, 4] in my_list)
# my_list = ["apple", "banana", "cherry"]
# print("apple" in my_list)
# print("app" in my_list)  # Ищет полное совпадение элемента

# my_list = [1, 2, 3, 4, 5]
# print(len(my_list))
# print(sum([1, 2, 3, 4]))
# print(sum(my_list))

# word = "python hello"
# # Строка "разбивается" на отдельные символы
# my_list = list(word)
# print(my_list)
# print(type(my_list))

# my_range = range(1, 11, 2)
# print(my_range)
# print(type(my_range))
# my_list = list(my_range)
# print(my_list)
# print(type(my_list))

# list1 = [1, 2, 3, 4]
# list2 = [1, 2, 3]
# list3 = [1, 3, 0]
# # # Сравнение на равенство
# # print(list1 == list2)
# # print(list1 == list3)
# # # Сравнение на неравенство
# # print(list1 != list2)
# # print(list1 != list3)
# ### Сравнение на больше/меньше, больше или равно/меньше или равно
# print(list1 < list2)
# print(list3 > list1)
# print(list1 <= list2)
# print(list1 >= list3)

# my_list = [1, 2, [3, 4], 5]
#
# for item in my_list:
#     print(item)

my_strings = ["apple", "banana", "cherry"]
# for word in my_strings:
#     print(word)

for word in my_strings:
    print(word)
    for letter in word:
        print("letter:", letter)
    print()

