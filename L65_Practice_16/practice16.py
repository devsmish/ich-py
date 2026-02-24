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