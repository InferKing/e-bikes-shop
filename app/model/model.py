from app.database import db
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean, TypeDecorator
from bcrypt import hashpw, gensalt

class PasswordType(TypeDecorator):
    impl = String

    def process_bind_param(self, password, dialect):
        return hashpw(password.encode('utf-8'), gensalt())

    def process_result_value(self, hashed_password, dialect):
        return hashed_password


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(PasswordType, nullable=False)
    is_admin = Column(Boolean, default=False) # True if admin
    cart = relationship("Cart", uselist=False, backref="user")

    def __repr__(self):
        return '<User %r>' % self.username


class Cart(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    product_id = Column(Integer, ForeignKey("product.id"))

    def __repr__(self):
        return '<Cart %r>' % self.user_id


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    description = Column(String(), unique=True, nullable=False)
    price = Column(Float, nullable=False)
    img_path = Column(String(), unique=True, nullable=False)
    color = Column(String(), nullable=False)
    availability = Column(Integer, nullable=False)

    def __repr__(self):
        return '<Product %r>' % self.name