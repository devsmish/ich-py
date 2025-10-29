-- SELECT 'Good morning';
# SELECT 'Good';

-- USE northwind;
-- select * from customers;
-- SELECT * FROM northwind.customers;

-- SELECT `first_name`, `last_name`
-- FROM customers;

show columns from orders;

SELECT * FROM northwind.products;

SELECT * 
FROM northwind.products
where standard_cost > 20 and list_price < 80;

-- Выбрать сотрудников, живущих в городах, 
-- названия которых заканчиваются на ‘mond’.
select * from employees;
select * from employees
where city like "%mond%";
select * from employees
where first_name like "A%";


-- Выбрать все строки, в которых shipping_fee больше либо равен 10 
-- и меньше либо равен 15.
SELECT * FROM northwind.orders where shipping_fee between 10 and 12;
-- Выбрать ship_name только для городов отгрузки ship_city Chicago и Miami.
SELECT * FROM northwind.orders where ship_city in ('Chicago', 'Miami');

select * from orders where shipped_date is null;

-- -------------------------------------------

SELECT * FROM products;

SELECT product_name, standard_cost, list_price FROM products;

SELECT product_name, standard_cost, list_price, list_price - standard_cost FROM products;

SELECT product_name, (list_price - standard_cost) * 2 as new_name FROM products;



SELECT product_name, standard_cost, list_price, list_price - standard_cost FROM products
where list_price - standard_cost < 5;

SELECT product_name, standard_cost, list_price FROM products
where list_price - standard_cost < 5;

-- Выбрать все строки из таблицы products где reorder_level в два раза меньше target_level.

SELECT * FROM northwind.products;