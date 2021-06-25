from core.utils.databases.alchemy import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Sequence,
    ForeignKey,
)


class EventsThemes(Base):
    __tablename__ = "eventsthemes"

    id = Column(Integer, Sequence('event_id_seq'), primary_key=True)
    event_id = Column(Integer, ForeignKey('event.id'))
    theme_id = Column(Integer, ForeignKey('theme.id'))

    def __repr__(self):
        return "<Event id={id} event_id={event_id} theme_id={theme_id}>".format(
            id=self.id,
            event_id=self.event_id,
            theme_id=self.theme_id,
        )
