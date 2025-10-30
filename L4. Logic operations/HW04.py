'''1. Логические операции
Напишите программу, которая получит два логических значения от пользователя и выведет результат
логических операций and, or, not для этих значений, а также сравнение на равенство и неравенство. Для
операции not используйте первое число. Продумайте в каком виде получать ввод от пользователя для
логического значения.
Пример вывода:
Enter first value: <value1>
Enter second value: <value1>
and: True
or: True
not: False
equal: False
not equal: True'''
first_value = bool(int(input("Enter 0 or 1: ")))
second_value = bool(int(input("Enter 0 or 1: ")))
print(first_value, second_value, "Результат AND:", first_value and second_value)
print(first_value, second_value, "Результат OR:", first_value or second_value)
print(first_value, "Результат NOT:", not first_value)
print(first_value, second_value, "Результат равенства:", first_value == second_value)
print(first_value, second_value, "Результат неравенства:", first_value != second_value)

'''2. Проверка условий
Напишите программу, которая принимает на вход логические значения двух переменных (свет включён и
окно открыто) и проверяет:
● Оба ли условия выполнены.
● Хотя бы одно из условий выполнено.
Пример вывода:
Свет включён? True
Окно открыто? False
Оба условия выполнены? False
Хотя бы одно условие выполнено? True'''
light_on = bool(int(input("Свет включён? (1 - Да, 0 - Нет): ")))
window_open = bool(int(input("Окно открыто? (1 - Да, 0 - Нет): ")))
print("Свет включён?", light_on)
print("Окно открыто?", window_open)
print("Оба условия выполнены?", light_on and window_open)
print("Хотя бы одно условие выполнено?", light_on or window_open)

'''3. * Стоимость мобильного тарифа
Напишите программу для расчёта стоимости использования мобильного тарифа:
● Базовая стоимость: 30 евро.
● Каждый мегабайт интернета сверх 500 МБ стоит 0.2 евро.
Программа должна запросить у пользователя количество использованных мегабайтов и вывести сколько
всего он заплатил (базовый и переплата).
Пример вывода:
Введите использованные мегабайты: 510
Общая стоимость: 32.0'''
standart_cost = 30
each_mb = 0.2
limit_mb = 500
number_used_mb = int(input("How many megabytes were used?: "))
new_cost = standart_cost + (number_used_mb - limit_mb) * each_mb * (number_used_mb > limit_mb)
print("The cost of your mobile plan is: ", new_cost, "Euro")