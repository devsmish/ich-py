# # Создание словаря без указания значения
# keys = ["x", "y", "z"]
# my_dict = dict.fromkeys(keys)  # Каждому ключу присваивается значение `None`
# print(my_dict)  # {'x': None, 'y': None, 'z': None}
#
# # Создание словаря с переданным значением
# keys = [1, 2, 3]
# default_value = "default"
# my_dict = dict.fromkeys(keys, default_value)
# print(my_dict)  # {1: 'default', 2: 'default', 3: 'default'}

#
# keys = ["a", "b", "c"]
# shared_list = []
# my_dict = dict.fromkeys(keys, shared_list)
# my_dict["a"].append(1)  # Изменит общий список для всех ключей
# print(my_dict)  # {'a': [1], 'b': [1], 'c': [1]}
# print(shared_list)


# # Получение значения по существующему ключу
# my_dict = {"name": "Alice", "age": 30}
# print(my_dict.get("name"))  # Alice
# print(my_dict.get("name", "Anonim"))  # Alice
#
# # Запрос отсутствующего ключа без указания значения по умолчанию
# print(my_dict.get("city"))  # None
# # Запрос отсутствующего ключа с указанным значением по умолчанию
# print(my_dict.get("city", "Unknown"))  # Unknown
#

# # Получение значения существующего ключа
# my_dict = {"name": "Alice", "age": 30}
# age = my_dict.setdefault("age")
# print(age)  # 30
# print(my_dict)  # {'name': 'Alice', 'age': 30}
#
# # Добавление нового ключа без указания значения по умолчанию
# country = my_dict.setdefault("country")
# print(country)  # None
# print(my_dict)  # {'name': 'Alice', 'age': 30, 'country': None}
#
# # Добавление нового ключа с переданным значением
# city = my_dict.setdefault("city", "Unknown")
# print(city)  # Unknown
# print(my_dict)  # {'name': 'Alice', 'age': 30, 'country': None, 'city': 'Unknown'}

# my_dict = {"name": "Alice", "age": 30}
# keys = my_dict.keys()
# print(type(keys))
# print(keys)
# # Изменение словаря
# my_dict["city"] = "New York"
# print(keys)  # Значения обновляются
# print(my_dict)  # Значения обновляются
# # Преобразование представления в список
# keys_list = list(keys)
# my_dict["country"] = "USA"
# print(keys_list)  # На списке изменения не отображаются

# my_dict = {"name": "Alice", "age": 30}
# values = my_dict.values()
# print(type(values))
# print(values)
# # Изменение словаря
# my_dict["age"] = 31
# print(values)  # Значение обновляется
# # Преобразование представления в список
# values_list = list(values)
# my_dict["age"] = 32
# print(values_list)  # Изменения на списке не отображаются

# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# for key in my_dict:
#     print(key)
#
# # Аналогично циклу по my_dict
# for key in my_dict.keys():
#     print(key)

#
# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# for value in my_dict.values():
#     print(value)
#
# for key in my_dict:
#     print(my_dict[key])

# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# for key, value in my_dict.items():
#     print(f"{key} - {value}")
#
# for item in my_dict.items():
#     print(f"{item}")
#
# print(my_dict.items())
#
# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# for key in my_dict:
#     print(f"{key} - {my_dict[key]}")


# student_scores = {
#     "Alice": [90, 85, 88],
#     "Bob": [72, 75, 80],
#     "Charlie": [95, 100, 98]
# }
#
# # Доступ к элементу списка внутри словаря
# print(student_scores["Alice"][1])


# school = {
#     "class1": {
#         "students": ["Alice", "Bob", "Charlie"],
#         "teacher": "Mrs. Smith"
#     },
#     "class2": {
#         "students": ["David", "Eva"],
#         "teacher": "Mr. Johnson",
#         "floor": 3
#     }
# }
# # # Доступ к элементу вложенного словаря
# # print(school["class2"]["teacher"])
# #
# # # Доступ к элементу списка, полученного из вложенного словаря
# # print(school["class1"]["students"][0])
#
# # for class_name, class_details in school.items():
# #     print(f"Class: {class_name}")
# #     for key, value in class_details.items():
# #         print(f"\t{key}: {value}")
#
# # Добавление ученика в список
# school["class1"]["students"].append("Daisy")
# print(school["class1"]["students"])
#
# # Удаление ключа из вложенного словаря
# del school["class2"]["teacher"]
# print(school["class2"])


#
# original_dict = {"name": "Alice", "age": 30, "scores": [90, 85, 88]}
# copied_dict = original_dict.copy()
# print(copied_dict)
#
# # Изменение не затронет копию для неизменяемых элементов
# original_dict["age"] = 31
# print(copied_dict)
# # # Изменение затронет копию для изменяемых элементов
# original_dict["scores"].append(80)
# # print(original_dict)
# print(copied_dict)


# import copy
# original_dict = {"name": "Alice", "age": 30, "scores": [90, 85, 88]}
# deep_copied_dict = copy.deepcopy(original_dict)
# print(deep_copied_dict)
# # Любые изменения во вложенном объекте не затронут копию
# original_dict["age"] = 31
# original_dict["scores"].append(80)
# print(original_dict)
# print(deep_copied_dict)


# # Создание словаря с квадратами чисел из списка
# numbers = [1, 2, 3, 4, 2]
# squared_dict = {num: num ** 2 for num in numbers}
# print(squared_dict)
# # Фильтрация элементов
# original_dict = {"a": 5, "b": 2, "c": 0, "d": 3, "e": 0, "f": 3}
# filtered_dict = {key: value for key, value in original_dict.items() if value > 0}
# print(filtered_dict)
# # Анализ данных и сохранение результатов
# words = ["apple", "banana", "cherry"]
# length_dict = {word: len(word) for word in words}
# print(length_dict)


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}
print(dict1 == dict2)  # True

dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}
print(dict1 == dict2)  # False

