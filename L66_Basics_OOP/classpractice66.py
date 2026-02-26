'''1. Класс User
Создайте класс User, который описывает пользователя.
● У каждого пользователя должно быть поля: username и email, а также
счётчик входов login_count.
● Добавьте метод show_info(), который выводит имя и почту пользователя.
● Добавьте метод login(), который приветствует пользователя и фиксирует
новый вход.
● Добавьте метод get_logins(), возвращающий текущее количество входов.
● Создайте пользователя, выполните несколько входов и выведите
информацию.
Пример вывода:
------------------------------
Пользователь: alice
Почта: alice@example.com
------------------------------
alice вошёл в систему
alice вошёл в систему
Количество входов: 2'''

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.login_count = 0

    def show_info(self):
        print("-" * 30)
        print("Пользователь:", self.username)
        print("Почта:", self.email)
        print("-" * 30)

    def login(self):
        self.login_count += 1
        print(f"{self.username} вошёл в систему")

    def get_logins(self):
        return self.login_count

user = User("alice", "alice@example.com")
user.show_info()
user.login()
user.login()
print("Количество входов:", user.get_logins())

'''2. Класс Product
Реализуйте класс Product, который описывает товар в магазине.
● Каждый объект должен хранить название (name) и цену (price).
● Добавьте метод apply_discount(), который уменьшает цену на заданный
процент и выводит информацию о размере примененной скидки.
● Добавьте метод info(), который выводит название и текущую цену товара.
● Проверьте работу класса: создайте товар, выведите его данные, примените
скидку, затем снова выведите информацию.
Пример вывода:
Название: Молоко
Цена: 120
Применяем скидку 25%
Новая цена: 90.0'''
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        print(f"Применяем скидку {percent}%")
        self.price -= self.price * percent / 100

    def info(self):
        print(f"Название: {self.name}")
        print(f"Цена: {self.price}")

p = Product("Молоко", 120)
p.info()
p.apply_discount(25)
p.info()