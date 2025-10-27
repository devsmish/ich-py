'''Сумма цифр числа
Напишите программу, которая получит четырехзначное число от пользователя и выведет на экран
сумму цифр этого числа.
Пример вывода:
Введите четырехзначное число: 1634
Сумма цифр числа: 14'''

number = int(float(input("Введите четырехзначное число: ")))
result = thousand = handred = tenth = digits = 0

thousand = number // 1000
handred = (number - thousand * 1000) // 100
tenth = (number - thousand * 1000 - handred * 100) // 10
digits = (number - thousand * 1000 - handred * 100 - tenth * 10) // 1

result = thousand + handred + tenth + digits
print("Сумма цифр числа ", number, " равна ", result)