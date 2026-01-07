'''1. Числа кратные 3 или 5
Напишите программу, которая создает множество из чисел, фильтруя элементы, не кратные 3 или 5.
Данные:
numbers = [16, 18, 1, 6, 3, 2, 6, 2, 14, 3, 20, 15, 19, 4, 18, 15, 15, 4, 20, 18]
Пример вывода:
{3, 6, 15, 18, 20}'''
numbers = [16, 18, 1, 6, 3, 2, 6, 2, 14, 3, 20, 15, 19, 4, 18, 15, 15, 4, 20, 18]
multi_set = {num for num in numbers if num % 3 != 0 and num % 5 != 0}
print(multi_set)

'''2. Проверка уникальности ключей
Напишите программу, которая проверяет, содержатся ли в двух заданных словарях одинаковые ключи. Вывести одинаковые ключи или "-", если таковых нет.
Данные:
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 5, "d": 7, "a": 8}
Пример вывода:
Общие ключи: ['a', 'b']'''
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 5, "d": 7, "a": 8}
dict_key = dict()
for key in dict1.keys():
    if key in dict2:
        dict_key.setdefault(key, True)
    else:
        dict_key.setdefault(key, '-')
for key in dict2.keys():
    if key in dict1:
        dict_key.setdefault(key, True)
    else:
        dict_key.setdefault(key, '-')
print(dict_key)

# Another variant
# result = []
# for key in dict1:
#     if key in dict2:
#         result.append(key)
#
# print("Общие ключи: ", result if result else "-")

# Variant 2
# result = dict1.keys() & dict2.keys()
# print("Общие ключи: ", list(result) if result else "-")

# Variant 3
# result = [key for key in dict1.keys() & dict2.keys()]
# print("Общие ключи: ", result if result else "-")

'''3. Строки с длиной
Напишите программу, которая преобразует список строк в словарь, где ключи — сами строки, а значения — их длины.
Данные:
words = ["apple", "banana", "cherry", "date"]
Пример вывода:
{'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}'''
words = ["apple", "banana", "cherry", "date"]
word_dict = {}
for word in words:
    word_dict[word] = len(word)
print(word_dict)

'''4. Проверка подмножества
Напишите программу, которая проверяет, является ли один словарь подмножеством другого (т.е. все его пары
"ключ-значение" содержатся в другом словаре).
Данные:
dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}
Пример вывода:
Первый словарь является подмножеством второго.'''
dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}
set1 = set(zip(dict1.keys(), dict1.values()))
set2 = set(zip(dict2.keys(), dict2.values()))
if set1 <= set2:
    print("Первый словарь является подмножеством второго.")
else:
    print("Второй словарь является подмножеством первого.")

'''5. Удаление пустых значений
Напишите программу, которая сформируем новый словарь удаляя все пары "ключ-значение", где значение пустое (например, 
None, пустая строка или пустой список).
Данные:
data = {"a": None, "b": 2, "c": "", "d": [], "e": [1, 2]}
Пример вывода:
{'b': 2, 'e': [1, 2]}'''
data = {"a": None, "b": 2, "c": "", "d": [], "e": [1, 2]}
new_dict = dict()
for key, value in data.items():
    if value:
        new_dict.setdefault(key, value)
print(new_dict)

# Another variant
data1 = {}

for key, value in data.items():
    if value:
        data1[key] = value

print(data1)

# Variant Dict comprehension
data1 = {key : value for key, value in data.items() if value}
print(data1)

'''6. Потерянные страницы книги
Вам дан словарь, где ключи — номера страниц книги, а значения — содержимое страниц. Некоторые страницы отсутствуют 
(значения None). Напишите программу, которая на пропущенных страницах заменит значение на "Страница потеряна".
Данные:
book = {1: "Начало истории", 2: None, 3: "Глава 1", 4: None, 5: "Глава 2"}
Пример вывода:
{1: 'Начало истории', 2: 'Страница потеряна', 3: 'Глава 1', 4: 'Страница потеряна', 5: 'Глава 2'}
'''
book = {1: "Начало истории", 2: None, 3: "Глава 1", 4: None, 5: "Глава 2"}
for key, value in book.items():
    if value:
        continue
    else:
        book[key] = "Страница потеряна"
print(book)

'''7. База оценок студентов
У вас есть словарь с именами студентов и списками их оценок. Напишите программу, которая вычисляет средний балл для 
каждого студента. Далее нужно сохранить средний балл в значениях для каждого студента, как показано на примере.
Данные:
grades = {
"anna": [5, 4, 3, 5],
"bennet": [3, 2, 4],
"john": [5, 5, 5]
}
Пример вывода:
{'anna': {'оценки': [5, 4, 3, 5], 'средний балл': 4.25}, 'bennet': {'оценки': [3, 2, 4], 'средний балл': 3.0}, 
'john': {'оценки': [5, 5, 5], 'средний балл': 5.0}}'''
grades = {
"anna": [5, 4, 3, 5],
"bennet": [3, 2, 4],
"john": [5, 5, 5]
}

for name, marks in grades.items():
    average = sum(marks) / len(marks)
    grades[name] = {"оценки": marks, "средний бал": average}
