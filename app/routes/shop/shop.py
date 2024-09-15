from flask import Blueprint, render_template, abort, session, request, jsonify
from app.database import db, User, Product

shop = Blueprint("shop", __name__, url_prefix='/shop')


@shop.route("/")
def index():
    return render_template("shop.html")


@shop.route("/<string:category>")
def products(category):
    data = db.session.query(Product).filter_by(category=category).all()
    if len(data) == 0:
        abort(404)
    return render_template("products.html", products=data)

@shop.route("/<string:category>/<int:product_id>")
def product(category, product_id):
    product = db.session.query(Product).filter_by(id=product_id).first()
    if product is None:
        abort(404)
    all_ids = find_id(session.get("picked", []), product.id)
    if len(all_ids) > 0:
        return render_template("product.html", product=product, is_picked=True)
    return render_template("product.html", product=product, is_picked=False)

@shop.route("/picked_product", methods=["POST"])
def picked():
    data = request.get_json()
    r = session.get("picked")
    if r is None:
        session["picked"] = [data]
    else:
        session["picked"].append(data)
    return jsonify({'status': 'ok'})

def find_id(data, id):
    return list(filter(lambda x: x["productId"] == id, data))

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