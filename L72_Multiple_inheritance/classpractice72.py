'''1. Класс Student
Создайте класс Student, представляющий ученика.
● При создании указываются имя и email.
● Добавьте строковое представление студента (например, только имя).
● Добавьте метод notify(message), который выводит сообщение: Email to <email>: <message>
Проверьте создание объекта и вызов метода.'''
class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return self.name

    def notify(self, message):
        print(f"Email to {self.email}: {message}")

s = Student("Alice", "alice@example.com")
print(s)
s.notify("You have been enrolled.")

'''2. Класс Course
Создайте класс Course, представляющий учебный курс.
● При создании указывается название курса.
● У каждого объекта Course должно быть поле students, в котором хранится список зарегистрированных студентов.
● Добавьте метод add_student(student), который принимает объект Student и добавляет его в курс.
● Добавьте метод show_students(), который выводит список имён студентов.
● Добавьте метод notify_all(message), который уведомляет всех студентов курса.
Проверьте работу методов, создав курс, добавив студентов и отправив уведомление.
Пример вывода:
Students enrolled in Python OOP:
- Alice
- Bob
Email to alice@example.com: Welcome to the course!
Email to bob@example.com: Welcome to the course!'''
class Course:
    def __init__(self, title):
        self.title = title
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        print(f"Students enrolled in {self.title}:")
        for student in self.students:
            print("-", student)

    def notify_all(self, message):
        for student in self.students:
            student.notify(message)

s1 = Student("Alice", "alice@example.com")
s2 = Student("Bob", "bob@example.com")

course = Course("Python OOP")
course.add_student(s1)
course.add_student(s2)
course.show_students()
course.notify_all("Welcome to the course!")