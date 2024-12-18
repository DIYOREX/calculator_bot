SELECT
    product_id,
    SUM(sale_amount) AS total_sales
FROM sales
GROUP BY ROLLUP(product_id);
