'''Рамка-обводка
Создайте декоратор framed, который оборачивает результат в рамку из символов = длиной 40.
Пример применения:
@framed
def show_title():
    print("== Menu ==")
Пример вывода:
========================================
== Menu ==
========================================'''
def framed(func):
    def wrapper():
        print('=' * 40)
        print(func())
        print('=' * 40)
    return wrapper

@framed
def show_title():
    menu = "== Menu =="
    return menu

if __name__ == "__main__":
    show_title()

'''2. Настраиваемая рамка-обводка
Доработайте декоратор framed, чтобы он принимал параметр width, определяющий ширину рамки, и параметр symbol, определяющий символ для рамки (по умолчанию "=").
Пример применения: 
@framed(30, "-")
def show_title():
    print("== Menu ==")
Пример вывода: 
------------------------------
== Menu ==
------------------------------'''
def framed(width, symbol="="):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(symbol * width)
            result = func(*args, **kwargs)
            print(f"{result:^{width}}")
            print(symbol * width)

            return result
        return wrapper
    return decorator

@framed(30, "#")
def show_title():
    menu = "== Menu =="
    return menu

if __name__ == "__main__":
    show_title()

'''1. Фабрика функций расчёта НДС
Создайте функцию vat_calculator(rate), которая принимает ставку НДС и возвращает другую функцию.
Полученная функция должна принимать сумму и возвращать цену с учётом НДС по переданной ставке.
Пример вызова:
print(vat_20(100))
print(vat_10(200))
Пример вывода:
120.0
220.0'''
def vat_calculator(rate):
    def calculate(price):
        return round(price * (1 + rate), 2)
    return calculate
vat_20 = vat_calculator(0.2)
vat_10 = vat_calculator(0.1)
print(vat_20(100))
print(vat_10(200))

'''2. Калькулятор скидок по категориям
Создайте функцию, которая возвращает другую функцию для расчёта скидки.
Внешняя функция принимает словарь скидок, например {"food": 0.1} — 10% на
еду.
Если категория не найдена — цена не меняется.
Данные:
discounts = {"food": 0.1, "clothes": 0.2}
Пример вызова:
discounts = {"food": 0.1, "clothes": 0.2}
print(friday_discount("food", 100))
print(friday_discount("clothes", 250))
print(friday_discount("electronics", 500))
Пример вывода:
90.0
200.0
500'''
def discount_maker(category_discounts):
    def apply_discount(category, price):
        discount = category_discounts.get(category, 0)
        return round(price * (1 - discount), 2)
    return apply_discount
discounts = {"food": 0.1, "clothes": 0.2}
friday_discount = discount_maker(discounts)
print(friday_discount("food", 100))
print(friday_discount("clothes", 250))
print(friday_discount("electronics", 500))

'''3. Настроенная функция вывода
Создайте функцию custom_printer(sep, end), которая возвращает новую
функцию печати,
использующую указанные значения sep и end по умолчанию.
Пример вызова:
printer = custom_printer(sep=' | ', end=' -->\n')
printer('Hello', 'World')
printer('Python', 'Java', 'C++')
Пример вывода:
Hello | World -->
Python | Java | C++ -->'''
def custom_printer(sep, end):
    def print_func(*args):
        print(*args, sep=sep, end=end)
    return print_func
# Использование
printer = custom_printer(sep=' | ', end=' -->\n')
printer('Hello', 'World')
printer('Python', 'Java', 'C++')

'''4. Нумерация вызовов функции
Создайте декоратор call_counter, который выводит имя и номер вызова функции
каждый раз, когда она вызывается.
Номер должен увеличиваться при каждом вызове.
Пример декорируемой функции:
def greet():
    print("Привет!")
Пример вывода:
Вызов функции 'greet' №1:
Привет!
Вызов функции 'greet' №2:
Привет!
Вызов функции 'greet' №3:
Привет!'''
def call_counter(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print(f"Вызов функции '{func.__name__}' №{count}:")
        func()
    return wrapper

@call_counter
def greet():
    print("Привет!")

greet()
greet()
greet()