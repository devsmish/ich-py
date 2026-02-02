# text = "Python"
# for letter in text:
#     print(letter)

# print(range(5))
# for i in range(5):
#     print(i)

# for i in range(2, 6):
#     print(i)

# for i in range(1, 9, 2):
#     print(i)

# for i in range(10, -1, -2):
#     print(i)
# # for i in range(0, 10, -2):  # not working
# #     print(i)
# for i in range(-4, -8, -1):
#     print(i)

# for letter in input("Enter text"):
#     if letter == "h":
#         # Останавливаем цикл
#         # если найден символ "h"
#         break
#     print(letter)


# for letter in "Python":
#     if letter == "h":
#         # Пропускаем букву "h" и
#         # продолжаем цикл
#         continue
#     print(letter)
#
# for letter in "Python":
#     if letter == "o":
#         # Этот код никогда не выполнится,
#         # так как "a" нет в строке
#         break
#     print(letter)
# else:
#     print("Цикл завершён нормально.")

# # Пример 1
# for i in "AB":
#     for j in "12":
#         print(i, j)

# Пример с выводом времени
# for hour in range(24):
#     for minute in range(60):
#         if minute < 10:
#             print("Время (часов:минут): ", hour, ':0', minute, sep='')
#         else:
#             print("Время (часов:минут): ", hour, ':', minute, sep='')



# current_hours = int(input("Введите текущий час: "))  # Текущее время
# hours = 3
# end_time = current_hours + 3
#
# while current_hours < 24 and current_hours < end_time:  # Внешний цикл с использованием while
#     for minutes in range(60):  # Внутренний цикл с использованием for
#         print("Время (часов:минут): ", current_hours, ':', minutes, sep='')
#     current_hours += 1  # Увеличение значения часов на 1
#


W = int(input()) # 5
H = int(input())# 3

for i in range(H):
    for j in range(W):
        print('*', end="")
    print('|', end="")

print()
for i in range(H):
    for j in range(W):
        print('*', end="")
    # print(end="\n")
    print()