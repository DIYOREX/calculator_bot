SELECT
    category_id,
    product_id,
    SUM(sale_amount) AS total_sales
FROM sales
GROUP BY CUBE(category_id, product_id);
