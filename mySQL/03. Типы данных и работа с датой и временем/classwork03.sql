-- Таблица: order_details. Задача: Выведите информацию о каждом заказе, включая идентификатор заказа (order_id), расчетную полную стоимость заказа после
-- применения скидки (net_price).
select order_id, unit_price, quantity, discount, round(unit_price * quantity * (1 - discount), 2) as net_price from northwind.order_details;

-- Преобразование типов CAST
select cast('123qwert4' as SIGNED);

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

SELECT id, transaction_created_date, day(transaction_created_date) 
FROM northwind.inventory_transactions
WHERE day(transaction_created_date) = 24;

-- Преобразование некорректной датыALTERselect cast("12.03.2025" as datetime);
select cast("2025-03-12" as datetime);
SELECT STR_TO_DATE('12.03.2025', '%d.%m.%Y');