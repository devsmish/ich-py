'''1. Класс Employee
Создайте класс Employee, представляющий сотрудника.
● У каждого объекта должно быть поле name.
● Метод work() выводит строку: <имя> is working....
● Проверьте работу класса, создав сотрудника и вызвав метод work().
Пример вывода:
Alice is working...'''
class Employee:
    def __init__(self, name):
       self.name = name

    def work(self):
        print(f"{self.name} is working...")

e = Employee("Alice")
e.work()

'''2. Класс Developer
Создайте класс Developer, который расширяет Employee.
● Добавьте дополнительное поле language.
● Переопределите метод work(), чтобы он включал сообщение из родительского метода и добавлял
строку:
<имя> writes <язык> code.
● Проверьте работу, создав объект Developer и вызвав метод work().
Пример вывода:
Bob is working...
Bob writes Python code.'''
class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def work(self):
        super().work()
        print(f"{self.name} writes {self.language} code.")

d = Developer("Bob", "Python")
d.work()