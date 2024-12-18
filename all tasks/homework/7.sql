SELECT city, total_sales
FROM regions
WHERE region_id = (
    SELECT region_id
    FROM cities
    WHERE city = 'Tashkent'
);
