CREATE SCHEMA online_store;

CREATE TABLE online_store.category (
                                       id SERIAL PRIMARY KEY,
                                       name VARCHAR(100) NOT NULL
);

CREATE TABLE online_store.product (
                                      id SERIAL PRIMARY KEY,
                                      name VARCHAR(100) NOT NULL,
                                      price NUMERIC(10, 2) NOT NULL,
                                      category_id INT NOT NULL,
                                      FOREIGN KEY (category_id) REFERENCES online_store.category (id) ON DELETE CASCADE
);

INSERT INTO online_store.category (name)
VALUES ('kondistsioner'), ('muzlatgich');

INSERT INTO online_store.product (name, price, category_id)
VALUES
    ('Smartphone', 699.99, 1),
    ('T-shirt', 19.99, 2),
    ('Novel', 14.99, 3);

SELECT * FROM online_store.category;

SELECT
    p.id AS product_id,
    p.name AS product_name,
    p.price AS product_price,
    c.name AS category_name
FROM online_store.product p
         JOIN online_store.category c ON p.category_id = c.id;

UPDATE online_store.category
SET name = 'Gadgets'
WHERE id = 1;

UPDATE online_store.product
SET price = 749.99
WHERE id = 1;

DELETE FROM online_store.category
WHERE id = 3;

DELETE FROM online_store.product
WHERE id = 2;
