SELECT
    region,
    YEAR(sale_date) AS year,
    SUM(sale_amount) AS total_sales
FROM sales
GROUP BY CUBE(region, YEAR(sale_date));