print(grades)

'''8. Рецепты по ингредиентам
Создайте словарь, в котором для каждого набора ингредиентов будут храниться все названия рецептов. Учитывайте что 
ингредиенты могут быть перечислены в произвольном порядке и некоторые рецепты могут иметь одинаковые ингредиенты.
Выведите возможные рецепты для каждого набора продуктов. В конце пользователь вводит список имеющихся у него 
ингредиентов через пробел, и программа должна вывести названия всех доступных рецептов. Если рецептов нет, нужно 
вывести сообщение "Нет рецептов".
Данные:
recipes = {
("flour", "egg", "milk"): "Pancakes",
("egg", "milk", "butter"): "Omelette",
("flour", "sugar", "butter"): "Cookies",
("flour", "egg", "butter", "sugar"): "Cake",
("milk", "flour", "egg"): "Waffles",
("butter", "milk", "egg"): "Scrambled Eggs",
("flour", "milk", "sugar", "butter"): "Sweet Bread"
}
Пример вывода:
milk egg butter flour
Ингредиенты                    | Рецепты                       
------------------------------------------------------------
flour, milk, egg               | Pancakes, Waffles             
butter, milk, egg              | Omelette, Scrambled Eggs      
flour, sugar, butter           | Cookies                       
flour, sugar, butter, egg      | Cake                          
flour, sugar, butter, milk     | Sweet Bread                   

Введите ингредиенты через пробел: milk egg butter flour
Доступные рецепты: Pancakes, Waffles, Omelette, Scrambled Eggs'''
recipes = {
("flour", "egg", "milk"): "Pancakes",
("egg", "milk", "butter"): "Omelette",
("flour", "sugar", "butter"): "Cookies",
("flour", "egg", "butter", "sugar"): "Cake",
("milk", "flour", "egg"): "Waffles",
("butter", "milk", "egg"): "Scrambled Eggs",
("flour", "milk", "sugar", "butter"): "Sweet Bread"
}
new_dict = dict()
print("Ингредиенты | Рецепты")
print("------------------------------------------------------------")
for key, value in recipes.items():
    products = frozenset(key)
    # if products not in new_dict:
    #     new_dict[products] = [value]
    # else:
    #     new_dict[products].append(value)

    new_dict.setdefault(products, []).append(value)
print(new_dict)

'''9. Одинаковые предметы
Есть список студентов и наборы предметов, которые они изучают. Необходимо сгруппировать студентов по идентичным наборам 
предметов, используя frozenset как ключ, и вывести группы.
Данные:
students = {
 "Alice": ["Math", "Physics"],
 "Bob": ["Math", "Physics"],
 "Charlie": ["Chemistry", "Biology"],
 "David": ["Math", "Physics"],
 "Eve": ["Chemistry", "Biology"]
}
Пример вывода:
Группа с предметами: Physics, Math: ['Alice', 'Bob', 'David']
Группа с предметами: Biology, Chemistry: ['Charlie', 'Eve']'''
students = {
 "Alice": ["Math", "Physics"],
 "Bob": ["Math", "Physics"],
 "Charlie": ["Chemistry", "Biology"],
 "David": ["Math", "Physics"],
 "Eve": ["Chemistry", "Biology"]
}
subj_group = {}
for student, subjects in students.items():
    key_subject = frozenset(subjects)
    subj_group.setdefault(key_subject, []).append(student)
for subject, student in subj_group.items():
    subjects_str = ", ".join(sorted(subject))
    print(f"Группа с предметами: {subjects_str}: {student}")

'''10. Перевод и расширение словаря
Напишите программу, которая позволяет пользователю вводить английские слова и получать их перевод на русский из словаря. 
Если слово отсутствует в словаре, программа должна выводить сообщение "Перевод отсутствует". В конце программа должна 
предложить пользователю добавить новые слова в словарь.
Данные:
english_words = {
 "Butterfly": "Бабочка",
 "Training": "Обучение",
 "Restaurant": "Ресторан",
 "Programming": "Программирование",
}
Пример вывода:
Введите слово на английском (или 'exit' для выхода): Butterfly
Перевод: Бабочка
Введите слово на английском (или 'exit' для выхода): Travel
Перевод отсутствует.
Хотите добавить перевод? (да/нет): да
Введите перевод для слова "Travel": Путешествие
Слово "Travel" добавлено в словарь.
Введите слово на английском (или 'exit' для выхода): exit
Программа завершена.'''
english_words = {
 "Butterfly": "Бабочка",
 "Training": "Обучение",
 "Restaurant": "Ресторан",
 "Programming": "Программирование",
}
while True:
    word = input("Введите слово на английском (или 'exit' для выхода): ").capitalize()
    if word == "exit".capitalize():
        print("Программа завершена.")
        break
    if word in english_words:
        print("Перевод:", english_words[word])
    else:
        print("Перевод отсутствует.")
        question = input("Хотите добавить перевод? (да/нет):")
        if question == question.strip().lower():
            continue
        else:
            translate = input(f'Введите перевод для слова "{word}": ')
            english_words[word] = translate
print("Обновленный словарь:", english_words)