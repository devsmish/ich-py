'''1. Звёздочки вместо чисел
Напишите программу, которая заменяет все цифры в строке на звёздочки *.
text = "My number is 123-456-789"'''
from itertools import count

text = "My number is 123-456-789"
new_text = ''
for letter in text:
    if letter.isdigit():
        new_text = new_text + '*'
    else:
        new_text = new_text + letter
print(new_text)

'''2. Количество символов
Напишите программу, которая подсчитывает количество вхождений всех символов в строке. Нужно вывести только символы, 
которые встречаются более 1 раза (игнорируя регистр), с указанием их количества. Выводите повторяющиеся символы только 
один раз. text = "Programming in python"
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
text = "Programming in python"
cp_text = text.lower()
temp_text = ''
for letter in cp_text:
    if cp_text.count(letter) > 1 and letter not in temp_text:
        count = cp_text.count(letter)
        temp_text += letter
        print(f"Символ {letter} встречается {count} раз(а)")

'''3. Увеличение чисел
Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
Пример вывода:
I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.'''
text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
temp_list = text.split()
new_string = ""
for i in range(len(temp_list)):
    if temp_list[i].isdigit():
        new_string += str(int(temp_list[i]) * 10) + ' ' # если здесь функцию int заменить на float, то получится ожидаемый результат, но мне кажется что с интом будет лучше
    elif temp_list[i].replace(".",'').isdigit() and temp_list[i].count('.') == 1:
        new_string += str(float(temp_list[i]) * 10) + ' '
    else:
        new_string += temp_list[i] + ' '
print(new_string)
