SELECT product_name, category_name
FROM products p
WHERE category_id = (
    SELECT category_id
    FROM categories
    WHERE category_name = 'Electronics'
);
