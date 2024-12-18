INSERT INTO category (name)
VALUES
    ('Electronics'),
    ('Groceries'),
    ('Clothing'),
    ('Books');

INSERT INTO product (name, description, price, category_id, image)
VALUES
    ('Smartphone', 'Latest model with 128GB storage', 500.0, 1, 'smartphone.jpg'),
    ('Laptop', '15-inch screen with Intel i7', 1200.0, 1, 'laptop.jpg'),
    ('Apples', 'Fresh red apples', 2.5, 2, 'apples.jpg'),
    ('T-shirt', '100% cotton, size M', 10.0, 3, 'tshirt.jpg'),
    ('Novel', 'Bestseller fiction', 15.0, 4, 'novel.jpg');

INSERT INTO "order" (full_name, phone, address)
VALUES
    ('John Doe', '+1234567890', '123 Main Street'),
    ('Jane Smith', '+1987654321', '456 Elm Street');

INSERT INTO orderitem (product_id, order_id, quantity, price)
VALUES
    (1, 1, 2, 1000.0),
    (3, 1, 5, 12.5),
    (4, 2, 3, 30.0),
    (5, 2, 1, 15.0);

SELECT *
FROM orderitem;

SELECT
    oi.order_id,
    p.name AS product_name,
    oi.quantity,
    oi.price,
    (oi.quantity * oi.price) AS total_price
FROM
    orderitem oi
        JOIN
    product p ON oi.product_id = p.id;

SELECT
    o.full_name,
    o.phone,
    o.address,
    p.name AS product_name,
    oi.quantity,
    oi.price,
    (oi.quantity * oi.price) AS total_price
FROM
    orderitem oi
        JOIN
    product p ON oi.product_id = p.id
        JOIN
    "order" o ON oi.order_id = o.id
WHERE
    oi.order_id = 1;
