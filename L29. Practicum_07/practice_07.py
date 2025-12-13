'''1. Номер покупки
Дан список покупок. Найдите какой по счету (начиная с единицы) товар с названием "Milk". Если товара нет, выведите
сообщение об отсутствии.
Данные:
products = ["Bread", "Butter", "Cheese", "Milk", "Eggs"]'''
products = ["Bread", "Butter", "Cheese", "Milk", "Eggs"]
if "Milk" in products:
    print('Tовар с названием "Milk" по счету:', products.index("Milk") + 1)
elif "Milk" not in products:
    print("Такого товара в списке нет")

'''2. Список уникальных слов
Дан текст. Программа должна: Разбить текст на слова. Создать список уникальных слов в алфавитном порядке (не учитывая 
регистр). Вывести количество уникальных слов.
Данные:
text = "Python is a great programming language. Python is popular and powerful."
Количество уникальных слов: 9
Уникальные слова: ['a', 'and', 'great', 'is', 'language', 'popular', 'powerful', 'programming', 'python']'''
text = "Python is a great programming language. Python is popular and powerful."
correct_text = text.lower().replace('.', '')
splitted_text = correct_text.split()
uniq_text = list()

for word in splitted_text:
    if word not in uniq_text:
        uniq_text.append(word)

uniq_text.sort()

print("Количество уникальных слов:", len(uniq_text))
print("Уникальные слова:", uniq_text)

'''3. Самое длинное слово
Дано предложение. Найдите самое длинное слово и выведите это слово с его длиной.
Данные:
sentence = "Programming in Python is both fun and educational"'''
sentence = "Programming in Python is both fun and educational"
text_list = sentence.split()
long_word = ''
for word in text_list:
    if len(word) > len(long_word):
        long_word = word
    elif len(word) == len(long_word):
        print("В тексте обнаружено яще одно слово такой же длинны:", word, "его длина:", len(word))
print("Самое длинное слово:", long_word, "его длина:", len(long_word))

'''4. Перемещение в конец
Напишите программу, которая перемещает все элементы списка, меньше 5, в конец списка, сохраняя порядок остальных элементов.
Данные:
numbers = [4, 7, 1, 6, 3, 8, 2]
Перемещённые элементы: [7, 6, 8, 4, 1, 3, 2]'''
numbers = [4, 7, 1, 6, 3, 8, 2]
new_list = list()
for number in numbers:
    if number >= 5:
        new_list.append(number)
for number in numbers:
    if number < 5:
        new_list.append(number)
print(new_list)

# Another variant
numbers = [4, 7, 1, 6, 3, 8, 2]
big = list()
little = list()
print(id(numbers))
for i, item in enumerate(numbers):
    if item < 5:
        little.append(item)
    else:
        big.append(item)
numbers.clear()
numbers.extend(big)
numbers.extend(little)
print(id(numbers))
print('Перемещённые элементы:', numbers)

# Variant 2
# numbers = [4, 7, 1, 6, 3, 8, 2]
# i = 0
# length = len(numbers)
# while i < length:
#     if numbers[i] < 5:
#         numbers.append(numbers.pop(i))
#         length -= 1
#     else:
#         i += 1
# print(numbers)

'''5. Суммы пар
Напишите программу, которая обрабатывает список чисел и возвращает новый список, содержащий все возможные суммы пар 
разных элементов без дубликатов значений. Результат должен быть отсортирован по убыванию.
Данные:
numbers = [3, 5, 9]
Вывод:
Суммы пар чисел по убыванию: [14, 12, 8]'''
numbers = [3, 5, 9]
uniq_sum = []

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        res = numbers[i] + numbers[j]
        if res not in uniq_sum:
            uniq_sum.append(sum)

uniq_sum.sort(reverse=True)
print("Суммы пар чисел по убыванию:", uniq_sum)

'''6. Покупки с лимитом бюджета
Дан список покупок, где каждый элемент — это кортеж с названием товара и его ценой. Покупки распределены по приоритетности. Пользователь вводит бюджет. Программа должна вывести:
список покупок, которые он может себе позволить;
итоговую стоимость этих товаров.
Данные:
shopping_list = [
("Bread", 1.20), 
("Milk", 0.99), 
("Eggs", 2.50), 
("Butter", 3.75), 
("Cheese", 4.10), 
("Apple", 0.50)
]
Введите ваш бюджет: 7
Покупки в рамках бюджета:
Bread: $1.20
Milk: $0.99
Eggs: $2.50
Apple: $0.50
Итоговая стоимость: $5.19'''
shopping_list = [
 ("Bread", 1.20),
 ("Milk", 0.99),
 ("Eggs", 2.50),
 ("Butter", 3.75),
 ("Cheese", 4.10),
 ("Apple", 0.50)
]
budget = float(input("Enter your budget: "))
total = 0
for item, price in shopping_list:
    if budget >= price:
        budget -= price
        total += price
        print(f"{item}, ${price:.2f}")
