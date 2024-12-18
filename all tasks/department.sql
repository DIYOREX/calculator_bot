CREATE TABLE employees (
                           id SERIAL PRIMARY KEY,
                           department VARCHAR(50),
                           name VARCHAR(100),
                           age INT,
                           email VARCHAR(100),
                           phone VARCHAR(20),
                           salary NUMERIC
);

INSERT INTO employees (department, name, age, email, phone, salary)
VALUES
    ('HR', 'Alice', 30, 'alice@example.com', '1234567890', 3000),
    ('Engineering', 'Bob', 25, 'bob@example.com', '1234567891', 4000),
    ('Sales', 'Charlie', 35, 'charlie@example.com', '1234567892', 3500),
    ('HR', 'Diana', 40, 'diana@example.com', '1234567893', 4500),
    ('Engineering', 'Eve', 28, 'eve@example.com', '1234567894', 4200),
    ('Sales', 'Frank', 45, 'frank@example.com', '1234567895', 2800),
    ('HR', 'Grace', 29, 'grace@example.com', '1234567896', 3700);

SELECT
    department,
    COUNT(*) AS employee_count,
    MAX(salary) AS highest_salary,
    MIN(salary) AS lowest_salary,
    AVG(salary) AS average_salary
FROM employees
GROUP BY department;

SELECT
    *
FROM employees
WHERE salary BETWEEN 2000 AND 5000;

SELECT
    *
FROM employees
WHERE department IN ('HR', 'Engineering');

SELECT
    *
FROM employees
WHERE email LIKE '%@example.com';
