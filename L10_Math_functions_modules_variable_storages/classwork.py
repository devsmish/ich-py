'''1. Скидки для оптовых покупателей. Напишите программу, которая получает от пользователя цену на товар и количество
товара. Программа должна рассчитать итоговую сумму заказа со скидкой, исходя из количества товара. Цену нужно округлить
до сотых. Условия скидки:
● Если количество товара от 10 до 19 — скидка 5%.
● Если количество товара от 20 до 49 — скидка 10%.
● Если количество товара от 50 до 99 — скидка 15%.
● Если количество товара 100 и более — скидка 20%.
Пример вывода:
Введите цену товара: 100
Введите количество товара: 25
Сумма заказа с учётом скидки: 2250.00'''
from decimal import Decimal

price_waren = Decimal(input("Enter price waren: "))
quantity = int(input("Enter quantity: "))
order_summa = 0
if quantity < 10:
    order_summa = price_waren * quantity
elif 10 <= quantity <= 19:
    order_summa = price_waren * quantity * (1 - Decimal('0.05'))
elif quantity <= 49:
    order_summa = price_waren * quantity * (1 - Decimal('0.1'))
elif quantity <= 99:
    order_summa = price_waren * quantity * (1 - Decimal('0.15'))
else:
    order_summa = price_waren * quantity * (1 - Decimal('0.2'))
print("Order summa with discount = ", order_summa)

'''2. Площадь и длина круга. Напишите программу, которая определяет площадь круга и длину окружности по радиусу,
полученному от пользователя, и выводит их на экран, округлив до сотых. Формулы:
● Площадь круга: S = π * r^2
● Длина окружности: C = 2 * π * r
Пример вывода:
Введите радиус: 5
Площадь круга: 78.54
Длина окружности: 31.42'''
import math
radius = float(input("Enter radius: "))
area = round(math.pi * math.pow(radius,2), 2)
print("Площадь круга: ", area)
circumference = round(2 * math.pi * radius, 2)
print("Длина окружности: ", circumference)
