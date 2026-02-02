'''1.1 Стереть после нуля
Напишите программу, которая удаляет все элементы списка, начиная с первого встреченного нуля.
Данные:
numbers = [1, 2, 0, 3, 4, 5]
Пример вывода:
Список после удаления: [1, 2]'''
numbers = [1, 2, 0, 3, 4, 5]
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] == 0:
        del numbers[i:len(numbers)]
print(numbers)

'''2.1 Объединение информации
Напишите программу, которая объединяет два списка: имена и возраст. Выведите пары в виде: <Имя> is
<Возраст> years old.
Данные:
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
Пример вывода:
Alice is 25 years old.
Bob is 30 years old.
Charlie is 35 years old.'''
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
personal_data = zip(names, ages)
for name, age in personal_data:
    print(f"{name} is {age} years old.")

'''2.2 Умножение пар чисел
Даны два списка чисел: 1, 2, 3] и 4, 5, 6.
Создайте список произведений всех пар чисел (первое число из list1, второе из list2).
Данные:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
Пример вывода:
[4, 5, 6, 8, 10, 12, 12, 15, 18]'''
list1 = [1, 2, 3]
list2 = [4, 5, 6]
multiplication = []
for i in range(len(list1)):
    for j in range(len(list2)):
        multiplication.append(list1[i] * list2[j])
print(multiplication)