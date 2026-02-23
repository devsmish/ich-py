
# import logging
# #
# # # Настраиваем логирование: записи будут сохраняться в файл "functions.log"
# logging.basicConfig(
#     filename="functions.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     encoding="utf-8"
# )
#
# def log_decorator(func):
#     def wrapper(*args, **kwargs):  # Принимаем все аргументы функции
#         logging.info(f"Функция {func.__name__} вызвана с аргументами: {args}, {kwargs}")
#         result = func(*args, **kwargs)  # Передаём аргументы в функцию
#         logging.info(f"Функция {func.__name__} вернула: {result}")
#         return result  # Возвращаем результат
#     return wrapper
#
#
# @log_decorator
# def add(a, b):
#     return a + b
#
# @log_decorator
# def say_hello():
#     print("Привет!")
#
# # Принимает аргументы
# print(add(a=3, b=5))
# # Без аргументов
# say_hello()
#
#
# def upper_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Возвращаем результат")
#         # Возвращаем результат в верхнем регистре
#         return func(*args, **kwargs).upper()
#     return wrapper
#
# @upper_decorator
# def get_text():
#     return "hello"
#
# result = get_text()
# print("Результат:", result)

# # import functools
# from functools import wraps
#
# def simple_decorator(func):
#     # @functools.wraps(func)  # Сохраняет имя и документацию оригинальной функции
#     @wraps(func)  # Сохраняет имя и документацию оригинальной функции
#     def wrapper(*args, **kwargs):
#         """Вложенная функция wrapper"""
#         print("\nДекорированная функция: ")
#         print(f"Оригинальное имя функции: {func.__name__}")
#         print(f"Оригинальная документация: {func.__doc__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# # @simple_decorator
# def example_function():
#     """Это оригинальная функция."""
#     print("Привет!")
#
# print("Имя декорированной функции:", example_function.__name__)
# print("Документация декорированной функции:", example_function.__doc__)
# example_function()


#
# def message_decorator(message):
#     def decorator(func):
#         def wrapper():
#             print(message)  # Используем переданный аргумент
#             return func()
#         return wrapper
#     return decorator
#
# @message_decorator("Начинаем выполнение")
# def analise_data():
#     print("Данные проанализированы")
#
# @message_decorator("Загрузка данных...")
# def load_data():
#     print("Данные загружены")
#
# analise_data()
# print()
# load_data()


# import time
#
# def retry(attempts):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(attempts):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     print(f"Попытка {i+1} не удалась: {e}")
#                     time.sleep(5)  # Подождём перед новой попыткой
#             print("Все попытки исчерпаны.")
#         return wrapper
#     return decorator
#
# @retry(3)
# def get_data(filename):
#     """Читает данные из файла"""
#     with open(filename, "r", encoding="utf-8") as file:
#         return file.read()
#
# # Пример использования
# data = get_data("data.txt")
# if data:
#     print("Содержимое файла:")
#     print(data)
# else:
#     print(f"Nothing: {data}")


# def border_decorator(func):
#     def wrapper():
#         print("*" * 100)  # Верхняя граница
#         func()
#         print("*" * 100)  # Нижняя граница
#     return wrapper
#
# def repeat_decorator(func):
#     def wrapper():
#         for _ in range(3):  # Повторяем вызов трижды
#             func()
#     return wrapper
#
# @repeat_decorator  # Применяется первым
# @border_decorator  # Применяется вторым
# def print_line():
#     print("-" * 100)
#
# print_line()


def log_decorator(func):
    def wrapper(*args, **kwargs):  # Принимаем все аргументы функции
        print(f"Функция {func.__name__} вызвана с аргументами: {args}, {kwargs}")
        result = func(*args, **kwargs)  # Передаём аргументы в функцию
        print(f"Функция {func.__name__} вернула: {result}")
        return result  # Возвращаем результат
    return wrapper

sum = log_decorator(sum)  # Вызываем декоратор, теперь decorated = wrapper

print(sum([1, 2, 3]))