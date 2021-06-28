from core.utils.databases.alchemy import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Sequence,
)


class Theme(Base):
    __tablename__ = "theme"

    id = Column(Integer, Sequence('theme_id_seq'), primary_key=True)
    name = Column(String, unique=True)

    def __repr__(self):
        return "<Event id={id} name={name}>".format(id=self.id, name=self.name)

    def dict(self):
        return {
            'theme.id': self.id,
            'name': self.name,
        }
