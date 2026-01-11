'''Простое число
Напишите функцию, которая проверяет, является ли число n простым (делится только на 1 и само себя) и
возвращает булевый результат.
Данные:
n = 17
Пример вывода:
Число 17 является простым'''
def prime_numbers(n):
    div_count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            div_count += 1
    if div_count == 2:
        return True
    return False

n = input("Enter any integer number: ")
print(f"Число {n} является простым {prime_numbers(int(n))}")

'''Фильтрация чисел по чётности
Напишите функцию, которая принимает filter_type ("even" или "odd") и произвольное количество чисел,
возвращая только те, которые соответствуют фильтру.
Пример вызова:
print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))
Пример вывода:
[2, 4, 6]
[15, 25]
Некорректный фильтр'''
def filter_numbers(filter_type, numbers):
    if filter_type == "even":
        list_numbers = []
        for number in numbers:
            if number % 2 == 0 and number not in list_numbers:
                list_numbers.append(number)
    elif filter_type == "odd":
        list_numbers = []
        for number in numbers:
            if number % 2 != 0 and number not in list_numbers:
                list_numbers.append(number)
    else:
        return "Некорректный фильтр"
    return sorted(list_numbers)

filter_type = input("Enter ever or odd: ")
numbers = []
num = ''
while True:
    num = input("Enter number: ")
    if num.lower() == "exit":
        break
    else:
        numbers.append(int(num))
print(filter_numbers(filter_type, numbers))

'''Объединение словарей
Напишите функцию, которая принимает любое количество словарей и объединяет их в один. Если ключи
повторяются, используется значение из последнего словаря.
Данные:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}
Пример вызова:
print(merge_dicts(dict1, dict2, dict3))'''
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}

def merge_dicts(*dicts):
    combination_dict = dict1.copy()
    combination_dict.update(dict2)
    combination_dict.update(dict3)
    return combination_dict

print(merge_dicts(dict1, dict2, dict3))