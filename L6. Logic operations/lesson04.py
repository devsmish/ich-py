# print(bool(5)) # True (ненулевое число)
# print(bool(0)) # False
# print(bool(None)) # False
# print(bool([])) # False (пустой список)
# print(bool("Hello")) # True (непустая строка)
# print(bool(""))
# # result = "0"
# result = "/"
# print(bool(result))
# # print(bool(not result))
# # print(bool(input("Enter text: ")))
# print(bool(int(input("Enter text: "))))

# "dfs" + "0"
# print(bool(0), bool("dsfs"))
# print("Result: " + str(bool(0)) + "-" + str(bool("dsfs")))
# print(True)
# print(False)
# print(None)
# print(7)


# a = 10
# b = 10
# print(a != b)
# a = 10
# b = 5
# print(a != b) # True, так как a не равно b
# a = 8
# b = 10
# print(a > b) # False, так как a меньше

a = 5
b = 10
# print(a > 0 and b > 0 or a == 5)
# print(a > 0 and b > 0 or a == 1)
# print(a > 0 and b > 0 and a == 2 / 0)
# print(a > 0 and b > 0 or a == 2 / 0)
# print(a < 0 and b > 1 and a == 2 / 0)

# print(a < 0 or b > 0 and a == 2 / 0 and a < b)
# print(a < 0 or (b > 0 and a == 2 / 0) or a < b)
# print(a > 0 or (b > 0 and a == 2 / 0))
#
# result = 4 < 3 + 2
# # Сначала выполняется сложение (3 + 2), затем
# # результат сравнивается с 4
# print(result) # True, так как 5 > 4

# good_weather = True
# is_weekend = False
# free_time = False
# can_go_out = good_weather or is_weekend and free_time
# print(can_go_out) # Результат:
# can_go_out = (good_weather or is_weekend) and free_time
# print(can_go_out) # Результат:

x = 5
print(1 < x <= 10)
# x находится между 1 и 10 (включительно)