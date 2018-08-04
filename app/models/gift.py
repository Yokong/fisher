from sqlalchemy import Column, Integer, Boolean, ForeignKey, String
from sqlalchemy.orm import relationship

from .base import db


class Gift(db.Model):
	id = Column(Integer, primaty_key=True)
	user = relationship('User')
	uid = Column(Integer, ForeignKey('user.id'))
	isbn = Column(String(15), nullable=True)
	launched = Column(Boolean, default=False)
