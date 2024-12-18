CREATE TABLE products (
                          id SERIAL PRIMARY KEY,
                          name VARCHAR(255) NOT NULL,
                          attributes JSONB NOT NULL,
                          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO products (name, attributes) VALUES
                                            ('Laptop A', '{"brand": "Dell", "features": {"Cpu": "i5", "ram": "8GB", "storage": "256GB SSD"}, "price": 900}'),
                                            ('Laptop B', '{"brand": "HP", "features": {"Cpu": "i7", "ram": "16GB", "storage": "512GB SSD"}, "price": 1200}'),
                                            ('Laptop C', '{"brand": "Lenovo", "features": {"Cpu": "i3", "ram": "4GB", "storage": "128GB SSD"}, "price": 500}'),
                                            ('Laptop D', '{"brand": "Dell", "features": {"Cpu": "i7", "ram": "8GB", "storage": "1TB HDD"}, "price": 1000}');

SELECT *
FROM products
WHERE attributes->'features'->>'ram' = '8GB';

SELECT *
FROM products
WHERE (attributes->>'price')::INT > 1000;

SELECT *
FROM products
ORDER BY (attributes->>'price')::INT DESC;
