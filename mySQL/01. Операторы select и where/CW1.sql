# SELECT 'Good morning';
# SELECT 'GUTEN';
-- USE northwind;
-- SELECT * from orders;
-- show columns from orders;
SELECT * FROM northwind.products
WHERE standard_cost > 20 and list_price < 80;

SELECT * FROM employees
WHERE city LIKE '%mond' or first_name LIKE 'A%';

SELECT * FROM northwind.orders
WHERE shipping_fee BETWEEN 10 and 15;

 SELECT * FROM northwind.orders
WHERE ship_city IN ('Chicago', 'Miami');