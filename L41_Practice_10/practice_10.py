'''1. Популярные слова
Реализуйте функцию, которая принимает любое количество строк с текстом. Функция должна возвращать
подсчет самых популярных слов в количестве, переданном в функцию. Программа должна игнорировать
регистр слов. Выведите 5 самых популярных слов и их количество.
Данные:
text1 = "This is a sample text with some repeated words."
text2 = "Another sample text with different words."
text3 = "Text processing is fun when words repeat."
Пример вывода:
5 самых популярных слов:
words: 3
text: 3
with: 2
sample: 2
is: 2'''
from unicodedata import category

text1 = "This is a sample text with some repeated words."
text2 = "Another sample text with different words."
text3 = "Text processing is fun when words repeat."
num = int(input("Enter count words: "))

from collections import Counter

def popular_words(num, *texts):
    word = " ".join(texts).replace(".", "").lower().split()
    count_word = Counter(word)
    return count_word.most_common(num)

print(popular_words(num, text1, text2, text3))

'''2. Группировка задач по категории
Реализуйте функцию, которая принимает словарь задач с категориями и группирует задачи по их категориям.
Данные:
tasks = {
 "task1": "работа",
 "task2": "учёба",
 "task3": "развлечения",
 "task4": "работа",
 "task5": "учёба"
}
Пример вывода:
Группировка по категориям:
{
 'работа': ['task1', 'task4'],
 'учёба': ['task2', 'task5'],
 'развлечения': ['task3']
}'''
from collections import defaultdict

def group_tasks(tasks):
    tasks_groups = defaultdict(list)
    for task, category in tasks.items():
        tasks_groups[category].append(task)
    return dict(tasks_groups)

tasks = {
 "task1": "работа",
 "task2": "учёба",
 "task3": "развлечения",
 "task4": "работа",
 "task5": "учёба"
}

print(group_tasks(tasks))

'''3. Поиск задач
Реализуйте функцию, которая принимает словарь задач с категориями и нужную категорию. Функция должна
возвращать список задач для указанной категории.
Данные:
tasks = {
 "task1": "работа",
 "task2": "учёба",
 "task3": "развлечения",
 "task4": "работа",
 "task5": "учёба"
}
category = "учёба"
Пример вывода:
Задачи для категории 'учёба':
['task2', 'task5']'''
from collections import defaultdict

def group_tasks(tasks):
    tasks_groups = defaultdict(list)
    for task, category in tasks.items():
        tasks_groups[category].append(task)
    return dict(tasks_groups)

def list_tasks(categ_tasks, tasks_groups):
    for category, groups in tasks_groups.items():
        if categ_tasks.lower() == category:
            return tasks_groups[category]
    return "Категория указана не верно!!!"

tasks = {
 "task1": "работа",
 "task2": "учёба",
 "task3": "развлечения",
 "task4": "работа",
 "task5": "учёба"
}
tasks_groups = group_tasks(tasks)
print(tasks_groups)

categ_tasks = input("Enter a category: ")
print(list_tasks(categ_tasks, tasks_groups))

# Another variant
tasks_data = {
"task1": "работа",
"task2": "учёба",
"task3": "развлечения",
"task4": "работа",
"task5": "учёба"
}

from collections import defaultdict
def group_by_categories(tasks):
    grouped_tasks = defaultdict(list)
    for task, category in tasks.items():
        grouped_tasks[category].append(task)
    return dict(grouped_tasks)
#
# print(group_by_categories(tasks_data))

def get_by_category(tasks, category):
    # print(group_by_categories(tasks))
    return group_by_categories(tasks).get(category, [])

print(get_by_category(tasks_data, "работа"))
print(get_by_category(tasks_data, "наука"))


'''4. Очередь задач с приоритетом
Есть очередь задач, где каждая задача имеет приоритет: "высокий", "средний", "низкий". Реализуйте функцию, которая 
сортирует очередь задач таким образом, чтобы более высокий приоритет был в начале очереди. Нужно изменить исходную 
очередь, а не создавать новую.
Данные:
from collections import OrderedDict
tasks = OrderedDict({
 "task1": "низкий",
 "task2": "средний",
 "task3": "высокий",
 "task4": "низкий",
 "task5": "высокий"
})
Пример вывода:
Очередь задач:
 task3: высокий
 task5: высокий
 task2: средний
 task1: низкий
 task4: низки'''
from collections import OrderedDict

def task_priority(tasks):
    for task, priority in list(tasks.items()):
        if priority == "низкий":
            tasks.move_to_end(task)
        elif priority == "высокий":
            tasks.move_to_end(task, last=False)
    return tasks

