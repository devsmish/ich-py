from collections import OrderedDict


# class ClassName:
#     pass
#
# print(ClassName)
# print(ClassName())


# OrderedDict

# class Book:
#     # ожидаемые данные для книги
#     def __init__(self, title, author):
#         # data = []
#         # сохраняем название книги
#         self.title = title
#         # сохраняем имя автора
#         self.author = author
#         self.status = "new"
#
# book = Book("title", "author")
# book2 = Book("title2", "author2")
# print(book)
# print(book2)
#
# print(book.title)
# print(book2.title)
# print(book2.status)
# # print(book2.data)


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         print(self.title)
#
# # Создание книг
# book1 = Book("1984", "George Orwell")
# book2 = Book("Brave New World", "Aldous Huxley")


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
# book = Book("1984", "George Orwell")
#
# print(book.title)
# print(book.author)


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         # print(self.title)
#
# book = Book("1984", "George Orwell")
# book2 = Book("Brave New World", "Aldous Huxley")
#
# print(book.title)  # старое имя
# print(book.author)
#
# book.title = "Animal Farm"  # изменение значения поля title
# print(book.title)  # измененное имя
#
# print(book2.title)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_description(self):  # self - ссылка на объект, у которого вызван метод
        return f"{self.title} — {self.author}"

    def show_info(self):  # self - ссылка на объект, у которого вызван метод
        print(self.get_description())  # вызов другого метода через self

    def make_author_upper(self):  # self - ссылка на объект, у которого вызван метод
        self.author = self.author.upper()

book = Book("1984", "George Orwell")
# book.show_info()  # вызов метода у объекта
# book.make_author_upper()  # изменение объекта с помощью метода
# book.show_info()  # вывод нового состояния
# print(book.get_description())

Book.show_info(book)
