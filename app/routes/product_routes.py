from flask import Blueprint, render_template, request, redirect, url_for
from db import get_connection

product_bp = Blueprint("product", __name__)

@product_bp.route("/products")
def products():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
    SELECT
        p.product_id,
        p.product_name,
        p.category,
        p.price,
        p.stock_quantity,
        s.supplier_name
    FROM Product p
    JOIN Supplier s
        ON p.supplier_id = s.supplier_id
""")

    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("products.html", products=products)


@product_bp.route("/add_product", methods=["GET", "POST"])
def add_product():

    if request.method == "POST":

        product_name = request.form["product_name"]
        category = request.form["category"]
        price = request.form["price"]
        stock_quantity = request.form["stock_quantity"]
        supplier_id = request.form["supplier_id"]

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO Product
            (product_name, category, price, stock_quantity, supplier_id)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            (
                product_name,
                category,
                price,
                stock_quantity,
                supplier_id
)
        ))

        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for("product.products"))

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT supplier_id, supplier_name FROM Supplier")
    suppliers = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("add_product.html", suppliers=suppliers)