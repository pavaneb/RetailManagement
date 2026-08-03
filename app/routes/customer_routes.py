from flask import Blueprint, render_template, request, redirect, url_for
from db import get_connection

customer_bp = Blueprint("customer", __name__)


# -----------------------------
# View Customers
# -----------------------------
@customer_bp.route("/customers")
def customers():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    search = request.args.get("search", "")

    query = """
        SELECT *
        FROM Customer
    """

    values = ()

    if search:
        query += """
        WHERE
            customer_name LIKE %s
            OR phone LIKE %s
            OR email LIKE %s
        """

        values = (
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        )

    cursor.execute(query, values)

    customers = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "customers.html",
        customers=customers,
        search=search
    )


# -----------------------------
# Add Customer
# -----------------------------
@customer_bp.route("/add_customer", methods=["GET", "POST"])
def add_customer():

    if request.method == "POST":

        customer_name = request.form["customer_name"]
        phone = request.form["phone"]
        email = request.form["email"]
        address = request.form["address"]

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO Customer
            (customer_name, phone, email, address)
            VALUES (%s, %s, %s, %s)
        """, (
            customer_name,
            phone,
            email,
            address
        ))

        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for("customer.customers"))

    return render_template(
        "add_customer.html",
        customer=None
    )


# -----------------------------
# Edit Customer
# -----------------------------
@customer_bp.route("/edit_customer/<int:customer_id>", methods=["GET", "POST"])
def edit_customer(customer_id):

    connection = get_connection()

    if request.method == "POST":

        customer_name = request.form["customer_name"]
        phone = request.form["phone"]
        email = request.form["email"]
        address = request.form["address"]

        cursor = connection.cursor()

        cursor.execute("""
            UPDATE Customer
            SET
                customer_name=%s,
                phone=%s,
                email=%s,
                address=%s
            WHERE customer_id=%s
        """, (
            customer_name,
            phone,
            email,
            address,
            customer_id
        ))

        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for("customer.customers"))

    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM Customer
        WHERE customer_id=%s
    """, (customer_id,))

    customer = cursor.fetchone()

    cursor.close()
    connection.close()

    return render_template(
        "add_customer.html",
        customer=customer
    )


# -----------------------------
# Delete Customer
# -----------------------------
@customer_bp.route("/delete_customer/<int:customer_id>")
def delete_customer(customer_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM Customer
        WHERE customer_id=%s
    """, (customer_id,))

    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for("customer.customers"))