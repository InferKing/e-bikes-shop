from flask import Blueprint, render_template, jsonify

bp = Blueprint('checkout', __name__, url_prefix='/checkout')

@bp.route('/', methods=["GET", "POST"])
def index():
    return render_template('checkout.html')


@bp.route("/billing", methods=["POST"])
def billing():
    return jsonify({"status": "OK"})