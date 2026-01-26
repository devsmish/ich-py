# Python Fundamentals 2025: Домашнее задание 22
'''1. Выбор заказов
У вас есть список заказов. Каждый заказ содержит название продукта и его цену. Напишите функцию, которая:
Отбирает заказы дороже 500.
Создаёт список названий отобранных продуктов в алфавитном порядке.
Возвращает итоговый список названий.
Данные:
orders = [
{"product": "Laptop", "price": 1200},
{"product": "Mouse", "price": 50},
{"product": "Keyboard", "price": 100},
{"product": "Monitor", "price": 300},
{"product": "Chair", "price": 800},
{"product": "Desk", "price": 400}]
Пример вывода:
['Chair', 'Laptop']'''
# teacher
def filter_and_sort_orders(orders):
    # Шаг 1: Фильтрация заказов дороже 500
    filtered = filter(lambda order: order["price"] > 500, orders)
    # print(filtered)
    # print(list(filtered))
    # Шаг 2: Извлечение названий продуктов и сортировка
    sorted_names = sorted(map(lambda order: order["product"], filtered))
    return sorted_names

orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

result = filter_and_sort_orders(orders)
print(result)

# Another variant
def filter_and_sort_orders(orders):
    return sorted(map(lambda order: order["product"], filter(lambda order: order["price"] > 500, orders)))

orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

result = filter_and_sort_orders(orders)
print(result)

# Another variant2
def filter_and_sort_orders(orders):
    return sorted([product['product'] for product in orders if product['price'] > 500])

orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

result = filter_and_sort_orders(orders)
print(result)

'''2. Статистика продаж
Дан список продаж в виде кортежей (товар, количество, цена). Напишите программу, которая:
Вычисляет общую выручку для каждого товара.
Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.
Данные:
sales = [
("Laptop", 5, 1200),
("Mouse", 50, 20),
("Keyboard", 30, 50),
("Monitor", 10, 300),
("Chair", 20, 800)]
Пример вывода:
{'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}'''
# teacher
def calculate_revenue(sales):
    # Вычисление выручки для каждого товара
    revenue = map(lambda sale: (sale[0], sale[1] * sale[2]), sales)
    # Сортировка по убыванию выручки
    sorted_revenue = sorted(revenue, key=lambda x: x[1], reverse=True)
    # print(sorted_revenue)
    # Создание словаря с товарами и выручкой
    return dict(sorted_revenue)

sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

result = calculate_revenue(sales)
print(result)

# Another variant
def calculate_revenue(sales):
    return dict(sorted(map(lambda sale: (sale[0], sale[1] * sale[2]), sales), key=lambda x: x[1], reverse=True))

sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

result = calculate_revenue(sales)
print(result)

# Another variant2
from functools import reduce
def total_sales(products):
    return dict(sorted(
        {product[0]: reduce(lambda x, y: x * y, (x for x in product if isinstance(x, (int, float))), 1) for product in
         products}.items(), key=lambda item: item[1], reverse=True))

sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

result = total_sales(sales)
print(result)

# Python Fundamentals 2025: Домашнее задание 23
'''1. Объединение данных в строку
Напишите функцию, которая принимает список любых данных (строки, числа, списки, словари) и возвращает их строковое 
представление, объединённое через " | ". Добавьте документацию и аннотации типов для всех параметров и возвращаемого 
значения.
Данные:
data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
Пример вывода:
42 | hello | [1, 2, 3] | {'a': 1, 'b': 2}'''
# teacher
from typing import Any

def combine_data(data: list[Any]) -> str:
    """
    Объединяет данные в строковое представление через разделитель ' | '.

    :param data: Список данных любого типа.
    :return: Строка с объединёнными данными.
    """
    return " | ".join(map(str, data))

data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
print(combine_data(data))

'''2. Сумма вложенных чисел
Напишите функцию, которая принимает список словарей, где каждый словарь содержит имя пользователя и список баллов. 
Функция должна вернуть сумму всех чисел. Добавьте документацию и аннотации типов для всех параметров и возвращаемого 
значения.
Данные:
data = [
{"name": "Alice", "scores": [10, 20, 30]},
{"name": "Bob", "scores": [5, 15, 25]},
{"name": "Charlie", "scores": [7, 17, 27]}]
Пример вывода:
Итоговый балл: 156'''
def sum_scores(data: list[dict[str, str | list[int]]]) -> int:
    """
    Вычисляет сумму всех чисел в списках внутри словарей.

    :param data: Список словарей, где каждый словарь содержит имя и список чисел.
    :return: Сумма всех чисел.
    """
    return sum([sum(item["scores"]) for item in data])
    # return sum([score for item in data for score in item["scores"]])

data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]
print(sum_scores(data))