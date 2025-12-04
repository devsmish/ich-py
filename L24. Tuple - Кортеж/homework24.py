'''1. Прогрессия увеличения
Напишите программу, которая создаёт новый кортеж, состоящий из элементов изначального в том же порядке. Добавить в него
только элементы, которые больше всех предыдущих значений в исходном кортеже. Данные:
numbers = (3, 7, 2, 8, 5, 10, 1)
Пример вывода:
Кортеж по возрастанию: (3, 7, 8, 10)'''
numbers = (3, 7, 2, 8, 5, 10, 1)
increase_tuple = (numbers[0],)
for index, value in enumerate(numbers[:-1]):
    if value > numbers[index + 1]:
        increase_tuple = increase_tuple + (value, )
print("Кортеж по возрастанию:", increase_tuple)

'''2. Повторяющиеся элементы
Напишите программу, которая находит индексы элементов кортежа, встречающихся более одного раза.
Вывести сами элементы и их индексы.
Данные:
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
Пример вывода:
Индексы элемента 2: 1 4 9
Индексы элемента 3: 2 6
Индексы элемента 4: 3 8'''
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
uniq_value = ()
for i in range(len(numbers)):
    if numbers[i] in uniq_value:
        continue
    count = 0
    enum_index = ''
    for index, value in enumerate(numbers):
        if value == numbers[i]:
            count += 1
            enum_index = enum_index + str(index) + " "
    if count > 1:
        uniq_value = uniq_value + (numbers[i],)
        print(f"Индексы элемента {numbers[i]}: {enum_index}")