-- 1. Создайте таблицу products со следующими столбцами и ограничениями:
-- ● product_id — тип INT, автоинкремент, первичный ключ.
-- ● product_name — тип VARCHAR100, не может быть пустым.
-- ● category — тип VARCHAR50, значение по умолчанию — 'General'.
-- ● price — тип DECIMAL8, 2, не может быть отрицательным, добавьте ограничение CHECK (price >= 0.
-- ● stock_quantity — тип INT, не может быть отрицательным.
-- ● supplier_id — тип INT, может быть NULL, указывает на поставщика продукта.
-- 2. Заполните таблицу products 5 строками данных.
-- 3. Измените значение в таблице, например, уменьшите количество на складе для продукта с product_id = 1
USE 101025_SerhiiM;
CREATE TABLE products (
	product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) DEFAULT ('General'),
    price DECIMAL(8, 2) CHECK (price >= 0),
    stock_quantity INT CHECK (stock_quantity >= 0),
    supplier_id INT
);

INSERT INTO products
	(product_name, category, price, stock_quantity, supplier_id)
VALUES
	('MacBook Pro 2019', 'Laptop', 1600.00, 7, 2212 ),
	('Samsung A53', 'Mobile', 799.99, 10, 25),
	('MicroTik PF20', 'Router', 123.02, 0, 160),
	('Dell C200', 'Monitor', 380.90, 25, 1141),
	('HP X3000', 'Mouse', 10.50, 160, 529);

SELECT * FROM products; 
    
UPDATE products
SET stock_quantity = 5
WHERE product_id = 1;

-- Добавим ко всем ценам 15%
SET sql_safe_updates = 0;
UPDATE products
SET price = round(price * 1.15, 2);
SET sql_safe_updates = 1;

/* 4. Создайте представление product_overview, которое будет содержать следующие данные:
● product_name — название продукта.
● category — категория продукта.
● stock_value — расчетная стоимость запасов (произведение price и stock_quantity).
● stock_status — строка "Low Stock", если stock_quantity меньше 20, и "In Stock" в противном случае.*/
CREATE VIEW product_overview AS
SELECT 
	product_name, 
	category, 
    price * stock_quantity AS stock_value, 
    IF (stock_quantity < 20, 'Low Stock', 'In Stock') AS stock_status 
FROM products;

-- 5. Вам необходима таблица с данными о мониторинге основных показателей здоровья. Подумайте какие столбцы и с какими ограничениями вы 
-- будете использовать. Создайте такую таблицу и заполните ее тремя тестовыми строками. Обсудите результаты с коллегами.
CREATE TABLE health_indicators (
	id INT PRIMARY KEY AUTO_INCREMENT,
    date_fix DATE NOT NULL,
    height INT CHECK(height > 0),
    weight DECIMAL(5, 2) CHECK(weight > 0),
    age INT CHECK(age > 0),
    pulse INT CHECK(pulse > 0),
    blood_pressure VARCHAR(7),
    body_temperature DECIMAL (4, 1) CHECK(body_temperature > 34 AND body_temperature < 43),
    patient_id INT
);
SET sql_safe_updates = 0;
INSERT INTO health_indicators(date_fix, height, weight, age, pulse, blood_pressure, body_temperature, patient_id)
VALUES 
	('2025-11-16', 187 , 102.4, 52, 110, '140/90', 36.6, 1234),
    ('2025-11-16', 179, 90, 40, 97, '120/80', 36.7, 7 ),
    ('2025-11-17', 160, 79, 25, 115, '150/100', 38.0, 9016);
SET sql_safe_updates = 1;