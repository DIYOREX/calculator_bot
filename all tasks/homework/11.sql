SELECT product_id, sale_amount
FROM sales
WHERE sale_amount < (
    SELECT MIN(sale_amount) + 10
    FROM sales
);
