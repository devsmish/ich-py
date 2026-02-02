'''Напишите программу, которая считывает четырёхзначное число и меняет местами первую и последнюю
цифры.
Пример вывода:
Введите четырёхзначное число: 1234
Число после изменения: 4231'''
numbers = int(input("Enter a four-digit number: "))
thousands = numbers // 1000
digits = numbers % 10
middle_numbers = numbers % 1000 // 10
result = digits * 1000 + middle_numbers * 10 + thousands
print("Число после изменения: " + str(result))