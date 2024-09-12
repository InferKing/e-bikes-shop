from flask import Blueprint

shop = Blueprint("shop", __name__)


@shop.route("/shop")
def index():
    return render_template("shop.html")


@shop.route("/shop/<int:id>")
def products(id):
    return render_template("products.html")

@shop.route("/shop/<int:id>/<int:product_id>")
def product(id, product_id):
    return render_template("product.html")