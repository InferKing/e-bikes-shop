from flask import Blueprint, render_template, abort
from app.database import db, News


bp = Blueprint('news', __name__, url_prefix='/news')

@bp.route('/')
def index():
    news = db.session.query(News).all()
    return render_template('news.html', news=news)

@bp.route('/<int:id>')
def news(id):
    news = db.session.query(News).filter(News.id == id).first()
    if not news:
        abort(404)
    return render_template('cur_news.html', news=news)


# @bp.route("/here")
# def here():
#     new = News()
#     new.title = "Best title ever"
#     new.description = "Best description ever. Lorem Ipsum dolor rest."
#     new.img_path = "img/news/news1.png"
#     db.session.add(new)
#     db.session.commit()
#     return "lol" 