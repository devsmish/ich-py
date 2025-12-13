'''1. Одно слово
Напишите программу, которая обрабатывает список из строк и удаляет все строки, содержащие более
одного слова, а также преобразует оставшиеся строки к нижнему регистру.
Данные:
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
Пример вывода:
Обработанный список: ['hello', 'world', 'simple']'''
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
processed_list = []
for item in text_list:
    if " " not in item:
        processed_list.append(item.lower())
print("Обработанный список:", processed_list)

'''2. Обновление цен товаров
Дан список товаров с ценами. Программа должна применить скидку к каждому товару и добавить в список
элемент с новой ценой. В конце вывести таблицу с новой ценой.
Данные:
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
Пример вывода:
Введите скидку (в процентах): 17
Товар Старая цена Новая цена
Laptop 1200.00$ 996.00$
Mouse 25.00$ 20.75$
Keyboard 75.00$ 62.25$
Monitor 200.00$ 166.00$'''
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
discount = int(input("Введите скидку (в процентах): "))
print(f"{"Товар":<10} {"Старая цена":>12} {"Новая цена":>11}")
for i in range(0, len(products)):
    new_price = 0
    for j in range(0, len(products[i])):
        new_price = round(products[i][1] - products[i][1] * discount / 100, 2)
    products[i].append(new_price)
for name, price, new_price in products:
    print(f"{name:<10} {price:>11.2f}$ {new_price:>10.2f}$")
print("Обновленный список:", products)