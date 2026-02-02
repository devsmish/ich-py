'''1. Выбор заказов
У вас есть список заказов. Каждый заказ содержит название продукта и его цену. Напишите функцию, которая:
1. Отбирает заказы дороже 500.
2. Создаёт список названий отобранных продуктов в алфавитном порядке.
3. Возвращает итоговый список названий.
Данные:
orders = [
 {"product": "Laptop", "price": 1200},
 {"product": "Mouse", "price": 50},
 {"product": "Keyboard", "price": 100},
 {"product": "Monitor", "price": 300},
 {"product": "Chair", "price": 800},
 {"product": "Desk", "price": 400}
]
Пример вывода:
['Chair', 'Laptop']
'''
orders = [
 {"product": "Laptop", "price": 1200},
 {"product": "Mouse", "price": 50},
 {"product": "Keyboard", "price": 100},
 {"product": "Monitor", "price": 300},
 {"product": "Chair", "price": 800},
 {"product": "Desk", "price": 400}
]
def sort_by_price(orders):
    filtered_orders = filter(lambda order: order["price"] > 500, orders)
    sorted_orders = sorted(filtered_orders, key=lambda order: order["product"])
    return list(order["product"] for order in sorted_orders)
print(sort_by_price(orders))

'''2. Статистика продаж
Дан список продаж в виде кортежей (товар, количество, цена).
Напишите программу, которая:
1. Вычисляет общую выручку для каждого товара.
2. Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.
Данные:
sales = [
 ("Laptop", 5, 1200),
 ("Mouse", 50, 20),
 ("Keyboard", 30, 50),
 ("Monitor", 10, 300),
 ("Chair", 20, 800)
]
Пример вывода:
{'Chair': 16000, 'Laptop': 6000,
'Monitor': 3000, 'Keyboard': 1500,
'Mouse': 1000}'''
sales = [
 ("Laptop", 5, 1200),
 ("Mouse", 50, 20),
 ("Keyboard", 30, 50),
 ("Monitor", 10, 300),
 ("Chair", 20, 800)
]

def sorted_revenue(sales):
    revenue = [sale + (sale[1] * sale[2],) for sale in sales]
    sorted_tuple = sorted(revenue, key=lambda value: value[-1], reverse=True)
    return {value[0]: value[-1] for value in sorted_tuple}

print(sorted_revenue(sales))