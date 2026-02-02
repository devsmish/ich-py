'''1. Начало равно концу
Напишите программу, которая принимает список строк и создает новый список только из слов, начинающихся и заканчиваются
одной и той же буквой. Данные:
strings = ["apple", "banana", "level", "radar", "grape"]
Пример вывода:
Строки, которые начинаются и заканчиваются одной и той же буквой: ['level', 'radar']'''
strings = ["apple", "banana", "level", "radar", "grape"]
new_list = []
for i in range(len(strings)):
    if strings[i][0] == strings[i][-1]:
        new_list.append(strings[i])
print(new_list)

'''2. Слова с гласных
Напишите программу, которая обрабатывает список строки создает новый список, где строки, начинающиеся с согласной 
буквы будут заканчиваться символом "!". Остальные слова добавьте в том же виде. Данные:
strings = ["apple", "banana", "cherry", "grape", "orange"]
Пример вывода:
Результат: ['apple!', 'banana', 'cherry', 'grape', 'orange!']'''
strings = ["apple", "banana", "cherry", "grape", "orange"]
new_list = []
for string in strings:
    if string[0].lower() not in "aouei":
        new_list += [string + "!"]
    else:
        new_list += [string]
print(new_list)