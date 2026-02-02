# Python Fundamentals 2025: Домашнее задание 10
'''1. Торговый автомат
Напишите программу, которая моделирует работу торгового автомата. Автомат принимает только монеты номиналом 1, 2, 5, 10
и 50. Программа должна запрашивать у пользователя общую стоимость покупки, а затем отображать сколько монет каждого типа
нужно потратить, чтобы использовать минимальное количество монет для оплаты товара.
Пример вывода:
Введите стоимость товара: 127
Внесите монеты номиналом 50: 2
Внесите монеты номиналом 10: 2
Внесите монеты номиналом 5: 1
Внесите монеты номиналом 2: 1'''
# teacher
cost = int(input("Введите стоимость товара: "))
remaining = cost
coins = [50, 10, 5, 2, 1]

print("Для оплаты внесите следующие монеты:")
for coin in coins:
    count = remaining // coin
    if count > 0:
        print("Внесите монеты номиналом ", coin, ": ", count, sep="")
    remaining %= coin
    if remaining == 0:
        break

'''2. Квадрат нечетных чисел
Напишите программу, которая изменяет изначальный список и возводит в квадрат только нечётные числа.
numbers = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
Пример вывода:
Изначальный список: [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
Измененный список: [4, 81, 1, 49, 2, 25, 0, 9, 49, 1, 9]'''
# teacher
numbers = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
print("Изначальный список:", numbers)

for i in range(len(numbers)):
    print(numbers[i])
    if numbers[i] % 2 == 1:
        numbers[i] = numbers[i] ** 2
print("Измененный список: ", numbers)

# Python Fundamentals 2025: Домашнее задание 11
'''1. Звёздочки вместо чисел
Напишите программу, которая заменяет все цифры в строке на звёздочки *.
text = "My number is 123-456-789"
Пример вывода:
Строка: My number is 123-456-789
Результат: My number is ***-***-***'''
# teacher
text = "My number is 123-456-789"
print("Строка:", text)
result = text
for char in text:
    if char.isdigit():
        result = result.replace(char, "*")
print("Результат:", result)

# Another variant
text = "My number is 123-456-789"
result = text
for digit in "0123456789":
    result = result.replace(digit, '*')

print("Строка:", text)
print("Результат:", result)

# Variant 2
text = "My number is 123-456-789"
result = text
for digit in range(10):
    result = result.replace(str(digit), '*')

print("Строка:", text)
print("Результат:", result)

# Variant 3
text = "My number is 123-456-789"
text_without_numbers = ""
for char in text:
    if "0" <= char <= "9":
    # if (ord(char) >= 48) and (ord(char) <= 57):
        char = '*'
    text_without_numbers += char

print(text_without_numbers)

'''2. Количество символов
Напишите программу, которая подсчитывает количество вхождений всех символов в строке. Нужно вывести только символы, 
которые встречаются более 1 раза (игнорируя регистр), с указанием их количества. Выводите повторяющиеся символы только 
один раз.
text = "Programming in python"
Пример вывода:
Строка: Programming in python
Символ 'p' встречается 2 раз(а)
Символ 'r' встречается 2 раз(а)
Символ 'o' встречается 2 раз(а)
Символ 'g' встречается 2 раз(а)
Символ 'm' встречается 2 раз(а)
Символ 'i' встречается 2 раз(а)
Символ 'n' встречается 3 раз(а)
Символ ' ' встречается 2 раз(а)'''
# teacher
text = "Programming in python"
print("Строка:", text)
text = text.lower()
unique = ""

for char in text:
    if char not in unique:
        unique += char
        count_char = text.count(char)
        if count_char > 1:
            print("Символ", "'" + char + "'", "встречается", count_char, "раз(а)")

'''3. Увеличение чисел
Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
Пример вывода:
I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.'''
text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
words = text.split()
for i in range(len(words)):
    if words[i].replace('.', '', 1).isdigit():
        words[i] = str(float(words[i]) * 10)
result = " ".join(words)
print(result)

# Another variant if after digit stand other simbol, ! ? ...
text = "I have 5 apples and 10 oranges, price is 0.5. Card number is ....3672."
words = text.split()

for i in range(len(words)):
    word = words[i].rstrip(".,")
    # if len(word) != len(words[i]):
    #     diff = len(word) - len(words[i])
    #     striped = words[i][diff:]
    # else:
    #     striped = ""

    # if . or , at the end of the sentence
    striped = words[i][len(word) - len(words[i]):] if len(word) != len(words[i]) else ""
    if word.count(".") < 2 and word.replace(".", "").isdecimal():
        words[i] = str(float(word) * 10) + striped
new_text = " ".join(words)
print(new_text)