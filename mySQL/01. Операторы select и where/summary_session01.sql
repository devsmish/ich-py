SELECT * FROM products;

SELECT product_name, standard_cost, list_price FROM products;

SELECT product_name, standard_cost, list_price, list_price - standard_cost FROM products;

SELECT product_name, (list_price - standard_cost) * 2 as new_name FROM products;

SELECT product_name, standard_cost, list_price, list_price - standard_cost FROM products
where list_price - standard_cost < 5;