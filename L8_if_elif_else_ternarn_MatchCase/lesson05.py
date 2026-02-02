# a > b + 1 and c - 2 < d

# математические
# сравнение
# логические

# x = 10
# print(x > 5)
# if x > 5:
#     print("----------")
#     print("x больше 5") # выполнится
# y = 1
# print(y == 0)
# if y == 0:
#     print("y равняется 1") # не выполнится

# a = 5
# # Неявное преобразование в True
# if a:
#     print("Число 5 - True")

# # Пример 1
# x = 4
# if x > 10:
#     print("x больше 10")
# elif x > 5:
#     print("x больше 5, но меньше или равно 10")

# # Пример 2
# age = 25
# if age < 18:
#     print("Несовершеннолетний")
# elif age < 30:
#     print("Молодой взрослый")
# elif age < 50:
#     print("Взрослый")

# # Пример 1
# x = 3
# if 1 < x < 5:
#     print("x между 1 и 5")
# else:
#     print("x не между 1 и 5")

# # Пример 2
# age = 25
# if age < 18:
#  print("Несовершеннолетний")
# elif age < 30:
#  print("Молодой взрослый")
# elif age < 50:
#  print("Взрослый")
# else:
#  print("Пожилой")


# x = 7
# if x > 5:
#     print("x больше 5") # Это условие истинно, выполнится
# if x < 10:
#     print("x меньше 10") # Это условие тоже истинно, выполнится
# if x == 7:
#     print("x равно 7") # Это условие также истинно, выполнится

# x = 7
# if x > 5:
#     print("x больше 5")  # Это условие истинно, выполнится
# elif x < 10:
#     print("x меньше 10")  # Это условие тоже истинно, выполнится
# if x == 7:
#     print("x равно 7")  # Это условие также истинно, выполнится


# role = "user"
# section_access = True
# if role == "admin":
#     print("Вы администратор.")
#     if section_access:
#         print("У вас есть доступ к разделу.")
#     else:
#         print("У вас нет доступа к разделу.")
# else:
#     print("Вы не администратор.")

# role = "user"
# section_access = True
# if role == "admin" and section_access:
#     print("Вы администратор.")
#     print("У вас есть доступ к разделу.")
# elif role == "admin" and not section_access:
#     print("Вы администратор.")
#     print("У вас нет доступа к разделу.")
# else:
#     print("Вы не администратор.")

# age = 18
# if age >= 18:
#     status = "Взрослый"
# else:
#     status = "Несовершеннолетний"
# print(status)

# age = 18
# status = "Взрослый" if age >= 18 else "Несовершеннолетний"
# print(status)
#
# x = 11
# print("Чётное" if x % 2 == 0 else "Нечётное")

# age = -3
# status = "Взрослый" if age >= 18 else "Несовершеннолетний" if 0 < age < 18 else "Некорректный возраст"
# print(status)

# age = 77
# status = ("Пожилой" if age > 70 else "Взрослый") \
#     if age >= 18 else "Несовершеннолетний" \
#     if 0 < age < 18 else "Некорректный возраст"
# print(status)


# number = 2
# match number:
#     case 1:
#         print("Это один.")
#     case 2 | 3: # Символ "|" является аналогом оператора "or"
#         print("Это два или три.")
#     case _ if number > 5:
#         print("Число больше 5.")
#     case _:
#         print("Это число меньше или равно 5.")


value = 1
match value:
    case bool():
        print("Это логический тип.")
    case int():
        print("Это целое число.")
    case str():
        print("Это строка.")
    case _:
        print("Неизвестный тип данных.")
