-- CASE 
--     WHEN условие1 THEN результат1
--     WHEN условие2 THEN результат2
--     ...
--     ELSE результатN
-- END
SELECT * FROM hr.employees;

SELECT employee_id, first_name, last_name, salary,  
	CASE 
--   		WHEN salary < 20000 THEN "---------"
		WHEN salary < 5000 or job_id = 'SA_MAN' THEN "Low"
-- 		WHEN salary < 5000 and job_id = 'ST_CLERK' THEN "Low2"
		WHEN salary > 20000 THEN "High"
		WHEN salary between 10000 and 15000 THEN "Middle"
--  		ELSE "Not in borders"
	END as new_name, 
job_id as job, salary * 1.1
FROM hr.employees;

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

SELECT employee_id, first_name, last_name, salary, 
	CASE 
		WHEN salary < 5000 THEN salary * 1.5
		WHEN salary > 20000 THEN salary * 1.05
		WHEN salary between 10000 and 15000 THEN salary * 1.2
		ELSE salary END as new_name, 
		job_id
FROM hr.employees;


-- Составьте запрос чтобы: классифицировать товары таблицы products 
-- по их стоимости standard_cost, присваивая каждому из них категорию:

-- "Дорогой" от 50
-- "Средний" от 20 до 50 включая 50 
-- "Дешевый" до 20 включительно

select product_code, product_name, standard_cost,
case
	when standard_cost > 50 then "Дорогой"
    when standard_cost > 20 and standard_cost <= 50 then "Средний"
--    when standard_cost <= 20 then "Дешевый"
    else "Дешевый"
end as price_grades
from products;

-- SELECT IF(condition, true_result, false_result) AS new_column_name
-- FROM table_name;

select product_code, product_name, standard_cost,
if(standard_cost > 30, "Дорогой", null),
if(standard_cost > 50, "Дорогой", 
							if(standard_cost > 20 and standard_cost <= 50, "Средний", "Дешевый")) 
                            as price_grades_if,
case
	when standard_cost > 50 then "Дорогой"
    when standard_cost > 20 and standard_cost <= 50 then "Средний"
--    when standard_cost <= 20 then "Дешевый"
    else "Дешевый"
end as price_grades
from products;





SELECT 
  product_id as id,
  unit_price,
  quantity,
  unit_price * quantity AS total_price
FROM order_details;


-- ----------------------------------------------------------------
-- string

SELECT company, 
RIGHT(company, 2) AS ShortName, 
left(job_title, 5) AS ShortName,
SUBSTRING(business_phone, 6, 3) as `code`,
SUBSTR(business_phone, 6) as `code`,
business_phone, 
last_name, 
first_name, 
concat(last_name, " ", first_name) as full_name, 
concat(left(last_name, 3), " ", first_name) as part_full_name
FROM customers;

SELECT 
    CONCAT_WS(' - ', first_name, last_name, "!") AS full_name
FROM customers;

SELECT id, last_name, first_name, job_title, notes, coalesce(notes, job_title, "Not filled") 
FROM northwind.employees;

SELECT * FROM northwind.order_details;
SELECT *, coalesce(date_allocated, purchase_order_id, inventory_id) FROM northwind.order_details;

SELECT standard_cost, list_price, minimum_reorder_quantity, 
coalesce(minimum_reorder_quantity, list_price, standard_cost)
FROM northwind.products;

SELECT *, coalesce(date_allocated, purchase_order_id) FROM northwind.order_details;


SELECT product_name, REPLACE(product_name, 'Olive Oil', 'Oil') AS new_name FROM products;


-- ------------------------------------------------------------
-- part 2
SELECT * 
FROM northwind.products;

SELECT * 
FROM northwind.products
order by standard_cost desc, product_name;

SELECT * 
FROM northwind.products
order by category, standard_cost desc;

SELECT * 
FROM northwind.products
where standard_cost > 8
order by target_level, standard_cost desc, product_name desc;


SELECT * 
FROM northwind.products
where standard_cost > 8
order by standard_cost desc, product_name desc
limit 3;

SELECT *, 
case
	when standard_cost > 50 then "Дорогой"
    when standard_cost > 20 and standard_cost <= 50 then "Средний"
    else "Дешевый"
end as price_grades 
FROM northwind.products
where standard_cost > 8
order by standard_cost desc, product_name desc
limit 10;

SELECT * 
FROM northwind.products
where standard_cost > 8
order by standard_cost desc, product_name desc
limit 3 offset 5;


-- ------------------------------------------------
-- distinct

SELECT * FROM northwind.customers;

SELECT city 
FROM northwind.customers
order by city;

SELECT distinct city 
FROM northwind.customers;

SELECT distinct * 
FROM northwind.customers;


SELECT job_title, city 
FROM northwind.customers;

SELECT distinct job_title, city 
FROM northwind.customers;