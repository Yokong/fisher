from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Book(db.Model):
    """book模型"""

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(50), default='未知')
    bindging = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(50))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=True, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))
