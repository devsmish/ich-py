# 1. Выведите список всех товаров из таблицы products, у которых цена (standard_cost) находится в диапазоне от 10 до 20 единиц.
SELECT * FROM northwind.products
where standard_cost between 10 and 20;

# 2. Найдите все заказы из таблицы orders, у которых стоят пропуски в payment_type, и которые были
# отправлены из Калифорнии ship_state_province равен английские буквы ‘CAʼ.
SELECT * FROM northwind.orders
where payment_type is null and ship_state_province = 'CA';

# 3. Выведите список всех сотрудников из таблицы employees, чья фамилия начинается на букву "C".
select * from northwind.employees
where last_name like 'C%';

# 4. Найдите всех клиентов в таблице customers, которые проживают в городах
# Minneapolis, Denver, Boston или работают в качестве Purchasing Manager (колонка job_title).
select * from northwind.customers
where city in ('Minneapolis', 'Denver', 'Boston') or job_title = 'Purchasing Manager';

# 5. Измените предыдущий запрос таким образом, чтобы из предыдущего результата выводились только записи там, где state_province Колородо 'CO'.
select * from northwind.customers
where state_province = 'CO' and (city in ('Minneapolis', 'Denver', 'Boston') or job_title = 'Purchasing Manager');

# 6. Выведите все строки из таблицы products там, где minimum_reorder_quantity входит в диапазон от 10 до 25, включая концы и 
# quantity_per_unit включает в себя слово 'boxes'. Кроме того? standard_cost должен быть менее 10.
select * from northwind.products
where minimum_reorder_quantity between 10 and 25 and quantity_per_unit like '%boxes%' and standard_cost >= 10;

# 7. Измените предыдущий запрос заменив операторы and на or Объясните какие строки выводятся в данном запросе.
select * from northwind.products
where minimum_reorder_quantity between 10 and 25 or quantity_per_unit like '%boxes%' or standard_cost >= 10;
# в даном запросе будут выведены все строки в которых выполнится одно из трех условий

# 8. Подумайте одинаковый ли результат дадут эти два запроса.
# Конечно не одинаковый. Второй запрос будет содержать на много больше данных и 100% будет включать в себя результаты первого.

# 9. Выберите все строки из таблицы products, где есть пропуски в столбце quantity_per_unit и reorder_level равен 100.
select * from northwind.products 
where quantity_per_unit is null and reorder_level = 100;

# 10. Выберите имена продуктов из таблицы products, где минимальная цена list_price превышает себестоимость standard_cost более чем на 5 уе.
select product_name from northwind.products
where list_price - 5 >  standard_cost;

# 11. Выбрать все строки из таблицы products, где reorder_level в два раза меньше target_level.
select * from northwind.products
where reorder_level * 2 = target_level;
# where reorder_level = target_level/2;
# where target_level/reorder_level = 2;

# 12. Выберите все строки из таблицы products, для которых product_code содержит 'NWTSO' и стандартная
# себестоимость standard_cost равна 1, либо минимальная цена list_price меньше 5 и target_level = 40.
select * from northwind.products
where (product_code like '%NWTSO%' and standard_cost = 1) or (list_price < 5 and target_level = 40);
# можно было без скобок

# 13. Выберите все строки из таблицы products, для которых product_code содержит 'NWTSO' или стандартная себестоимость standard_cost равна 1 
# минимальная. При этом target_level должен быть равен 40. Решить задачу двумя способами.
# Variant1
select * from northwind.products
where (product_code like '%NWTSO%' or standard_cost = 1) and target_level = 40;
# Variant2
select * from northwind.products
where (product_code like '%NWTSO%' or standard_cost in (1)) and target_level = 40;