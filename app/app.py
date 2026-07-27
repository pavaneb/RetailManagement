from flask import Flask, render_template
from routes.product_routes import product_bp

app = Flask(__name__)
app.register_blueprint(product_bp)

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)