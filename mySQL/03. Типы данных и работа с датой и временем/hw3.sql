-- 1. Выведите Ваш возраст на текущий день в секундах
SELECT 
    TIMESTAMPDIFF(
		SECOND,
        '2000-04-29 10:15:33',
        NOW()
	) as seconds_with_time, 
    TIMESTAMPDIFF(
		SECOND,
        '2000-04-29',
        NOW()
	) as seconds_without_time
;

-- 2. Выведите какая дата будет через 51 день
SELECT now() + INTERVAL 51 DAY;
SELECT current_date + INTERVAL 51 DAY;
SELECT DATE_ADD(NOW(), INTERVAL 51 DAY);
SELECT ADDDATE(NOW(), INTERVAL 51 DAY);
SELECT DATE_SUB(NOW(), INTERVAL -51 DAY);
 
-- 3. Отформатируйте предыдущей запрос - выведите день недели 
-- для этой даты 
-- Используйте документацию My SQL 
SELECT WEEKDAY(NOW() + INTERVAL 51 DAY) as weekday;
SELECT WEEKDAY(DATE_ADD(CURRENT_TIMESTAMP, INTERVAL 51 DAY));
SELECT dayofweek(DATE_ADD(NOW(), INTERVAL 51 DAY));
SELECT dayname(DATE_ADD(NOW(), INTERVAL 51 DAY));
-- SELECT day(DATE_ADD(CURRENT_TIMESTAMP, INTERVAL 51 DAY));
SELECT date_format(DATE_ADD(NOW(), INTERVAL 51 DAY), '%a');
SELECT date_format(DATE_ADD(NOW(), INTERVAL 51 DAY), '%W');
SELECT date_format(DATE_ADD(NOW(), INTERVAL 51 DAY), '%w');
-- SELECT date_format('%w', DATE_ADD(NOW(), INTERVAL 51 DAY));
-- SELECT date_format(DATE_ADD(NOW(), INTERVAL 51 DAY));
 
-- 4.  Подключитесь к базе данных northwind 
-- Выведите столбец с исходной датой создания транзакции 
-- transaction_created_date из таблицы inventory_transactions, а также столбец 
-- полученный прибавлением 3 часов к этой дате

SELECT 
    transaction_created_date,
    DATE_ADD(transaction_created_date, INTERVAL 3 HOUR) AS change_time,
    transaction_created_date + INTERVAL 3 HOUR AS change_time2
FROM
    northwind.inventory_transactions;
 
-- 5. Выведите столбец с текстом  'Клиент с id <customer_id> сделал заказ <order_date>' 
-- из таблицы orders
-- Запрос написать двумя способами - с использованием неявных преобразований 
-- а также с указанием изменения типа данных для столбца customer_id
-- Внимание В MySQL функция CAST не принимает VARCHAR в качестве параметра для длины. 
-- Вместо этого, нужно использовать CHAR для указания длины.
SELECT 
    customer_id, 
    order_date, 
    concat('Клиент с id ', customer_id, ' сделал заказ ', order_date) as info
FROM northwind.orders;

-- ---------------------------------------------------------------------------------

SELECT customer_id, order_date,
	CONCAT(
		'Клиент с id ', 
		CAST(customer_id AS CHAR), 
		' сделал заказ ', 
		CAST(order_date as CHAR)) 
	AS info
FROM northwind.orders;