print(f"Итоговая стоимость: $ {total:.2f}")

'''7. Упаковка товаров по ящикам
У вас есть список весов товаров. Каждый ящик может выдержать не более заданного веса. Напишите программу, которая 
распределяет товары по минимальному количеству ящиков, не превышая допустимый вес.
Данные:
weights = [3, 4, 9, 8, 2, 5, 3, 6, 1, 7, 1, 1, 2, 4]'''
weights = [3, 4, 9, 8, 2, 5, 3, 6, 1, 7, 1, 1, 2, 4]
box_weight = int(input("Enter your box weight: "))
pack = []
weights.sort(reverse=True)
while weights:
    box = []
    current_weight = 0
    # 1. берём самый тяжёлый
    max_item = weights.pop(0)
    if max_item > box_weight:
        print(f"Error! Товар весом {max_item} не помещается")
        continue
    box.append(max_item)
    current_weight += max_item
    # 2. добираем более лёгкие
    i = 0
    while i < len(weights):
        if current_weight + weights[i] <= box_weight:
            box.append(weights[i])
            current_weight += weights[i]
            weights.pop(i)
        else:
            i += 1
        if current_weight == box_weight:
            break
    pack.append(box)
print("Коробки:", pack)
print("Количество коробок:", len(pack))

'''8. Оценки студентов
Дан список студентов, где каждый элемент — это кортеж с именем студента и его оценками. Программа должна вывести их 
имена и средний балл в виде таблицы. Используйте форматирование для выравнивания колонок.
Данные:
students = [
("Alice", [85, 90, 78]),
("Bob", [88, 76, 92]),
("Charlie", [90, 87, 85]),
("Diana", [72, 80, 65])
]
Имя       Средний балл
Alice            84.33
Bob              85.33
Charlie          87.33
Diana            72.33'''
students = [
    ("Alice", [85, 90, 78]),
    ("Bob", [88, 76, 92]),
    ("Charlie", [90, 87, 85]),
    ("Diana", [72, 80, 65])
]

print(f"{'Имя':<10} {'Средний балл':>12}")
for student in students:
    total = 0
    grades = student[1]

    for grade in grades:
        total += grade

    avg = total / len(grades)

    print(f"{student[0]:<10} {avg:>12.2f}")

'''9. Новая задача
Дан список сотрудников, где каждый элемент — это кортеж с именем и списком задач. Добавьте новую задачу "Prepare 
presentation" к сотруднику с именем "Alice" и отобразите её текущие задачи. Данные:
employees = [
 ("Alice", ["Review documents", "Call clients"]),
 ("Bob", ["Check emails"]),
 ("Charlie", ["Organize meeting"])]'''

'''10. Перестановка элементов
Дан список проектов, где каждый элемент — это кортеж с названием проекта и списком сотрудников.
Поменяйте местами сотрудников "Alice" и "Bob" в проекте "Project A" и отобразите их список.
Данные:
projects = [
 ("Project A", ["Alice", "Bob", "Charlie"]),
 ("Project B", ["Diana", "Eve"])]'''

'''11. Приходы и расходы
В списке кортежей, где каждый кортеж символизирует запись о приходах и расходах, необходимо оставить только те записи, в 
которых общий баланс не уходит в минус (сумма элементов кортежа должна быть больше или равна нулю). Необходимо изменить 
исходный список, а не создать новый. Данные:
transactions = [(100, -50, -30), (-200, 100, 50), (300, -100, -50), (-50, -50), (200, -300, 150)]'''

'''12. Последовательность цифр
Напишите программу, которая проверяет, находятся ли цифры, введённые пользователем, в заданном списке строк в указанном 
порядке. Данные:
my_list = ["3", "6", "3", "2", "9", "3", "9", "4", "3", "9", "0"]'''

'''13. Зашифрованное послание
Есть строка с зашифрованным посланием. Всё, что было приложено к этой строке - это небольшой набор слов: 
"ave caesar-dyh#fdhvdu"
Кажется нам было отправлено сообщение по шифру Цезаря. Его принцип - сдвиг каждой буквы вправо по алфавиту на одинаковое 
количество символов. Нужно расшифровать послание и вывести найденный сдвиг и послание на экран.
Данные:
message = "92 114 120 35 102 100 113 35 103 114 35 108 119 36 35 92 114 120 35 100 117 104
35 106 117 104 100 119 35 100 113 103 35 76 35 101 104 111 108 104 121 104 35 108 113 35 124
114 120 36"'''