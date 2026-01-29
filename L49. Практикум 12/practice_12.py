'''Напишите программу, которая запрашивает у пользователя число и обрабатывает возможные ошибки ввода, пока не получат
корректное число.
Пример вывода
Введите число: qwe
Ошибка: Введите корректное число.
Введите число: 12.5
Вы ввели число: 12.5'''
while True:
    data = input('Введите число: ')
    try:
        float(data)
        print('Вы ввели число:', data)
        break

    except ValueError:
        print('Ошибка: Введите корректное число.')

'''Напишите функцию, которая проверяет, что возраст пользователя не меньше 18 лет с использованием ошибок
Пример вывода
Введите возраст: 17
Ошибка: Возраст должен быть 18 лет и старше.'''
def control_age(age: int) -> bool:
    if age < 18:
        raise ValueError("Ошибка: Возраст должен быть 18 лет и старше.")

age = int(input("Enter your age: "))
try:
    control_age(age)
except ValueError as err:
    print(err)

'''1. Сумма чисел списка
Напишите рекурсивную функцию, которая вычисляет сумму всех чисел в списке.
Функция должна проверять:
● Аргумент должен быть списком.
● Все элементы списка должны быть числами.
Если данные не валидны необходимо выбрасывать исключение. При вызове функции обработайте возможное исключение.
Данные
numbers = [1, 2, 3, 4, 5]
Пример вывода
15'''
def sum_numbers(numbers: list) -> float:
    # Проверка, что аргумент — список
    if not isinstance(numbers, list):
        raise TypeError("Аргумент должен быть списком")

    # Базовый случай рекурсии
    if not numbers:
        return 0

    first = numbers[0]

    # Проверка элемента
    if not isinstance(first, (int, float)):
        raise ValueError(f"В списке есть элемент {first} не числового типа")

    # Рекурсивный шаг
    return first + sum_numbers(numbers[1:])

numbers = [1, 2, 3, 4, 5]

try:
    result = sum_numbers(numbers)
    print(result)
except (TypeError, ValueError) as err:
    print(f"Ошибка: {err}")

'''2. Реверс строки
Напишите рекурсивную функцию, которая переворачивает строку. Если передан не строковый тип, выбросить
исключение. При вызове функции обработайте возможное исключение.
Данные
text = "recursion"
Пример вывода
noisrucer'''
def str_reverse(text: str) -> str:
    # Проверка, что аргумент — список
    if not isinstance(text, str):
        raise TypeError("Аргумент должен быть строкой")

    # Базовый случай рекурсии
    if not text:
        return ''

    first = text[0]

    # Рекурсивный шаг
    return str_reverse(text[1:]) + first

text = "recursion"

try:
    result = str_reverse(text)
    print(result)
except (TypeError) as err:
    print(f"Ошибка: {err}")

'''3. Реверс строки
Глубина вложенности списка
Напишите рекурсивную функцию, которая определяет максимальную глубину вложенности списка. Функция
должна проверять:
● Аргумент должен быть списком.
● Вложенные структуры, если они есть, также должны быть списками.
Если данные не валидны необходимо выбрасывать исключение. При вызове функции обработайте возможное исключение.
Данные
nested_list = [1, [2, [3, [4, [5]]]], 6, [[7, 8], 9]]
Пример вывода
Максимальная глубина: 5'''
def depth(nested_list: list) -> float:
    if not isinstance(nested_list, list):
        raise TypeError("Аргумент должен быть списком")

    depth_nesting = 1  # сам список — уже глубина 1

    for item in nested_list:
        if isinstance(item, list):
            current_depth = 1 + depth(item) # recursion
            depth_nesting = max(depth_nesting, current_depth)
        elif not isinstance(item, (int, float)):
            raise TypeError("Вложенные структуры должны быть списками")

    return depth_nesting

nested_list = [1, [2, [3, [4, [5]]]], 6, [[7, 8], 9]]

try:
    print(f"Максимальная глубина: {depth(nested_list)}")
except TypeError as err:
    print(f"Ошибка: {err}")

'''4. Сумма продаж
Есть дерево подразделений внутри компании (каждое подразделение может содержать «дочерние» отделы).
Напишите рекурсивную функцию, которая подсчитывает суммарные продажи для всех отделов. Функция должна
проверять:
● Аргумент должен быть словарем.
● Дочерние отделы (если есть) должны быть списком словарей.
Если данные не валидны необходимо выбрасывать исключение. При вызове функции обработайте
возможное исключение.
company_structure = {
 "dept_name": "Head Office",
 "sales": 100,
 "sub_departments": [
 {
 "dept_name": "Sales Department",
 "sales": 200,
 "sub_departments": [
 {
 "dept_name": "B2B Sales",
"sales": 120,
 }
 ]
 },
 {
 "dept_name": "IT Department",
 "sales": 150,
 "sub_departments": [
 { 
"dept_name": "DevOps",
"sales": 300,
"sub_departments": [
 {
 "dept_name": "Cloud
Infrastructure",
 "sales": 180,
 }
 ]
 },
 {
 "dept_name": "QA Department",
"sales": 90,
 }
 ]
 }
 ]
}
Пример вывода
Общая сумма продаж: 1140'''
def sum_sales(structure: dict) -> float:
    if not isinstance(structure, dict):
        raise TypeError("Аргумент должен быть словарём")

    if "sales" not in structure or not isinstance(structure["sales"], (int, float)):
        raise TypeError("Поле 'sales' должно быть числом")

    total = structure["sales"]

    sub_departments = structure.get("sub_departments", [])

    if not isinstance(sub_departments, list):
        raise TypeError("Дочерние отделы должны быть списком словарей")

    for dept in sub_departments:
        if not isinstance(dept, dict):
            raise TypeError("Каждый дочерний отдел должен быть словарём")
        total += sum_sales(dept)

    return total

