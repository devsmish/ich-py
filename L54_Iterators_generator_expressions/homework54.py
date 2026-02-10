'''1. Фильтрация по ключевому слову
Напишите программу, которая помогает планировать дела. Программа должна бесконечно выводить план на
следующий день недели, пока пользователь нажимает 'Enter'.
Данные:
# Расписание дел на неделю
weekly_schedule = {
 "Monday": ["Gym", "Work", "Read book"],
 "Tuesday": ["Meeting", "Work", "Study Python"],
 "Wednesday": ["Shopping", "Work", "Watch movie"],
 "Thursday": ["Work", "Call parents", "Play
guitar"],
 "Friday": ["Work", "Dinner with friends"],
 "Saturday": ["Hiking", "Rest"],
 "Sunday": ["Family time", "Rest"]\
Пример ввода:
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана:
Tuesday: Meeting, Work, Study Python
...
Нажмите 'Enter' для получения плана:
Sunday: Family time, Rest
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана: q'''
from itertools import cycle

weekly_schedule = {
 "Monday": ["Gym", "Work", "Read book"],
 "Tuesday": ["Meeting", "Work", "Study Python"],
 "Wednesday": ["Shopping", "Work", "Watch movie"],
 "Thursday": ["Work", "Call parents", "Play guitar"],
 "Friday": ["Work", "Dinner with friends"],
 "Saturday": ["Hiking", "Rest"],
 "Sunday": ["Family time", "Rest"]}

cycler = cycle(weekly_schedule)
while True:
    user_input = input("Нажмите 'Enter' для получения плана: ")
    if user_input == '':
        key = next(cycler)
        value = ', '.join(weekly_schedule[key])
        print(f"{key}: {value}")
    elif user_input.lower() == 'q':
        break
    else:
        print("Введена не корректная команда!")

'''2. Объединение списков продуктов
Напишите функцию, которая принимает несколько списков с названиями продуктов и возвращает генератор,
содержащий все продукты в нижнем регистре. Выведите содержимое генератора.
Данные:
fruits = ["Apple", "Banana",
"Orange"]
vegetables = ["Carrot", "Tomato",
"Cucumber"]
dairy = ["Milk", "Cheese",
"Yogurt"]
Пример вывода:
apple
banana
orange
carrot
tomato
cucumber
milk
cheese
yogurt'''
import itertools

def list_merging(merged):
    return (item.lower() for item in merged)

fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]

merged = itertools.chain(fruits, vegetables, dairy)

for item in list_merging(merged):
    print(item)

'''3. Комбинации одежды
Напишите функцию, которая принимает списки типов одежды, цветов и размеров, а затем генерирует все
возможные комбинации в формате "Clothe - Color - Size".
Данные:
clothes = ["T-shirt", "Jeans",
"Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]
Пример вывода:
T-shirt - Red - S
T-shirt - Red - M
T-shirt - Red - L
T-shirt - Blue - S
...
Jacket - Black - L'''
from itertools import product

def data_combination(clothes, colors, sizes):
    return product(clothes, colors, sizes)

clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

for clothe, color, size in data_combination(clothes, colors, sizes):
    print(f"{clothe} - {color} - {size}")