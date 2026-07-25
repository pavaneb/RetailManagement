from flask import Flask, render_template
from db import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/products")
def products():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Product")

    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("products.html", products=products)


if __name__ == "__main__":
    app.run(debug=True)