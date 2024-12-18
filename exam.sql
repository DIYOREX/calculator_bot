CREATE SCHEMA store;

CREATE TABLE store.categories (
                                  id SERIAL PRIMARY KEY,
                                  name VARCHAR(300) NOT NULL
);
CREATE TABLE store.subcategories (
                                     id SERIAL PRIMARY KEY,
                                     name VARCHAR(255) NOT NULL,
                                     parent_id INT REFERENCES store.categories(id)
);
CREATE TABLE store.products (
                                id SERIAL PRIMARY KEY,
                                name VARCHAR(255) NOT NULL,
                                color VARCHAR(50),
                                gpu_type VARCHAR(100),
                                gpu_model VARCHAR(100),
                                ram INT,
                                ram_type VARCHAR(50),
                                brand VARCHAR(100),
                                screen_size FLOAT,
                                resolution VARCHAR(50),
                                storage_size INT,
                                processor_model VARCHAR(100),
                                processor_generation VARCHAR(50),
                                price DECIMAL(10, 2),
                                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                subcategory_id INT REFERENCES store.subcategories(id)
);

CREATE TABLE store.attribute (
                                 id SERIAL PRIMARY KEY,
                                 key_value VARCHAR(255),
                                 value VARCHAR(100)
);

CREATE TABLE store.attribute_value (
                                       id SERIAL PRIMARY KEY,
                                       value VARCHAR(255)
);

CREATE TABLE store.product_attribute (
                                         id INT REFERENCES store.attribute(id),
                                         attribute_value_id INT REFERENCES store.attribute_value(id),
                                         product_id INT REFERENCES store.products(id)
);

CREATE OR REPLACE FUNCTION store.get_product_count_by_category(category_name VARCHAR)
    RETURNS INTEGER AS $$
BEGIN
    RETURN (
        SELECT COUNT(p.id)
        FROM store.categories c
                 JOIN store.subcategories s ON c.id = s.parent_id
                 JOIN store.products p ON s.id = p.subcategory_id
        WHERE c.name = category_name
    );
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION store.update_product_price(product_name VARCHAR, new_price DECIMAL)
    RETURNS VOID AS $$
BEGIN
    UPDATE store.products
    SET price = new_price, updated_at = CURRENT_TIMESTAMP
    WHERE name = product_name;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION store.get_products_by_subcategory(subcategory_name VARCHAR)
    RETURNS TABLE(
                     product_name VARCHAR,
                     brand VARCHAR,
                     price DECIMAL
                 ) AS $$
BEGIN
    RETURN QUERY
        SELECT p.name, p.brand, p.price
        FROM store.subcategories s
                 JOIN store.products p ON s.id = p.subcategory_id
        WHERE s.name = subcategory_name;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION store.add_new_product(
    product_name VARCHAR,
    color VARCHAR,
    brand VARCHAR,
    price DECIMAL,
    subcategory_name VARCHAR
)
    RETURNS VOID AS $$
DECLARE
    subcategory_id INT;
BEGIN
    SELECT id INTO subcategory_id
    FROM store.subcategories
    WHERE name = subcategory_name;

    IF subcategory_id IS NULL THEN
        RAISE EXCEPTION 'Subcategory % not found', subcategory_name;
    END IF;

    INSERT INTO store.products (name, color, brand, price, subcategory_id)
    VALUES (product_name, color, brand, price, subcategory_id);
END;
$$ LANGUAGE plpgsql;

INSERT INTO store.categories (name)
VALUES
    ('Phones'),
    ('Notebooks'),
    ('TV');

INSERT INTO store.subcategories (name, parent_id)
VALUES
    ('Smartphones', 1),
    ('Gadgets', 1),
    ('Notebooks', 2);

INSERT INTO store.products (name, color, gpu_type, gpu_model, ram, ram_type, brand, screen_size,
                            resolution, storage_size, processor_model, processor_generation, price, subcategory_id)
