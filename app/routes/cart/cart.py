from flask import Blueprint, render_template, session, jsonify
from app.database import db, Product


bp = Blueprint("cart", __name__, url_prefix="/cart")

@bp.route("/")
def index():    
    if "picked" not in session:
        return render_template("cart.html", error_msg="Cart is empty!")
    temp_data = []
    for kv in session["picked"]:
        temp_data.append(db.session.query(Product).filter_by(id=kv.get("productId")).first())
    return render_template("cart.html", data=temp_data)

@bp.route("/get_cart")
def get_cart():
    if "picked" not in session:
        return {}
    temp_data = []
    for kv in session["picked"]:
        temp_data.append(db.session.query(Product).filter_by(id=kv.get("productId")).first().get_data())
    return jsonify(temp_data)