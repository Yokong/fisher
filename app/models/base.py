from contextlib import contextmanager
from datetime import datetime

from sqlalchemy import Column, SmallInteger, Integer
from flask_sqlalchemy import SQLAlchemy as SA


class SQLAlchemy(SA):
	@contextmanager
	def auto_commit(self):
		try:
			yield
			self.session.commit()
		except Exception as e:
			self.session.rollback()
			raise e


db = SQLAlchemy()


class Base(db.Model):
	__abstract__ = True
	status = Column(SmallInteger, default=1)
	create_time = Column('create_time', Integer)

	def __init__(self):
		self.create_time = int(datetime.now().timestamp())
	
	def set_attr(self, attr_dict):
		for key, value in attr_dict.items():
			if hasattr(self, key) and key != 'id':
				setattr(self, key, value)
