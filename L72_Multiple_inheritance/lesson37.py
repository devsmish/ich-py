# class Printable:
#     def print_info(self):
#         print("Печать информации...")
#
# class Savable:
#     def save(self):
#         print("Сохраняем в файл...")
#
# class Report(Printable, Savable):
#     pass
#
# r = Report()
# r.print_info()  # унаследовано от Printable
# r.save()        # унаследовано от Savable




# class User:
#     def __init__(self, username):
#         self.username = username
#
# user = User("Alice")
# user.email = "dfsdf"
#
# print(hasattr(user, "username"))  # Атрибут существует
# print(hasattr(user, "email"))     # Атрибута нет



# class AuthMixin:
#     def login(self):
#         if not hasattr(self, "username"):
#             raise AttributeError("Не задан username")
#         print(f"{self.username} вошёл в систему.")
#
#     def logout(self):
#         print("Пользователь вышел из системы.")
#
#
# class NotificationMixin:
#     def send_email(self, message):
#         if not hasattr(self, "email"):
#             raise AttributeError("Не задан email")
#         print(f"Отправка письма на {self.email}: {message}")
#
#
# class UserProfile(AuthMixin, NotificationMixin):
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
# user = UserProfile("alice", "alice@example.com")
# user.login()                             # alice вошёл в систему.
# user.send_email("Добро пожаловать!")     # Отправка письма на alice@example.com: Добро пожаловать!
# user.logout()                            # Пользователь вышел из системы.

# class A:
#     pass
#     def greet(self):
#         print("Hello from A")
#
# class B(A):
#     pass
#
# class C(A):
#     pass
#     def greet(self):
#         print("Hello from C")
#
# class D(B, C):
#     pass
#
# d = D()  # D и B не имеют метода greet
# d.greet()
#
# class S:
#     pass
#
# class A:
#     def greet(self):
#         print("Hello from A")
#
# class B(S, A):
#     pass
#
# class C(B):
#     def greet(self):
#         print("Hello from C")
#
# class D(B, A):
#     pass
#
# class E(C, D):
#     pass
#
# print(E.__mro__)  # Возвращает кортеж классов


# class A:
#     def action(self):
#         print("A")
#
# class B(A):
#     def action(self):
#         print("B")
#         super().action()
#
# class C(A):
#     def action(self):
#         print("C")
#         super().action()
#
# class D(B, C):
#     def action(self):
#         print(super())
#         print("D")
#         super().action()
#
# d = D()
# d.action()


# class ExitButton:
#     def click(self):
#         print("Выход из программы")
#
# class Menu:
#     def __init__(self):
#         self.exit_button = ExitButton()  # создаётся внутри
#         # self.exit_button = "exit"  # создаётся внутри
#
#     def show(self):
#         print("Меню открыто")
#         self.exit_button.click()
#
# menu = Menu()
# menu.show()


# class ExitButton:
#     def click(self):
#         print("Выход из программы")
#
# class Menu:
#     def __init__(self, menu_name):
#         self.name = menu_name
#         self.exit_button = ExitButton()  # создаётся внутри
#
#     def show(self):
#         print("Меню открыто")
#         self.exit_button.click()
#
# menu = Menu("Main menu")
# menu.show()


#
# class University:
#     def __init__(self, name):
#         self.name = name
#
#     def get_info(self):
#         print(f"Обучение проходит в университете: {self.name}")
#
# class Teacher:
#     def __init__(self, name, university):
#         self.name = name
#         self.university = university  # передаётся извне
#
#     def introduce(self):
#         print(f"Преподаватель: {self.name}")
#         self.university.get_info()
#
#
# # Университет создаётся один раз
# uni = University("Tech University")
#
# # Передаётся в нескольких преподавателей
# t1 = Teacher("Anna", uni)
# t2 = Teacher("Dmitry", uni)
#
# t1.introduce()
# t2.introduce()
#


class Smartphone:
    class Battery:
        def __init__(self, capacity):
            self.capacity = capacity
            self.charge = capacity

        def use(self, amount):
            self.charge = max(self.charge - amount, 0)
            print(f"Батарея: {self.charge}/{self.capacity} мАч")

    def __init__(self, model, battery_capacity):
        self.model = model
        self.battery = self.Battery(battery_capacity)

    def play_video(self):
        print(f"{self.model} воспроизводит видео...")
        self.battery.use(300)

phone = Smartphone("Pixel 9", 4000)
phone.play_video()