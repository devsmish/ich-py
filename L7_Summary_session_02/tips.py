'''Напишите программу, которая принимает сумму счёта и процент чаевых, который пользователь хочет оставить.
Программа должна рассчитать и вывести сумму чаевых.
Пример вывода:
Введите сумму счёта: 150
Введите процент чаевых: 8
Сумма чаевых: 12.0'''
invoice = float(input("Enter the invoice amount: "))
tips_percent = float(input("Enter the tip percentage: "))
result = invoice * (1 + tips_percent / 100)
print("Сумма чаевых: ", result)