-- 1. Выведите текущую дату и время:
select now();
-- 2. Выведите день недели, когда был сделан каждый заказ из таблицы orders
select order_date, date_format(order_date, '%W') as day_name from northwind.orders;

select order_date, dayname(order_date) from northwind.orders;

-- 3. Добавьте 30 дней к дате каждого заказа в таблице orders и выведите результат
select order_date, date_add(order_date, interval 30 day) from northwind.orders;

select order_date, adddate(order_date, interval 30 day) from northwind.orders;

select order_date, order_date + INTERVAL 30 DAY from northwind.orders;

-- 4. Выведите количество дней между датой заказа и датой доставки для каждого заказа из таблицы orders
SELECT order_date, shipped_date, datediff(shipped_date, order_date) as diff_date from northwind.orders;

SELECT order_date, shipped_date, TIMESTAMPDIFF(DAY, order_date, shipped_date) as diff_date from northwind.orders;

-- 5. Найдите все заказы, сделанные в пятницу из таблицы orders
SELECT * FROM northwind.orders
WHERE weekday(order_date) = 6;

SELECT * FROM northwind.orders
where date_format(order_date, '%W') = 'Friday';

-- 6. Выведите дату, которая будет через 100 дней от текущей:
SELECT now(), date_add(now(), interval 100 day);

SELECT CURRENT_DATE,
	DATE_ADD(CURRENT_DATE, INTERVAL 100 DAY);

-- 7. Выведите заказы, сделанные в выходные дни (суббота и воскресенье) из таблицы orders
SELECT * FROM northwind.orders
WHERE weekday(order_date) in (1, 7);

SELECT * FROM northwind.orders
WHERE date_format(order_date, '%W') in ('Saturday', 'Sunday');

-- 8. Найдите количество дней до конца текущего года
SELECT DATEDIFF('2025-12-31', now()) as rest_day;

select DATEDIFF(concat(YEAR(now()),'-12-31'), now()) as rest_days;

-- 9. Выведите дату, которая была 15 дней назад от текущей даты
SELECT NOW() - INTERVAL 15 DAY;

SELECT DATE_SUB(NOW(), INTERVAL 15 DAY), DATE_SUB(CURRENT_DATE(), INTERVAL 15 DAY);

SELECT ADDDATE(NOW(), INTERVAL -15 DAY);

-- 10. Примените явное преобразование Выведите столбец id из таблицы customers в виде строки
select id, cast(id as CHAR) as str_id from northwind.customers;

-- Задание 3. Найдите разницу в днях между датой заказа order_date и датой отправки shipped_date для всех заказов в таблице orders.
SELECT order_date, shipped_date, datediff(shipped_date, order_date) as diff_date from northwind.orders;

-- Задание 4. Найдите дату, которая была 90 дней до текущей даты.
SELECT NOW() - INTERVAL 90 DAY;

-- Задание 5. Использование скрытых преобразований. Сложите строку, содержащую дату, с числом и выведите результат. Объедините числовое значение с текстом и
-- выведите результат в виде строки.
select now(), cast(now() as char) + 7;
select cast(123 + 'abc' as char);

-- Задание 6. Извлеките год из даты получения заказа order_date.
select order_date, year(order_date) from northwind.orders;

-- Задание 7. Преобразуйте текстовое значение, представляющее дату, в формат DATE.
SELECT CAST('2025-11-06' as DATE) as correct_date;

SELECT STR_TO_DATE('06/11/2025', '%d/%m/%Y') AS date_str_to_date;