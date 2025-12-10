'''Напишите программу, которая принимает список строк и создает новый список только из слов, начинающихся и
заканчиваются одной и той же буквой. Данные:
strings = ["apple", "banana", "level", "radar", "grape"]
Пример вывода:
Строки, которые начинаются и заканчиваются одной и той же буквой: ['level', 'radar']'''
strings = ["apple", "banana", "level", "radar", "grape"]
stendletter_str = []
for n in strings:
    if n[0] == n[-1]:
        stendletter_str.append(n)
print("Строки, которые начинаются и заканчиваются одной и той же буквой:", stendletter_str)

# Python Fundamentals 2025: Домашнее задание 12
'''1. Сумма положительных чисел
Напишите программу, которая обрабатывает список float чисел, вычисляет сумму положительных чисел. Результат необходимо 
вывести в формате денежной суммы (до 2 символов после запятой), добавляя символ валюты "$" вначале и разделяя тысячи 
запятой. Данные:
numbers = [1245.4435, -302.1403, 87459.99, -520.8265, 1450.001]
Пример вывода:
Сумма положительных чисел: $90,155.43'''
# teacher
numbers = [1245.4435, -1302.1403, 87459.99, -520.8265, 1450.001]

positive_sum = 0

for num in numbers:
    if num > 0:
        positive_sum += num

form = "${:,.2f}"
formatted_sum = form.format(positive_sum)
print("Сумма положительных чисел:", formatted_sum)
print("Сумма отрицательных чисел:", form.format(sum(numbers) - positive_sum))

print(f"Сумма положительных чисел: ${positive_sum:,.2f}")
print(f"Сумма положительных чисел: ${sum(numbers) - positive_sum:,.2f}")

'''2. Счета клиентов
Напишите программу, которая принимает список строк в формате "name age balance" и выводит информацию о каждом человеке 
с отформатированными данными: имя — 10 символов, возраст — 3 символа, баланс — 10 символов с двумя знаками после 
запятой. Используйте заранее подготовленный список строк.
Данные:
data_list = [ "John 23 12345.678", "Alice 30 200.50", "Bob 35 15000.3", "Charlie 40 500.75" ]
Пример вывода:
Имя: John       | Возраст:  23 | Баланс:  12345.68
Имя: Alice      | Возраст:  30 | Баланс:    200.50
Имя: Bob        | Возраст:  35 | Баланс:  15000.30
Имя: Charlie    | Возраст:  40 | Баланс:    500.75'''
# teacher
data_list = [
    "John 23 12345.678",
    "Alice 30 200.50",
    "Bob 35 15000.3",
    "Charlie 40 500.75"
]

for person in data_list:
    name, age, balance = person.split()
    age = int(age)
    balance = float(balance)
    print("Имя: {:<10} | Возраст: {:>3} | Баланс: {:>10.2f}".format(name, age, balance))
    print("Имя: {:10} | Возраст: {:3} | Баланс: {:10.2f}".format(name, age, balance))

# Python Fundamentals 2025: Домашнее задание 13
'''1. Прогрессия увеличения
Напишите программу, которая создаёт новый кортеж, состоящий из элементов изначального в том же порядке. Добавить в него 
только элементы, которые больше всех предыдущих значений в исходном кортеже.
Данные:
numbers = (3, 7, 2, 8, 5, 10, 1)
Пример вывода:
Кортеж по возрастанию: (3, 7, 8, 10)'''
# teacher
numbers = (3, 7, 2, 8, 5, 10, 1)
result = numbers[:1]
current_max = numbers[0]
for num in numbers[1:]:
    if num > current_max:
        result += (num,)
        current_max = num
print("Кортеж по возрастанию:", result)

'''2. Повторяющиеся элементы
Напишите программу, которая находит индексы элементов кортежа, встречающихся более одного раза. Вывести сами элементы и 
их индексы. Данные:
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
Пример вывода:
Индексы элемента 2: 1 4 9
Индексы элемента 3: 2 6
Индексы элемента 4: 3 8'''
# teacher
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
indices = []

for i, el in enumerate(numbers):
    if numbers.count(el) > 1 and i not in indices:
        print(f"Индексы элемента {el}: ", end="\t")
        for j in range(i, len(numbers)):
            if numbers[j] == el:
                indices += [j]
                print(j, end=' ')
        print()

# Another variant
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
indices = []

for i in range(len(numbers)):
    if numbers.count(numbers[i]) > 1 and i not in indices:
        print(f"Индексы элемента {numbers[i]}: ", end="\t")
        for j in range(i, len(numbers)):
            if numbers[j] == numbers[i]:
                indices += [j]
                print(j, end=' ')
        print()

# Variant 2
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
indices = []

for i, el in enumerate(numbers):
    if numbers.count(el) > 1 and i not in indices:
        print(f"Индексы элемента {el}: ", end="\t")
        start = i
        while el in numbers[start:]:
            founded_index = numbers.index(el, start)
            indices += [founded_index]
            print(founded_index, end=' ')
            start = founded_index + 1
        print()

# Variant 3
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
# условия для продолжения перебора
for i, n in enumerate(numbers):
    if n in numbers[:i]:
        continue

    # условие для перебора
    index = []
    for j, x in enumerate(numbers):
        if x == n:
            index += [j]
    if len(index) > 1:
        print(f"Индексы элемента {n}:", *index)

# Variant 4
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
uniq = ()
for index, number in enumerate(numbers):
    if numbers.count(number) > 1 and number not in uniq:
        typle2 = ()
        uniq += (number,)
        for index2, number2 in enumerate(numbers[index:]):
            if number2 == number:
                typle2 += (str(index2 + index),)
        print(f"Индексы элемента {number}: {" ".join(typle2)} ")