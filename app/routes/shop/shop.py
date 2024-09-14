from flask import Blueprint, render_template
from app.database import db, User, Product

shop = Blueprint("shop", __name__, url_prefix='/shop')


@shop.route("/")
def index():
    return render_template("shop.html")


@shop.route("/<string:category>")
def products(category):
    data = db.session.query(Product).filter_by(category=category).all()
    return render_template("products.html", products=data)

@shop.route("/<string:category>/<int:product_id>")
def product(category, product_id):
    return render_template("product.html")

# @shop.route("/z")
# def z():
#     new_pr = Product()
#     new_pr.name = "Super power 8500"
#     new_pr.description = "Super mega bike for all of you"
#     new_pr.price = 10000
#     new_pr.img_path = "img/products/bike1.png"
#     new_pr.color = "red"
#     new_pr.availability = 3
#     new_pr.category = "e-bikes"
#     db.session.add(new_pr)
#     db.session.commit()
#     return "lol"