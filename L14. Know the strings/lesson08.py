# s = "Hello"
# s = s + " world!"
# print(s)

# text = "hello"
# # # Кодирует текст, полученный из
# # # переменной text в 'utf-8'
# # print(text.encode('utf-8'))
#
# print(text.capitalize())
# print("python".capitalize())
# print(input().capitalize())

#
# text = "Python"
# # Метод .encode() кодирует строку в байты с использованием UTF-8
# encoded_text = text.encode('utf-8')
# print(encoded_text)
#
# # Оригинальная строка
# text = "Привет"
#
# # Кодирование строки в байты с использованием UTF-8
# encoded_text = text.encode('utf-8')
# print(encoded_text)
#
# # Декодирование байтов обратно в строку
# decoded_text = encoded_text.decode('utf-8')
# print(decoded_text)

#
# print(ord('A'))
# print(ord('a'))
# print(ord(' '))
#
# print(chr(65))
# print(chr(9700))
# print(chr(32))
# print(chr(0x1F600))


# print("apple" != "Apple")
# print("apple" == "banana")

# print("apple" < "ban")
# print("Apple" < "banana")
# print("apple" > "Apple")

# print("apple" < "anple")
# print("apple" < "apples")

# text = "Python "
# length = len(text)
# print(length)


# Для строк:
# text = "Python"
# print("Hello"[4])
# print(text[0])   # Вывод: 'P' (первый символ)
# print(text[2])   # Вывод: 't' (третий символ)
# # print(input()[4])
# print(len(text))
# print(text[len(text) // 2])
#
# i = 0
# while i < len(text):
#     print(text[i])
#     i += 1

# # print(text[6])  # error
# text = "Python"
# print(text[-2])
#
# text = "hello"
# index = 2
# if 0 <= index < len(text):
#     print(text[index])
# else:
#     print("Индекс вне диапазона!")

# text = "Python programming"
# print(text[0:8])
#
# text = "Python programming"
# print(text[:6])
#
# text = "Python programming"
# print(text[7:])
#
# text = "Python programming"
# print(text[:])
#
# text = "Python programming"
# print(text[5:60])
#
# text = "Python programming"
# print(text[-11:])

# text = "Python programming"
# print(text[-11:-4])  # -11 < -4
# print(text[7:14])  # 7 < 14
#
# text = "Python programming"
# print(text[-4:-11])  # Пустая строка
# print(text[14:7])  # Пустая строка


# # Положительный шаг
# text = "Python programming"
# print(text[0:12:2])  # Вывод: 'Pto rg'
# print(text[1:12:2])

# Отрицательный шаг (обратный порядок)
# text = "Python programming"
# print(text[12:6:-1])  # Вывод: 'argorp'
#
# text = "Python programming"
# print(text[-4:-11:-1])  # -11 < -4
# print(text[14:7:-1])  # 7 < 14
#
# text = "Python programming"
# print(text[-11:-4:-1])  # Пустая строка
# print(text[7:14:-1])  # Пустая строка
#
# text = "Python"
# print(text[::-1])  # Вывод: 'nohtyP'
# print(text[:-3:-1])
# print(text[-3::-1])
#
# text = "! Py   Python programming"
# print("Python" in text)
# print("Hello" in text)
# print("a" in text)

text = "Python programming"
print("Java" not in text)
print(not "Java" in text)
