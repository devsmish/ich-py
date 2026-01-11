# def greet(name):
#     print("----")
#     print(f"Привет, {name}!")
#     if True:
#         print(1)
#
# a = "Ann"
# # greet()
# greet("Алиса")
# greet(a)
# greet("Боб")
# # greet("Алиса")

# # Условие
# if True:
#     pass  # Блок кода будет добавлен позже
# else:
#     print("False")
# # Цикл
# for i in range(5):
#     pass  # Цикл ничего не делает, но синтаксически корректен
# # Функция
# def validate_data():
#     pass  # Функция пока не реализована
#
# validate_data()


# def sum(a, b):
# # Переопределение встроенной функции
#     print(a + b)
#
# sum(1, 4)  # Вызов собственной функции
#
# numbers = [1, 2, 3]
# print(sum(numbers))
# # Ошибка: ожидает 2 аргумента


# def greet():
#     print("Hello!")
#
# # Вызов функции без аргументов
# greet()
#
# def greet_person(name):
#     print(f"Hello, {name}!")
#
# # Вызов функции с аргументами
# greet_person("Alice")


# def greet(name, age):  # Ожидаемые аргументы
#    print(f"My name is {name} and I am {age} years old.")
#
# greet("Alice", 25)  # Переданные аргументы
# greet("Bob", 30)  # Переданные аргументы
# greet(30, "Bob")  # Переданные аргументы

# def greet(name, age):  # Ожидаемые аргументы
#    print(f"My name is {name} and I am {age} years old.")
#
# greet("Alice")  # Ошибка: меньше чем ожидается

# def greet(name, age):  # Ожидаемые аргументы
#    print(f"My name is {name} and I am {age} years old.")
#
# greet("Alice", 25, "Minsk")  # Ошибка: больше чем ожидается

# def greet(name, age):  # Ожидаемые аргументы
#     print(f"My name is {name} and I am {age} years old.")
#
#
# greet(age=30, name="Bob")  # Именованные аргументы
#
#
# def greet(name, greeting="Hello"):
#    print(f"{greeting}, {name}!")
#
# greet("Alice")  # Приветствие не передано, будет использовано "Hello"
# greet("Bob", "Hi")  # Вывод: Hi, Bob!
# greet("Bob")  # Вывод: Hi, Bob!

# def calculate_sum(*args):
#     print("Аргументы:", args)
#     print("Сумма:", sum(args))
#     print(*args)
#
# calculate_sum(1, 2, 3)
# calculate_sum()
#
# print(1, 2, 3, 4, 5)

#
# def print_user_info(name, name2, *args, **kwargs):
#     print(name)
#     print(name2)
#     print(args)
#     print(kwargs)
#     # print(*kwargs.values())
#     print("Информация о пользователе:")
#     for key, value in kwargs.items():
#         print(f"\t{key}: {value}")
#
# print_user_info("bob", 1, 2, 3, 4, name3="Alice", age=25, city="New York")
# # print_user_info()

# def show_full_info(name, *args, age=25, **kwargs):
#    print(f"Name: {name}")
#    print(f"Other details: {args}")
#    print(f"Age: {age}")
#    print(f"Additional info: {kwargs}")
#
# show_full_info("Alice", "Developer", age=30, city="New York", hobby="Reading")


# def add(a, b):
#     return a + b
#
# result = add(3, 5)
# print(result)
# def check_positive(number):
#     if number > 0:
#         return "Положительное число"
#     return "Отрицательное или ноль"
#
# print(check_positive(10))
# print(check_positive(-5))


# def say_hello():
#     print("Hello, World!")
#     # pass
#
# result = say_hello()
# print(result)

# def calculate(a, b):
#     return a + b, a - b
#
# result = calculate(10, 5)
# print(result)
def calculate_factorial(n):
    if n < 0:
        return  # Завершаем функцию без вычислений
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num1 = -5
print(f"Факториал числа {num1}: {calculate_factorial(num1)}")
num2 = 5
print(f"Факториал числа {num2}: {calculate_factorial(num2)}")
