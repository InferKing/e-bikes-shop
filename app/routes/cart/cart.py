from flask import Blueprint, render_template

bp = Blueprint('cart', __name__, url_prefix='/cart')

@bp.route('/')
def index():
    return render_template('cart.html')