-- 1. Объедините с помощью UNION ALL названия компаний сотрудников из таблицы employees, названия компаний клиентов из таблицы customers и названия компаний 
-- для поставщиков из таблицы suppliers.
select company, 'employees' as `Entity` FROM employees
UNION ALL
select company, 'customers' as `Entity` from customers
UNION ALL
select company, 'suppliers' as `Entity` from suppliers;

-- 2. Объясните почему в предыдущем запросе не стоит использовать UNION ALL.Добавьте к предыдущему запросу столбец, показывающий из какой таблицы была взята 
-- запись.
select company, 'employees' as `Entity` FROM employees
UNION
select company, 'customers' as `Entity` from customers
UNION
select company, 'suppliers' as `Entity` from suppliers;

-- 3. У каких сотрудников в таблице employees нет привилегий таблица employee_privileges. Выведите имя и фамилию.
SELECT emp.first_name, emp.last_name,  ep.privilege_id 
FROM employees AS emp
LEFT JOIN employee_privileges AS ep
ON emp.id = ep.employee_id
WHERE ep.privilege_id IS NULL;

-- 4. Работаем с таблицей inventory_transactions. Выведите transaction_created_date, а также название типа транзакции и название продукта.
SELECT it.transaction_created_date, itt.type_name, pr.product_name FROM inventory_transactions as it
LEFT JOIN inventory_transaction_types as itt
ON it.transaction_type = itt.id
LEFT JOIN products as pr
ON it.product_id = pr.id; 

-- 5. Используя предыдущий запрос, посчитайте количество транзакций по типу. Оставьте только те типы транзакций, в которых отсутствует слово 'Sold'.
SELECT itt.type_name, count(itt.type_name) FROM inventory_transactions as it
LEFT JOIN inventory_transaction_types as itt
ON it.transaction_type = itt.id
WHERE itt.type_name not like '%Sold%'
GROUP BY itt.type_name;

-- 6. В таблице orders расшифруйте значения всех столбцов, в именах которых присутствует 'id' и для которых в базе данных имеются соответствующие таблицы. 
-- Выведите все строки, в которых ship_city Seattle. Объясните почему в данном случае важно использовать LEFT JOIN.
SELECT 
	orders.id as order_id,
    concat_ws(' ', emp.last_name, emp.first_name) as employee_name,
    concat_ws(' ', cust.last_name, cust.first_name) as customer_name,
    order_date, 
    ship.company as shipper_name, 
    ship_city, 
    ots.tax_status_name as tax_name, 
    os.status_name
FROM orders
LEFT JOIN employees as emp
ON employee_id = emp.id
LEFT JOIN customers as cust
ON customer_id = cust.id
LEFT JOIN shippers as ship
ON shipper_id = ship.id
LEFT JOIN orders_tax_status as ots
ON tax_status_id = ots.id
LEFT JOIN orders_status as os
ON status_id = os.id
WHERE ship_city = 'Seattle';