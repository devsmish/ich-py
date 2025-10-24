original_print = print
def custom_print(*args, **kwargs):
     original_print("[LOG]:", *args, **kwargs)
print = custom_print
print("Это тестовый вывод")

# определение типа данных
print(type(7))
print(type(2.5))
print(type(""))
print(type(True))
print(type(print())) # тип аргумента функции print
print(type(print))   # тип самой функции print