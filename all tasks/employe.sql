CREATE TABLE Employee (
                          ID INT PRIMARY KEY,
                          Name VARCHAR(50) NOT NULL UNIQUE,
                          Age INT CHECK (Age > 0),
                          Salary integer(10, 2),
                          Level VARCHAR(100),
                          created DATE DEFAULT CURRENT_DATE
);

CREATE TABLE Category (
                          id INT PRIMARY KEY,
                          title VARCHAR(100) NOT NULL,
                          created DATE DEFAULT CURRENT_DATE
);

INSERT INTO Employee (ID, Name, Age, Salary, Level, created)
VALUES
    (1, 'Diyorbek Yaxyo', 30, 50000.00, 'Senior', '2024-11-15'),
    (2, 'john Smith', 25, 45000.00, 'Junior', '2024-11-15');
SELECT * FROM Employee;
CREATE TABLE Employee_Backup AS
SELECT * FROM Employee;

SELECT * INTO Employee_Copy FROM Employee;
INSERT INTO Category (id, title, created)
VALUES
    (1, 'IT', '2024-11-15'),
    (2, 'Finance', '2024-11-15');
SELECT * FROM Category;
CREATE TABLE Category_Backup AS
SELECT * FROM Category;
SELECT * INTO Category_Copy FROM Category;
