from flask import Blueprint, render_template


bp = Blueprint('news', __name__, url_prefix='/news')

@bp.route('/')
def index():
    return render_template('news.html')

@bp.route('/<int:id>')
def news(id):
    return render_template('cur_news.html')