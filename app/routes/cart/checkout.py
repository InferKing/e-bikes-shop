from flask import Blueprint, render_template

bp = Blueprint('checkout', __name__, url_prefix='/checkout')

@bp.route('/', methods=["GET", "POST"])
def index():
    return render_template('checkout.html')