'''5. Журнал вызовов функции
Создайте декоратор log_to_file, который будет записывать в файл все вызовы функции с её аргументами и результатом.
Лог сохраняется в файл call_log.log, каждый вызов — на новой строке.
Пример применения:
@log_to_file
def add(a, b):
return a + b

@log_to_file
def greet_with_name(name, punctuation="!"):
return f"Hello, {name}{punctuation}"

@log_to_file
def greet():
return "Hello"
Пример вывода (файл call_log.log):
function: add | args: 5, 3; kwargs: None | return: 8
function: greet_with_name | args: Alice; kwargs: punctuation='.' | return: Hello, Alice.
function: greet | args: None; kwargs: None | return: Hello'''
import functools
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    filename='call_log.log',
    encoding='utf-8')

def log_to_file(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        all_args = ', '.join(str(arg) for arg in args)
        all_kwargs = ', '.join(f"{key} = {value}" for key, value in kwargs.items())
        logging.info(f"func {func.__name__} | {all_args} | {all_kwargs} | return: {result}")
        return result
    return wrapper


@log_to_file
def add(a, b):
    return a + b

@log_to_file
def greet_with_name(name, punctuation="!"):
    return f"Hello, {name}{punctuation}"

@log_to_file
def greet():
    return "Hello"

# Пример вызова:
# try:
    print(add(5, 3))
    print(greet_with_name("Anna"))
    print(add("one", 3))             # ошибка
    print(greet_with_name("Anna", 0))  # ошибка
# except Exception as e:
    print(e)

print(add(5, 3))
print(greet_with_name("Anna"))
# print(add("one", 3))             # ошибка
# print(greet_with_name("Anna", 0))