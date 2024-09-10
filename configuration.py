import os


class IBaseConfig:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(IBaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///development.db"


class ProductionConfig(IBaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///production.db"


class TestConfig(IBaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
