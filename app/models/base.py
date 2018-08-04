from sqlalchemy import Column, SmallInteger
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Base(db.Model):
	__abstract__ = True
	status = Column(SmallInteger, default=1)
	
	def set_attr(self, attr_dict):
		for key, value in attr_dict.items():
			if hasattr(self, key) and key != 'id':
				setattr(self, key, value)
