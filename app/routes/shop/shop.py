from flask import Blueprint, render_template
from app.database import db, User

shop = Blueprint("shop", __name__, url_prefix='/shop')


@shop.route("/")
def index():
    return render_template("shop.html")


@shop.route("/<string:category>")
def products(category):
    return render_template("products.html")

@shop.route("/<string:category>/<int:product_id>")
def product(category, product_id):
    return render_template("product.html")

@shop.route("/z")
def z():
    users = db.session.query(User).all()
    print(users)
    return "lol"