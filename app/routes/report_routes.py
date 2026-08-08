from flask import Blueprint, render_template
from db import get_connection

report_bp = Blueprint("report", __name__)


@report_bp.route("/reports")
def reports():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    # Total sales amount
    cursor.execute("""
        SELECT COALESCE(SUM(total_amount), 0) AS total_sales
        FROM Sales
    """)
    total_sales = cursor.fetchone()["total_sales"]

    # Number of sales
    cursor.execute("""
        SELECT COUNT(*) AS total_transactions
        FROM Sales
    """)
    total_transactions = cursor.fetchone()["total_transactions"]

    # Top selling products
    cursor.execute("""
        SELECT
            p.product_name,
            SUM(s.quantity) AS quantity_sold
        FROM Sales s
        JOIN Product p
            ON s.product_id = p.product_id
        GROUP BY p.product_id, p.product_name
        ORDER BY quantity_sold DESC
        LIMIT 5
    """)
    top_products = cursor.fetchall()

    # Low stock products
    cursor.execute("""
        SELECT
            product_id,
            product_name,
            stock_quantity
        FROM Product
        WHERE stock_quantity <= 5
        ORDER BY stock_quantity ASC
    """)
    low_stock = cursor.fetchall()

    # Recent sales
    cursor.execute("""
        SELECT
            s.sale_id,
            c.customer_name,
            p.product_name,
            s.quantity,
            s.sale_date,
            s.total_amount
        FROM Sales s
        LEFT JOIN Customer c
            ON s.customer_id = c.customer_id
        LEFT JOIN Product p
            ON s.product_id = p.product_id
        ORDER BY s.sale_id DESC
        LIMIT 10
    """)
    recent_sales = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "reports.html",
        total_sales=total_sales,
        total_transactions=total_transactions,
        top_products=top_products,
        low_stock=low_stock,
        recent_sales=recent_sales
    )