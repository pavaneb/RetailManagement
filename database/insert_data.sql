USE RetailManagement;

INSERT INTO Supplier (supplier_name, phone, email, address) VALUES
('Fresh Foods Ltd', '9876543210', 'contact@freshfoods.com', 'Bangalore'),
('Tech Distributors', '9876543211', 'sales@techdist.com', 'Hyderabad'),
('Daily Needs Pvt Ltd', '9876543212', 'support@dailyneeds.com', 'Mumbai'),
('Global Traders', '9876543213', 'info@globaltraders.com', 'Chennai'),
('Sunrise Supplies', '9876543214', 'hello@sunrise.com', 'Pune');

select count(*) from Supplier;

USE RetailManagement;

INSERT INTO Customer (customer_name, phone, email, address) VALUES
('Rahul Sharma', '9876500001', 'rahul.sharma@gmail.com', 'Bangalore'),
('Priya Patel', '9876500002', 'priya.patel@gmail.com', 'Mumbai'),
('Amit Verma', '9876500003', 'amit.verma@gmail.com', 'Delhi'),
('Sneha Reddy', '9876500004', 'sneha.reddy@gmail.com', 'Hyderabad'),
('Arjun Kumar', '9876500005', 'arjun.kumar@gmail.com', 'Chennai'),
('Neha Joshi', '9876500006', 'neha.joshi@gmail.com', 'Pune'),
('Rohan Mehta', '9876500007', 'rohan.mehta@gmail.com', 'Ahmedabad'),
('Kavya Nair', '9876500008', 'kavya.nair@gmail.com', 'Kochi'),
('Vikram Singh', '9876500009', 'vikram.singh@gmail.com', 'Jaipur'),
('Ananya Das', '9876500010', 'ananya.das@gmail.com', 'Kolkata');


INSERT INTO Employee (employee_name, designation, salary, phone) VALUES
('Ravi Kumar', 'Store Manager', 55000.00, '9876510001'),
('Anjali Singh', 'Cashier', 30000.00, '9876510002'),
('Kiran Patel', 'Sales Executive', 35000.00, '9876510003'),
('Megha Rao', 'Inventory Manager', 42000.00, '9876510004'),
('Suresh Naik', 'Sales Executive', 34000.00, '9876510005');

-- ==========================
-- Product Data
-- ==========================
INSERT INTO Product (product_name, category, price, stock_quantity, supplier_id) VALUES
('Rice 5kg', 'Groceries', 350.00, 100, 1),
('Wheat Flour 10kg', 'Groceries', 480.00, 80, 1),
('Laptop', 'Electronics', 55000.00, 15, 2),
('Wireless Mouse', 'Electronics', 700.00, 60, 2),
('Shampoo', 'Personal Care', 250.00, 90, 3),
('Toothpaste', 'Personal Care', 120.00, 150, 3),
('Cooking Oil 1L', 'Groceries', 180.00, 120, 1),
('LED Bulb', 'Electrical', 150.00, 200, 4),
('Extension Board', 'Electrical', 450.00, 50, 4),
('Notebook', 'Stationery', 80.00, 250, 5),
('Pen Pack', 'Stationery', 60.00, 300, 5),
('Printer', 'Electronics', 8500.00, 12, 2),
('Hand Wash', 'Personal Care', 140.00, 110, 3),
('Coffee Powder', 'Beverages', 320.00, 70, 1),
('Water Bottle', 'Accessories', 220.00, 95, 5);


-- ==========================
-- Sales Data
-- ==========================
INSERT INTO Sales (customer_id, employee_id, sale_date, total_amount) VALUES
(1, 2, '2026-07-01', 1050.00),
(2, 3, '2026-07-02', 55700.00),
(3, 1, '2026-07-03', 500.00),
(4, 5, '2026-07-04', 390.00),
(5, 2, '2026-07-05', 9200.00),
(6, 4, '2026-07-06', 260.00),
(7, 3, '2026-07-07', 700.00),
(8, 1, '2026-07-08', 320.00),
(9, 5, '2026-07-09', 1500.00),
(10, 2, '2026-07-10', 600.00);


-- ==========================
-- Sale Items Data
-- ==========================
INSERT INTO Sale_Items (sale_id, product_id, quantity, price) VALUES
(1, 1, 2, 350.00),
(1, 14, 1, 320.00),

(2, 3, 1, 55000.00),
(2, 4, 1, 700.00),

(3, 2, 1, 480.00),

(4, 5, 1, 250.00),
(4, 6, 1, 120.00),

(5, 12, 1, 8500.00),
(5, 11, 2, 60.00),

(6, 13, 1, 140.00),
(6, 6, 1, 120.00),

(7, 4, 1, 700.00),

(8, 14, 1, 320.00),

(9, 8, 10, 150.00),

(10, 9, 1, 450.00),
(10, 10, 1, 80.00),
(10, 11, 1, 60.00);

SELECT COUNT(*) AS TotalSaleItems FROM Sale_Items;

select * from customer;