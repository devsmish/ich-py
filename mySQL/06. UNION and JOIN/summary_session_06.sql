-- 1 Выведите одним запросом с использованием UNION столбцы id, employee_id из таблицы orders и соответствующие им столбцы из таблицы purchase_orders
-- В таблице purchase_orders created_by соответствует employee_id

SELECT id, employee_id as new_name FROM orders
UNION ALL
SELECT id, created_by FROM purchase_orders;


-- 2 Из предыдущего запроса удалите записи там где employee_id не имеет значения 
-- Добавьте дополнительный столбец со сведениями из какой таблицы была взята запись

SELECT id, employee_id, 'orders' as `table`
FROM orders
WHERE employee_id IS NOT NULL
UNION ALL
SELECT id, created_by, 'purchase orders' as `table`
FROM purchase_orders;
-- WHERE created_by IS NOT NULL;

-- 3 Выведите все столбцы таблицы order_details 
-- а также дополнительный столбец payment_method из таблицы purchase_orders 
-- Оставьте только заказы для которых известен payment_method 

SELECT order_details.*, payment_method
FROM northwind.order_details
inner join northwind.purchase_orders
on order_details.purchase_order_id = purchase_orders.id
where payment_method is not null;
-- -----

SELECT o.*, payment_method 
FROM order_details as o 
JOIN purchase_orders as po
ON o.purchase_order_id = po.id
where payment_method IS NOT NULL;

-- 4 Выведите заказы orders и фамилии клиентов customers для тех заказов по которым были инвойсы таблица invoices

SELECT o.*, c.last_name
FROM invoices AS i
LEFT JOIN orders AS o 
ON i.order_id = o.id 
LEFT JOIN customers AS c 
ON o.customer_id = c.id;

-- 5 Подсчитайте количество инвойсов для каждого клиента из предыдущего запроса
SELECT customer_id, concat(last_name, ' ', first_name) as full_name, count(invoice_date) as count
FROM invoices AS i
LEFT JOIN orders AS o 
ON i.order_id = o.id 
LEFT JOIN customers AS c 
ON o.customer_id = c.id
group by customer_id;

-- ленивый CROSS JOIN
SELECT * FROM purchase_order_status, inventory_transaction_types;

-- HR. Посчитать сколько сотрудников работают в каждом из городов, в том числе города без сотрудников
USE hr;
SELECT loc.city, count(emp.employee_id) FROM locations as loc
LEFT JOIN departments as dep
ON loc.location_id = dep.location_id
LEFT JOIN employees as emp
ON dep.department_id = emp.department_id
GROUP BY loc.city;
