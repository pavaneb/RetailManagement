from flask import Blueprint, render_template, request, redirect, url_for
from db import get_connection

supplier_bp = Blueprint("supplier", __name__)


# -----------------------------
# View Suppliers
# -----------------------------
@supplier_bp.route("/suppliers")
def suppliers():

    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    search = request.args.get("search", "")

    query = """
        SELECT *
        FROM Supplier
    """

    values = ()

    if search:
        query += """
        WHERE
            supplier_name LIKE %s
            OR phone LIKE %s
            OR email LIKE %s
        """

        values = (
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        )

    cursor.execute(query, values)

    suppliers = cursor.fetchall()

    print(suppliers)

    cursor.close()
    connection.close()

    return render_template(
        "suppliers.html",
        suppliers=suppliers,
        search=search
    )


# -----------------------------
# Add Supplier
# -----------------------------
@supplier_bp.route("/add_supplier", methods=["GET", "POST"])
def add_supplier():

    if request.method == "POST":

        supplier_name = request.form["supplier_name"]
        phone = request.form["phone"]
        email = request.form["email"]
        address = request.form["address"]

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO Supplier
            (supplier_name, phone, email, address)
            VALUES (%s,%s,%s,%s)
        """,(
            supplier_name,
            phone,
            email,
            address
        ))

        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for("supplier.suppliers"))

    return render_template(
        "add_supplier.html",
        supplier=None
    )


# -----------------------------
# Edit Supplier
# -----------------------------
@supplier_bp.route("/edit_supplier/<int:supplier_id>", methods=["GET","POST"])
def edit_supplier(supplier_id):

    connection = get_connection()

    if request.method == "POST":

        supplier_name = request.form["supplier_name"]
        phone = request.form["phone"]
        email = request.form["email"]
        address = request.form["address"]

        cursor = connection.cursor()

        cursor.execute("""
            UPDATE Supplier
            SET
                supplier_name=%s,
                phone=%s,
                email=%s,
                address=%s
            WHERE supplier_id=%s
        """,(
            supplier_name,
            phone,
            email,
            address,
            supplier_id
        ))

        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for("supplier.suppliers"))

    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM Supplier
        WHERE supplier_id=%s
    """,(supplier_id,))

    supplier = cursor.fetchone()

    cursor.close()
    connection.close()

    return render_template(
        "add_supplier.html",
        supplier=supplier
    )


# -----------------------------
# Delete Supplier
# -----------------------------
@supplier_bp.route("/delete_supplier/<int:supplier_id>")
def delete_supplier(supplier_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM Supplier
        WHERE supplier_id=%s
    """,(supplier_id,))

    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for("supplier.suppliers"))