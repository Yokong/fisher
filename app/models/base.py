from sqlalchemy import Column, SmallInteger
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Base(db.Model):
	status = Column(SmallInteger, default=1)
