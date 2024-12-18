SELECT product_id, sale_amount
FROM sales
WHERE sale_amount > (
    SELECT AVG(sale_amount)
    FROM sales
);
