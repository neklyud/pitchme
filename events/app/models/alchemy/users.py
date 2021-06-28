from core.utils.databases.alchemy import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Sequence,
)
from datetime import datetime


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    email = Column(String)
    password_hash = Column(String)
    access_key = Column(String)
    expires_at = Column(DateTime, default=datetime.utcnow())

    def __repr__(self):
        return "<Usr id={id}>".format(id=self.id)

    def dict(self):
        return {
            'users.id': self.id,
            'name': self.name,
            'email': self.name,
        }