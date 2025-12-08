'''1. Число в конце
Напишите программу, которая создает новый список. В него необходимо добавить только те строки из исходного списка, в
которых цифры находятся только в конце.
Данные:
strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
Пример вывода:
Строки с цифрами только в конце: ['apple23', 'grape3']'''
strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
new_list = []
for string in strings:
    i = 0
    while i < len(string) and string[i].isalpha():
        i += 1
    if i < len(string) and string[i:].isdigit():
        new_list.append(string)
print("Строки с цифрами только в конце:", new_list)

'''2. Удаление кратных
Напишите программу, которая удаляет из списка все значения, кратные числу, которое вводится пользователем.
Данные:
numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
Пример вывода:
Введите число для удаления кратных ему элементов: 3
Список без кратных значений: [1, 10, 19, 20]'''
numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
multip = int(input("Enter a number: "))
del_num = []
for i in range(len(numbers)):
    if numbers[i] % multip == 0:
        del_num.append(numbers[i])
for num in del_num:
    if num in numbers:
        numbers.remove(num)
print("Список без кратных значений:", numbers)

'''3. Порядок четных
Напишите программу, которая формирует новый список чисел. Добавьте в него все элементы исходного списка, где:
нечетные числа занимают те же позиции, чётные числа отсортированы между собой обратном порядке.
Данные:
numbers = [5, 2, 3, 8, 4, 1, 2, 7]
Пример вывода:
Список после сортировки: [5, 8, 3, 4, 2, 1, 2, 7]'''
numbers = [5, 2, 3, 8, 4, 1, 2, 7]
new_list = []
even_num = []
for num in numbers:
    if num % 2 == 0:
        even_num.append(num)
    even_num.sort(reverse=True)
for num in numbers:
    if num % 2 != 0:
        new_list.append(num)
    else:
        new_list.append(even_num[0])
        even_num.remove(even_num[0])
print("Список после сортировки:", new_list)
