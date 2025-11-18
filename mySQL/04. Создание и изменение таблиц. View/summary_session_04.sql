CREATE TABLE supplier (
    id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_name VARCHAR(255) NOT NULL,
    contact_name VARCHAR(255),
    phone VARCHAR(20),
    email VARCHAR(255),
    created_at DATETIME DEFAULT NOW()
);

INSERT INTO supplier (supplier_name, contact_name, phone, email)
VALUES
('FreshFood Ltd.', 'Anna Petrova', '+995555123456', 'anna@freshfood.com'),
('TechImport LLC', 'Sergey Ivanov', '+79215552211', 'sergey@techimport.com'),
('GlobalTrade Co', 'John Smith', '+12023331900', 'john@globaltrade.com'),
('MedSupply Group', 'Elena Volkova', '+74951234567', 'elena@medsupply.com'),
('OfficePlus', 'Dmitry Orlov', '+375292221122', 'd.orlov@officeplus.by');

/*1. Создайте таблицу products со следующими столбцами и ограничениями:
● product_id — тип INT, автоинкремент, первичный ключ.
● product_name — тип VARCHAR100, не может быть пустым.
● category — тип VARCHAR50, значение по умолчанию — 'General'.
● price — тип DECIMAL8, 2, не может быть отрицательным, добавьте ограничение CHECK (price >= 0.
● stock_quantity — тип INT, не может быть отрицательным.
● supplier_id — тип INT, может быть NULL, указывает на поставщика продукта.*/
CREATE TABLE `products` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `product_name` varchar(100) NOT NULL,
  `category` varchar(50) DEFAULT ('General'),
  `price` decimal(8,2) CHECK (`price` >= 0),
  `stock_quantity` int CHECK (`stock_quantity` >= 0),
  `supplier_id` int,
  FOREIGN KEY (supplier_id) REFERENCES supplier(id)
);

-- not valid
INSERT INTO products (product_name, category, price, stock_quantity, supplier_id)
VALUES
('Apples Golden', 'Fruits', 3.50, 120, 100);

-- 2. Заполните таблицу products 5 строками данных.
INSERT INTO products (product_name, category, price, stock_quantity, supplier_id)
VALUES
('Apples Golden', 'Fruits', 3.50, 120, 1),
('Laptop Sleeve 15"', 'Accessories', 19.99, 40, 2),
('USB-C Cable 1m', 'Electronics', 7.49, 200, 2),
('Vitamin C 500mg', 'Medicine', 12.30, 85, 4),
('Office Paper A4 80g', 'Office', 4.20, 500, 5),
('Orange Juice 1L', 'Beverages', 2.80, 150, 1),
('Wireless Mouse', 'Electronics', 14.99, 60, 2),
('Hand Sanitizer 250ml', 'Hygiene', 3.99, 70, 4);

-- 3. Измените значение в таблице, например, уменьшите количество на складе для продукта с product_id = 1
UPDATE products
SET stock_quantity = stock_quantity + 2
WHERE product_id = 1;

/* 4. Создайте представление product_overview, которое будет содержать следующие данные:
● product_name — название продукта.
● category — категория продукта.
● stock_value — расчетная стоимость запасов (произведение price и stock_quantity).
● stock_status — строка "Low Stock", если stock_quantity меньше 20, и "In Stock" в противном случае.*/

CREATE ALGORITHM=UNDEFINED DEFINER=`ich1`@`%` SQL SECURITY DEFINER VIEW `product_overview` AS 
select `products`.`product_name` AS `product_name`,
	   `products`.`category` AS `category`,
       (`products`.`price` * `products`.`stock_quantity`) AS `stock_value`,
       if((`products`.`stock_quantity` < 20),'Low Stock','In Stock') AS `stock_status` 
from `products`

-- not valid
DELETE FROM supplier WHERE id = 4;
-- valid
DELETE FROM supplier WHERE id = 3;


CREATE TABLE supplier_products (
    supplier_id INT NOT NULL,
    product_id INT NOT NULL,
    supply_price DECIMAL(8,2) NOT NULL CHECK (supply_price >= 0),

    PRIMARY KEY (supplier_id, product_id),

    FOREIGN KEY (supplier_id) REFERENCES supplier(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);