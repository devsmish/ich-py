SELECT * FROM hr.employees;

SELECT COUNT(commission_pct) FROM hr.employees;
-- SELECT employee_id, COUNT(commission_pct) FROM hr.employees;  -- without employee_id
-- SELECT salary, COUNT(commission_pct) FROM hr.employees  -- without salary
-- WHERE salary > 10000;

SELECT COUNT(*), COUNT(employee_id) FROM hr.employees
WHERE year(hire_date) >= 2020;

SELECT SUM(salary) as sum_salary FROM hr.employees
WHERE department_id = 30;  --  AND sum_salary > 20000

SELECT 
	AVG(commission_pct) as avg_c, 
	SUM(commission_pct) / COUNT(commission_pct) as avg_c2 
FROM hr.employees;

SELECT 
	AVG(commission_pct) as avg_c, 
	SUM(commission_pct) / COUNT(*) as avg_c2 
FROM hr.employees;

SELECT MIN(salary) as min_salary, MAX(salary) as max_salary FROM hr.employees;

-- SELECT MIN(salary) as min_salary, MAX(salary) as max_salary FROM hr.employees  --not working
-- where salary > MIN(salary) * 1.1;

SELECT COUNT(DISTINCT job_id), COUNT(job_id) AS unique_job_id
FROM employees;

SELECT GROUP_CONCAT(DISTINCT job_id SEPARATOR ", "), GROUP_CONCAT(job_id) AS unique_jobs
FROM employees
WHERE year(hire_date) >= 2020;

-- Найдите общее количество товаров quantity в таблице order_details.
SELECT SUM(quantity) as sum_quantity FROM order_details;

-- Посчитайте количество уникальных order_id в таблице order_details.
SELECT COUNT(DISTINCT order_id) as count_uni_order FROM order_details;

SELECT GROUP_CONCAT(first_name) FROM employees;

SELECT * FROM northwind.order_details;

SELECT COUNT(distinct order_id) AS Counter FROM order_details;
-- counter = 40
-- data_ids = [30, 31, 32, ...];

SELECT distinct COUNT(order_id) AS Counter FROM order_details; -- Not correct
-- counter = 58

SELECT distinct order_id FROM order_details;

-- Перечислите через запятую и пробел имена всех сотрудников из таблицы employees.
SELECT GROUP_CONCAT(first_name, " ", last_name SEPARATOR ", ") as names_emp FROM northwind.employees;

SELECT * FROM hr.employees;

SELECT AVG(salary) FROM hr.employees;

SELECT department_id, AVG(salary) FROM hr.employees
GROUP BY department_id;

SELECT department_id, job_id, AVG(salary) FROM hr.employees
GROUP BY department_id, job_id;

SELECT job_id, AVG(salary) FROM hr.employees
GROUP BY job_id;

SELECT job_id FROM hr.employees
GROUP BY job_id;

-- 1. Из таблицы employees посчитать количество сотрудников в каждом городе city.
SELECT city, count(*)  as count_employees FROM employees
GROUP BY city;

-- 2. Отсортировать результаты по убыванию.
SELECT city, count(*)  as count_employees FROM employees
GROUP BY city
ORDER BY count_employees DESC;

-- 3. Посчитать общее количество продуктов из таблицы order_details для каждого заказа.
SELECT order_id, SUM(quantity) as order_products  FROM order_details
GROUP BY order_id;

-- 4. Отсортировать по убыванию общего количества продуктов. Для краткости записи в GROUP BY можно не указывать конкретное имя колонки, а указать 
-- ее порядковый номер в SELECT.
SELECT order_id, SUM(quantity) as order_products  FROM order_details
GROUP BY 1
ORDER BY order_products DESC;

-- 5. Сделать то же самое в ORDER BY.
SELECT order_id, SUM(quantity) as order_products  FROM order_details
GROUP BY 1
ORDER BY 2 DESC;

-- 6. Посчитать сколько сотрудников работает в каждой компании из таблицы customers. Учитывать только тех сотрудников, у которых job_id 
-- равен 'Purchasing Manager'.
SELECT * FROM northwind.customers;

SELECT COUNT(*) FROM northwind.customers
WHERE job_title = 'Purchasing Manager' ;

-- 7. Если столбец, который вы хотите использовать для группировки содержит только уникальные неповторяющиеся значения, то в группировке нет 
-- смысла - любая агрегатная функция даст один и тот же результат. Попробуйте сгруппировать любую таблицу по первичному ключу и применить агрегатные
-- функции к столбцам.
SELECT department_id, AVG(salary) FROM hr.employees
GROUP BY department_id;

SELECT employee_id, salary, AVG(salary) FROM hr.employees
GROUP BY employee_id;

-- 8. Посчитать количество сотрудников в разрезе компании и занимаемой должности из таблицы employees.
SELECT company, job_title, COUNT(*) as count_empl FROM employees
GROUP BY company, job_title;

--------------------------------------------------------------------------------------------------------
-- HAVING
SELECT department_id, AVG(salary) FROM hr.employees
GROUP BY department_id;

SELECT department_id, AVG(salary) AS avg_sal FROM hr.employees
GROUP BY department_id
HAVING avg_sal < 8000;

SELECT department_id FROM hr.employees
GROUP BY department_id
HAVING AVG(salary) < 8000;

SELECT department_id, AVG(salary) AS avg_sal FROM hr.employees
WHERE year(hire_date) > 2020
GROUP BY department_id
HAVING avg_sal < 8000;

SELECT department_id, AVG(salary) AS avg_sal FROM hr.employees
WHERE year(hire_date) > 2020
GROUP BY department_id
HAVING avg_sal < 8000
ORDER BY avg_sal ASC, department_id ASC;

-- Выбрать supplier_ids для тех поставщиков, у которых количество продуктов больше 2. Используем таблицу products
SELECT supplier_ids, COUNT(DISTINCT product_name) AS count_prod FROM products
GROUP BY supplier_ids
HAVING count_prod > 2;

-- Вы можете использовать несколько условий в HAVING. Сгруппировать продукты по standard_cost и list_price Посчитать количество продуктов и вывести только 
-- те данные, где количество продуктов не менее 2
SELECT standard_cost, list_price,
count(product_name)
FROM products
GROUP BY 1,2
HAVING count(product_name) > 1;

-- Часто HAVING и WHERE используются вместе, чтобы максимально сузить набор данных перед тем, как применять агрегатные функции и группировку. Выбрать 
-- только те продукты в quantity_per_unit встречается слово 'oz' как в нижнем так и в верхнем регистрах Сгруппировать по standard_cost. Оставить только 
-- данные где количество продуктов не менее 3
SELECT standard_cost, COUNT(product_name)
FROM products
WHERE lower(quantity_per_unit) LIKE '%oz%'
GROUP BY 1
HAVING COUNT(product_name) > 2;