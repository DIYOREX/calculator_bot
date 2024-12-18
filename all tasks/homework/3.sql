SELECT
    region,
    city,
    SUM(sale_amount) AS total_sales
FROM sales
GROUP BY ROLLUP(region, city);
