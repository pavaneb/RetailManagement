-- View 1: Product Details
USE RetailManagement;

CREATE VIEW ProductDetails AS
SELECT
    p.product_id,
    p.product_name,
    p.category,
    p.price,
    p.stock_quantity,
    s.supplier_name
FROM Product p
JOIN Supplier s
ON p.supplier_id = s.supplier_id;

-- View 2: Sales Report
CREATE VIEW SalesReport AS
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

-- View 3: Low Stock Products
CREATE VIEW LowStockProducts AS
SELECT
    product_name,
    stock_quantity
FROM Product
WHERE stock_quantity < 100;

-- View 4: Customer Purchases
CREATE VIEW CustomerPurchases AS
SELECT
    c.customer_name,
    COUNT(sa.sale_id) AS TotalOrders,
    SUM(sa.total_amount) AS TotalSpent
FROM Customer c
LEFT JOIN Sales sa
ON c.customer_id = sa.customer_id
GROUP BY c.customer_name;

-- View 5: Supplier Inventory
CREATE VIEW SupplierInventory AS
SELECT
    s.supplier_name,
    COUNT(p.product_id) AS TotalProducts,
    SUM(p.stock_quantity) AS TotalStock
FROM Supplier s
JOIN Product p
ON s.supplier_id = p.supplier_id
GROUP BY s.supplier_name;
