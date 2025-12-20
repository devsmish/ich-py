# Python Fundamentals 2025: Домашнее задание 14
'''1. Число в конце
Напишите программу, которая создает новый список. В него необходимо добавить только те строки из исходного списка, в
которых цифры находятся только в конце. Данные:
strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
Пример вывода:
Строки с цифрами только в конце: ['apple23', 'grape3']'''
# teacher
strings = ["apple23", "ban1ana45", "12cherry", "gr!ape3", "blue23berry"]
filtered_strings = []

for string in strings:
    # Проверяем, начинается ли строка с букв и заканчивается цифрами
    i = 0
    while i < len(string) and not string[i].isdigit():
        i += 1

    # Если после букв идет хотя бы одна цифра и она находится в конце
    if 0 < i < len(string) and string[i:].isdigit():
        filtered_strings.append(string)

print("Строки с цифрами только в конце:", filtered_strings)

# Another variant
strings = ["apple23", "ban1ana45", "12cherry", "grape", "blue23berry"]
result =[]
for string in strings:
    if string.rstrip("0123456789").isalpha() and string[-1].isdigit():
         result.append(string)
print(f"Строки с цифрами только в конце: {result}")

# Variant 2
strings = ["apple23", "ban1ana45", "12cherry", "grape", "blue23berry"]
result =[]
for string in strings:
    striped = string.rstrip("0123456789")
    if striped.isalpha() and string != striped:
         result.append(string)
print(f"Строки с цифрами только в конце: {result}")

# Variant 3
strings = ["app!le23", "ban1ana45", "12cherry", "grape", "blue23berry"]
result =[]
for string in strings:
    striped = string.rstrip("0123456789")
    if string != striped:
        number_in_string = False
        for char in striped:
            if char.isdigit():
                number_in_string = True
                break
        if not number_in_string:
            result.append(string)
    # if striped.isalpha() and string != striped:
    #      result.append(string)
print(f"Строки с цифрами только в конце: {result}")

'''2. Удаление кратных
Напишите программу, которая удаляет из исходного списка все значения, кратные числу, которое вводится пользователем.
Данные:
numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
Пример вывода:
Введите число для удаления кратных ему элементов: 3
Список без кратных значений: [1, 10, 19, 20]'''
# teacher
numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
multiple = int(input("Введите число для удаления кратных ему элементов: "))

i = 0
while i < len(numbers):
    if numbers[i] % multiple == 0:
        numbers.pop(i)
    else:
        i += 1

print("Список без кратных значений:", numbers)

# Another variant
numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]

num = int(input("Введите число для удаления кратных ему элементов: "))

for value in numbers[:]:
    if value % num == 0:
        numbers.remove(value)

print(f"Список без кратных значений: {numbers}")

# Variant 2
numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
num = int(input("Введите число для удаления кратных ему элементов:"))#num = 3
for n in range(len(numbers) -1, -1, -1):
    if numbers[n] % num == 0:
        numbers.pop(n)
print(numbers)

'''3. Порядок четных
Напишите программу, которая формирует новый список чисел. Добавьте в него все элементы исходного списка, где: нечетные 
числа занимают те же позиции, чётные числа отсортированы между собой обратном порядке. Данные:
numbers = [5, 2, 3, 8, 4, 1, 2, 7]
Пример вывода:
Список после сортировки: [5, 8, 3, 4, 2, 1, 2, 7]'''
# teacher
numbers = [5, 2, 3, 8, 4, 1, 2, 7]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
even_numbers.sort()

result = []
for num in numbers:
    if num % 2 == 0:
        result.append(even_numbers.pop())
    else:
        result.append(num)
print("Список после сортировки:", result)

# Another variant
numbers = [5, 2, 3, 8, 4, 1, 2, 7]
even = sorted([n for n in numbers if n % 2 == 0],reverse=True)
new_numbers = [even.pop(0) if n % 2 == 0 else n for n in numbers]
print("Список после сортировки:", new_numbers)

# Python Fundamentals 2025: Домашнее задание 15
'''1. Одно слово
Напишите программу, которая обрабатывает список из строк и удаляет все строки, содержащие более одного слова, а также 
преобразует оставшиеся строки к нижнему регистру. Данные:
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
Пример вывода:
Обработанный список: ['hello', 'world', 'simple']'''
# teacher
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]

for i in range(len(text_list) - 1, -1, -1):
    if " " in text_list[i]:  # Проверка на наличие более одного слова
        del text_list[i]
    else:
        text_list[i] = text_list[i].lower()  # Преобразование к нижнему регистру

print("Обработанный список:", text_list)

'''2. Обновление цен товаров
Дан список товаров с ценами. Программа должна применить скидку к каждому товару и добавить в список элемент с новой 
ценой. В конце вывести таблицу с новой ценой. Данные:
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
Пример вывода:
Введите скидку (в процентах): 17
Товар          Старая цена    Новая цена
Laptop            1200.00$       996.00$
Mouse               25.00$        20.75$
Keyboard            75.00$        62.25$
Monitor            200.00$       166.00$'''
# teacher
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
discount = int(input("Введите скидку (в процентах): "))

for product in products:
    new_price = product[1] * (1 - discount / 100)
    product.append(round(new_price, 2))
print(f"\n{'Товар':<12}{'Старая цена':>14}{'Новая цена':>14}")

for name, price, new_price in products:
    print(f"{name:<12}{price:>13.2f}${new_price:>13.2f}$")

# Another variant
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
discount = int(input("Введите скидку (в процентах): "))


print(f"\n{'Товар':<12}{'Старая цена':>14}{'Новая цена':>14}")
for product in products:
    new_price = product[1] * (1 - discount / 100)
    product.append(round(new_price, 2))
    print(f"{product[0]:<12}{product[1]:>13.2f}${new_price:>13.2f}$")

print(products)

# Перемещение в конец
# Напишите программу, которая перемещает все элементы списка, меньше 5, в конец списка, сохраняя порядок остальных
# элементов. Данные:
# numbers = [4, 7, 1, 6, 3, 8, 2]
# Перемещённые элементы: [6, 7, 8, 4, 1, 3, 2]
numbers = [4, 7, 1, 6, 3, 8, 2]
i = 0
length = len(numbers)
while i < length:
    if numbers[i] < 5:
        numbers.append(numbers.pop(i))
        length -= 1
    else:
        i += 1
print(numbers)