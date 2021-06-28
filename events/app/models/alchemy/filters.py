from core.utils.databases.alchemy import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Sequence,
)


class Filters(Base):
    __tablename__ = "filters"

    id = Column(Integer, Sequence('filter_id_seq'), primary_key=True)
    name = Column(String)
    filter_body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return "<Filter id={id}>".format(id=self.id)

    def dict(self):
        return {
            'filters.id': self.id,
            'name': self.name,
            'filter_body': self.filter_body,
            'user_id': self.user_id,
        }