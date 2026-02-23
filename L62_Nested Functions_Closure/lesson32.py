# def outer_function():
#     print("Внутри внешней функции")
#
#     def inner_function():
#         print("Внутри вложенной функции")
#
#     inner_function()  # Вызов вложенной функции
#     print("some extra")
#     inner_function()
#
# outer_function()
# # inner_function()  # Вызовет ошибку

# def inner_function():
#     print("Внутри вложенной функции")
#
# def outer_function():
#     print("Внутри внешней функции")
#
#     inner_function()  # Вызов вложенной функции
#     print("some extra")
#     inner_function()
#
# outer_function()
# # inner_function()  # Вызовет ошибку



# def outer_function(repeat):
#     message = "Внешняя функция\n"
#
#     def inner_function():
#         print(message * repeat)  # Переменные внешней функции
#
#     inner_function()
#
# outer_function(3)

# def outer_function():
#     message = "Внешняя функция"
#
#     def inner_function():
#         print("message")
#         message = "Вложенная функция"  # Создается новая локальная переменная
#
#     inner_function()
#     print(message)  # Выведет неизмененное значение внешней переменной
#
# outer_function()
#
# def outer_function():
#     message = "Внешняя функция"
#
#     def inner_function():
#         # Указываем, что message принадлежит внешней функции
#         nonlocal message
#         message = "Изменено во вложенной функции"
#
#     inner_function()
#     print(message)  # Теперь message изменилось
#
# outer_function()
#
# def outer_function():
#     message = "Внешняя функция"
#
#     def middle_function():
#         def inner_function():
#             nonlocal message
#             message = "Изменено во вложенной функции"
#
#         inner_function()
#
#     middle_function()
#     print(message)
#
# outer_function()


# def process_data(data):
#     def clean_text(text):
#         return text.strip().lower()
#
#     cleaned_data = [clean_text(item).upper() for item in data]
#     return cleaned_data
#
# data = ["  Apple  ", " BaNaNa ", " CHERRY "]
# print(process_data(data))

# def analyze_text(text):
#     def count_words():
#         return len(text.split())
#
#     def count_letters():
#         return sum(1 for char in text if char.isalpha())
#
#     print(f"Слов: {count_words()}")
#     print(f"Букв: {count_letters()}")
#
# analyze_text("Пример текста!")

#
# def outer_function(text):
#     def inner_function():
#         print(text)  # Запоминает переменную text
#
#     return inner_function  # Возвращаем незапущенную функцию
#
# closure = outer_function("Переданный текст")  # Объект замыкания
# print(closure)
#
# closure()  # Вызываем внутреннюю функцию после завершения внешней
# closure()  # Вызываем внутреннюю функцию после завершения внешней


# def outer_function(text):
#     def inner_function():
#         print(text)  # Запоминает переменную text
#
#     return inner_function()
#
# closure = outer_function("Переданный текст")  # Объект замыкания
# print(closure)
#
# closure()  # Вызываем внутреннюю функцию после завершения внешней


# def counter():
#     count = 0
#
#     def increment():
#         nonlocal count  # Используем count из enclosing-области
#         count += 1
#         return count
#
#     return increment  # Возвращаем функцию
#
# counter_function = counter()
# print(counter_function())
# print(counter_function())
# print(counter_function())
# print(counter_function())



# def create_filter(border):
#     def filter_value(value):
#         return value > border  # Использует сохранённый border
#     return filter_value
#
# greater_than_five = create_filter(5)  # Объект замыкания
# print(greater_than_five)
# print(greater_than_five(7))
# print(greater_than_five(3))
#
# greater_than_fifty = create_filter(50)  # Объект замыкания
# print(greater_than_fifty(7))
# print(greater_than_fifty(3))


# def multiplier(factor):
#     def multiply(number):
#         return number * factor  # Использует сохранённый factor
#     return multiply
#
# double = multiplier(2)  # Сохраняет 2 в переменной factor
# triple = multiplier(3)  # Сохраняет 3 в переменной factor
#
# print(double(4))
# print(triple(4))


# def greet():
#     """Функция приветствия"""
#     print("Привет!")
#
# print("Имя функции:", greet.__name__)
# print("Документация:", greet.__doc__)


# def outer():
#     def inner():
#         """Вложенная функция"""
#         pass
#     return inner
#
# func = outer()
# print("Имя функции:", func.__name__)
# print("Документация:", func.__doc__)


# def simple_decorator(func):    # Функция-декоратор, принимает другую функцию
#     def wrapper():  # Вложенная функция-обертка, добавляющая дополнительное поведение
#         print("Перед вызовом функции!")
#         func()  # Вызываем переданную функцию
#         print("После вызова функции!")
#     return wrapper  # Возвращаем изменённую функцию
#
# @simple_decorator
# def say_hello():
#     print("Привет!")
#
# # say_hello = simple_decorator(say_hello)  # Вызываем декоратор, теперь decorated = wrapper
# print(say_hello)
# say_hello()  # Теперь вызов say_hello() происходит через wrapper
# say_hello()  # Теперь вызов say_hello() происходит через wrapper
# say_hello()  # Теперь вызов say_hello() происходит через wrapper


# import time
#
# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()  # Засекаем время перед выполнением функции
#         func(*args, **kwargs)  # Вызываем декорируемую функцию
#         end_time = time.time()  # Засекаем время после выполнения
#         print(f"Функция {func.__name__} выполнялась {end_time - start_time:.5f} секунд")
#     return wrapper
#
# @timing_decorator  # Применение декоратора
# def slow_function(a):
#     time.sleep(a)  # Имитация долгой операции
#     print("Функция выполнена")
#
# @timing_decorator  # Применение декоратора
# def slow(a, b):
#     time.sleep(a + b)  # Имитация долгой операции
#     print("Функция выполнена")
#
# print(slow_function)
# slow_function(3)
# slow(1, 1)