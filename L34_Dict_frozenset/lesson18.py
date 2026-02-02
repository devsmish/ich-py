# # Создание множества с числами
# numbers = [1, 2, 2, 4, 7, 8, 8, 10]
# even_numbers_set = {num for num in numbers if num % 2 == 0}
# print(even_numbers_set)


# immutable_set = frozenset([1, 2, 3, 4, 5])
# print(immutable_set)
# immutable_from_range = frozenset(range(10))
# print(immutable_from_range)

# # Создание frozenset
frozen_set1 = frozenset([1, 2, 3])
# frozen_set2 = frozenset([4, 5, 6])
#
# # Создание множества, содержащего frozenset
# set_of_frozen_sets = {frozen_set1, frozen_set2}
# print(set_of_frozen_sets)

# person = {"name": "Alice",
#           # "name": "Bob",
#           "age": 30,
#           "city": "New York"}
# print(person)

# print(hash(1))
# print(hash(1.0))
# print(hash(True))

# # При использовании 1, 1.0 и True в качестве ключей в одном словаре или элементах
# #множества, они будут рассматриваться как один и тот же ключ или элемент.
# my_dict = {1.0: "float", 1: "integer", True: "boolean"}
# print(my_dict)
# # В этом примере значение 1.0: "float" будет перезаписано значением 'boolean', так как
# # все три ключа считаются одинаковыми. При этом ключ остается первый из добавленных.
# # Множества также будут содержать только один из таких элементов:
# my_set = {True, 1, 1.0}
# print(my_set)


# # Список кортежей
# pairs = [(("name", "surname"), "Charlie"), ("age", 35), ("city", "Paris")]
# person = dict(pairs)
# print(person)
#
# # Словарь с использованием функции dict()
# person = dict(name="Bob", age=25, city="London")
# print(person)


# # Получение значения по ключу
# my_dict = {"name": "Alice", "age": 30, 1: "num"}
# print(my_dict["name"])
# print(my_dict[1])
# age = my_dict["age"]
# print(age)
# # print(my_dict["city"])
# # Вызовет ошибку

# my_dict = {"name": "Alice", "age": 30}
# if "name" in my_dict:
#     print(my_dict["name"])  # Выведет значение по ключу 'name'
# if "city" in my_dict:
#     print(my_dict["city"])  # Не выполняется, так как ключ 'city' отсутствует

# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# for key in my_dict:
#     print(f"Ключ={key}, значение={my_dict[key]}")



# my_dict = {"name": "Alice", "age": 30}
# print(my_dict)
# my_dict["city"] = "New York"  # Добавление нового элемента
# print(my_dict)
# my_dict["city"] = "Minsk"  # Обновление элемента
# print(my_dict)

# Обновление значений и добавление новых ключей
my_dict = {"name": "Alice", "age": 30}
my_dict.update({"age": 32, "country": "USA"})
print(my_dict)

# Обновление с использованием списка кортежей
my_dict.update([("name", "Bob"), ("email", "bob@example.com")])
print(my_dict)

# Обновление с использованием именованных аргументов
my_dict.update(city="New York", orders=[])
print(my_dict)



