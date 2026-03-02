'''1. Счётчик экземпляров
Создайте класс User, представляющий пользователя.
● При создании должны указываться логин (username) и пароль (password).
● У класса должно быть поле total_users, хранящее общее количество
созданных пользователей.
● При каждом создании нового объекта User, счётчик должен увеличиваться.
● Добавьте метод get_total(), возвращающий количество пользователей.
● Проверьте, что счётчик работает.
Пример вывода:
Total users: 2'''
class User:
    total_users = 0
    def __init__(self, username, password):
        self.username = username
        self.password = password
        User.total_users += 1

    @classmethod
    def get_total(cls):
        return cls.total_users

us1 = User("alice", "secret")
us2 = User("bob", "qwe")
print(User.get_total())

'''2. Проверка данных пользователя
Доработайте класс User.
● Добавьте валидации полей при создании.
● Имя должно быть непустой строкой.
● Пароль должен быть строкой длиной не менее 5 символов.
● Если данные некорректны — выбрасывайте ValueError.
● Добавьте строковое представление объекта.
● Проверьте работу класса с разными значениями.
Пример вывода:
User: alice
 ...
ValueError: Invalid password:
'qwe'.
Пример вызова:
user1 = User("alice", "secret")
user2 = User("bob", "qwe")'''
class User:
    total_users = 0
    def __init__(self, username, password):
        self.data_validator(username, password)
        self.username = username
        self.password = password
        User.total_users += 1

    @classmethod
    def get_total(cls):
        return cls.total_users

    @staticmethod
    def data_validator(username, password):
        if not isinstance(username, str) or len(username) == 0:
            raise ValueError('Invalid username')
        if  not isinstance(password, str) or len(password) < 5:
            raise ValueError('Invalid password')

        return True

    def __str__(self):
        return f'{self.username} ; {self.password}'

users = []

test_data = [
    ("alice", "secret"),
    ("bob", "qwe"),
    ("", "1234567"),
    ("player", "soccer25"),
    ("", "")
]

for username, password in test_data:
    try:
        user = User(username, password)
        users.append(user)
    except ValueError as e:
        print(f'ValueError: {e} | username="{username}", password="{password}"')

print("\nСозданные пользователи:")
for user in users:
    print(user)

print("\nTotal:", User.get_total())