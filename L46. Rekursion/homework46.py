'''Сумма цифр числа
Напишите рекурсивную функцию, которая находит сумму всех цифр числа.
Данные:
num = 43197
Пример вывода:
24'''
def sum_numbers(num: int) -> int:
    if num == 0:
        return 0
    return num % 10 + sum_numbers(num // 10)

num = input("Enter a integer number: ")
if num == '' or not num.isdigit():
    print("WARNING!!! Incorrectly value")
    exit()
tmp_num = int(num)
print(sum_numbers(tmp_num))

'''Сумма вложенных чисел
Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.
Данные:
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
Пример вывода:
28'''
def sum_nums(numbers: list[int | list]) -> int:
    result = 0
    if numbers == []:
        return 0
    for i in range (len(numbers)):
        if isinstance(numbers[i], int):
            result += numbers[i]
        elif isinstance(numbers[i], list):
            result += sum_nums(numbers[i])
    return result

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

print(sum_nums(nested_numbers))