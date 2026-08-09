# 🛍 Retail Management System

A web-based Retail Management System built using Python, Flask, MySQL, HTML, and Bootstrap.

## ✨ Features

### 🏠 Dashboard
- View total products
- View total customers
- View total suppliers
- View total sales

### 📦 Product Management
- Add, edit, delete and search products
- Manage product categories
- Track prices and stock
- Manage suppliers

### 👥 Customer Management
- Add, edit, delete and search customers
- Store phone, email and address

### 🚚 Supplier Management
- Add, edit, delete and search suppliers
- Store supplier contact information

### 💰 Sales Management
- Create new sales
- Select customers, employees and products
- Record quantity and sale date
- Calculate total sale amount
- Update product stock
- Search sales

### 📊 Reports
- View total sales
- View total transactions
- View top-selling products
- View low-stock products
- View recent sales

---

## 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend |
| Flask | Web framework |
| MySQL | Database |
| HTML | Frontend |
| Bootstrap 5 | UI design |
| Jinja2 | Templates |
| Git & GitHub | Version control |

---

## 📂 Project Structure

```text
RETAILMANAGEMENT/
│
├── app/
│   ├── app.py
│   ├── config.py
│   ├── db.py
│   ├── routes/
│   │   ├── customer_routes.py
│   │   ├── product_routes.py
│   │   ├── report_routes.py
│   │   ├── sales_routes.py
│   │   └── supplier_routes.py
│   ├── static/
│   └── templates/
│
├── database/
│   ├── create_database.sql
│   ├── insert_data.sql
│   ├── queries.sql
│   └── views.sql
│
├── docs/
├── .gitignore
├── README.md
└── requirements.txt
```

## ⚙️ Requirements

Before running the project, install:

- Python 3.x
- MySQL Server
- Git
- Web browser

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd RETAILMANAGEMENT
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up MySQL Database

Open **MySQL Workbench** and run the SQL files from the `database` folder.

Run them in this order:

1. `create_database.sql`
2. `insert_data.sql`
3. `views.sql`

Database name:

```text
RetailManagement
```

### 5. Configure Database Connection

Open:

```text
app/db.py
```

Use your own MySQL credentials:

```python
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="RetailManagement"
    )
```

⚠️ **Never upload your real MySQL password to GitHub.**

### 6. Run the Application

```bash
python app/app.py
```

Then open:

```text
http://127.0.0.1:5000
```

---

## 📌 Project Status

**Core Version Completed ✅**

The main Retail Management System features have been implemented and tested locally.

---

## 🔮 Future Enhancements

- User authentication
- Admin and employee roles
- Invoice generation
- PDF reports
- Sales charts and analytics
- Advanced inventory alerts
- Email notifications
- Permanent cloud deployment
- REST API

---

## 👨‍💻 Purpose

This project was developed as a practical software project to demonstrate:

- Python programming
- Flask web development
- MySQL database management
- CRUD operations
- Database relationships
- Inventory management
- Sales processing
- Reporting
- Git and GitHub