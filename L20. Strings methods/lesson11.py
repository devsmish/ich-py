# text = "s"
# print(text.isascii())
#
# # проверяет, состоит ли строка только из букв и цифр (без пробелов и специальных символов)
# print("Hello 123".isalnum())
# # проверяет, начинается ли строка с указанной подстроки
# print("Hello world.txt".startswith("Hello"))
#
# # проверяет, состоит ли строка только из числовых символов, включая дробные числа или надстрочные символы
# print("½".isnumeric())
# print("½".isdecimal())

# text = "Python is awesome. Python is dynamic."
# # Поиск первого вхождения подстроки
# print(text.find("Python"))
# # Поиск последнего вхождения подстроки
# print(text.rfind("Python"))
# # Подстрока не найдена
# print(text.find("Java"))

# text = "Python is awesome. Python is dynamic."
# # Поиск первого вхождения подстроки
# print(text.index("Python"))
# # Поиск последнего вхождения подстроки
# print(text.rindex("Python"))
# # Попытка найти отсутствующую подстроку вызывает ошибку
# # print(text.index("Java"))  # ValueError
#
# text = "Python is awesome. Python is dynamic."
# # Подсчёт количества вхождений подстроки
# print(text.count("Python"))
# # Если подстрока не найдена, возвращает 0
# print(text.count("Java"))
# # Следующую подстроку ищет после конца предыдущей,
# # т.е. без пересечений
# text = "hahahahahaha"
# print(text.count("ha"))
# print(text.count("haha"))

# text = "Hello, worlD!"
# # Преобразование строки в верхний регистр
# print(text.upper())
# # Преобразование строки в нижний регистр
# print(text.lower())
# # Первая буква строки становится заглавной, остальные строчными
# print(text.capitalize())
# # Первая буква каждого слова становится заглавной
# print(text.title())
# # Меняет регистр всех символов на противоположный
# print(text.swapcase())
# # Приводит строку к нижнему регистру с учётом особенностей языка
# print("Straße".casefold())

# # Пример замены всех вхождений
# text = "I love Python, Python is great"
# new_text = text.replace("Python", "Java")
# print(new_text)
# # Пример с ограничением замен
# text = "apple apple apple"
# new_text = text.replace("apple", "orange", 2)
# # print(text.replace("apple", "orange", 2))
# print(text)
# print(new_text)


# # Пример с ограничением замен
# text = "apple apple apple"
# new_text = text.replace("apple", "orange", 2).replace("apple", "banana")
# # print(text.replace("apple", "orange", 2))
# print(text)
# print(new_text)


# # Пример 1: Разделение строки по пробелам
# text = "apple banana cherry"
# fruits = text.split()
# print(fruits)
# print(type(fruits))
# # Пример 2: Разделение строки по запятой
# text = "apple, banana, cherry"
# fruits = text.split(", ")
# print(fruits)
# # Пример 3: Разделение строки с ограничением количества разбиений
# text = "apple---banana---cherry"
# fruits = text.split("---", 1)
# print(fruits)


# text = "apple     banana   \n cherry"
# fruits = text.split()
# print(fruits)
#
# # fruits = text.split("  ")
# # print(fruits)
#
# print(" - ".join(fruits))


# # Пример 1: Объединение списка строк с пробелом
# fruits = ['apple', 'banana', 'cherry']
# text = " ".join(fruits)
# print(text)
# # Пример 2: Объединение списка строк с запятой и пробелом
# fruits = ['apple', 'banana', 'cherry']
# text = ", ".join(fruits)
# print(text)
# # Пример 3: Объединение списка строк по пустому символу
# litters = ['a', 'b', 'c', 'd', 'e']
# text = "".join(litters)
# print(text)
#
# text = "\t  hello world\n  "
# print(text.strip())  # Удаляет все пробельные символы
#
# text_with_chars = "***hello***"
# print(text_with_chars.strip("*"))  # Удаляет указанный символ
#
# text_with_chars = "**--*hello---***"
# print(text_with_chars.strip("*-"))  # Удаляет все указанные символы

# text = "  hello world  "
# print(text.lstrip())  # Вывод: "hello world  "
# text_with_chars = "***hello***"
# print(text_with_chars.lstrip("*"))  # Вывод: "hello***"
# text = "  hello world  "
# print(text.rstrip())  # Вывод: "  hello world"
# text_with_chars = "***hello***"
# print(text_with_chars.rstrip("*"))  # Вывод: "***hello"

# text = "Python, Java, C++"
# languages = text.split(",")
# print(languages)
# print(list(text))

text = """I have '2' apples and "14" bananas"""

new_list = text.split()
for i in range(len(new_list)):
    tmp = new_list[i].strip('\'"')
    if tmp.isdigit():
        new_list[i] = "'" + str(int(tmp) ** 2) + "'"
print(' '.join(new_list))

