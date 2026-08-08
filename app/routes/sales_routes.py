from flask import Blueprint, render_template, request, redirect, url_for
from db import get_connection

sales_bp = Blueprint("sales", __name__)


# -----------------------------
# View Sales
# -----------------------------
@sales_bp.route("/sales")
def sales():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    search = request.args.get("search", "")

    query = """
        SELECT
            s.sale_id,
            c.customer_name,
            e.employee_name,
            p.product_name,
            s.quantity,
            s.sale_date,
            s.total_amount
        FROM Sales s

        LEFT JOIN Customer c
            ON s.customer_id = c.customer_id

        LEFT JOIN Employee e
            ON s.employee_id = e.employee_id

        LEFT JOIN Product p
            ON s.product_id = p.product_id
    """

    values = ()

    if search:
        query += """
        WHERE
            c.customer_name LIKE %s
            OR e.employee_name LIKE %s
            OR p.product_name LIKE %s
        """

        values = (
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        )

    query += " ORDER BY s.sale_id DESC"

    cursor.execute(query, values)

    sales = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "sales.html",
        sales=sales,
        search=search
    )

# -----------------------------
# Add Sale
# -----------------------------
@sales_bp.route("/add_sale", methods=["GET", "POST"])
def add_sale():

    connection = get_connection()

    # -------------------------
    # Save Sale
    # -------------------------
    if request.method == "POST":

        customer_id = request.form["customer_id"]
        employee_id = request.form["employee_id"]
        product_id = request.form["product_id"]
        quantity = int(request.form["quantity"])
        sale_date = request.form["sale_date"]

        cursor = connection.cursor(dictionary=True)

        # Get product price and current stock
        cursor.execute("""
            SELECT price, stock_quantity
            FROM Product
            WHERE product_id = %s
        """, (product_id,))

        product = cursor.fetchone()

        # Check whether product exists
        if product is None:

            cursor.close()
            connection.close()

            return "Product not found"

        # Check stock
        if quantity <= 0:

            cursor.close()
            connection.close()

            return "Quantity must be greater than 0"

        if quantity > product["stock_quantity"]:

            cursor.close()
            connection.close()

            return "Insufficient stock"

        # Calculate total
        total_amount = product["price"] * quantity

        # Insert sale
        cursor.execute("""
            INSERT INTO Sales
            (
                customer_id,
                employee_id,
                product_id,
                quantity,
                sale_date,
                total_amount
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            customer_id,
            employee_id,
            product_id,
            quantity,
            sale_date,
            total_amount
        ))

        # Reduce product stock
        cursor.execute("""
            UPDATE Product
            SET stock_quantity = stock_quantity - %s
            WHERE product_id = %s
        """, (
            quantity,
            product_id
        ))

        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for("sales.sales"))

    # -------------------------
    # Load dropdown data
    # -------------------------

    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT customer_id, customer_name
        FROM Customer
        ORDER BY customer_name
    """)
    customers = cursor.fetchall()

    cursor.execute("""
        SELECT employee_id, employee_name
        FROM Employee
        ORDER BY employee_name
    """)
    employees = cursor.fetchall()

    cursor.execute("""
        SELECT product_id, product_name, price, stock_quantity
        FROM Product
        WHERE stock_quantity > 0
        ORDER BY product_name
    """)
    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "add_sale.html",
        customers=customers,
        employees=employees,
        products=products
    )