tasks = OrderedDict({
 "task1": "низкий",
 "task2": "средний",
 "task3": "высокий",
 "task4": "низкий",
 "task5": "высокий"
})

print(task_priority(tasks))

# Another variant (sorted)
from collections import OrderedDict

tasks = OrderedDict({
 "task1": "низкий",
 "task2": "средний",
 "task3": "высокий",
 "task4": "низкий",
 "task5": "высокий"
})

def task_priority(tasks):
    priority_order = {
        "высокий": 0,
        "средний": 1,
        "низкий": 2
    }

    sorted_items = sorted(
        tasks.items(),
        key=lambda item: priority_order[item[1]]
    )

    tasks.clear()
    tasks.update(sorted_items)

    return tasks

print(task_priority(tasks))

'''5. Подсчёт посещений страниц
Реализуйте функцию, которая принимает список посещённых страниц и подсчитывает количество посещений
каждой страницы, используя defaultdict.
Данные:
pages = ["home", "about", "home", "products", "home", "contact", "products"]
Пример вывода:
Посещения страниц:
{'home': 3, 'about': 1, 'products': 2, 'contact': 1}'''
from collections import defaultdict

pages = ["home", "about", "home", "products", "home", "contact", "products"]

def page_visits(pages):
    page_count = defaultdict(int)
    for page in pages:
        page_count[page] += 1
    return page_count

print(page_visits(pages))

'''6. Группировка слов по длине
Реализуйте функцию, которая группирует слова по их длине и возвращает словарь с ними.
Данные:
words = ["apple", "banana", "kiwi", "grape", "orange", "peach"]
Пример вывода:
Слова по длине:
5: ['apple', 'grape', 'peach']
6: ['banana', 'orange']
4: ['kiwi']'''
from collections import defaultdict

def group_len_words(words):
    len_words = defaultdict(list)
    for word in words:
        len_words[len(word)].append(word)
    return len_words

words = ["apple", "banana", "kiwi", "grape", "orange", "peach"]

print(f"Слова по длине:\n{dict(group_len_words(words))}")

'''7. Создание глобального счётчика
Создайте функцию increment_counter, которая использует глобальную переменную counter для подсчёта
вызовов этой функции.
Пример вызова:
increment_counter()
increment_counter()
print(counter)
Пример вывода:
Вызовов функции: 2'''
counter = 0

def increment_counter():
    global counter
    counter += 1

increment_counter()
increment_counter()

print(f"Вызовов функции: {counter}")

'''8. Очередь с LRU-кэшированием
Реализуйте функцию, которая поддерживает механизм LRU-кэша для очереди задач. Функция должна
принимать:
● Текущую очередь задач.
● Новые задачи для добавления.
● Максимальный размер очереди.
Если лимит очереди превышен, удаляйте задачи, которые не использовались дольше всех.
Данные:
tasks = ["task1", "task2", "task3", "task4", "task5", "task6"]
new1 = "task4"
new2 = "task1"
new3 = "task7"
new4 = "task2"
Пример вывода:
Очередь из 4 новых задач: ['task4', 'task1', 'task7', 'task2']'''
def lru_queue(tasks, new_tasks, max_size):
    queue = tasks.copy()  # чтобы не портить исходный список

    for task in new_tasks:
        # если задача уже есть — считаем её использованной
        if task in queue:
            queue.remove(task)

        # добавляем как самую свежую
        queue.append(task)
        queue.pop(0)

        # если превышен лимит — удаляем самую старую
        if len(queue) > max_size:
            queue.pop(0)

    return queue

tasks = ["task1", "task2", "task3", "task4", "task5", "task6"]
new_tasks = ["task4", "task1", "task7", "task2"]
queue_size = 4

result = lru_queue(tasks, new_tasks, queue_size)
print(f"Очередь из {queue_size} задач: {result}")

# Another variant
def lru_queue(tasks, max_size, *new_tasks):
    queue = tasks.copy()

    for task in new_tasks:
        if task in queue:
            queue.remove(task)

        queue.append(task)
        queue.pop(0)

        if len(queue) > max_size:
            queue.pop(0)

    return queue

tasks = ["task1", "task2", "task3", "task4", "task5", "task6"]
new1 = "task4"
new2 = "task1"
new3 = "task7"
new4 = "task2"
max_size = 4

result = lru_queue(tasks, max_size, new1, new2, new3, new4)
print(f"Очередь из {max_size} задач: {result}")