VALUES
    ('iPhone 15 Pro', 'Silver', 'Apple', 'A17 Pro', 8, 'LPDDR5', 'Apple', 6.1,
     '1179x2556', 512, 'Apple A17', '1st Gen', 1499.99, 1),
    ('Samsung Galaxy S23', 'Black', 'Qualcomm', 'Adreno 740', 8, 'LPDDR5X', 'Samsung', 6.8,
     '1440x3088', 256, 'Snapdragon 8 Gen 2', '2nd Gen', 1199.99, 1),
    ('MacBook Pro 16"', 'Space Gray', 'Apple', 'M1 Pro', 16, 'Unified', 'Apple', 16.2,
     '3456x2234', 1024, 'Apple M1 Pro', '1st Gen', 2499.99, 3),

    ('iPhone 14', 'Gold', 'Apple', 'A16 Bionic', 6, 'LPDDR5', 'Apple', 6.1,
     '1170x2532', 256, 'Apple A16', '1st Gen', 1099.99, 1),

    ('Galaxy Z Flip 5', 'Lavender', 'Qualcomm', 'Adreno 740', 8, 'LPDDR5', 'Samsung',
     6.7, '2640x1080', 512, 'Snapdragon 8 Gen 2', '2nd Gen', 1299.99, 1),

    ('OnePlus 11', 'Green', 'Qualcomm', 'Adreno 740', 16, 'LPDDR5X', 'OnePlus', 6.7,
     '1440x3216', 256, 'Snapdragon 8 Gen 2', '2nd Gen', 799.99, 1),

    ('Pixel 7 Pro', 'White', 'Google', 'Mali-G710', 12, 'LPDDR5', 'Google', 6.7,
     '1440x3120', 128, 'Google Tensor G2', '1st Gen', 899.99, 1),

    ('Sony Xperia 1 V', 'Black', 'Qualcomm', 'Adreno 740', 12, 'LPDDR5X', 'Sony',
     6.5, '1644x3840', 256, 'Snapdragon 8 Gen 2', '2nd Gen', 1399.99, 1),

    ('Apple Watch Series 8', 'Silver', 'N/A', 'N/A', 1, 'Unified', 'Apple',
     1.9, '396x484', 32, 'S8', '1st Gen', 399.99, 2),

    ('Samsung Galaxy Watch 5', 'Graphite', 'N/A', 'N/A', 1, 'Unified', 'Samsung',
     1.4, '450x450', 16, 'Exynos W920', '1st Gen', 299.99, 2),

    ('Fitbit Versa 4', 'Pink', 'N/A', 'N/A', 0.5, 'Unified', 'Fitbit', 1.58,
     '336x336', 4, 'N/A', '1st Gen', 199.99, 2),

    ('Garmin Venu 2 Plus', 'Cream Gold', 'N/A', 'N/A', 1, 'Unified', 'Garmin',
     1.3, '416x416', 8, 'N/A', '1st Gen', 449.99, 2),

    ('Xiaomi Smart Band 8', 'Black', 'N/A', 'N/A', 0.5, 'Unified', 'Xiaomi', 1.6,
     '490x192', 8, 'N/A', '1st Gen', 49.99, 2),

    ('Dell XPS 13', 'Silver', 'Intel', 'Iris Xe', 16, 'LPDDR4x', 'Dell',
     13.4, '1920x1200', 512, 'Intel Core i7-1355U', '13th Gen',1249.99, 3),

    ('HP Spectre x360', 'Black', 'Intel', 'Iris Xe', 16, 'LPDDR4x', 'HP',
     13.5, '3000x2000', 1024, 'Intel Core i7-1360P', '13th Gen', 1599.99, 3),

    ('Lenovo ThinkPad X1 Carbon', 'Black', 'Intel', 'Iris Xe', 32, 'LPDDR5', 'Lenovo',
     14, '2560x1600', 1024, 'Intel Core i7-1370P', '13th Gen', 1999.99, 3),

    ('ASUS ZenBook 14X OLED', 'Blue', 'Intel', 'Iris Xe', 16, 'LPDDR5', 'ASUS',
     14, '2880x1800', 512, 'Intel Core i7-1260P', '12th Gen', 139.99, 3);
