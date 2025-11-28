-- 1. Выведите одним запросом с использованием UNION столбцы id, employee_id из таблицы orders и соответствующие им столбцы из таблицы purchase_orders. В 
-- таблице purchase_orders created_by соответствует employee_id.
select id, employee_id from orders
UNION
select id, created_by from purchase_orders;

-- 2. Из предыдущего запроса удалите записи там, где employee_id не имеет значения. Добавьте дополнительный столбец со сведениями из какой таблицы была взята запись.
select id, employee_id, 'orders' as `name_table` from orders
WHERE employee_id IS NOT NULL
UNION
select id, created_by, 'purchase_orders' as `name_table` from purchase_orders;

-- 3. Выведите все столбцы таблицы order_details, а также дополнительный столбец payment_method из таблицы purchase_orders. Оставьте только заказы, для которых 
-- известен payment_method.
USE northwind;
SELECT *, po.payment_method FROM order_details as od
LEFT JOIN purchase_orders as po
ON od.purchase_order_id = po.id
WHERE po.payment_method is not null;

-- 4. Выведите заказы orders и фамилии клиентов customers для тех заказов, по которым были инвойсы таблица invoices.
SELECT orders.id, customers.last_name, invoices.invoice_date from orders
LEFT JOIN customers
ON orders.customer_id = customers.id
RIGHT JOIN invoices
ON orders.id = invoices.order_id
WHERE invoices.order_id IS NOT NULL; -- в таблице инвойсов нет пустых значений, поэтому это условие можно было и не добавлять

-- 5. Подсчитайте количество инвойсов для каждого клиента из предыдущего запроса.
SELECT customers.id, customers.last_name, customers.first_name, COUNT(invoices.invoice_date) as count_inv from orders
LEFT JOIN customers
ON orders.customer_id = customers.id
RIGHT JOIN invoices
ON orders.id = invoices.order_id
WHERE invoices.order_id IS NOT NULL
GROUP BY customers.id, customers.last_name;