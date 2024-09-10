from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('configuration.DevelopmentConfig')
    # здесь должна быть регистрация компонентов приложения
    return app