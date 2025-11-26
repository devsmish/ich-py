-- UNION

-- 1. Выведите в одну общую выборку из таблиц customers и employees имена и фамилии клиентов и сотрудников.
USE northwind;
SELECT first_name, last_name from employees
UNION ALL
SELECT first_name, last_name from customers;

-- 2. Добавьте дополнительный столбец в котором будет значение employee для сотрудника и customer для клиента.
USE northwind;
SELECT first_name, last_name, ‘employee’ as status from employees
UNION ALL
SELECT first_name, last_name, ‘customer’ as status from customers;

-- JOIN

-- 1. Выведите все строки из объединенных таблиц employees и employee_privileges с помощью INNER/RIGHT и LEFT JOIN. Объясните полученные результаты.
SELECT *
from employees as e
JOIN employee_privileges as ep;
SELECT *
from employees as e
LEFT JOIN employee_privileges as ep;
SELECT *
from employees as e
RIGHT JOIN employee_privileges as ep;

-- 2. Выведите идентификаторы заказов из таблицы order_details. Дополнительно выведите вместо product_id столбец с именем продукта product_name из products.
SELECT order_id, product_name
from order_details as od
JOIN products as p
ON od.product_id = p.id;

-- 3. Используя предыдущий запрос, посчитайте количество заказов для каждого наименования продукта.
SELECT product_name, COUNT(order_id)
from order_details as od
JOIN products as p
ON od.product_id = p.id
GROUP BY product_name;

-- 4. Выведите идентификаторы заказов из таблицы order_details. Дополнительно выведите вместо product_id столбец с именем продукта product_name из products и 
-- столбец payment_amount из таблицы purchase_orders.
SELECT product_name, order_id, po.payment_amount
from order_details as od
LEFT JOIN products as p
ON od.product_id = p.id;
LEFT JOIN purchase_orders po
ON od.purchase_order_id = po.id

-- 5. Оставить все строки из таблицы order_details.
SELECT *
from order_details as od
LEFT JOIN products as p
ON od.product_id = p.id
LEFT JOIN purchase_orders po
ON od.purchase_order_id = po.id