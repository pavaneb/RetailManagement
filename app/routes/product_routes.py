from flask import Blueprint, render_template, request, redirect, url_for
from db import get_connection

product_bp = Blueprint("product", __name__)


# -----------------------------
# View Products
# -----------------------------
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


# -----------------------------
# Add Product
# -----------------------------
@product_bp.route("/add_product", methods=["GET", "POST"])
def add_product():

    connection = get_connection()

    if request.method == "POST":

        product_name = request.form["product_name"]
        category = request.form["category"]
        price = request.form["price"]
        stock_quantity = request.form["stock_quantity"]
        supplier_id = request.form["supplier_id"]

        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO Product
            (product_name, category, price, stock_quantity, supplier_id)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            product_name,
            category,
            price,
            stock_quantity,
            supplier_id
        ))

        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for("product.products"))

    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT supplier_id, supplier_name
        FROM Supplier
    """)

    suppliers = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "add_product.html",
        suppliers=suppliers,
        product=None
    )


# -----------------------------
# Edit Product
# -----------------------------
@product_bp.route("/edit_product/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):

    connection = get_connection()

    if request.method == "POST":

        product_name = request.form["product_name"]
        category = request.form["category"]
        price = request.form["price"]
        stock_quantity = request.form["stock_quantity"]
        supplier_id = request.form["supplier_id"]

        cursor = connection.cursor()

        cursor.execute("""
            UPDATE Product
            SET
                product_name=%s,
                category=%s,
                price=%s,
                stock_quantity=%s,
                supplier_id=%s
            WHERE product_id=%s
        """, (
            product_name,
            category,
            price,
            stock_quantity,
            supplier_id,
            product_id
        ))

        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for("product.products"))

    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM Product
        WHERE product_id=%s
    """, (product_id,))

    product = cursor.fetchone()

    cursor.execute("""
        SELECT supplier_id, supplier_name
        FROM Supplier
    """)

    suppliers = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "add_product.html",
        product=product,
        suppliers=suppliers
    )

# -----------------------------
# Delete Product
# -----------------------------
@product_bp.route("/delete_product/<int:product_id>")
def delete_product(product_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM Product
        WHERE product_id = %s
    """, (product_id,))

    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for("product.products"))