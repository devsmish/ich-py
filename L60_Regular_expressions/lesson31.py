# import re
#
# text = "\tPython 3.12,         Java 17, C++ 14!\n"
#
# print("Цифры:", re.findall(r"d", text))
# print("Двузначные цифры:", re.findall(r"\d\d", text))
#
# print("НЕ цифры:", re.findall(r"\D", text))
#
# print("Буквы, цифры, _:", re.findall(r"\w", text))
#
# print("НЕ буквы, цифры, _:", re.findall(r"\W", text))
#
# print("Пробелы:", re.findall(r"\s", text))
#
# print("НЕ пробелы:", re.findall(r"\S", text))
#
# print("Все символы (кроме \\n):", re.findall(r".", text))
#
#
# print(re.findall(r" {4}", text))
#
# import re
#
# text = "Report.txt, rreport-txt, report2, report10, file"
#
#
# print("Буквы r или R в слове:", re.findall(r"[rR]+eport\.txt", text))
#
# print("Все цифры:", re.findall(r"[0-9]+", text))
#
# print("Заглавные буквы:", re.findall(r"[A-Z]", text))
#
# print("Строчные буквы:", re.findall(r"[a-z]", text))
#
# print("Все буквы:", re.findall(r"[a-zA-Z]", text))
#
# print("Все, кроме цифр:", re.findall(r"[^0-9]", text))


# import re
#
# text = """
# Orders: ID123, ID4567, ID89
# Numbers: 123-45-67, 321-45-67
# Prices: 100$, 199.50$, 99.99€, 0.49€, .99€
# File names: report.txt, report2.txt, report10.txt
# ******
# ++++++++
# """
#
# print("Одна или более цифр:", re.findall(r"\d+", text))
#
# print("Телефонные номера (формата xxx-xx-xx):", re.findall(r"\d{3}-\d{2}-\d{2}", text))
#
# print("Цены (числа с десятичной точкой):", re.findall(r"\d+\.\d+", text))
#
# print("ID-коды:", re.findall(r"ID\d{2,}", text))
#
# print("Имена файлов 0+ цифр:", re.findall(r"report\d*.txt", text))
#
# print("Имена файлов 0/1 цифр:", re.findall(r"report\d?.txt", text))
#
# print("Имена файлов 1/2 цифр:", re.findall(r"report\d{1,2}.txt", text))
# print(re.findall(r"\++", text))


# import re
# text = "<div>Hello</div><div>World</div>"
#
# greedy = re.findall(r"<.*>", text)  # Жадный
# lazy = re.findall(r"<.*?>", text)   # Ленивый
#
# print(greedy)
# print(lazy)



# import re
#
# text = "report.txt, report2.txt, report10.txt, some_txt_report, some_report_txt"
#
# print("Имена файлов с txt:", re.findall(r"\w+.txt", text))
#
# # Имена файлов с расширением .txt
# print("Имена файлов с расширением .txt:", re.findall(r"\w+\.txt", text))
#
# # Имена файлов в папке
# print("Имена файлов в папке:", re.findall(r"\w+\\\w+\.\w+", r"reports\report.txt, report2.txt"))


# import re
#
# text = "Hello world! Welcome to world"
#
# print("Слово в начале строки:", re.findall(r"^\w+", text))
# print("Слово в конце строки:", re.findall(r"\w+$", text))
#
# text2 = "category wildcat education _cat_ catalog"
#
# print("Слова с 'cat' внутри:", re.findall(r"\w+cat\w+", text2))
# print("Слова с 'cat' в начале слов:", re.findall(r"\bcat\w*", text2))
# print("Слова с 'cat' в конце слов:", re.findall(r"\w*cat\b", text2))

# text3 = "X123X 234 4567X X999"
# print("Числа внутри строк:", re.findall(r"\B\d+\B", text3))



# import re
#
# text = "Meeting on 2024-05-10 or 10/05/2024 at 14:30"
#
# # Найдём даты в формате YYYY-MM-DD или DD/MM/YYYY
# print("Даты:", re.findall(r"(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})", text))
# print("Даты:", re.findall(r"( \d{4}|[a-z]{2})", text))


# import re
#
# text = "Order ID: 12345, Invoice No: 67890"
#
# # Найдём ID заказа и счёта
# match = re.search(r"Order ID: (\d+), Invoice No: (\d+)", text)
#
# if match:
#     print("ID заказа:", match.group(1))
#     print("Номер счёта:", match.group(2))
#
#
# import re
#
# text = "USD 100, EUR 200, GBP 300, BYN 150"
#
# # Найдём суммы, не выделяя валюту
# matches = re.findall(r"(?:USD|EUR|GBP) (\d+)", text)
# print("Суммы:", matches)
#
# # Найдём суммы и валюту
# matches = re.findall(r"(USD|EUR|GBP) (\d+)", text)
# print("Суммы:", matches)


# import re
#
# text = "ID12345 is confirmed. ID23456 is confirmed"
#
# # Проверяем, начинается ли строка с "ID" + цифры
# match = re.match(r"ID\d+", text)
#
# if match:
#     print("Объект Match:", match)
#     print("Само совпадение:", match.group())
#     print("Диапазон совпадения:", match.span())
# else:
#     print("Нет совпадения.")

# import re
#
# text = "Order ID: 12345, Invoice No: 67890, Ref: ABC9876"
#
# # Найдём первое число в тексте
# match = re.search(r"\d+", text)
#
# if match:
#     print("Объект Match:", match)
#     print("Само совпадение:", match.group())
#     print("Индекс начала:", match.start())
#     print("Индекс конца:", match.end())
#     print("Диапазон совпадения:", match.span())
# else:
#     print("Нет совпадения.")


# import re
#
# text = "Python is popular."
#
# # Найдём слово "python" без учёта регистра
# match = re.search(r"python", text, re.IGNORECASE)
#
# if match:
#     print("Найдено:", match.group())

#
# import re
#
# text = "Order ID: 12345, Invoice No: 67890, Ref: ABC9876"
#
# # Найдём все числа в тексте
# matches = re.finditer(r"\d+", text)
#
# for match in matches:
#     print("Объект Match:", match)
#     print("Само совпадение:", match.group())
#     print("Диапазон совпадения:", match.span())
#     print()


# import re
#
# text = """Python is popular. It is used in web development, data science,
# and automation. Many developers choose Python for its simplicity."""
#
# # Разделяем строку по запятым, пробелам и точкам
# words = re.split(r"[,\s.]+", text)
#
# print("Список слов:", words)

#
# import re
#
# text = "apple,   banana ,  orange ,grape"
#
# # Удаляем лишние пробелы перед и после запятых
# clean_text = re.sub(r"\s*,\s*", ", ", text)
#
# print("Отформатированный текст:", clean_text)

import re

texts = [
    "Order ID: 12345, Invoice No: 67890, Ref: ABC9876",
    "Shipment ID: 54321, Tracking No: 98765, Customer Ref: XYZ123",
    "Invoice 22222 processed successfully."
]

# Компилируем регулярное выражение для поиска числовых идентификаторов
number_pattern = re.compile(r"\d+")

# Применяем шаблон к разным текстам
for text in texts:
    match = number_pattern.findall(text)
    if match:
        print(f"Совпадение в тексте: {match}")
