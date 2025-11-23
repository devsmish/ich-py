-- Вы можете использовать несколько условий в HAVING Сгруппировать продукты по standard_cost и list_price Посчитать количество продуктов и
-- вывести только те данные, где количество продуктов не менее 2
select product_name, standard_cost, list_price, COUNT(product_name) as prod_count from products
GROUP BY standard_cost, list_price
HAVING prod_count >=2;

-- Часто HAVING и WHERE используются вместе, чтобы максимально сузить набор данных перед тем, как применять агрегатные функции и группировку.
-- Выбрать только те продукты в quantity_per_unit встречается слово 'oz' как в нижнем так и в верхнем регистрах Сгруппировать по standard_cost
-- Оставить только данные, где количество продуктов не менее 3
select product_name, standard_cost, quantity_per_unit, count(product_name) as prod_count from products
where quantity_per_unit like lower('%oz%') or quantity_per_unit like upper('%oz%')
GROUP BY standard_cost
HAVING prod_count >= 3;

-- 1. Вывести среднее, минимум, максимум и сумму по столбцу standard_cost
select AVG(standard_cost), min(standard_cost), max(standard_cost), sum(standard_cost) from products;

-- 2. Посчитайте количество товаров в каждой категории category Выведите только записи с количеством товаров не менее 3
select category, count(product_name) as prod_count from products
GROUP BY category
HAVING prod_count >= 3;

-- 3. Выведите среднюю себестоимость standard_cost для пары supplier_ids + category
select supplier_ids, category, avg(standard_cost) as avg_cost from products
GROUP BY supplier_ids, category;

-- 4. Посчитайте количество продуктов, для которых отсутсвует minimum_reorder_quantity
select count(id) as prod_count from products
where minimum_reorder_quantity is NULL;

-- variant2
select count(*) from products
where minimum_reorder_quantity is NULL;

-- 4.1 Посчитайте количество продуктов для каждой категории, для которых отсутсвует minimum_reorder_quantity  и 
-- отобразите те, которых больше 3
select category, count(*) as prod_count from products
GROUP BY category
HAVING prod_count > 3;

-- 5. Посчитайте количество уникальных категорий
select count(DISTINCT category) as uniq_ctgr from products;

-- 6. Разделите все товары на группы по reorder_level если reorder_level меньше 10 то 'low' , от 10 до 20 включительно - 'medium' , 
-- осталные - 'hight'. 
-- Вывести среднее, максимум и минимум столбца list_price для каждой группы
select 
	CASE
		WHEN reorder_level < 10 then 'low'
        WHEN reorder_level BETWEEN 10 and 20 then 'medium'
        ELSE 'hight'
	end as group_level,
    avg(list_price),
    max(list_price),
    min(list_price)
        from products
GROUP BY group_level;

-- 7. Найти средний standard_cost только для тех продуктов, которые продаются коробками quantity_per_unit 
select avg(standard_cost) from products
where quantity_per_unit like '%box%';

-- 8. Вычислите суммарную прибыль компании для каждой категории для продуктов с target_level больше 40 Прибыль компании вычисляется как list_price - standard_cost
select category, (list_price - standard_cost) as profit from products
where target_level > 40
GROUP BY category;