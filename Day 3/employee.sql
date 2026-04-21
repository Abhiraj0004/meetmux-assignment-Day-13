CREATE DATABASE day3_db;
USE day3_db;

CREATE TABLE employees (
    name VARCHAR(50),
    age INT,
    salary INT
);

INSERT INTO employees VALUES ('Rahul', 25, 30000);
INSERT INTO employees VALUES ('Amit', 28, 45000);
INSERT INTO employees VALUES ('Neha', 24, 35000);
INSERT INTO employees VALUES ('Priya', 30, 60000);
INSERT INTO employees VALUES ('Ravi', 27, 40000);

SELECT * FROM employees;


SELECT * FROM employees WHERE salary > 30000;

SELECT * FROM employees ORDER BY salary DESC;