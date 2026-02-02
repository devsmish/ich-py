''' 1. Счетчик слов
Напишите программу, которая обрабатывает строку и выводит её, добавив к каждому слову его
порядковый номер, выравнивая текст по левому краю с длиной в 15 символов. Слова выводите с
большой буквы.
Пример вывода:
Введите строку: Hello world Python is great
1. Hello
2. World
3. Python
4. Is
5. Great '''
text = input("Hello world Python is great")
text_list = text.split()
for i in range(len(text_list)):
    print(f"{i + 1}. {text_list[i].title():<15}")

'''2. Формат даты
Напишите программу, которая принимает дату в виде числа, месяца и года, а затем выводит её в
формате "dd/mm/yyyy", где день и месяц всегда состоят из двух цифра.
Пример вывода:
Введите день: 3
Введите месяц: 7
Введите год: 2024
Дата: 03/07/2024 '''
day = input("Enter day: ")
month = input("Enter month: ")
year = input("Enter year: ")
print(f"Дата: {int(day):02d}/{int(month):02d}/{year}")