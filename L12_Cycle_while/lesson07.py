# i = 1
# while i <= 5:
#     print(i)
#     i += 1
#
# print("End")

# while i <= 5:
#     i += 1
#     print(i)
#
# print("End")

# i = 10
# while i > 7:
#     print("-")
#     i -= 1
# print(i)

# i = 2
# while i <= 8:
#     i += 2
# # print(i)

# i = 1
# while i <= 10:
#     print(i)
#     if i == 5:
#         break  # Прерывание цикла, когда i станет равно 5
#     i += 1
#
# print("End")


# while True:
#     user_input = input("Введите 'exit', чтобы завершить цикл: ")
#     if user_input == "exit":
#         break
#     print("Вы ввели:", user_input)
#
# print("End")

# while True:
#     user_input = input("Введите 'exit', чтобы завершить цикл: ")
#     if user_input == "admin_pass":
#         break
#     print("----------------------")
#     if user_input == "exit":
#         break
#     print("Вы ввели:", user_input)
#
# print("End")

# user_input = input("Введите 'exit', чтобы завершить цикл: ")
# while user_input != "exit":
#     print("Вы ввели:", user_input)
#     user_input = input("Введите 'exit', чтобы завершить цикл: ")
#
# print("End")

# i = 0
# while i < 5:
#     i += 1
#     if i % 2 == 0:
#         continue  # Пропускаем итерацию, когда i четное
#     print(i / 2)
#     if i > 2:
#         print(i)
#     print("----------")


# result = 1
# while True:
#     user_input = input("Введите число для перемножения: ")
#     if user_input == "0":
#         print("Пропуск итерации")
#         continue  # Пропускаем оставшуюся часть текущей итерации
#     if user_input == "exit":
#         print("Выход из программы")
#         break  # Прерывание цикла
#     result *= int(user_input)
#     print("Результат перемножения:", result)

# while True:
#     print("Этот цикл будет выполняться бесконечно")

# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# else:
#     print("Цикл завершён без прерываний.")

# result = 1
# num = 1
# while num < 6:
#     user_input = input("Введите " + str(num) + "-е число для перемножения: ")
#     num += 1
#     if user_input == "0":
#         print("Некорректные данные. Выход из программы")
#         break  # Прерывание цикла
#     result *= int(user_input)
# else:
#     print("Цикл завершён без прерываний.")
#     print("Результат перемножения:", result)
# print("End")

# result = 1
# num = 1
# while num < 6:
#     user_input = input("Введите число №" + str(num) + " для перемножения: ")
#     if user_input == "0":
#         print("Некорректные данные. Выход из программы")
#         break  # Прерывание цикла
#     if int(user_input) > 1000:
#         print("Слишком большое число. Пропуск итерации")
#         continue  # Пропускаем оставшуюся часть текущей итерации
#     result *= int(user_input)
#     num += 1
# else:
#     print("Цикл завершён без прерываний.")
#     print("Результат перемножения:", result)


# import random
#
# # Генерируем случайное число от 0.0 до 1.0
# print(random.random())
#
# import random
#
# # Генерируем случайное целое число от 1 до 10 (включая обе границы)
# print(random.randint(1, 10))

import random

# Генерируем случайное целое число от 1 до 10 (не включая число 10)
print(random.randrange(1, 10))
# Генерируем случайное целое число от 1 до 10 (не включая число 10) и с шагом 2 (только по
# нечетным числам)
print(random.randrange(1, 10, 2))