company_structure = {"dept_name": "Head Office", "sales": 100, "sub_departments": [
    {"dept_name": "Sales Department", "sales": 200, "sub_departments": [
        {"dept_name": "B2B Sales", "sales": 120, }]},
    {"dept_name": "IT Department", "sales": 150, "sub_departments": [
        {"dept_name": "DevOps", "sales": 300, "sub_departments": [
            {"dept_name": "Cloud Infrastructure", "sales": 180, }]},
        {"dept_name": "QA Department", "sales": 90, }]}]}

try:
    print(f"Общая сумма продаж: {sum_sales(company_structure)}")
except TypeError as err:
    print(f"Ошибка: {err}")

'''5. Читабельный формат словаря
Дан вложенный словарь. Напишите рекурсивную функцию, которая преобразует его в «плоский» формат,
где в ключе будет содержаться полный путь к значению.
Данные
data = {
 "user": {
 "id": 123,
 "info": {
 "name": "Alice",
 "location": {
 "city": "Berlin",
 "coordinates": {"lat": 52.52, "lon": 13.405}
 },
 "hobby": ["swimming", "drawing"]
 }
 },
 "score": 95
}
Пример вывода
Данные для анализа:
user.id : 123
user.info.name : Alice
user.info.location.city : Berlin
user.info.location.coordinates.lat : 52.52
user.info.location.coordinates.lon : 13.405
user.info.hobby : ['swimming', 'drawing']
score : 95'''
def dict_converter(data: dict, parent_key: str = "") -> dict:
    if not isinstance(data, dict):
        raise TypeError("Аргумент должен быть словарём")

    result = {}

    for key, value in data.items():
        full_key = f"{parent_key}.{key}" if parent_key else key

        if isinstance(value, dict):
            result.update(dict_converter(value, full_key))
        else:
            result[full_key] = value

    return result

data = {
 "user": {
 "id": 123, "info": {
 "name": "Alice", "location": {
 "city": "Berlin", "coordinates": {
 "lat": 52.52, "lon": 13.405} },
 "hobby": ["swimming", "drawing"]} },
 "score": 95
}

# Рабочее рекурсивное решение
def dict_converter(data: dict, parent_key: str = "") -> dict:
    if not isinstance(data, dict):
        raise TypeError("Аргумент должен быть словарём")

    result = {}

    for key, value in data.items():
        full_key = f"{parent_key}.{key}" if parent_key else key

        if isinstance(value, dict):
            result.update(dict_converter(value, full_key))
        else:
            result[full_key] = value

    return result

# Использование и вывод
convert_data = dict_converter(data)

print("Данные для анализа:")
for key, value in convert_data.items():
    print(f"{key} : {value}")

'''Реализуйте аналог deepcopy() с помощью рекурсии. Не забудьте проверить, чтобы изменения в копии не затронули оригинал.
Данные:
original_data = [
[1, 2, 3], # Вложенный список
(4, [5, 6], {7, 8}), # Кортеж с вложенными структурами
{"a": 9, "b": [10, 11]}, # Словарь со списком
"Hello", # Строка
[12, (13, 14)], # Список с кортежем
15.5, # Число с плавающей точкой
5 # Целое число
]
Пример вывода:
Исходный: [[1, 2, 3], (4, [0, 6], {8, 7}), {'a': 9, 'b': [10, 11]}, 'Hello', [12, (13, 14)], 15.5, 5]
Копия: [[1, 2, 3], (4, [5, 6], {8, 7}), {'a': 9, 'b': [10, 11]}, 'Hello', [12, (13, 14)], 15.5, 5]'''
original_data = [
[1, 2, 3], # Вложенный список
(4, [5, 6], {7, 8}), # Кортеж с вложенными структурами
{"a": 9, "b": [10, 11]}, # Словарь со списком
"Hello", # Строка
[12, (13, 14)], # Список с кортежем
15.5, # Число с плавающей точкой
5 # Целое число
]

def deep_copy(obj):
    if isinstance(obj, list):
        return [deep_copy(x) for x in obj]
    elif isinstance(obj, dict):
        return {key: deep_copy(value) for key, value in obj.items()}
    elif isinstance(obj, set):
        return {deep_copy(x) for x in obj}
    elif isinstance(obj, tuple):
        return tuple([deep_copy(x) for x in obj])
    else:
        return obj

baselist = [1, 2, "stroka"]
result = deep_copy(original_data)
# result.append(55)
result[0].append(55)
print(result)
print(original_data)

# Через циклы вместо лист-компрехеншн для наглядности при дебаггинге
original_data = [
[1, 2, 3], # Вложенный список
(4, [5, 6], {7, 8}), # Кортеж с вложенными структурами
{"a": 9, "b": [10, 11]}, # Словарь со списком
"Hello", # Строка
[12, (13, 14)], # Список с кортежем
15.5, # Число с плавающей точкой
5 # Целое число
]

def deep_copy(obj):
    if isinstance(obj, list):
        temp_list = []
        for x in obj:
            temp_list.append(deep_copy(x))
        return temp_list
    elif isinstance(obj, dict):
        temp_list = {}
        for key, value in obj.items():
            temp_list[key] = deep_copy(value)
        return temp_list
    elif isinstance(obj, set):
        temp_list = set()
        for x in obj:
            temp_list.add(deep_copy(x))
        return temp_list
    elif isinstance(obj, tuple):
        temp_list = []
        for x in obj:
            temp_list.append(deep_copy(x))
        return tuple(temp_list)
    else:
        return obj

baselist = [1, 2, "stroka"]
result = deep_copy(original_data)
# result.append(55)
result[0].append(55)
print(result)
print(original_data)