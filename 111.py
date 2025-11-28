data_list = [
 "John 23 12345.678",
 "Alice 30 200.50",
 "Bob 35 15000.3",
 "Charlie 40 500.75"]
for item in data_list:
    item_list = item.split()
    for i in range(len(item_list)):
        name = item_list[i]
        age = item_list[i + 1]
        balance = item_list[i + 2]
        break
    text = f'''Имя: {name:<8} | Возраст: {age:<3} | Баланс: {balance:<10}'''
    print(text)