SELECT
    category_id,
    product_id,
    SUM(sale_amount) AS total_sales
FROM sales
GROUP BY GROUPING SETS (
    (category_id),
    (product_id),
    (category_id, product_id)
    );
