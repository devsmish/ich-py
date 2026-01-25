# def function_a():
#     print("Начало A")
#     function_b()
#     print("Конец A")
#
# def function_b():
#     print("Начало B")
#     function_c()
#     print("Конец B")
#
# def function_c():
#     print("Начало C")
#     print("Конец C")
#
# function_a()


# def countdown_iterative(n: int) -> None:
#     while n > 0:
#         print(n)
#         n -= 1
#     print("Конец!")
#
# countdown_iterative(5)


# def countdown(n: int) -> None:
#     # Базовый случай
#     if n <= 0:
#         print("Конец!")
#         return
#     print(n)
#     # Рекурсивный случай
#     countdown(n - 1)
#     print("-")
#
# countdown(5)


# def infinite_recursion():
#     infinite_recursion()
#
# infinite_recursion()


# def factorial(n: int) -> int:
#     if n == 0 or n == 1:  # Базовый случай
#         return 1
#     return n * factorial(n - 1)  # Рекурсивный случай
#
# print(factorial(5))
import math
# math.factorial()

# def binary_search(arr: list[int], target: int, left: int, right: int) -> int:
#     if left > right:  # Базовый случай: элемент не найден
#         return -1
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return binary_search(arr, target, mid + 1, right)  # Поиск в правой части
#     else:
#         return binary_search(arr, target, left, mid - 1)  # Поиск в левой части
# array = [1, 3, 5, 7, 9, 11, 13]
# # print(binary_search(array, 5, 0, len(array) - 1))
# # print(binary_search(array, 13, 0, len(array) - 1))
# print(binary_search(array, 8, 0, len(array) - 1))


# print(2 ** 100)


# def factorial_tail(n: int, accumulator: int = 1) -> int:
#     if n == 0 or n == 1:
#         return accumulator
#     return factorial_tail(n - 1, n * accumulator)
#
# print(factorial_tail(5))


def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)


def print_nums(n):
    if n == 0:
        return
    print_nums(n - 1)
    print(n)

print(print_numbers(5))
print(print_nums(5))
