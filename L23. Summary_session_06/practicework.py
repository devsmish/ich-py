'''1. Удаление лишних символов
Напишите программу, которая создает новую строку, удаляя из строки все
символы, кроме букв, цифр и пробелов.
Пример вывода:
Введите строку: Hello, World! 2025...
Результат: Hello World 2025'''
text = input("Enter your text: ")
new_text = ''
for char in text:
    if 'a' <= char.lower() <= 'z' or "0" <= char <= "9" or char == " ":
        new_text += char
print(new_text)

'''2. Проверка на панограмму
Напишите программу, которая проверяет, содержит ли строка все буквы
английского алфавита хотя бы по одному разу (игнорируя регистр и пробелы).
Пример вывода:
Введите строку: The quick brown fox jumps over the lazy dog
Панограмма? True'''
text = input("Enter your text: ")
tmp_text = ''
count = 0
for char in text:
    if char.lower() not in tmp_text and char != ' ':
        tmp_text += char.lower()
        count += 1
if count == 26:
    print("Панограмма? True")
else:
    print("Панограмма? False")