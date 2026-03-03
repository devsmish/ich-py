'''1. Создайте класс Student, представляющий студента.
У каждого объекта должно быть имя и дата рождения.
Дата передаётся как строка (YYYY-MM-DD) и сохраняется в виде объекта datetime.date.
Добавьте проверку возраста — студенту должно быть не менее 16 лет, иначе выбрасывается ValueError.
Добавьте строковое представление объекта.
Пример вывода:
Student: Alice, birth_date: 2005-05-10, ID: 1'''
from datetime import date, datetime


class Student:
    def __init__(self, student_name, birthday):
        birthday_date = datetime.strptime(birthday, "%Y-%m-%d").date()
        age = Student.calculate_age(birthday_date)
        Student.validate_age(age)
        self.name = student_name
        self.birthday = birthday_date

    @staticmethod
    def calculate_age(birthday):
        today = datetime.now()
        age = today.year - birthday.year
        if (birthday.month, birthday.day) < (today.month, today.day):
            age -= 1
        return age

    @staticmethod
    def validate_age(age):
        if age < 16:
            raise ValueError("Возраст должен быть не менее 16 лет")

student1 = Student("Nina", "2000-02-12")
# print(student1.calculate_age("2013-02-12"))
print(student1.name)

'''2. Номер студента
Каждому студенту должен автоматически присваиваться уникальный номер - student_id, начиная с 1.'''

'''3. Строковое представление
Добавьте строковое представление объекта.
Пример вывода:
Student: Alice, birth_date: 2005-05-10, ID: 1'''
from datetime import date, datetime


class Student:

    id_counter = 0

    def __init__(self, student_name, birthday):
        birthday_date = datetime.strptime(birthday, "%Y-%m-%d").date()
        age = Student.calculate_age(birthday_date)
        Student.validate_age(age)
        self.name = student_name
        self.birthday = birthday_date
        Student.id_counter += 1
        self.id = Student.id_counter


    @staticmethod
    def calculate_age(birthday):
        today = datetime.now()
        age = today.year - birthday.year
        if (birthday.month, birthday.day) < (today.month, today.day):
            age -= 1
        return age

    @staticmethod
    def validate_age(age):
        if age < 16:
            raise ValueError("Возраст должен быть не менее 16 лет")

    def __str__(self):
        return f"Student: {self.name}, birth_date: {self.birthday}, ID: {self.id}"

print(Student.id_counter)
student1 = Student("Nina", "2000-02-12")
student2 = Student("Nina", "2000-02-12")

print(student1.name)
print(Student.id_counter)
print(student1)

'''4. Карточка студента
Добавьте метод, который выводит информацию о студенте на текущий момент.
Возраст вычисляется автоматически на основе даты рождения.
Пример вывода:
Student:
Name: Alice
Age: 19
ID: 1'''

'''5. Альтернативный конструктор
Реализуйте метод, позволяющий создавать объект из строки формата:
"Bob, 2001-12-03"'''

'''6. Возраст на конкретную дату
Добавьте возможность получить возраст студента на переданную дату'''

'''7. Фильтрация студентов по
возрасту
Реализуйте способ отобрать из списка студентов только тех, кто старше определённого возраста.'''

'''8. Проверка работы класса
● Создайте нескольких студентов разными способами.
● Выведите информацию о каждом.
● Попробуйте передать некорректную дату и отловите исключение.
● Получите список студентов старше указанного возраста.
Пример вывода:
Student: Alice, birth_date: 2005-05-10, ID: 1
Student:
Name: Alice
Age: 19
ID: 1
Student: Bob, birth_date: 2001-12-03, ID: 2
Student:
Name: Bob
Age: 23
ID: 2
Min age 21: [Student: Bob, birth_date: 2001-12-03, ID: 2]'''
from datetime import datetime, date


class Student:
    current_id = 1
    def __init__(self, name, birth_date):
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
        if not self.is_valid_birthdate():
            raise ValueError("Student must be at least 16 years old.")
        self.name = name
        self.student_id = Student.current_id
        Student.current_id += 1

    def __str__(self):
        return f"Student: {self.name}, birth_date: {self.birth_date}, ID: {self.student_id}"

    def __repr__(self):
        return f"Student: {self.name}, birth_date: {self.birth_date}, ID: {self.student_id}"

    def show_info(self):
        print(f"Student:\n\tName: {self.name}\n\tAge: {self.calculate_age()}\n\tID: {self.student_id}")

    def calculate_age(self):
        today = date.today()
        return self.calculate_age_on(today)

    def calculate_age_on(self, target_date):
        age = target_date.year - self.birth_date.year
        if (target_date.month, target_date.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def is_valid_birthdate(self):
        return self.calculate_age() >= 16

    @classmethod
    def from_string(cls, data):
        name, date = map(str.strip, data.split(", "))
        return cls(name, date)

    @staticmethod
    def filter_by_min_age(students, min_age):
        return [s for s in students if s.calculate_age() >= min_age]

# Пример использования
s1 = Student("Alice", "2005-05-10")
s2 = Student.from_string("Bob, 2001-12-03")
# s3 = Student.from_string("Bill, 2009-05-15") # ошибка
print(s1)
s1.show_info()
print(s2)
s2.show_info()
print(f"Min age 21:")
for s in Student.filter_by_min_age([s1, s2], 21):
    print("\t", s)