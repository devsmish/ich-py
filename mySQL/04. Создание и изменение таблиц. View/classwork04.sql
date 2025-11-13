-- 1. Создать таблицу Employees со следующими столбцами:
-- ● EmployeeID
-- ● FirstName
-- ● LastName
-- ● BirthDate
-- ● HireDate
-- ● Salary
-- ● Email

# создать отдельную БД
create DATABASE 101025_SerhiiM;

# создать таблицу 
use 101025_SerhiiM;
create TABLE Employees (
	id INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) not null,
    LastName VARCHAR(50) not null,
    BirthDate DATE,
    HireDate DATE DEFAULT(current_date),
    Salary DECIMAL(9, 2) check(Salary > 0),
    Email VARCHAR(100) UNIQUE
);
-- 2. Указать ограничения
-- ● EmployeeID - первичный ключ, увеличивается автоматически на 1 при добавлении записи
-- ● FirstName и LastName - строка длиной в 50 символов Не может быть пустой
-- ● BirthDate - дата
-- ● HireDate - дата по умолчанию указывается текущая дата
-- ● Salary - число с количеством цифр 2 после запятой Общее число знаков, включая запятую, 10 Должна быть больше 0
-- ● Email - строка длиной в 100 символов Должна быть уникальной-- 

# проверка БД или таблицы на наличие в системе через конструкцию
create DATABASE if not exists 101025_SerhiiM;

# добавление данных в таблицу
use 101025_SerhiiM;
INSERT INTO Employees
	(FirstName, LastName, BirthDate, Salary, Email)
VALUES
	('Serg', 'Serginio', '2000-01-01', 700.00, 'serg@gmail.com');
# добавить несколько строк в таблицу
use 101025_SerhiiM;
INSERT INTO Employees
	(FirstName, LastName, BirthDate, Salary, Email)
VALUES
	('Serg', 'Serginio', '2000-01-01', 7000.00, 'serg@gmail.com'),
    ('Iv', 'Rocher', '1995-02-02', 4700.00, 'ivro@outlook.com'),
    ('Arno', 'Lehmann', '1990-03-03', 2500.00, 'lehmar@yahoo.com');
    
# удаление записей
delete from Employees
where EmployeedID = 5;

# удаление нескольких записей с отключением безопасного режима
SET sql_safe_updates = 0;
DELETE FROM Employees;

# очистка данных в таблице
TRUNCATE TABLE Employees;

# создание копии таблицыALTER

# обновление данных в таблице
UPDATE Employees
SET Salary = 65000
WHERE EmployeeID = 1;

UPDATE Employees
SET Salary = Salary * 1.1
WHERE YEAR(HireDate) >= '2024';