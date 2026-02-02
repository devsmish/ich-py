'''1. Проверка кодировки. Напишите программу, которая принимает от пользователя один символ и выводит его код в таблице
Unicode и его принадлежность к диапазону ASCII (True/False).
Пример вывода:
Введите символ: A
Код Unicode: 65
ASCII символ: True'''
simbol = input("Enter one Symbol: ").upper()
if len(simbol) > 1:
    print("You have entered more than one character!!!")
print("Код Unicode:", ord(simbol))
if ord(simbol) < 128:
    print("ASCII символ: True")
else:
    print("ASCII символ: False")

'''2. Подстрока с заполнением. Напишите программу, которая принимает строку и индексы начала и конца. Программа должна
вывести подстроку на указанных позициях. Также если конечный индекс выходит за пределы строки, программа заполняет 
недостающие символы символами _.
Пример вывода:
Введите строку: Программирование
Введите начальный индекс: 3
Введите конечный индекс: 20
Подстрока: граммирование_____'''
text = input("Введите строку: ")
start_index = int(input("Введите начальный индекс: "))
finish_index = int(input("Введите конечный индекс: "))
if len(text) < finish_index - start_index + 1:
    dop_simbol = finish_index - len(text[start_index:finish_index])
    print(text[start_index:finish_index] + dop_simbol * "_")
else:
    print(text[start_index:finish_index])

'''3. Подсчёт символа
Напишите программу, которая принимает строку и символ, а затем подсчитывает, сколько раз символ встречается в строке.
Пример вывода:
Введите строку: Hello, world!
Введите символ: o
Символ o встречается 2 раз(а).'''
text = input("Enter your text: ")
simbol = input("Enter your simbol: ")
count_simbol = 0
iterat = 0
while  iterat < len(text):
    if simbol == text[iterat]:
        count_simbol += 1
        iterat += 1
    else:
        iterat += 1
print(f"Символ {simbol} встречается {count_simbol} раз(а).")

'''4. Инвертирование строки без цифр
Напишите программу, которая принимает строку и выводит её в обратном порядке, пропуская все цифры.
Пример вывода:
Введите строку: n52uFs6Inoh67ty8P
Результат: PythonIsFun'''
text = input("Enter any text: ")
invert_text = ""
iterat = 0
while iterat < len(text):
    if text[-iterat - 1] not in '0123456789':
        invert_text += text[-iterat - 1]
        iterat += 1
    else:
        iterat += 1
print("Result:", invert_text)