'''1. Создайте декоратор limit_output, который обрезает строку, возвращаемую функцией, до max_len символов.
Если строка длиннее, то она обрезается до выбранного лимита и завершается троеточием ..., входящим в этот лимит.
Пример применения:
@limit_output
def get_text():
return "Это очень длинный текст, который нужно обрезать."
Пример вывода:
Это очень длинный...'''
def limit_output(func):
    def wrapper(*args, **kwargs):
        original_string = func(*args, **kwargs)
        max_len = 20
        if len(original_string) > max_len:
            return original_string[:max_len-3] + "..."
        return original_string
    return wrapper


@limit_output
def get_text():
    return "Это очень длинный текст, который нужно обрезать."

print(get_text())

'''2. Доработайте декоратор limit_output, чтобы он принимал параметр max_len — максимальная длина строки.
Пример применения: 
@limit_output(26)
def get_text():
return "Это очень длинный текст, который нужно обрезать."
Пример вывода: 
Это очень длинный текст...'''
def limit_output(max_len):
    def decorator(func):
        def wrapper(*args, **kwargs):
            original_string = func(*args, **kwargs)
            if len(original_string) > max_len:
                return original_string[:max_len-3] + "..."
            return original_string
        return wrapper
    return decorator

@limit_output(max_len=28)
def get_text():
    return "Это очень длинный текст, который нужно обрезать."
print(get_text())

'''3. Кеширование результатов
Создайте декоратор cache, который сохраняет результат вызова функции для каждого набора аргументов.
Если функция вызывается повторно с теми же аргументами — возвращается сохранённый результат.
Пример применения: 
@cache
def multiply(a, b):
    print(f"Вычисляем {a} * {b}: ")
    return a * b
Пример вывода: 
Вычисляем 2 * 3: 6
Результат из кеша: 6
Вычисляем 4 * 5: 20
Результат из кеша: 6'''
def cache(func):
    memory = {}
    def wrapper(*args, **kwargs):
        parameters = (args, tuple(sorted(kwargs.items())))
        print(parameters)
        if parameters not in memory:
            print("Результат 1")
            result = func(*args, **kwargs)
            memory[parameters] = result
        return memory[parameters]
    return wrapper

@cache
def multiply(a, b):
    print(f"Вычисляем {a} * {b}: ")
    return a * b

print(multiply(1,b=2))
print(multiply(1,b=2))
print(multiply(1,b=2))

'''4. Кеш с ограничением по размеру
Доработайте декоратор cache, чтобы он:
Принимал параметр max_size, ограничивающий количество сохранённых записей.
При превышении max_size — удалял самую старую запись из кеша.
Пример применения:
@cache(max_size=2)
def multiply(a, b):
print(f"Вычисляем {a} * {b}: ")
return a * b
Пример вывода: 
Вычисляем 2 * 3: 6
Результат из кеша: 6
Вычисляем 4 * 5: 20
Вычисляем 6 * 7: 42
Вычисляем 2 * 3: 6'''
from collections import OrderedDict

def cache(maxsize=100):
    def decorator(func):
        memory = OrderedDict()
        def wrapper(*args, **kwargs):
            parameters = (args, tuple(sorted(kwargs.items())))
            if parameters in memory:
                memory.move_to_end(parameters)
            else:
                if len(memory) >= maxsize:
                    memory.popitem(last=False)
                result = func(*args, **kwargs)
                memory[parameters] = result
            # print(memory)
            return memory[parameters]
        return wrapper
    return decorator

@cache(2)
def multiply(a, b):
    print(f"Вычисляем {a} * {b}: ")
    return a * b

print(multiply(1,b=2))
print(multiply(1,b=3))
print(multiply(1,b=2))
print(multiply(1,b=4))
print(multiply(1,b=3))

'''5. Журнал вызовов функции
Создайте декоратор log_to_file, который будет записывать в файл все вызовы
функции с её аргументами и результатом.
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
import logging


logging.basicConfig(
    filename="call_log.log",
    level=logging.INFO,
    format="%(message)s",
    encoding="utf-8"
    )
def log_to_file(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        all_args = ", ".join(str(arg) for arg in args)
        all_kwargs = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        logging.info(f"function: {func.__name__} | " f"args: {all_args if all_args else None}; kwargs:"
                     f"{all_kwargs if all_kwargs else None} | " f"return: {result}")
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

# Использование
add(5, 3)
greet_with_name("Alice", punctuation=".")
greet()

'''6. Проверка типов аргументов по порядку
Создайте декоратор accepts_types, который проверяет, что позиционные аргументы функции соответствуют указанным типам.
Если тип хотя бы одного аргумента не совпадает — должна быть выброшена ошибка
TypeError с указанием ожидаемого и полученного типа.
Пример применения:
@accepts_types(int, int)
def add(a, b):
 return a + b
@accepts_types(str)
def greet(name):
 return f"Hello, {name}!"
@accepts_types(str, str)
def greet_by_name(name, punctuation="!"):
 return f"Hello, {name}{punctuation}"
Пример вызова:
try:
 print(add(5, 3))
 print(greet_by_name("Anna"))
 print(add("one", 3)) # ошибка
 print(greet_by_name("Anna", 0)) # ошибка
except Exception as e:
 print(e)
Пример вывода:
8
Hello, Anna!
Incorrect type for argument 'one': expected - <class 'int'>, received - <class
'str'>
Incorrect type for argument '0'
: expected
-
<class 'str'>, received
-
<class
'int'
>'''
def accepts_types(*expected_types):
    def decorator(func):
        def wrapper(*args):
            for arg, expected in zip(args, expected_types):
                if not isinstance(arg, expected):
                    raise TypeError(f"Incorrect type for argument '{arg}': expected - {expected}, received - {type(arg)}")
            return func(*args)
        return wrapper
    return decorator

@accepts_types(int, int)
def add(a, b):
    return a + b

@accepts_types(str)
def greet(name):
    return f"Hello, {name}!"

@accepts_types(str, str)
def greet_by_name(name, punctuation="!"):
    return f"Hello, {name}{punctuation}"

# Вызовы функций
try:
    print(add(5, 3))
    print(greet_by_name("Anna"))
# print(add("one", 3)) # ошибка
    print(greet_by_name("Anna", 0)) # ошибка
except Exception as e:
    print(e)