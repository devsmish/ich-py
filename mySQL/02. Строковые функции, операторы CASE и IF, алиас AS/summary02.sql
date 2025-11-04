SELECT * FROM northwind.suppliers;

SELECT id, company, last_name, first_name, email_address AS email, job_title, business_phone AS phone FROM northwind.suppliers AS supp;


SELECT SUBSTRING("some text", 2, 5);
SELECT SUBSTRING("some text", 2);
SELECT SUBSTRING(first_name, 1, 5) FROM suppliers;
SELECT concat(first_name, "-", last_name) as fullname FROM suppliers;
SELECT SUBSTRING(concat(first_name, "-", last_name), 3, 7) as fullname FROM suppliers;
SELECT concat_ws(", ", first_name, last_name, id, company) as fullname FROM suppliers;

SELECT *, coalesce(date_allocated, purchase_order_id, inventory_id) 
FROM northwind.order_details;

SELECT *, 
	CASE
		WHEN date_allocated IS NOT NULL THEN date_allocated
		WHEN purchase_order_id IS NOT NULL THEN purchase_order_id
		WHEN inventory_id IS NOT NULL THEN inventory_id
    END 
FROM northwind.order_details;

SELECT '    Sample Text    ' as full_text, TRIM('    Sample Text    ') AS trimmed_text;
