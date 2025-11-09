-- Таблица: order_details. Задача: Выведите информацию о каждом заказе, включая идентификатор заказа (order_id), расчетную полную стоимость заказа после
-- применения скидки (net_price).
select order_id, unit_price, quantity, discount, round(unit_price * quantity * (1 - discount), 2) as net_price from northwind.order_details;

-- Таблица: customers. Задача: Выведите полный адрес каждого клиента, объединяя адрес (address), город (city) и страну (country_region) в одну строку.
SELECT id, CONCAT(address, ', ', city, ',', country_region) AS full_address FROM customers;

-- Таблица: employees. Задача: Выведите информацию о каждом сотруднике, включая идентификатор сотрудника (id), имя (first_name), фамилию (last_name) и
-- роль (role), где роль определяется на основе значения поля is_manager (если значение 1, то "Manager", иначе "Employee")
SELECT id, first_name, last_name, 
	CASE
		WHEN is_manager = 1 THEN 'Manager'
        ELSE 'Employee'
	END AS role
FROM employees;

-- Преобразование типов CAST
select cast('123qwert4' as SIGNED);

-- Ситуация: У вас есть числовые данные, которые хранятся в текстовом формате. Например, количество товаров на складе. Проблема: Вы хотите рассчитать 
-- общую стоимость товаров на складе. Если количество товаров хранится как текст, вы не сможете сделать расчет.
SELECT product_name, CAST(unit_in_stock AS SIGNED) * list_price AS total_value FROM products;

-- Создать отчет, который показывает количество и цену продуктов в текстовом формате, чтобы представить информацию в более понятном виде для конечных 
-- пользователей. Количество и цена хранятся в числовом формате, но для отчетов вы хотите объединить эти данные в строку, которая будет легко читаться.
SELECT 
product_name, 
unit_in_stock, 
CONCAT(
'Available: ',
CAST(unit_in_stock AS CHAR), 
' units, Price: $', 
CAST(list_price AS CHAR)) 
AS product_report 
FROM products;

SELECT 
product_name, 
unit_in_stock, 
CONCAT(
'Available: ',
unit_in_stock, 
' units, Price: $', 
list_price) 
AS product_report 
FROM products;

SELECT "123num" + 10;

SELECT "234" * "10";

-- Date and Time
SELECT NOW() AS
CurrentDateTime;

SELECT CURDATE() AS
CurrentDate;

SELECT CURTIME() AS
CurrentTime;

SELECT NOW(), DATE_FORMAT(NOW(), '%d-%m-%Y %H:%i') AS
FormattedDateTime;

SELECT DATEDIFF ('2024-08-30','2024-08-25') AS DaysDifference;

SELECT DATE_ADD(NOW(), INTERVAL 10 DAY) AS FutureDate;
SELECT DATE_ADD(NOW(), INTERVAL -10 DAY) AS FutureDate;
SELECT DATE_SUB(NOW(), INTERVAL 10 DAY) AS PastDate;

SELECT EXTRACT(day FROM NOW()) AS CurrentYear;

-- Выведите дату получения заказа order_date из таблицы orders в формате ДД-ММ-ГГГГ.
SELECT id,
 DATE_FORMAT(order_date, '%d-%m-%Y')
AS formatted_order_date
FROM orders;

-- Выведите дату и время отправки заказа shipped_date из таблицы orders в формате ДД/ММ/ГГГГ ЧЧ:ММ:СС.
SELECT id,
	DATE_FORMAT(shipped_date, '%d/%m/%Y %H:%i:%s') AS formatted_shipped_date
FROM orders;

-- Найдите разницу в днях между датой заказа order_date и датой отправки shipped_date для всех заказов в таблице orders.
SELECT id,
	DATEDIFF(shipped_date, order_date)
	AS days_to_ship
FROM orders;

-- Найдите дату, которая была 90 дней до текущей даты.
SELECT DATE_SUB(CURDATE(), INTERVAL 90 DAY) AS PastDate;

-- Использование скрытых преобразований. Сложите строку, содержащую дату, с числом и выведите результат. Объедините числовое значение с текстом и
-- выведите результат в виде строки.
SELECT '2024-08-25' + 5 AS Result;

SELECT CONCAT('Total sales: $', 12345.67) AS SalesReport;

-- Извлеките год из даты получения заказа order_date.
SELECT id, YEAR(order_date) AS order_year FROM orders;

-- Преобразуйте текстовое значение, представляющее дату, в формат DATE.
SELECT CAST('2024-08-25' AS DATE) AS ConvertedDate;

SELECT id, transaction_created_date, day(transaction_created_date) 
FROM northwind.inventory_transactions
WHERE day(transaction_created_date) = 24;

-- Преобразование некорректной даты ALTERselect cast("12.03.2025" as datetime);
select cast("2025-03-12" as datetime);
SELECT STR_TO_DATE('12.03.2025', '%d.%m.%Y');