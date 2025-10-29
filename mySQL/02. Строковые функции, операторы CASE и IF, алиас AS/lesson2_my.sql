SELECT 
	employee_id, first_name, last_name, salary, 
	CASE 
		WHEN salary < 5000 THEN "Low" 
		WHEN salary > 20000 THEN "High" 
		WHEN salary between 10000 and 15000 THEN "Middle" 
		ELSE "Not in borders" 
	END as new_name, 
	job_id
FROM hr.employees;

# Составьте запрос чтобы: классифицировать товары таблицы products по их стоимости standard_cost, присваивая каждому из них категорию:
# "Дорогой" от 50
# "Средний" от 20 до 50 включая 50 
# "Дешевый" до 20 включительно
SELECT * ,
	CASE 
		WHEN standard_cost > 50 THEN 'Дорогой'
		WHEN 20 < standard_cost <= 50 THEN 'Средний'
        WHEN standard_cost <= 20 THEN 'Дешевый'
			ELSE null
            END as View
FROM northwind.products;

-- Составьте запрос чтобы: вывести имя продукта из таблицы products и его категорию.
-- standard_cost > 20 - 'Expensive'. 
-- В обратном случае - 'Affordable' с применением оператора IF.
SELECT product_name, standard_cost, 
	IF(standard_cost > 20,'Expensive','Affordable') 
    FROM northwind.products;
    
-- 
SELECT product_name, standard_cost, 
	IF(standard_cost > 50,'Expensive', 
		IF(standard_cost < 20, "Cheap", 'Affordable')) as type_cost
FROM northwind.products;

--
SELECT 
	company,
	RIGHT (company, 2) AS ShortName
FROM customers;

SELECT 
business_phone , SUBSTRING(business_phone, 6, 3)
FROM customers;

SELECT 
product_name , SUBSTRING(product_name, 19)
FROM products;

SELECT * FROM employees;
SELECT last_name AS LN, first_name AS FN, concat(last_name, " ", first_name) AS full_name FROM employees;
SELECT 
	last_name, first_name, 
	concat(last_name, " - ", first_name, " - ", email_address) AS full_name 
FROM employees;
SELECT 
	last_name, first_name, 
	concat_ws(" - ", last_name, first_name, email_address) AS full_name 
FROM employees;

--
SELECT product_name, LENGTH(product_name) AS name_length FROM products;

SELECT product_name, REPLACE(product_name, 'Olive Oil', 'Oil') AS new_name FROM products;

SELECT UPPER('sql функции'), 'hello';

SELECT product_name, UPPER(product_name) AS new_name FROM products;