SELECT product_id, sale_amount
FROM sales
WHERE sale_amount = (
    SELECT MAX(sale_amount)
    FROM sales
);
