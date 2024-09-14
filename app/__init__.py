from flask import Flask
from app.routes.index import bp as index_bp
from app.routes.error import error_404
from app.database import db
from app.routes.shop import shop
from app.routes.news import news
from app.routes.cart.cart import bp as cart_bp
from app.routes.cart.checkout import bp as checkout_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('configuration.DevelopmentConfig')
    app.register_blueprint(index_bp)
    app.register_blueprint(shop.shop)
    app.register_blueprint(news.bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(checkout_bp)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_error_handler(404, error_404)
    return app