from flask import Flask, render_template

from routes.product_routes import product_bp
from routes.customer_routes import customer_bp
from routes.supplier_routes import supplier_bp
from routes.sales_routes import sales_bp
from routes.report_routes import report_bp

from db import get_connection


app = Flask(__name__)


# Register Blueprints
app.register_blueprint(product_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(supplier_bp)
app.register_blueprint(sales_bp)
app.register_blueprint(report_bp)


# -----------------------------
# Dashboard
# -----------------------------
@app.route("/")
def home():

    connection = get_connection()
    cursor = connection.cursor()

    # Count Products
    cursor.execute("SELECT COUNT(*) FROM Product")
    product_count = cursor.fetchone()[0]

    # Count Customers
    cursor.execute("SELECT COUNT(*) FROM Customer")
    customer_count = cursor.fetchone()[0]

    # Count Suppliers
    cursor.execute("SELECT COUNT(*) FROM Supplier")
    supplier_count = cursor.fetchone()[0]

    # Count Sales
    cursor.execute("SELECT COUNT(*) FROM Sales")
    sales_count = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return render_template(
        "index.html",
        product_count=product_count,
        customer_count=customer_count,
        supplier_count=supplier_count,
        sales_count=sales_count
    )


if __name__ == "__main__":
    app.run(debug=True)