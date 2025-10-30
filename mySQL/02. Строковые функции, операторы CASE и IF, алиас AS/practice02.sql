# 1. Из таблицы inventory_transactions вывести столбец quantity, а также рассчитанный на его основе столбец category, который принимает 
# значения 'Almost finish', если quantity меньше 20 и 'Enought', если quantity больше либо равно 20. Решить задачу с помощью IF и CASE.
# variant CASE
select quantity,
	case 
		when quantity < 20 then 'Almost finish'
        else 'Enought'
	end as category
from inventory_transactions;

# Variant IF
select quantity, if (quantity < 20, 'Almost finish', 'Enought') as category
from inventory_transactions
order by quantity;

# 2. Из таблицы purchase_order_details вывести все строки, где purchase_order_id изменяется от 90 до 100 включительно. Добавить столбец с категорией 
# по количеству. Если quantity меньше 30 то 'small', от 30 до 70 включительно - 'medium', в остальных случаях 'large'.
select *,
	case
		when quantity < 30 then 'small'
        when quantity between 30 and 70 then 'medium'
        else 'large'
	end as category
from purchase_order_details
where purchase_order_id between 90 and 100;

# 3. Решите предыдущую задачу используя вложенные IF.
select *, 
	if (quantity < 30, 'small', if (quantity between 30 and 70, 'medium', 'large')) as category
from purchase_order_details
where purchase_order_id between 90 and 100;

# 4. Вывести уникальные значения purchase_order_id для строк где unit_cost больше 10. Отсортировать данные по убыванию выводимого 
# столбца. Таблица purchase_order_details.
select distinct(purchase_order_id)
from purchase_order_details
where unit_cost > 10
order by purchase_order_id desc;

# 5. Вывести пять строк начиная со второй из customers, где job_title равно 'Owner'. Отсортировать строки в алфавитном порядке по state_province.
select * from customers
where job_title = 'Owner'
order by state_province
limit 5
offset 1;

# 6. Выбрать уникальные id продуктов из таблицы order_details в том случае, если суммарная стоимость продукта quantity*unit_price 
# превышает 200 отсортировать столбец по возрастанию и выбрать 7 строк.
select distinct product_id from order_details
where quantity * unit_price > 200
order by id
limit 7;

# 7. Вывести инициалы - первую букву имени и первую букву фамилии сотрудника из таблицы employees.
select 
	concat_ws ('. ', left (last_name, 1), left (first_name, 1)) as Initial 
from employees;

# 8. Вывести все строки и вычисляемый столбец - если payment_type не указан, то 'No data' в остальных случаях значение столбца 
# payment_type из таблицы orders. Решить задачу с помощью IF и CASE.
# Variant IF
select *, if (payment_type is null, 'No data', payment_type) as type_payment from orders;

# Variant CASE
select *, 
	case 
		when payment_type is null then 'No data'
        else payment_type
	end as type_payment
from orders;

# 9. Вывести имя и фамилию клиентов из таблицы customers в верхнем регистре.
select upper(first_name), upper (last_name) from customers;