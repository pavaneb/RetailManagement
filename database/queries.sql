USE RetailManagement;

-- Basic Queries

-- 1. Display all customers
SELECT * FROM Customer;

-- 2. Display all products
SELECT * FROM Product;

-- 3. Display all employees
SELECT * FROM Employee;

-- 4. Display all suppliers
SELECT * FROM Supplier;

-- 5. Display all sales
SELECT * FROM Sales;

-- 6. Products costing more than ₹500
SELECT * FROM Product
WHERE price > 500;

-- 7. Customers from Bangalore
SELECT * FROM Customer
WHERE address = 'Bangalore';

-- 8. Employees with salary greater than 35000
SELECT * FROM Employee
WHERE salary > 35000;

-- 9. Products with stock less than 100
SELECT * FROM Product
WHERE stock_quantity < 100;

-- 10. Products in Electronics category
SELECT * FROM Product
WHERE category = 'Electronics';

-- 11. Products sorted by price (High to Low)
SELECT * FROM Product
ORDER BY price DESC;

-- 12. Customers sorted alphabetically
SELECT * FROM Customer
ORDER BY customer_name ASC;

-- 13. Employees sorted by salary
SELECT * FROM Employee
ORDER BY salary DESC;

-- Aggregate Functions

-- 14. Count total customers
SELECT COUNT(*) AS TotalCustomers
FROM Customer;

-- 15. Count total products
SELECT COUNT(*) AS TotalProducts
FROM Product;

-- 16. Average product price
SELECT AVG(price) AS AveragePrice
FROM Product;

-- 17. Maximum salary
SELECT MAX(salary) AS HighestSalary
FROM Employee;

-- 18. Minimum salary
SELECT MIN(salary) AS LowestSalary
FROM Employee;

-- 19. Total stock available
SELECT SUM(stock_quantity) AS TotalStock
FROM Product;


-- =====================================
-- JOIN QUERIES
-- =====================================

-- 20.Show Product with Supplier Name
SELECT
    p.product_name,
    p.category,
    p.price,
    s.supplier_name
FROM Product p
JOIN Supplier s
ON p.supplier_id = s.supplier_id;

-- 21.Show Sales with Customer Name
SELECT
    sa.sale_id,
    c.customer_name,
    sa.sale_date,
    sa.total_amount
FROM Sales sa
JOIN Customer c
ON sa.customer_id = c.customer_id;

-- 22.Show Employee who handled each Sale
SELECT
    sa.sale_id,
    e.employee_name,
    sa.sale_date
FROM Sales sa
JOIN Employee e
ON sa.employee_id = e.employee_id;

-- 23.Complete Sales Report
SELECT
    sa.sale_id,
    c.customer_name,
    e.employee_name,
    sa.sale_date,
    sa.total_amount
FROM Sales sa
JOIN Customer c
ON sa.customer_id = c.customer_id
JOIN Employee e
ON sa.employee_id = e.employee_id;

-- 24. Product with Supplier and Stock
SELECT
    p.product_name,
    s.supplier_name,
    p.stock_quantity
FROM Product p
JOIN Supplier s
ON p.supplier_id = s.supplier_id;

-- 25. Sale Items with Product Name
SELECT
    si.sale_item_id,
    p.product_name,
    si.quantity,
    si.price
FROM Sale_Items si
JOIN Product p
ON si.product_id = p.product_id;

-- 26. Detailed Bill
SELECT
    sa.sale_id,
    c.customer_name,
    p.product_name,
    si.quantity,
    si.price
FROM Sale_Items si
JOIN Sales sa
ON si.sale_id = sa.sale_id
JOIN Customer c
ON sa.customer_id = c.customer_id
JOIN Product p
ON si.product_id = p.product_id;

-- 27. Products Sold More Than Once
SELECT
    p.product_name,
    SUM(si.quantity) AS TotalSold
FROM Sale_Items si
JOIN Product p
ON si.product_id = p.product_id
GROUP BY p.product_name
HAVING SUM(si.quantity) > 1;

-- 28. Total Sales by Employee
SELECT
    e.employee_name,
    SUM(sa.total_amount) AS TotalSales
FROM Sales sa
JOIN Employee e
ON sa.employee_id = e.employee_id
GROUP BY e.employee_name;

-- 29. Total Purchases by Customer
SELECT
    c.customer_name,
    SUM(sa.total_amount) AS TotalSpent
FROM Sales sa
JOIN Customer c
ON sa.customer_id = c.customer_id
GROUP BY c.customer_name;

-- 30. Supplier-wise Product Count
SELECT
    s.supplier_name,
    COUNT(p.product_id) AS TotalProducts
FROM Supplier s
JOIN Product p
ON s.supplier_id = p.supplier_id
GROUP BY s.supplier_name;