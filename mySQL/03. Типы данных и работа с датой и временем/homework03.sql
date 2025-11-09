-- 1. Выведите Ваш возраст на текущий день в секундах
SELECT 
    TIMESTAMPDIFF(SECOND,
        '1985-10-01 16:25:00',
        NOW()) AS age_seconds;

SELECT 
    TIMESTAMPDIFF(SECOND,
        CAST('1985-10-01' AS DATETIME),
        NOW()) AS age_in_seconds;

-- 2. Выведите какая дата будет через 51 день
SELECT DATE_ADD(NOW(), INTERVAL 51 DAY);

-- 3. Отформатируйте предыдущей запрос - выведите день недели для этой даты Используйте документацию My SQL
SELECT DATE_FORMAT(DATE_ADD(NOW(), INTERVAL 51 DAY), '%W');

-- 4.  Подключитесь к базе данных northwind Выведите столбец с исходной датой создания транзакции transaction_created_date из таблицы inventory_transactions, 
-- а также столбец полученный прибавлением 3 часов к этой дате
use northwind;
SELECT 
    transaction_created_date,
    DATE_ADD(transaction_created_date,
        INTERVAL 3 HOUR) AS plus_3_hours
FROM
    inventory_transactions;

-- 5. Выведите столбец с текстом  'Клиент с id <customer_id> сделал заказ <order_date>' из таблицы orders. Запрос написать двумя способами - с использованием 
-- неявных преобразований, а также с указанием изменения типа данных для столбца customer_id. Внимание В MySQL функция CAST не принимает VARCHAR в качестве 
-- параметра для длины. Вместо этого, нужно использовать CHAR для указания длины.
-- неявные преобразования
select customer_id, order_date, concat_ws(' ','Клиент с id', customer_id, 'сделал заказ', order_date) as final_text from northwind.orders;

-- явные преобразования
select customer_id, 
	order_date, 
    concat_ws(' ','Клиент с id', 
		cast(customer_id as char), 
        'сделал заказ', 
        cast(order_date as char)) as final_text 
from northwind.orders;

-- 6.  Отформатируйте стиль написания запросов

-- 7. Сохраните запросы в виде файла с расширением .sql и загрузите на платформу