from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Float,
    Boolean,
    TypeDecorator,
    DateTime,
)
from bcrypt import hashpw, gensalt
import datetime



db = SQLAlchemy()

class PasswordType(TypeDecorator):
    impl = String

    def process_bind_param(self, password, dialect):
        return hashpw(password.encode("utf-8"), gensalt())

    def process_result_value(self, hashed_password, dialect):
        return hashed_password


class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(PasswordType, nullable=False)
    is_admin = Column(Boolean, default=False)  # True if admin
    cart = relationship("Cart", uselist=False, backref="user")

    def get_data(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "is_admin": self.is_admin
        }

    def __init__(self, username, email, password, is_admin = False):
        self.username = username
        self.email = email
        self.password = password
        self.is_admin = is_admin
        

    def __repr__(self):
        return "<User %r>" % self.username


class Cart(db.Model):
    __tablename__ = "cart"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, default=1)

    def __repr__(self):
        return "<Cart %r>" % self.user_id


class Product(db.Model):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    description = Column(String(), unique=True, nullable=False)
    price = Column(Float, nullable=False)
    img_path = Column(String(), unique=True, nullable=False)
    color = Column(String(), nullable=False)
    availability = Column(Integer, nullable=False)
    category = Column(String(), nullable=False)

    def get_data(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "img_path": self.img_path,
            "color": self.color,
            "availability": self.availability,
            "category": self.category,
        }

    def __repr__(self):
        return "<Product %r>" % self.name


class Orders(db.Model):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))

    def __repr__(self):
        return "<Orders %r>" % self.user_id


class News(db.Model):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True)
    title = Column(String(80), unique=True, nullable=False)
    description = Column(String(), unique=True, nullable=False)
    img_path = Column(String(), unique=True, nullable=False)
    date = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))

    def __repr__(self):
        return "<News %r>" % self.title
