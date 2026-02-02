'''1. Кортеж уникальных
Напишите программу, которая обрабатывает кортеж чисел. Программа должна вернуть кортеж, в котором будут только
уникальные элементы. Не используйте неизученные коллекции.
Данные:
numbers = (1, 2, 3, 2, 1, 4, 5, 3, 6)
Пример вывода:
Уникальные элементы: (1, 2, 3, 4, 5, 6)'''
numbers = (1, 2, 3, 2, 1, 4, 5, 3, 6)
uniq_num = []
for index, value in enumerate(numbers):
    if value not in uniq_num:
        uniq_num = uniq_num + list([value])
print("Уникальные элементы:", uniq_num)

# Another variant
numbers = (1, 2, 3, 2, 1, 4, 5, 3, 6)
uniq = ()
for n in numbers:
    if n not in uniq:
        uniq += (n,)
print("Уникальные элементы: ", uniq)

'''2. Кортеж выше среднего
Напишите программу, которая обрабатывает кортеж чисел. Программа должна вернуть кортеж, состоящий из элементов, которые 
больше среднего значения всех элементов исходного кортежа. Данные:
numbers = (10, 15, 20, 25, 30)
Пример вывода:
Элементы больше среднего: (25, 30)'''
numbers = (10, 15, 20, 25, 30)
avg_num = round(sum(numbers) / len(numbers), 2)
max_tuple = ()
print("Среднее значение:", avg_num)
for index, value in enumerate(numbers):
    if value > avg_num:
        max_tuple = max_tuple + (value, )
print("Элементы больше среднего:", max_tuple)