import os

basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "dbs")

class IBaseConfig:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(IBaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "development.db")
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'development_migrate')


class ProductionConfig(IBaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "production.db")
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'production_migrate')


class TestConfig(IBaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "test.db")
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'test_migrate')
