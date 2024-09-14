from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

db = SQLAlchemy(model_class=DeclarativeBase)